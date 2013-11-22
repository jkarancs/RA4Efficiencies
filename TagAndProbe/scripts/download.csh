#!/bin/tcsh -v

# Storage element directories
set SE = "srm://grid143.kfki.hu:8446/srm/managerv2\?SFN="
set USERDIR = "/dpm/kfki.hu/home/cms/phedex/store/user"

# Aliases
alias se-ls 'lcg-ls -b -D srmv2 --vo cms -l "$SE"\!*'
alias se-cp 'lcg-cp -b -D srmv2 --vo cms -v "$SE"\!*'

# Default options
set OPT_FORMAT=0
set OPT_PARALLEL_DOWNLOAD=0
set OPT_MERGE_ROOT_FILES=0
set OPT_SKIP_DUPLICATES=1
set Nmerge=-1
set Npar=2

# Print info about usage
echo "-----------------------  Usage: -----------------------">! Usage.txt
echo "download.csh [OPTION(S)] [USERDIR] ">> Usage.txt
echo "Userdir inside T2_HU_Budapest:$USERDIR/">> Usage.txt
echo "Options:">> Usage.txt
echo "--format">> Usage.txt
echo "  Format crab job output files to [JobName]_[JobNum].root">> Usage.txt
echo "    where [SubmitNum],[Random] subscripts ares stripped off">> Usage.txt
echo "          [JobNum] is set to [0-9][0-9][0-9][0-9]">> Usage.txt
echo "--merge [N]">> Usage.txt
echo "  Merge each N root files with the hadd command">> Usage.txt
echo "  cmsenv must be set">> Usage.txt
echo "  N = -1 merges all files">> Usage.txt
echo "--parallel [N]">> Usage.txt
echo "  Download N files simultaneously">> Usage.txt
echo "eg: source download.csh --parallel 5 --merge jkarancs/Mu_121203">> Usage.txt
echo "-------------------------------------------------------">> Usage.txt

#Check for options arguments
if ( $#argv == 0 ) then
    echo "Error: No directory Specified"
    cat Usage.txt
    rm Usage.txt; unalias se-ls; unalias se-cp; exit
else if ( $1 == "--help" ) then
    cat Usage.txt
    rm Usage.txt; unalias se-ls; unalias se-cp; exit
endif

foreach i ( `seq 1 $#argv` )
    set opt=$argv[$i]
    set j=`expr $i + 1`
    if ( $opt == "--parallel" ) then
	set OPT_PARALLEL_DOWNLOAD=1
	if ( $j <= $#argv ) then
	    set next=$argv[$j]
	    if ( $next =~ [0-9]* ) then
		set Npar=$next
	    else
		echo "Number of files to download simultaneously is not given, default: N = 2"
	    endif
	else
	    echo "Error: Wrong format"
	    cat Usage.txt
	    rm Usage.txt; unalias se-ls; unalias se-cp; exit
	endif
    else if ( $opt == "--merge" ) then
        set OPT_MERGE_ROOT_FILES=1
	if ( $j <= $#argv ) then
	    set next=$argv[$j]
	    if ( ( $next =~ [0-9]* ) || ( $next == "-1" ) ) then
		set Nmerge=$next
	    else
		echo "Number of files to merge is not given, default = all"
	    endif
	else
	    echo "Error: Wrong format"
	    cat Usage.txt
	    rm Usage.txt; unalias se-ls; unalias se-cp; exit
	endif
    else if ( $opt == "--format" ) then
        set OPT_FORMAT=1
    endif
    if ( $i == $#argv ) then
	set DIR = $opt
	set LASTDIR=`echo $DIR | sed "s;/; ;g" | awk '{ print $NF }'`
    endif
end

# Check for LCG env
if (! $?GLITE_LOCATION) then
    source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.csh
endif

# Checking voms proxy
voms-proxy-info > & ! vomsout.txt
if ( `grep "Couldn't find a valid proxy." vomsout.txt` != "" ) then
    echo "---------------- Requesting Voms Proxy ----------------"
    voms-proxy-init --voms cms -valid 120:00
else if ( `grep "timeleft" vomsout.txt | awk '{ print $3 }'` == "0:00:00" ) then
    echo "------------ Proxy Expired, Requesting New ------------"
    voms-proxy-init --voms cms -valid 120:00
endif
rm vomsout.txt

# Check for cmsenv
if ( ( $OPT_MERGE_ROOT_FILES == 1 ) && ( $?CMSSW_BASE == 0 ) ) then
    echo "Error: Please set cmsenv"
    rm Usage.txt; unalias se-ls; unalias se-cp; exit
endif

############################ Loop on directories ############################
echo "-------------------------------------------------------"
echo "Copying files from directory: $USERDIR/"$DIR":"
#  Create directories and download files
set NSUBDIR=1
echo $USERDIR/$DIR >! dirlist.txt
while ( $NSUBDIR <= `cat dirlist.txt | wc -l` )
    set dpmdir=`sed -n $NSUBDIR"p" dirlist.txt`
    se-ls $dpmdir >! ls_out.txt
    set nline=`cat ls_out.txt | wc -l`
    if ( $nline == 0 ) then 
	# lcg-ls command gives an error message here: No such file or directory
	rm Usage.txt dirlist.txt ls_out.txt RECV.log SENT.log TEST.log
	unalias se-ls; unalias se-cp; exit
    else if ( ( $nline == 1 ) && ( `cat ls_out.txt | grep "^dr" | awk '{ print $NF }'` == $dpmdir  ) ) then
	echo "Error: Empty directory"
	rm Usage.txt dirlist.txt ls_out.txt RECV.log SENT.log TEST.log
	unalias se-ls; unalias se-cp; exit
    endif
    grep "^dr" ls_out.txt | awk '{ print $NF }' >> dirlist.txt
    grep "^-r" ls_out.txt | awk '{ print $NF }' >! filelist.txt
    # Create local directory
    set localdir=`echo $dpmdir | sed "s;"$USERDIR"/"$DIR";$LASTDIR;"`
    echo "mkdir "$localdir; mkdir $localdir
    # Look for duplicate files
    if ( $OPT_SKIP_DUPLICATES == 1) then
        grep "^-r" ls_out.txt | sed "s;_[0-9]*_[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]\.root;\.root;;s;/; ;g" | awk '{ print NR,$5,$NF }' | uniq -D -f2 >! dupl_list.txt
        #awk 'BEGIN{ print "Duplicates found:" }{ print "File: "$3" Size: "$2 }' dupl_list.txt
        # Remove files we want to keep from delete list
        foreach dupl ( `awk '{ print $3 }' dupl_list.txt | uniq` )
            set keep=`awk '{ print NR,$0 }' dupl_list.txt | grep $dupl | awk '{ print $4,$3,$1 }' | sort | awk 'END{ print $3 }'`
            sed -i $keep'd' dupl_list.txt
        end
        # Removing smaller or equal size duplicates
        foreach del ( `awk '{ print $1 }' dupl_list.txt` )
            sed -n $del'p' filelist.txt >>! $LASTDIR/duplicates.log
            sed -i $del'd' filelist.txt
        end
	rm dupl_list.txt
    endif
########################### Download Files in Dir ###########################
    set nfiles=`cat filelist.txt | wc -l`
    if ( $nfiles > 0 ) then
	cat filelist.txt | awk '{ print "se-cp "$1" "$1 }' | sed "s;"$USERDIR"/"$DIR";$LASTDIR;2" >! dl.csh
	# Format root files: strip off SubmitNumber and Random subscript, add leading zeroes for better sorting
	# Duplicate files will also overwrite (keeping only the one with the latest SubmitNumber due to sorting)
	# eg: tpZEE_MC_79_0_HWX.root -> tpZEE_MC_0079.root
	if ( $OPT_FORMAT  == 1 ) then
	     sed 's;_[0-9]_[a-zA-Z0-9]*\.root;_root;2;s;[0-9]*_root;000&;;s;000[0-9][0-9][0-9][0-9];###&;;s;###000;;;s;00[0-9][0-9][0-9][0-9];##&;;s;##00;;;s;0[0-9][0-9][0-9][0-9];#&;;s;#0;;;s;_root;.root;' dl.csh | sort -k 3 >! dl_formatted.csh
	    mv dl_formatted.csh dl.csh
	endif
	# Download files simultaneously
	if ( $OPT_PARALLEL_DOWNLOAD  == 1 ) then
	    awk '{ printf $0" >&! '$LASTDIR'/dl_temp_%04d.log &\n", NR }' dl.csh >! par_dl.csh
	    foreach i ( `seq 1 $nfiles` )
		while ( `ps | awk '{ print $4 }' | grep lcg-cp | wc -l` == $Npar )
		    sleep 2
		end
		set ndl=`ps | awk '{ print $4 }' | grep lcg-cp | wc -l`
		set ndown=`expr $i - $ndl - 1`
		printf "\rDownloading files: %d/%d" $ndown $nfiles
		( eval `sed -n $i"p" par_dl.csh` ) >& /dev/null
		sleep 0.2
            end
	    # Wait until all files are downloaded
	    while ( `ps | awk '{ print $4 }' | grep lcg-cp | wc -l` )
		sleep 2
		set ndl=`ps | awk '{ print $4 }' | grep lcg-cp | wc -l`
		set ndown=`expr $nfiles - $ndl`
		printf "\rDownloading files: %d/%d" $ndown $nfiles
	    end
	    cat $LASTDIR/dl_temp_*.log >>! $LASTDIR/dl.log
	    rm dl.csh par_dl.csh $LASTDIR/dl_temp_*.log
	else
	    foreach i ( `seq 1 $nfiles` )
                printf "\rDownloading files: %d/%d" $i $nfiles
	        eval `sed -n $i"p" dl.csh` >>&! $LASTDIR/dl.log
            end
	endif
############################ Merge Files in Dir #############################
        if ( $OPT_MERGE_ROOT_FILES  == 1 ) then
	    printf "\rDownloaded: "$nfiles", Merging files..."
            # Create list of files to merge
            if ( $OPT_FORMAT  == 1 ) then
                ls -l $localdir | grep ".root" | awk '{ print "'$localdir'/"$NF }' | sort >! filelist_merge.txt
                set output=`sed "1\\!d;s;_[0-9]*.root;;" filelist_merge.txt`
            else
                ls -l $localdir | grep ".root" | awk '{ print "'$localdir'/"$NF }' | awk 'BEGIN { FS = "_" }{ print $(NF-2),$0 }' | sort -n | cut -f2- -d' ' >! filelist_merge.txt
                set output=`sed "1\\!d;s;_[0-9]*_[0-9]*_[a-zA-Z0-9]*.root;;" filelist_merge.txt`
            endif
            # First merge n files (maximum 100)
	    # hadd doesn't handle well too many input files,
	    # so we merge a maximum of 100 files at a time
	    #echo; cat filelist_merge.txt
            set nlines=`cat filelist_merge.txt | wc -l`
	    set nmerge=$Nmerge
	    if ( $Nmerge == "-1" ) then
		set nmerge=100
	    endif
	    echo -n >! merge.csh
            set nloop=`expr $nlines / $nmerge + 1`
	    if ( ! ( ( $Nmerge == "-1" ) && ( $nloop == 1 ) ) ) then
                foreach n ( `seq 1 $nloop` )
                    set nfirst=`expr \( $n - 1 \) \* $nmerge + 1`
                    set nlast=`expr $n \* $nmerge`
                    set inputlist=`sed -n $nfirst","$nlast"p" filelist_merge.txt | tr "\n" " "`
                    set outputn=`echo $output"_"$n".root"`
	            echo "hadd -O "$outputn" "$inputlist >> merge.csh
                    echo "rm "$inputlist >> merge.csh
                end
	    endif
	    if ( ( $Nmerge == "-1" ) ) then
		echo "hadd -O "$output".root "$output"_*.root" >> merge.csh
		echo "rm "$output"_*.root" >> merge.csh
	    endif
	    #echo; cat merge.csh
	    source merge.csh >>! $LASTDIR/merge.log
	    printf "\rDownloaded: "$nfiles", Merging of files complete.\n"
	    rm filelist_merge.txt merge.csh
	else
	    printf "\rDownloaded: "$nfiles".            \n"
        endif
    endif
    set NSUBDIR=`expr $NSUBDIR + 1`
end

#echo "----------------- Listing Directories -----------------"
#ls -l $LASTDIR/*/*
echo "------------------------ Done -------------------------"

# Cleanup
rm Usage.txt filelist.txt dirlist.txt ls_out.txt RECV.log SENT.log TEST.log
unalias se-ls
unalias se-cp
