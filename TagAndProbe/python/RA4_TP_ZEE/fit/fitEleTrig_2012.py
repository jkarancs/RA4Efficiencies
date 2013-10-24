import FWCore.ParameterSet.Config as cms

import sys
import os
import ROOT

process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

isMC = False
set2012=True
useData = "Single" #Double / Single / Had / All
PDFName = "pdfSignalPlusBackground"

if not set2012:
    pathNamesData_Single = [
        "Ele_111124_2/Data/SingleElectron-Run2011A-Aug5ReReco-v1/",
        "Ele_111124_2/Data/SingleElectron-Run2011A-May10ReReco-v1/",
        "Ele_111124_2/Data/SingleElectron-Run2011A-PromptReco-v4/",
        "Ele_111124_2/Data/SingleElectron-Run2011A-PromptReco-v6/",
        "Ele_111124_2/Data/SingleElectron-Run2011B-PromptReco-v1/",
    ##     "Ele_111124/Data/SingleElectron-Run2011A-Aug5ReReco-v1/",
    ##     "Ele_111124/Data/SingleElectron-Run2011A-May10ReReco-v1/",
    ##     "Ele_111124/Data/SingleElectron-Run2011A-PromptReco-v4/",
    ##     "Ele_111124/Data/SingleElectron-Run2011A-PromptReco-v6/",
    ##     "Ele_111124/Data/SingleElectron-Run2011B-PromptReco-v1/"
    ]
    
    pathNamesData_Double = [
    ]
    
    pathNamesData_Had = [
        "Ele_111124_2/Data/ElectronHad-Run2011A-Aug5ReReco-v1/",
        "Ele_111124_2/Data/ElectronHad-Run2011A-May10ReReco-v1__SUBMIT2/",
        "Ele_111124_2/Data/ElectronHad-Run2011A-PromptReco-v4/",
        "Ele_111124_2/Data/ElectronHad-Run2011A-PromptReco-v6/",
        "Ele_111124_2/Data/ElectronHad-Run2011B-PromptReco-v1/",
    ##     "Ele_111124/Data/ElectronHad-Run2011A-Aug5ReReco-v1/",
    ##     "Ele_111124/Data/ElectronHad-Run2011A-May10ReReco-v1__SUBMIT2/",
    ##     "Ele_111124/Data/ElectronHad-Run2011A-PromptReco-v4/",
    ##     "Ele_111124/Data/ElectronHad-Run2011A-PromptReco-v6/",
    ##     "Ele_111124/Data/ElectronHad-Run2011B-PromptReco-v1/"
    ]
    
    pathNamesMC = [
        "Ele_111124/MC/DYToEE_M-20_TuneZ2_7TeV-pythia6_Summer11-PU_S3_START42_V11-v2_AODSIM/",
        "Ele_111124/MC/DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola_Summer11-PU_S3_START42_V11-v2_AODSIM/",
        "Ele_111124/MC/QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6_Summer11-PU_S4_START42_V11-v1_AODSIM/",
        "Ele_111124/MC/TT_TuneZ2_7TeV-pythia6-tauola_Summer11-PU_S3_START42_V11-v2_AODSIM/",
        "Ele_111124/MC/WToENu_TuneZ2_7TeV-pythia6_Summer11-PU_S3_START42_V11-v2_AODSIM/",
        "Ele_111124/MC/WToTauNu_TuneZ2_7TeV-pythia6-tauola_Summer11-PU_S3_START42_V11-v2_AODSIM/"
    ]
else:

    #main_dir = "/home/jkarancs/gridout/LeptonEfficiency/Ele_121204_CleanPFHT300_Ele15_PFMET"
    #main_dir = "/home/jkarancs/gridout/LeptonEfficiency/Ele_121205_CleanPFHT350_Ele5_PFMET"
    #main_dir = "/home/jkarancs/gridout/LeptonEfficiency/Ele_130115_Ele25_TriCentralPFNoPUJet30"
    main_dir = "/home/jkarancs/gridout/LeptonEfficiency/Ele_121017"
    
    pathNamesData_Single = [
        #main_dir+"/Data/SingleElectron_Run2012A-13Jul2012-v1/",
        #main_dir+"/Data/SingleElectron_Run2012A-recover-06Aug2012-v1/",
        #main_dir+"/Data/SingleElectron_Run2012B-13Jul2012-v1/",
        #main_dir+"/Data/SingleElectron_Run2012C-24Aug2012-v1/",
        #main_dir+"/Data/SingleElectron_Run2012C-PromptReco-v2/",
        main_dir+"/Data/SingleElectron_Run2012D-PromptReco-v1/",
    ]
    pathNamesData_Had = [
        #main_dir+"/Data/ElectronHad_Run2012A-13Jul2012-v1/",
        #main_dir+"/Data/ElectronHad_Run2012A-recover-06Aug2012-v1/",
        #main_dir+"/Data/ElectronHad_Run2012B-13Jul2012-v1/",
        #main_dir+"/Data/ElectronHad_Run2012C-24Aug2012-v1/",
        #main_dir+"/Data/ElectronHad_Run2012C-PromptReco-v2/",
        main_dir+"/Data/ElectronHad_Run2012D-PromptReco-v1/",
    ]

    pathNamesMC = [
        main_dir+"/MC/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/",
        main_dir+"/MC/QCD_HT-250To500_TuneZ2star_8TeV-madgraph-pythia6/",
        main_dir+"/MC/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/",
        main_dir+"/MC/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/",
        main_dir+"/MC/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/",
        main_dir+"/MC/T_s-channel_TuneZ2star_8TeV-powheg-tauola/",
        main_dir+"/MC/T_t-channel_TuneZ2star_8TeV-powheg-tauola/",
        main_dir+"/MC/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/",
        main_dir+"/MC/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/",
        main_dir+"/MC/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/",
        main_dir+"/MC/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/",
        main_dir+"/MC/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/",
        main_dir+"/MC/WW_TuneZ2star_8TeV_pythia6_tauola/",
        main_dir+"/MC/WZ_TuneZ2star_8TeV_pythia6_tauola/",
        main_dir+"/MC/ZZ_TuneZ2star_8TeV_pythia6_tauola/",
    ]

    #pathNamesMC = ["Ele_local/MC/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/"]
    

if set2012:
    #suffix = "_CleanPFHT300_Ele15_PFMET_All2012"
    #suffix = "_CleanPFHT350_Ele5_PFMET_2012D"
    #suffix = "_Ele25_TriCentralPFNoPUJet30_All2012"
    suffix = "_Ele30_2012D"
else:
    suffix = "2011"

pathNames = []
if not isMC:
    suffix = useData + suffix
    outputFilePrefix = "Data"
    pathNames = pathNamesData_Single
    if (useData == "Single"): pathNames = pathNamesData_Single
    if (useData == "Double"): pathNames = pathNamesData_Double
    if (useData == "Had"): pathNames = pathNamesData_Had
    #if (useData == "All"): pathNames = pathNamesData_Single + pathNamesData_Double + pathNamesData_Had
    if (useData == "All"): pathNames = pathNamesData_Single + pathNamesData_Had
    weightVar = ""
    theUnbinned = cms.vstring("mass")
    subdir  = ""

else:
    outputFilePrefix = "MC"
    pathNames = pathNamesMC
    weightVar = "weight"   
    theUnbinned = cms.vstring("mass",weightVar)
    subdir  = "vtx_reweighted/"

output="EleEffPlot"+outputFilePrefix+suffix+".root"

selectedAll = cms.vstring()
dataChains = []
for (i,dir) in enumerate(pathNames):
    print "Adding files in " + dir + subdir + ":"
    filenames = os.listdir( dir + subdir )
    addedFiles = []
    selectedFiles = []
    for file in filenames:
       if (file.rpartition(".")[2] != "root"): continue
       fname = file.rpartition("_")[0].rpartition("_")[0]
       #print fname
       if (addedFiles.count(fname) > 0): 
           print "   omitting file " + file + "(dublicate)"
           continue
       else:
           addedFiles.append( fname )
           selectedFiles.append( dir + subdir + file )
           print "   adding file " + dir + subdir + file
    for file in selectedFiles:
        selectedAll.append(file)
    print "      " + str(len(selectedFiles)) + " selected files"
    print

    
      
print str(len(selectedAll)) + " files added"


CUTVTX_BIN = cms.PSet(
    d0_b = cms.vdouble(-0.02, 0.02),
    dz_v = cms.vdouble(-1, 1)
)

##
## ET 
##
    
ET_BINS_10 = cms.PSet(
    probe_gsfEle_et     = cms.vdouble( 10, 15, 20, 30, 40, 60, 80, 200 ),
#    probe_gsfEle_et     = cms.vdouble( 8, 12, 16, 20, 24, 28, 32, 36, 40, 60, 80, 200 ),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
#    dB = cms.vdouble( -0.2, 0.2),
)

ET_BINS_15 = cms.PSet(
#    probe_gsfEle_et     = cms.vdouble( 10, 15, 20, 30, 40, 60, 80, 200 ),
    #probe_gsfEle_et     = cms.vdouble( 8, 12, 16, 20, 24, 28, 32, 36, 40, 60, 80, 200 ),
    probe_gsfEle_et     = cms.vdouble( 8, 14, 17, 20, 24, 28, 32, 36, 40, 60, 80, 200 ),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
#    dB = cms.vdouble( -0.2, 0.2),
)

ET_BINS_15_HT250 = cms.PSet(
    probe_gsfEle_et     = cms.vdouble( 8, 14, 17, 20, 24, 28, 32, 36, 40, 60, 80, 200 ),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
#    dB = cms.vdouble( -0.2, 0.2),
)

ET_BINS_30 = cms.PSet(
#    probe_gsfEle_et     = cms.vdouble( 10, 15, 20, 30, 40, 60, 80, 200 ),
    #probe_gsfEle_et     = cms.vdouble( 8, 12, 16, 20, 24, 28, 32, 36, 40, 60, 80, 200 ),
    probe_gsfEle_et     = cms.vdouble(20, 30, 35, 40, 50, 60, 80, 200),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
#    dB = cms.vdouble( -0.2, 0.2),
)

ET_BINS_65 = cms.PSet(
#    probe_gsfEle_et     = cms.vdouble( 10, 15, 20, 30, 40, 60, 80, 200 ),
    #probe_gsfEle_et     = cms.vdouble( 8, 12, 16, 20, 24, 28, 32, 36, 40, 60, 80, 200 ),
    probe_gsfEle_et     = cms.vdouble( 50, 55, 60, 65, 70, 80, 90, 200 ),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
#    dB = cms.vdouble( -0.2, 0.2),
)


## Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200

Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.PSet(
    tag_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.vstring("pass")
)
effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200","pass"),
    UnbinnedVariables = theUnbinned,
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200,CUTVTX_BIN),
    BinToPDFmap = cms.vstring("vpvPlusExpo2")#,"*pt_bin4*","vpvPlusQuadratic","*pt_bin5*","vpvPlusQuadratic","*pt_bin6*","vpvPlusQuadratic","*pt_bin7*","vpvPlusQuadratic"),
)

## Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200

## Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 = cms.PSet(
##     tag_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 = cms.vstring("pass")
## )
## effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
##     EfficiencyCategoryAndState = cms.vstring("HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200","pass"),
##     BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
## )

## Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200

Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 = cms.PSet(
    tag_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 = cms.vstring("pass")
)
effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200","pass"),
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)
effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_30_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200","pass"),
    BinnedVariables = cms.PSet(ET_BINS_30,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)
effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_65_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200","pass"),
    BinnedVariables = cms.PSet(ET_BINS_65,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

## Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200

Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 = cms.PSet(
    tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 = cms.vstring("pass")
)
effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200","pass"),
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

## Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250

Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250 = cms.PSet(
    tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250 = cms.vstring("pass")
)
effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250","pass"),
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250,CUTVTX_BIN),
)

## Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25

Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.PSet(
    tag_matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.vstring("pass"),
    tag_passingHLT_Ele15_HT250_PFMHT25 = cms.vdouble(0.5, 1.5)
)
effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25","pass"),
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25,CUTVTX_BIN),
)

#print effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt

## Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40

Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.PSet(
    tag_matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.vstring("pass"),
    tag_passingHLT_Ele15_HT250_PFMHT40 = cms.vdouble(0.5, 1.5)
)
effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40","pass"),
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40,CUTVTX_BIN),
)


## HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT50 __MISSING__


## HT350_Ele30_CaloIdT_TrkIdT

Trigger_HLT_HT350_Ele30_CaloIdT_TrkIdT = cms.PSet(
    tag_HT350_Ele30_CaloIdT_TrkIdT = cms.vstring("pass")
)
effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HT350_Ele30_CaloIdT_TrkIdT","pass"),
    BinnedVariables = cms.PSet(ET_BINS_30,Trigger_HLT_HT350_Ele30_CaloIdT_TrkIdT,CUTVTX_BIN),
)

## HT400_Ele60_CaloIdT_TrkIdT

Trigger_HLT_HT400_Ele60_CaloIdT_TrkIdT = cms.PSet(
    tag_HT400_Ele60_CaloIdT_TrkIdT = cms.vstring("pass")
)
effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HT400_Ele60_CaloIdT_TrkIdT","pass"),
    BinnedVariables = cms.PSet(ET_BINS_65,Trigger_HLT_HT400_Ele60_CaloIdT_TrkIdT,CUTVTX_BIN),
)


## HLT_HT450_Ele60_CaloIdT_TrkIdT __MISSING__


## Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL

Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL = cms.PSet(
    tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL = cms.vstring("pass")
)
effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    EfficiencyCategoryAndState = cms.vstring("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL","pass"),
    BinnedVariables = cms.PSet(ET_BINS_10,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL,CUTVTX_BIN),
)


##
## ETA
##


ETA_BINS = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(20,200),
    probe_gsfEle_eta = cms.vdouble(-2.5, -2.1, -1.6, -1.1, -0.6, 0, 0.6, 1.1, 1.6, 2.1, 2.5),
)

ETA_BINS_65 = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(70,200),
    probe_gsfEle_eta = cms.vdouble(-2.5, -2.1, -1.6, -1.1, -0.6, 0, 0.6, 1.1, 1.6, 2.1, 2.5),
)


effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_eta = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200,CUTVTX_BIN),
)

## effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
##     BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
## )

effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_eta = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_eta = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_eta = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40,CUTVTX_BIN),
)

effSpec_HT350_Ele30_CaloIdT_TrkIdT_eta = effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_HT350_Ele30_CaloIdT_TrkIdT,CUTVTX_BIN),
)
effSpec_HT350_Ele30_CaloIdT_TrkIdT_eta.BinnedVariables.probe_gsfEle_et  = cms.vdouble(40,200)

effSpec_HT400_Ele60_CaloIdT_TrkIdT_eta = effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS_65,Trigger_HLT_HT400_Ele60_CaloIdT_TrkIdT,CUTVTX_BIN),
)
effSpec_HT400_Ele60_CaloIdT_TrkIdT_eta.BinnedVariables.probe_gsfEle_et  = cms.vdouble(80,200)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_eta = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt.clone(
    BinnedVariables = cms.PSet(ETA_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL,CUTVTX_BIN),
)



##
## HT
##


HT_BINS = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(20,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    tag_ht = cms.vdouble(100., 250., 300., 350., 400., 600., 1000.)
)

HT_BINS_65 = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(70,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    tag_ht = cms.vdouble(100., 250., 300., 350., 400., 600., 1000.)
)


effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_ht = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200,CUTVTX_BIN),
)

## effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
##     BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
## )

effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_ht = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_ht = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_ht = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40,CUTVTX_BIN),
)

effSpec_HT350_Ele30_CaloIdT_TrkIdT_ht = effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_HT350_Ele30_CaloIdT_TrkIdT,CUTVTX_BIN),
)

effSpec_HT400_Ele60_CaloIdT_TrkIdT_ht = effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS_65,Trigger_HLT_HT400_Ele60_CaloIdT_TrkIdT,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_ht = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt.clone(
    BinnedVariables = cms.PSet(HT_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL,CUTVTX_BIN),
)

##
## MET
##

MET_BINS = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(20,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    tag_met = cms.vdouble(0., 10., 20., 30., 40., 60., 150.),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_met = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt.clone(
    BinnedVariables = cms.PSet(MET_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_met = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt.clone(
    BinnedVariables = cms.PSet(MET_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40,CUTVTX_BIN),
)



##
## ISOLATION
##


RELISO_BINS = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(20,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    reliso = cms.vdouble(0., 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.13, 0.2),
)

RELISO_BINS_65 = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(70,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    reliso = cms.vdouble(0., 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.13, 0.2),
)


effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_reliso = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200,CUTVTX_BIN),
)

## effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
##     BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
## )

effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_reliso = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_reliso = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_reliso = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40,CUTVTX_BIN),
)

effSpec_HT350_Ele30_CaloIdT_TrkIdT_reliso = effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_HT350_Ele30_CaloIdT_TrkIdT,CUTVTX_BIN),
)

effSpec_HT400_Ele60_CaloIdT_TrkIdT_reliso = effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS_65,Trigger_HLT_HT400_Ele60_CaloIdT_TrkIdT,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_reliso = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt.clone(
    BinnedVariables = cms.PSet(RELISO_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL,CUTVTX_BIN),
)


##
## PILEUP
##

NVTX_BINS = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(20,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    nVertices = cms.vdouble(0.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 9.5, 14.5),
)

NVTX_BINS_65 = cms.PSet(
    probe_gsfEle_et  = cms.vdouble(70,100),
    probe_gsfEle_abseta = cms.vdouble(  0.0, 2.5),
    nVertices = cms.vdouble(0.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 9.5, 14.5),
)


effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_nvtx = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200,CUTVTX_BIN),
)

## effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
##     BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
## )

effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_nvtx = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_nvtx = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_nvtx = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40,CUTVTX_BIN),
)

effSpec_HT350_Ele30_CaloIdT_TrkIdT_nvtx = effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_HT350_Ele30_CaloIdT_TrkIdT,CUTVTX_BIN),
)

effSpec_HT400_Ele60_CaloIdT_TrkIdT_nvtx = effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS_65,Trigger_HLT_HT400_Ele60_CaloIdT_TrkIdT,CUTVTX_BIN),
)

effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_nvtx = effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt.clone(
    BinnedVariables = cms.PSet(NVTX_BINS,Trigger_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL,CUTVTX_BIN),
)

if set2012:
    CUTS_2012 = cms.PSet(
        probe_gsfEle_eta = cms.vdouble(-2.5, 2.5),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.1, 0.1),
        reliso = cms.vdouble(0., 0.12),
        drjet = cms.vdouble(0.3, 7),
        absdeltapt = cms.vdouble(-10000., 5.0),
    )
        
    ET_BINS_27 = cms.PSet(
        probe_gsfEle_et = cms.vdouble(10, 15, 20, 25, 29, 34, 40, 50,  60, 100),
    )
    
    # HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    Trigger_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(
        tag_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.vstring("pass")
    )
    
    effSpec_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_pt = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL","pass"),
        UnbinnedVariables = theUnbinned,
        BinnedVariables = cms.PSet(ET_BINS_27, Trigger_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL, CUTS_2012),
        BinToPDFmap = cms.vstring("vpvPlusExpo2")
    )

    # HLT_Ele27_WP80
    Trigger_HLT_Ele27_WP80 = cms.PSet(
        tag_HLT_Ele27_WP80 = cms.vstring("pass")
    )
    
    effSpec_Ele27_WP80_pt = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele27_WP80","pass"),
        UnbinnedVariables = theUnbinned,
        BinnedVariables = cms.PSet(ET_BINS_27, Trigger_HLT_Ele27_WP80, CUTS_2012),
        BinToPDFmap = cms.vstring("vpvPlusExpo2")
    )

    
    ###################################
    #       Single Ele  Triggers      #
    ###################################

    #Ele22_CaloIdL_CaloIsoVL
    #Ele27_CaloIdL_CaloIsoVL
    #Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    #Ele30_CaloIdVT_TrkIdT
    #Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    #Ele65_CaloIdVT_TrkIdT
    #Ele80_CaloIdVT_TrkIdT
    #Ele80_CaloIdVT_GsfTrkIdT
    #Ele90_CaloIdVT_GsfTrkIdT
    #Ele100_CaloIdVT_TrkIdT
    #Ele27_WP80
    #Ele27_WP80_PFMET_MT50
    #Ele27_WP80_CentralPFJet80
    #Ele27_WP80_WCandPt80
    
    CUTS_2012 = cms.PSet(
        probe_gsfEle_eta = cms.vdouble(-2.5, 2.5),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.1, 0.1),
        reliso = cms.vdouble(0., 0.15),
        drjet = cms.vdouble(0.3, 7),
        absdeltapt = cms.vdouble(-10000., 10.0),
    )
    
    ET10_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(10, 200) )
    ET20_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(20, 200) )
    ET30_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(30, 200) )
    ET35_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(35, 200) )
    ET40_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(40, 200) )
    ET50_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(50, 200) )
    ET60_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(60, 200) )
    ET70_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(70, 200) )
    ET80_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(80, 200) )
    ET100_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(100, 200) )
    ET110_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(110, 200) )
    ET120_CUTS_2012 = CUTS_2012.clone( probe_gsfEle_et = cms.vdouble(120, 200) )
    
    #NVTX_BINS   = cms.PSet( nVertices    = cms.vdouble(0.5, 4.5, 8.5, 12.5, 16.5, 20.5, 24.5, 28.5, 32.5, 36.5, 40.5) )
    NVTX_BINS   = cms.PSet( nVertices    = cms.vdouble(0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.50) )
    ETA_BINS    = cms.PSet( probe_gsfEle_eta = cms.vdouble(-2.5, -2.3, -2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.3, 2.5) )
    HT_BINS     = cms.PSet( tag_ht           = cms.vdouble(100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 1000) )
    MET_BINS    = cms.PSet( tag_met          = cms.vdouble(0, 10, 20, 30, 40, 60, 150) )
    
    RELISO_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.01, 0.02, 0.04, 0.06, 0.09, 0.12, 0.15, 0.2, 0.25) )

    RELISO001_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.01) )
    RELISO002_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.02) )
    RELISO004_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.04) )
    RELISO006_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.06) )
    RELISO009_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.09) )
    RELISO012_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.12) )
    RELISO015_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.15) )
    RELISO020_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.20) )
    RELISO025_BINS = cms.PSet( reliso           = cms.vdouble(0., 0.25) )    
    
    ET5_BINS   = cms.PSet( probe_gsfEle_et = cms.vdouble( 2,  4,  5,  6,  8, 11, 15, 20, 30,  60, 100) )
    ET8_BINS   = cms.PSet( probe_gsfEle_et = cms.vdouble( 5,  7,  8,  9, 11, 14, 17, 20, 30,  60, 100) )
    ET12_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble( 5,  8, 10, 12, 14, 17, 20, 25, 30,  40,  60, 100) )
    ET15_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble( 5,  8, 11, 14, 16, 19, 22, 25, 30,  40,  60, 100) )
    ET20_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(10, 13, 16, 19, 21, 24, 27, 30, 35,  40,  50,  60, 100) )
    ET22_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(10, 14, 18, 21, 23, 26, 30, 35, 40,  50,  60, 100) )
    ET24_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(10, 15, 20, 23, 25, 28, 33, 40, 50,  60, 100) )
    ET25_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(10, 15, 20, 25, 30, 35, 40, 50,  60, 100) )
    ET27_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(10, 15, 20, 25, 29, 34, 40, 50, 60, 100) )
    ET30_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(15, 20, 24, 28, 32, 36, 40, 45, 50,  60, 100) )
    ET32_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(15, 20, 26, 30, 34, 38, 42, 50, 60, 100) )
    ET34_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(15, 25, 29, 32, 36, 40, 45, 50, 55,  60, 100) )
    ET40_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(30, 34, 38, 42, 46, 50, 60, 70, 80, 100) )
    ET60_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(40, 45, 50, 54, 58, 62, 66, 70, 80, 100) )
    ET65_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(50, 55, 59, 63, 67, 71, 75, 80, 90, 100) )
    ET80_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(60, 65, 70, 74, 78, 82, 86, 90, 100, 110, 120) )
    ET90_BINS  = cms.PSet( probe_gsfEle_et = cms.vdouble(70, 75, 80, 84, 88, 92, 96, 100, 110, 120, 130) )
    ET100_BINS = cms.PSet( probe_gsfEle_et = cms.vdouble(80, 85, 90, 94, 98, 102, 106, 110, 120, 130, 140) )

    ST_BINS   = cms.PSet( stlep = cms.vdouble( 0,  25, 50, 75, 100, 150, 200, 250, 300, 400, 500) )
    
    EffTemplate = cms.PSet(
        UnbinnedVariables = theUnbinned,
        BinToPDFmap = cms.vstring("vpvPlusExpo2")
    )
    
    BinVar_HLT_Ele27_WP80                               =  ET40_CUTS_2012.clone(tag_HLT_Ele27_WP80 = cms.vstring("pass") )
    BinVar_HLT_Ele22_CaloIdL_CaloIsoVL                  =  ET30_CUTS_2012.clone(tag_HLT_Ele22_CaloIdL_CaloIsoVL = cms.vstring("pass") )
    BinVar_HLT_Ele27_CaloIdL_CaloIsoVL                  =  ET40_CUTS_2012.clone(tag_HLT_Ele27_CaloIdL_CaloIsoVL = cms.vstring("pass") )
    BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL =  ET40_CUTS_2012.clone(tag_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.vstring("pass") )
    BinVar_HLT_Ele30_CaloIdVT_TrkIdT                    =  ET40_CUTS_2012.clone(tag_HLT_Ele30_CaloIdVT_TrkIdT = cms.vstring("pass") )
    BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL =  ET40_CUTS_2012.clone(tag_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.vstring("pass") )
    BinVar_HLT_Ele65_CaloIdVT_TrkIdT                    =  ET80_CUTS_2012.clone(tag_HLT_Ele65_CaloIdVT_TrkIdT = cms.vstring("pass") )
    BinVar_HLT_Ele80_CaloIdVT_TrkIdT                    = ET100_CUTS_2012.clone(tag_HLT_Ele80_CaloIdVT_TrkIdT = cms.vstring("pass") )
    BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT                 = ET100_CUTS_2012.clone(tag_HLT_Ele80_CaloIdVT_GsfTrkIdT = cms.vstring("pass") )
    BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT                 = ET110_CUTS_2012.clone(tag_HLT_Ele90_CaloIdVT_GsfTrkIdT = cms.vstring("pass") )
    BinVar_HLT_Ele100_CaloIdVT_TrkIdT                   = ET120_CUTS_2012.clone(tag_HLT_Ele100_CaloIdVT_TrkIdT = cms.vstring("pass") )
    
    # HLT_Ele27_WP80
    EffptHLT_Ele27_WP80 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele27_WP80", "pass"),
        BinnedVariables = BinVar_HLT_Ele27_WP80.clone( probe_gsfEle_et = ET27_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele27_WP80 = EffptHLT_Ele27_WP80.clone( BinnedVariables = BinVar_HLT_Ele27_WP80.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele27_WP80 = EffptHLT_Ele27_WP80.clone( BinnedVariables = BinVar_HLT_Ele27_WP80.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele27_WP80 = EffptHLT_Ele27_WP80.clone( BinnedVariables = BinVar_HLT_Ele27_WP80.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele27_WP80 = EffptHLT_Ele27_WP80.clone( BinnedVariables = BinVar_HLT_Ele27_WP80.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele27_WP80 = EffptHLT_Ele27_WP80.clone( BinnedVariables = BinVar_HLT_Ele27_WP80.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele27_WP80 = EffptHLT_Ele27_WP80.clone( BinnedVariables = BinVar_HLT_Ele27_WP80.clone(tag_met = MET_BINS.tag_met) )

    #Ele22_CaloIdL_CaloIsoVL
    EffptHLT_Ele22_CaloIdL_CaloIsoVL = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele22_CaloIdL_CaloIsoVL", "pass"),
        BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone( probe_gsfEle_et = ET22_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele22_CaloIdL_CaloIsoVL = EffptHLT_Ele22_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele22_CaloIdL_CaloIsoVL = EffptHLT_Ele22_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele22_CaloIdL_CaloIsoVL = EffptHLT_Ele22_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele22_CaloIdL_CaloIsoVL = EffptHLT_Ele22_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele22_CaloIdL_CaloIsoVL = EffptHLT_Ele22_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele22_CaloIdL_CaloIsoVL = EffptHLT_Ele22_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele22_CaloIdL_CaloIsoVL.clone(tag_met = MET_BINS.tag_met) )
    
    #Ele27_CaloIdL_CaloIsoVL
    EffptHLT_Ele27_CaloIdL_CaloIsoVL = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele27_CaloIdL_CaloIsoVL", "pass"),
        BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone( probe_gsfEle_et = ET27_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele27_CaloIdL_CaloIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele27_CaloIdL_CaloIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele27_CaloIdL_CaloIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele27_CaloIdL_CaloIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele27_CaloIdL_CaloIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele27_CaloIdL_CaloIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL.clone(tag_met = MET_BINS.tag_met) )

    #Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL", "pass"),
        BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( probe_gsfEle_et = ET27_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone(tag_met = MET_BINS.tag_met) )

    #Ele30_CaloIdVT_TrkIdT
    EffptHLT_Ele30_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele30_CaloIdVT_TrkIdT", "pass"),
        BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET30_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele30_CaloIdVT_TrkIdT = EffptHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele30_CaloIdVT_TrkIdT = EffptHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele30_CaloIdVT_TrkIdT = EffptHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele30_CaloIdVT_TrkIdT = EffptHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele30_CaloIdVT_TrkIdT = EffptHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele30_CaloIdVT_TrkIdT = EffptHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )

    Effreliso001HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO001_BINS.reliso ) )
    Effreliso002HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO002_BINS.reliso ) )
    Effreliso004HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO004_BINS.reliso ) )
    Effreliso006HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO006_BINS.reliso ) )
    Effreliso009HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO009_BINS.reliso ) )
    Effreliso012HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO012_BINS.reliso ) )
    Effreliso015HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO015_BINS.reliso ) )
    Effreliso020HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO020_BINS.reliso ) )
    Effreliso025HLT_Ele30_CaloIdVT_TrkIdT = EffrelisoHLT_Ele30_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele30_CaloIdVT_TrkIdT.clone( reliso = RELISO025_BINS.reliso ) )

    #Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL", "pass"),
        BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( probe_gsfEle_et = ET32_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( BinnedVariables = BinVar_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone(tag_met = MET_BINS.tag_met) )

    #Ele65_CaloIdVT_TrkIdT
    EffptHLT_Ele65_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele65_CaloIdVT_TrkIdT", "pass"),
        BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET65_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele65_CaloIdVT_TrkIdT = EffptHLT_Ele65_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele65_CaloIdVT_TrkIdT = EffptHLT_Ele65_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele65_CaloIdVT_TrkIdT = EffptHLT_Ele65_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele65_CaloIdVT_TrkIdT = EffptHLT_Ele65_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele65_CaloIdVT_TrkIdT = EffptHLT_Ele65_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele65_CaloIdVT_TrkIdT = EffptHLT_Ele65_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele65_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )

    #Ele80_CaloIdVT_TrkIdT
    EffptHLT_Ele80_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele80_CaloIdVT_TrkIdT", "pass"),
        BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET80_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele80_CaloIdVT_TrkIdT = EffptHLT_Ele80_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele80_CaloIdVT_TrkIdT = EffptHLT_Ele80_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele80_CaloIdVT_TrkIdT = EffptHLT_Ele80_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele80_CaloIdVT_TrkIdT = EffptHLT_Ele80_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele80_CaloIdVT_TrkIdT = EffptHLT_Ele80_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele80_CaloIdVT_TrkIdT = EffptHLT_Ele80_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )

    #Ele80_CaloIdVT_GsfTrkIdT
    EffptHLT_Ele80_CaloIdVT_GsfTrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele80_CaloIdVT_GsfTrkIdT", "pass"),
        BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone( probe_gsfEle_et = ET80_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele80_CaloIdVT_GsfTrkIdT = EffptHLT_Ele80_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele80_CaloIdVT_GsfTrkIdT = EffptHLT_Ele80_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele80_CaloIdVT_GsfTrkIdT = EffptHLT_Ele80_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele80_CaloIdVT_GsfTrkIdT = EffptHLT_Ele80_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele80_CaloIdVT_GsfTrkIdT = EffptHLT_Ele80_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele80_CaloIdVT_GsfTrkIdT = EffptHLT_Ele80_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele80_CaloIdVT_GsfTrkIdT.clone(tag_met = MET_BINS.tag_met) )

    #Ele90_CaloIdVT_GsfTrkIdT
    EffptHLT_Ele90_CaloIdVT_GsfTrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele90_CaloIdVT_GsfTrkIdT", "pass"),
        BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone( probe_gsfEle_et = ET90_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele90_CaloIdVT_GsfTrkIdT = EffptHLT_Ele90_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele90_CaloIdVT_GsfTrkIdT = EffptHLT_Ele90_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele90_CaloIdVT_GsfTrkIdT = EffptHLT_Ele90_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele90_CaloIdVT_GsfTrkIdT = EffptHLT_Ele90_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele90_CaloIdVT_GsfTrkIdT = EffptHLT_Ele90_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele90_CaloIdVT_GsfTrkIdT = EffptHLT_Ele90_CaloIdVT_GsfTrkIdT.clone( BinnedVariables = BinVar_HLT_Ele90_CaloIdVT_GsfTrkIdT.clone(tag_met = MET_BINS.tag_met) )

    #Ele100_CaloIdVT_TrkIdT
    EffptHLT_Ele100_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele100_CaloIdVT_TrkIdT", "pass"),
        BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET100_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele100_CaloIdVT_TrkIdT = EffptHLT_Ele100_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone( probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta ) )
    EffnvtxHLT_Ele100_CaloIdVT_TrkIdT = EffptHLT_Ele100_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone( nVertices = NVTX_BINS.nVertices ) )
    EffrelisoHLT_Ele100_CaloIdVT_TrkIdT = EffptHLT_Ele100_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone( reliso = RELISO_BINS.reliso ) )
    EffstHLT_Ele100_CaloIdVT_TrkIdT = EffptHLT_Ele100_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele100_CaloIdVT_TrkIdT = EffptHLT_Ele100_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele100_CaloIdVT_TrkIdT = EffptHLT_Ele100_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_Ele100_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )
    
    ## ST try
    ST20_BINS  = cms.PSet( stlep = cms.vdouble(20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100) )
    
    BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = CUTS_2012.clone(tag_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.vstring("pass") )
    EffstHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL", "pass"),
        BinnedVariables = BinVar_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL.clone( stlep = ST20_BINS.stlep )
    )
    
    
    ###################################
    #        Ele Cross  Triggers      #
    ###################################

    #CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    #CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    #CleanPFHT300_Ele40_CaloIdVT_TrkIdT
    #CleanPFHT300_Ele60_CaloIdVT_TrkIdT
    #CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    #CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    #CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    #CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    #CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT
    #CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT
    #CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    #CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    
    BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30 = ET20_CUTS_2012.clone( tag_HLT_Ele8_CaloIdT_TrkIdVL_Jet30 = cms.vstring("pass") )
    
    BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = ET20_CUTS_2012.clone(
        tag_passingHLT_CleanPFHT300_Ele15_PFMET45 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT300_Ele15_PFMET45 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = ET20_CUTS_2012.clone(
        tag_passingHLT_CleanPFHT300_Ele15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT300_Ele15_PFMET50 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = ET50_CUTS_2012.clone(
        tag_passingHLT_CleanPFHT300_Ele15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT300_Ele40 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = ET70_CUTS_2012.clone(
        tag_passingHLT_CleanPFHT300_Ele15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT300_Ele60 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = ET10_CUTS_2012.clone(
        tag_passingHLT_CleanPFHT350_Ele5_PFMET45 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT350_Ele5_PFMET45 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = ET10_CUTS_2012.clone(
        tag_passingHLT_CleanPFHT350_Ele5_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT350_Ele5_PFMET50 = cms.vstring("pass"),
    )



    BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = ET20_CUTS_2012.clone(
        tag_passingHLT_CleanPFNoPUHT300_Ele15_PFMET45 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFNoPUHT300_Ele15_PFMET45 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = ET20_CUTS_2012.clone(
        tag_passingHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = ET50_CUTS_2012.clone(
        tag_passingHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFNoPUHT300_Ele40 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = ET70_CUTS_2012.clone(
        tag_passingHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFNoPUHT300_Ele60 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = ET10_CUTS_2012.clone(
        tag_passingHLT_CleanPFNoPUHT350_Ele5_PFMET45 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFNoPUHT350_Ele5_PFMET45 = cms.vstring("pass"),
    )
    BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = ET10_CUTS_2012.clone(
        tag_passingHLT_CleanPFNoPUHT350_Ele5_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFNoPUHT350_Ele5_PFMET50 = cms.vstring("pass"),
    )

    BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = ET35_CUTS_2012.clone(
        tag_passingHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30 = cms.vstring("pass"),
    )
    
    #Ele8_CaloIdT_TrkIdVL_Jet30
    EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele8_CaloIdT_TrkIdVL_Jet30", "pass"),
        BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( probe_gsfEle_et = ET8_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele8_CaloIdT_TrkIdVL_Jet30    = EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_Ele8_CaloIdT_TrkIdVL_Jet30   = EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_Ele8_CaloIdT_TrkIdVL_Jet30 = EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_Ele8_CaloIdT_TrkIdVL_Jet30 = EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele8_CaloIdT_TrkIdVL_Jet30 = EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele8_CaloIdT_TrkIdVL_Jet30 = EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone( BinnedVariables = BinVar_HLT_Ele8_CaloIdT_TrkIdVL_Jet30.clone(tag_met = MET_BINS.tag_met) )

    #CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFHT300_Ele15_PFMET45", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( probe_gsfEle_et = ET15_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    Effreliso001HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO001_BINS.reliso) )
    Effreliso002HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO002_BINS.reliso) )
    Effreliso004HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO004_BINS.reliso) )
    Effreliso006HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO006_BINS.reliso) )
    Effreliso009HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO009_BINS.reliso) )
    Effreliso012HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO012_BINS.reliso) )
    Effreliso015HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO015_BINS.reliso) )
    Effreliso020HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO020_BINS.reliso) )
    Effreliso025HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO025_BINS.reliso) )
    
    #CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFHT300_Ele15_PFMET50", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( probe_gsfEle_et = ET15_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFHT300_Ele40_CaloIdVT_TrkIdT
    EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFHT300_Ele40", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET40_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT    = EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT   = EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )
 
    #CleanPFHT300_Ele60_CaloIdVT_TrkIdT
    EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFHT300_Ele60", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET60_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT    = EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT   = EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )

    #CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFHT350_Ele5_PFMET45", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( probe_gsfEle_et = ET5_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_met = MET_BINS.tag_met) )

    #CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFHT350_Ele5_PFMET50", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( probe_gsfEle_et = ET5_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    #CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    #CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT
    #CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT
    #CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    #CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    
    #CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFNoPUHT300_Ele15_PFMET45", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( probe_gsfEle_et = ET15_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFNoPUHT300_Ele15_PFMET50", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( probe_gsfEle_et = ET15_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT
    EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFNoPUHT300_Ele40", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET40_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT    = EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT   = EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT
    EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFNoPUHT300_Ele60", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( probe_gsfEle_et = ET60_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT    = EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT   = EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45
    EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFNoPUHT350_Ele5_PFMET45", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( probe_gsfEle_et = ET5_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    #CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50
    EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_CleanPFNoPUHT350_Ele5_PFMET50", "pass"),
        BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( probe_gsfEle_et = ET5_BINS.probe_gsfEle_et )
    )
    EffetaHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone( BinnedVariables = BinVar_HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50.clone(tag_met = MET_BINS.tag_met) )

    #HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30
    EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("HLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30", "pass"),
        BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( probe_gsfEle_et = ET25_BINS.probe_gsfEle_et )
    )
    EffetaHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30    = EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(probe_gsfEle_eta = ETA_BINS.probe_gsfEle_eta) )
    EffnvtxHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30   = EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(nVertices = NVTX_BINS.nVertices) )
    EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO_BINS.reliso) )
    EffstHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(probe_gsfEle_et = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffhtHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(tag_met = MET_BINS.tag_met) )
    
    Effreliso001HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO001_BINS.reliso) )
    Effreliso002HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO002_BINS.reliso) )
    Effreliso004HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO004_BINS.reliso) )
    Effreliso006HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO006_BINS.reliso) )
    Effreliso009HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO009_BINS.reliso) )
    Effreliso012HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO012_BINS.reliso) )
    Effreliso015HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO015_BINS.reliso) )
    Effreliso020HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO020_BINS.reliso) )
    Effreliso025HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone( BinnedVariables = BinVar_HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30.clone(reliso = RELISO025_BINS.reliso) )
    
    #debug
    ET20 = cms.PSet(
        probe_gsfEle_et = cms.vdouble(20, 200),
        probe_gsfEle_eta = cms.vdouble(-2.5, 2.5),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.1, 0.1),
        reliso = cms.vdouble(0., 0.15),
        drjet = cms.vdouble(0.3, 7),
        absdeltapt = cms.vdouble(-10000., 10.0),
    )
    
    BinVar_debug = ET20.clone(
        #tag_passingHLT_CleanPFHT300_Ele15_PFMET45 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_CleanPFHT300_Ele15_PFMET45 = cms.vstring("pass"),
    )
    debug = EffTemplate.clone(
        #EfficiencyCategoryAndState = cms.vstring("matchedHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45", "pass"),
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_CleanPFHT300_Ele15_PFMET45", "pass"),
        #BinnedVariables = BinVar_debug.clone( probe_gsfEle_et = ET15_BINS.probe_gsfEle_et )
        BinnedVariables = cms.PSet( probe_gsfEle_et = ET15_BINS.probe_gsfEle_et )
    )
    
    
    
##
## Data/MC efficiencies
##
if set2012:
    DataEfficiencies = cms.PSet(
        # # SingleEle Triggers
        # # pt
        # EffptHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffptHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffptHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffptHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffptHLT_Ele30_CaloIdVT_TrkIdT),
        # EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffptHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffptHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffptHLT_Ele65_CaloIdVT_TrkIdT),
        # EffptHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffptHLT_Ele80_CaloIdVT_TrkIdT),
        # EffptHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffptHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffptHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffptHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffptHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffptHLT_Ele100_CaloIdVT_TrkIdT),
        # EffptHLT_Ele27_WP80                               = cms.PSet(EffptHLT_Ele27_WP80),
        # # st
        # EffstHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffstHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffstHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffstHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffstHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffstHLT_Ele30_CaloIdVT_TrkIdT),
        # EffstHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffstHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffstHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffstHLT_Ele65_CaloIdVT_TrkIdT),
        # EffstHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffstHLT_Ele80_CaloIdVT_TrkIdT),
        # EffstHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffstHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffstHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffstHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffstHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffstHLT_Ele100_CaloIdVT_TrkIdT),
        # EffstHLT_Ele27_WP80                               = cms.PSet(EffstHLT_Ele27_WP80),
        # # eta
        # EffetaHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffetaHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffetaHLT_Ele27_CaloIdL_CaloIsoVL                  = cms.PSet(EffetaHLT_Ele27_CaloIdL_CaloIsoVL),
        # EffetaHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffetaHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffetaHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffetaHLT_Ele30_CaloIdVT_TrkIdT),
        # EffetaHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffetaHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffetaHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffetaHLT_Ele65_CaloIdVT_TrkIdT),
        # EffetaHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffetaHLT_Ele80_CaloIdVT_TrkIdT),
        # EffetaHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffetaHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffetaHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffetaHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffetaHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffetaHLT_Ele100_CaloIdVT_TrkIdT),
        # #EffetaHLT_Ele27_WP80                               = cms.PSet(EffetaHLT_Ele27_WP80),
        # # nvtx
        # EffnvtxHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffnvtxHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffnvtxHLT_Ele27_CaloIdL_CaloIsoVL                  = cms.PSet(EffnvtxHLT_Ele27_CaloIdL_CaloIsoVL),
        # EffnvtxHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffnvtxHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffnvtxHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffnvtxHLT_Ele30_CaloIdVT_TrkIdT),
        # EffnvtxHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffnvtxHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffnvtxHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffnvtxHLT_Ele65_CaloIdVT_TrkIdT),
        # EffnvtxHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffnvtxHLT_Ele80_CaloIdVT_TrkIdT),
        # EffnvtxHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffnvtxHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffnvtxHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffnvtxHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffnvtxHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffnvtxHLT_Ele100_CaloIdVT_TrkIdT),
        # #EffnvtxHLT_Ele27_WP80                               = cms.PSet(EffnvtxHLT_Ele27_WP80),
        # # reliso
        # EffrelisoHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffrelisoHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffrelisoHLT_Ele27_CaloIdL_CaloIsoVL                  = cms.PSet(EffrelisoHLT_Ele27_CaloIdL_CaloIsoVL),
        # EffrelisoHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffrelisoHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffrelisoHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffrelisoHLT_Ele30_CaloIdVT_TrkIdT),
        # EffrelisoHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffrelisoHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffrelisoHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffrelisoHLT_Ele65_CaloIdVT_TrkIdT),
        # EffrelisoHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffrelisoHLT_Ele80_CaloIdVT_TrkIdT),
        # EffrelisoHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffrelisoHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffrelisoHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffrelisoHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffrelisoHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffrelisoHLT_Ele100_CaloIdVT_TrkIdT),
        # #EffrelisoHLT_Ele27_WP80                               = cms.PSet(EffrelisoHLT_Ele27_WP80),
        # # ht
        # EffhtHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffhtHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffhtHLT_Ele27_CaloIdL_CaloIsoVL                  = cms.PSet(EffhtHLT_Ele27_CaloIdL_CaloIsoVL),
        # EffhtHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffhtHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffhtHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffhtHLT_Ele30_CaloIdVT_TrkIdT),
        # EffhtHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffhtHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffhtHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffhtHLT_Ele65_CaloIdVT_TrkIdT),
        # EffhtHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffhtHLT_Ele80_CaloIdVT_TrkIdT),
        # EffhtHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffhtHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffhtHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffhtHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffhtHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffhtHLT_Ele100_CaloIdVT_TrkIdT),
        # #EffhtHLT_Ele27_WP80                               = cms.PSet(EffhtHLT_Ele27_WP80),
        # # met
        # EffmetHLT_Ele22_CaloIdL_CaloIsoVL                  = cms.PSet(EffmetHLT_Ele22_CaloIdL_CaloIsoVL),
        # EffmetHLT_Ele27_CaloIdL_CaloIsoVL                  = cms.PSet(EffmetHLT_Ele27_CaloIdL_CaloIsoVL),
        # EffmetHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffmetHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        EffmetHLT_Ele30_CaloIdVT_TrkIdT                    = cms.PSet(EffmetHLT_Ele30_CaloIdVT_TrkIdT),
        # EffmetHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffmetHLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        # EffmetHLT_Ele65_CaloIdVT_TrkIdT                    = cms.PSet(EffmetHLT_Ele65_CaloIdVT_TrkIdT),
        # EffmetHLT_Ele80_CaloIdVT_TrkIdT                    = cms.PSet(EffmetHLT_Ele80_CaloIdVT_TrkIdT),
        # EffmetHLT_Ele80_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffmetHLT_Ele80_CaloIdVT_GsfTrkIdT),
        # EffmetHLT_Ele90_CaloIdVT_GsfTrkIdT                 = cms.PSet(EffmetHLT_Ele90_CaloIdVT_GsfTrkIdT),
        # EffmetHLT_Ele100_CaloIdVT_TrkIdT                   = cms.PSet(EffmetHLT_Ele100_CaloIdVT_TrkIdT),
        # #EffmetHLT_Ele27_WP80                               = cms.PSet(EffmetHLT_Ele27_WP80),
        
        # Cross Triggers
        #EffptHLT_Ele27_WP80_PFMET_MT50                    = cms.PSet(EffptHLT_Ele27_WP80_PFMET_MT50),
        #EffptHLT_Ele27_WP80_CentralPFJet80                = cms.PSet(EffptHLT_Ele27_WP80_CentralPFJet80),
        #EffptHLT_Ele27_WP80_WCandPt80                     = cms.PSet(EffptHLT_Ele27_WP80_WCandPt80),
        #EffetaHLT_Ele27_WP80_PFMET_MT50                    = cms.PSet(EffetaHLT_Ele27_WP80_PFMET_MT50),
        #EffetaHLT_Ele27_WP80_CentralPFJet80                = cms.PSet(EffetaHLT_Ele27_WP80_CentralPFJet80),
        #EffetaHLT_Ele27_WP80_WCandPt80                     = cms.PSet(EffetaHLT_Ele27_WP80_WCandPt80),
        
        #MuHad
        #EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30 = cms.PSet(EffptHLT_Ele8_CaloIdT_TrkIdVL_Jet30),

        #EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffstHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffstHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffhtHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffhtHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffmetHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffmetHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffetaHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffetaHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffnvtxHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = cms.PSet(EffnvtxHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #
        #EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffptHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffstHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffstHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffhtHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffhtHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffmetHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffmetHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffetaHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffetaHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffnvtxHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = cms.PSet(EffnvtxHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = cms.PSet(EffrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        
        #EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffstHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffstHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffhtHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffhtHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffmetHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffmetHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffetaHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffetaHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffnvtxHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = cms.PSet(EffnvtxHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffrelisoHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(EffrelisoHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #
        #EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffptHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffstHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffstHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffhtHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffhtHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffmetHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffmetHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffetaHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffetaHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffnvtxHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = cms.PSet(EffnvtxHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffrelisoHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = cms.PSet(EffrelisoHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #
        #EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT     = cms.PSet(EffptHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #EffstHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT     = cms.PSet(EffstHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #EffhtHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT     = cms.PSet(EffhtHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #EffmetHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT    = cms.PSet(EffmetHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #EffetaHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT    = cms.PSet(EffetaHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #EffnvtxHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT   = cms.PSet(EffnvtxHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #EffrelisoHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = cms.PSet(EffrelisoHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT),
        #
        #EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT     = cms.PSet(EffptHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        #EffstHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT     = cms.PSet(EffstHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        #EffhtHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT     = cms.PSet(EffhtHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        #EffmetHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT    = cms.PSet(EffmetHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        #EffetaHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT    = cms.PSet(EffetaHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        #EffnvtxHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT   = cms.PSet(EffnvtxHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        #EffrelisoHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT = cms.PSet(EffrelisoHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT),
        
        #NoPU version
        #EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffstHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffstHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffhtHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffhtHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffmetHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffmetHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffetaHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffetaHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffnvtxHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = cms.PSet(EffnvtxHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffrelisoHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(EffrelisoHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #
        #EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffptHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffstHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffstHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffhtHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffhtHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffmetHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffmetHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffetaHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffetaHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffnvtxHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = cms.PSet(EffnvtxHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffrelisoHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = cms.PSet(EffrelisoHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        
        #EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffstHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffstHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffhtHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.PSet(EffhtHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffmetHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffmetHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffetaHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45    = cms.PSet(EffetaHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffnvtxHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   = cms.PSet(EffnvtxHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #EffrelisoHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(EffrelisoHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #
        #EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffptHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffstHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffstHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffhtHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.PSet(EffhtHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffmetHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffmetHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffetaHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50    = cms.PSet(EffetaHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffnvtxHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50   = cms.PSet(EffnvtxHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),
        #EffrelisoHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = cms.PSet(EffrelisoHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50),

        #EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT     = cms.PSet(EffptHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #EffstHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT     = cms.PSet(EffstHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #EffhtHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT     = cms.PSet(EffhtHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #EffmetHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT    = cms.PSet(EffmetHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #EffetaHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT    = cms.PSet(EffetaHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #EffnvtxHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT   = cms.PSet(EffnvtxHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #EffrelisoHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = cms.PSet(EffrelisoHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT),
        #
        #EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT     = cms.PSet(EffptHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),
        #EffstHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT     = cms.PSet(EffstHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),
        #EffhtHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT     = cms.PSet(EffhtHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),
        #EffmetHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT    = cms.PSet(EffmetHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),
        #EffetaHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT    = cms.PSet(EffetaHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),
        #EffnvtxHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT   = cms.PSet(EffnvtxHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),
        #EffrelisoHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT = cms.PSet(EffrelisoHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT),

        # HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30
        #EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30     = cms.PSet(EffptHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #EffstHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30     = cms.PSet(EffstHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #EffhtHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30     = cms.PSet(EffhtHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #EffmetHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30    = cms.PSet(EffmetHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #EffetaHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30    = cms.PSet(EffetaHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #EffnvtxHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30   = cms.PSet(EffnvtxHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(EffrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        
        # Cumulative X - reliso plots:
        #Effreliso001HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso001HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso002HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso002HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso004HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso004HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso006HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso006HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso009HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso009HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso012HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso012HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso015HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso015HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso020HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso020HLT_Ele30_CaloIdVT_TrkIdT),
        #Effreliso025HLT_Ele30_CaloIdVT_TrkIdT = cms.PSet(Effreliso025HLT_Ele30_CaloIdVT_TrkIdT),
        #
        #Effreliso001HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso001HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso002HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso002HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso004HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso004HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso006HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso006HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso009HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso009HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso012HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso012HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso015HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso015HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso020HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso020HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #Effreliso025HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.PSet(Effreliso025HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45),
        #
        #Effreliso001HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso001HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso002HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso002HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso004HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso004HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso006HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso006HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso009HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso009HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso012HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso012HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso015HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso015HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso020HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso020HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        #Effreliso025HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30 = cms.PSet(Effreliso025HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30),
        
        #stlep try
        #EffstHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL = cms.PSet(EffstHLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL),
        
        #debug  = cms.PSet(debug),
        
        #EffptHLT_Ele27_WP80 = cms.PSet(EffptHLT_Ele27_WP80),
        #EffetaHLT_Ele27_WP80 = cms.PSet(EffetaHLT_Ele27_WP80),
        
        #EffptHLT_Ele27_WP80 = cms.PSet(effSpec_Ele27_WP80_pt),
    )
    MCEfficiencies = DataEfficiencies.clone()
    
else:
    DataEfficiencies = cms.PSet(
        #passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt),
    #    passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt),
        #passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_30_pt = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_30_pt),
        #passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_65_pt = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_65_pt),
    #    passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt),
    #    passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt),
        # #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt),
        # #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt),
    #    passing_HT350_Ele30_CaloIdT_TrkIdT_pt = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt),
    #    passing_HT400_Ele60_CaloIdT_TrkIdT_pt = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt),
        # #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt),
    
        #passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_eta = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_eta),
        passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta),
        passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta),
        passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_eta),
        #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_eta),
        #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_eta),
        passing_HT350_Ele30_CaloIdT_TrkIdT_eta = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_eta),
        passing_HT400_Ele60_CaloIdT_TrkIdT_eta = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_eta),
        #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_eta),
        
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_ht = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_ht),
    ##     passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_ht),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_ht = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_ht),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_ht = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_ht),
        
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_met = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_met),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_met = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_met),
        
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_reliso = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_reliso),
    ##     passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_reliso),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_reliso = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_reliso),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_reliso = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_reliso),
        
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_nvtx),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_nvtx = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_nvtx),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_nvtx = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_nvtx),
    )
    
    MCEfficiencies = cms.PSet(
        #passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_pt),
        passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt),
        passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_30_pt = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_30_pt),
        passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_65_pt = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_with_ET_BINS_65_pt),
        #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_pt),
        #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_pt),
        # #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_pt),
        # #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_pt),
        #passing_HT350_Ele30_CaloIdT_TrkIdT_pt = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_pt),
        #passing_HT400_Ele60_CaloIdT_TrkIdT_pt = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_pt),
        # #passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_pt),
    
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_eta = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_eta),
        passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_eta),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_eta),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_eta),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_eta),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_eta = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_eta),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_eta = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_eta),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_eta = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_eta),
        
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_ht = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_ht),
    ##     passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_ht),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_ht = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_ht),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_ht = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_ht),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_ht = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_ht),
        
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_met = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_met),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_met = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_met),
        
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_reliso = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_reliso),
    ##     passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_reliso),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_reliso = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_reliso),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_reliso = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_reliso),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_reliso = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_reliso),
        
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele10_CaloIdL_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_nvtx),
    ##     passing_HT350_Ele30_CaloIdT_TrkIdT_nvtx = cms.PSet(effSpec_HT350_Ele30_CaloIdT_TrkIdT_nvtx),
    ##     passing_HT400_Ele60_CaloIdT_TrkIdT_nvtx = cms.PSet(effSpec_HT400_Ele60_CaloIdT_TrkIdT_nvtx),
    ##     passing_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_nvtx = cms.PSet(effSpec_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_nvtx),
    )

if not isMC:
    EfficiencySelection = DataEfficiencies
else:
    EfficiencySelection = MCEfficiencies

if not set2012:
    process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        InputFileNames = selectedAll,
        InputTreeName = cms.string("fitter_tree"),
        InputDirectoryName = cms.string("goodPATEleToHLT"),
        OutputFileName = cms.string(output),
        
        NumCPU = cms.uint32(5),
        SaveWorkspace = cms.bool(False),
        binnedFit = cms.bool(False),
        binsForFit = cms.uint32(40),    
        WeightVariable = cms.string(weightVar),
    
        Variables = cms.PSet(
            weight   = cms.vstring("MC event weight", "0", "10000", ""),
            mass = cms.vstring("Tag-Electron Mass", "55", "120", "GeV/c^{2}"),
            probe_gsfEle_et = cms.vstring("electron e_{T}", "0", "1000", "GeV/c"),
            probe_gsfEle_eta    = cms.vstring("electron #eta", "-2.5", "2.5", ""),
            probe_gsfEle_abseta = cms.vstring("electron |#eta|", "0", "2.5", ""),
    #        probe_gsfEle_phi    = cms.vstring("electron #phi at vertex", "-3.1416", "3.1416", ""),
    #        probe_gsfEle_charge = cms.vstring("electron charge", "-2.5", "2.5", ""),
    #        tag_gsfEle_pt = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
            nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
            probe_gsfEle_ecaliso    = cms.vstring("Probe ecal iso", "-2", "9999999", ""),
            probe_gsfEle_hcaliso    = cms.vstring("Probe hcal iso", "-2", "9999999", ""),
            probe_gsfEle_trackiso    = cms.vstring("Probe trk iso", "-2", "9999999", ""),
    #        tag_gsfEle_ecaliso = cms.vstring("Tag ecal iso", "-2", "9999999", ""),
    #        tag_gsfEle_hcaliso = cms.vstring("Tag hcal iso", "-2", "9999999", ""),
    #        tag_gsfEle_trackiso = cms.vstring("Tag trk iso", "-2", "9999999", ""),
    #        d0_v     = cms.vstring("electron d0_{vertex}"  , "-20", "20", "cm"),
            d0_b     = cms.vstring("electron d0_{beamspot}", "-20", "20", "cm"),
            dz_v     = cms.vstring("electron dz_{vertex}"  , "-20", "20", "cm"),
    #        dz_b     = cms.vstring("electron dz_{beamspot}", "-20", "20", "cm"),
    #        drjet  = cms.vstring("electron-jet_{pt>30} #DeltaR", "0", "10000000000", ""),
    #        njet   = cms.vstring("number of jets_{pt>30}", "0", "100", ""),
    #        tag_d0_v     = cms.vstring("Tag electron d0_{vertex}"  , "-20", "20", "cm"),
    #        tag_d0_b     = cms.vstring("Tag electron d0_{beamspot}", "-20", "20", "cm"),
    #        tag_dz_v     = cms.vstring("Tag electron dz_{vertex}"  , "-20", "20", "cm"),
    #        tag_dz_b     = cms.vstring("Tag electron dz_{beamspot}", "-20", "20", "cm"),
            tag_ht       = cms.vstring("Event HT", "0", "600", "GeV"),
            tag_met       = cms.vstring("Event MET", "0", "600", "GeV"),
            tag_passingHLT_Ele15_HT250_PFMHT25 = cms.vstring("Event passing HLT_Ele15_HT250_PFMHT25", "-0.5", "1.5", ""),
            tag_passingHLT_Ele15_HT250_PFMHT40 = cms.vstring("Event passing HLT_Ele15_HT250_PFMHT40", "-0.5", "1.5", ""),
    #        tag_HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT   = cms.vstring("Tag fired HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*", "0", "2", ""),
        ),
    
        Categories = cms.PSet(
    #        probe_passingGOOD   = cms.vstring("electronID('simpleEleId80cIso') == 7", "dummy[pass=1,fail=0]"),
    #        probe_passingGOODNoIso   = cms.vstring("electronID('simpleEleId80cIso') == 5", "dummy[pass=1,fail=0]"),
    #        probe_passingID   = cms.vstring("electronID('simpleEleId80cIso') == 5 or 7", "dummy[pass=1,fail=0]"),
            HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.vstring("Electron passing HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200", "dummy[pass=1,fail=0]"), 
            HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Electron passing HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250  = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250 ", "dummy[pass=1,fail=0]"), 
    #        HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix  = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix ", "dummy[pass=1,fail=0]"),  
            HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL        = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL       ", "dummy[pass=1,fail=0]"),  
    ##         HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele17_CaloIdL_CaloIsoVL                        = cms.vstring("Electron passing HLT_Ele17_CaloIdL_CaloIsoVL                       ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.vstring("Electron passing HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL      ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele25_WP80_PFMT40                              = cms.vstring("Electron passing HLT_Ele25_WP80_PFMT40                             ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele27_WP70_PFMT40_PFMHT20                      = cms.vstring("Electron passing HLT_Ele27_WP70_PFMT40_PFMHT20                     ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Electron passing HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele32_WP70_PFMT50                              = cms.vstring("Electron passing HLT_Ele32_WP70_PFMT50                             ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Electron passing HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele45_CaloIdVT_TrkIdT                          = cms.vstring("Electron passing HLT_Ele45_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele52_CaloIdVT_TrkIdT                          = cms.vstring("Electron passing HLT_Ele52_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele65_CaloIdVT_TrkIdT                          = cms.vstring("Electron passing HLT_Ele65_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele8                                           = cms.vstring("Electron passing HLT_Ele8                                          ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele8_CaloIdL_CaloIsoVL                         = cms.vstring("Electron passing HLT_Ele8_CaloIdL_CaloIsoVL                        ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                   = cms.vstring("Electron passing HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                  ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele8_CaloIdL_TrkIdVL                           = cms.vstring("Electron passing HLT_Ele8_CaloIdL_TrkIdVL                          ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL        = cms.vstring("Electron passing HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
    ##         HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL        = cms.vstring("Electron passing HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
            matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.vstring("Probe matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25", "dummy[pass=1,fail=0]"),
            matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.vstring("Probe matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40", "dummy[pass=1,fail=0]"),
            HT350_Ele30_CaloIdT_TrkIdT                         = cms.vstring("Electron passing HLT_HT350_Ele30_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            HT400_Ele60_CaloIdT_TrkIdT                         = cms.vstring("Electron passing HLT_HT400_Ele60_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            tag_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.vstring("Tag passing HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200", "dummy[pass=1,fail=0]"), 
            tag_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Tag passing HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250  = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250 ", "dummy[pass=1,fail=0]"), 
    #        tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix  = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix ", "dummy[pass=1,fail=0]"),  
            tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL        = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL       ", "dummy[pass=1,fail=0]"),  
    ##         tag_HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele17_CaloIdL_CaloIsoVL                        = cms.vstring("Tag passing HLT_Ele17_CaloIdL_CaloIsoVL                       ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.vstring("Tag passing HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL      ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele25_WP80_PFMT40                              = cms.vstring("Tag passing HLT_Ele25_WP80_PFMT40                             ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele27_WP70_PFMT40_PFMHT20                      = cms.vstring("Tag passing HLT_Ele27_WP70_PFMT40_PFMHT20                     ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Tag passing HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele32_WP70_PFMT50                              = cms.vstring("Tag passing HLT_Ele32_WP70_PFMT50                             ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Tag passing HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele45_CaloIdVT_TrkIdT                          = cms.vstring("Tag passing HLT_Ele45_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele52_CaloIdVT_TrkIdT                          = cms.vstring("Tag passing HLT_Ele52_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele65_CaloIdVT_TrkIdT                          = cms.vstring("Tag passing HLT_Ele65_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele8                                           = cms.vstring("Tag passing HLT_Ele8                                          ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele8_CaloIdL_CaloIsoVL                         = cms.vstring("Tag passing HLT_Ele8_CaloIdL_CaloIsoVL                        ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                   = cms.vstring("Tag passing HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                  ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele8_CaloIdL_TrkIdVL                           = cms.vstring("Tag passing HLT_Ele8_CaloIdL_TrkIdVL                          ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL        = cms.vstring("Tag passing HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
    ##         tag_HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL        = cms.vstring("Tag passing HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.vstring("Tag matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25", "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.vstring("Tag matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40", "dummy[pass=1,fail=0]"),
            tag_HT350_Ele30_CaloIdT_TrkIdT                         = cms.vstring("Tag passing HLT_HT350_Ele30_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            tag_HT400_Ele60_CaloIdT_TrkIdT                         = cms.vstring("Tag passing HLT_HT400_Ele60_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
    
    #        tag_Mu24 = cms.vstring("MC true", "dummy[pass=1,fail=0]"),
            mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        ),
        
        Cuts = cms.PSet(
    #        combRelIso15 = cms.vstring("comb. rel. isolation < 0.15", "combRelIso", "0.15"),
        ),
     
        PDFs = cms.PSet(
            #voigtPlusExpo = cms.vstring(
            #    "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            #    "Exponential::backgroundPass(mass, lp[0,-5,5])",
            #    "Exponential::backgroundFail(mass, lf[0,-5,5])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            #vpvPlusExpo = cms.vstring(
            #    "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            #    "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            #    "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
            #    "Voigtian::signal1f(mass, mean1, width, sigma1)",
            #    "Voigtian::signal2f(mass, mean2, width, sigma2)",
            #    "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
            #    "Exponential::backgroundPass(mass, lp[-0.0001.,-1,0.1])",
            #    "Exponential::backgroundFail(mass, lf[-0.0001.,-1,0.1])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            vpvPlusExpo2 = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
                "Voigtian::signal1f(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2f(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
                "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
                "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
            #vpvPlusExpoPassFail = cms.vstring(
            #    "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",     
            #    "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",    
            #    "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",                         
            #    "Voigtian::signal1f(mass, mean1, width, sigma1)",                              
            #    "Voigtian::signal2f(mass, mean2, width, sigma2)",                              
            #    "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",                         
            #    "Exponential::backgroundPass(mass, l[-0.0001.,-1,0.1])",
            #    "Exponential::backgroundFail(mass, l)",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            #vpvPlusExpoMin70 = cms.vstring(
            #    "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            #    "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
            #    "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            #    "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            #    "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            #    "efficiency[0.9,0.7,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            # voigtPlusQuadratic = cms.vstring(
            #    "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            #    "Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1]})",
            #    "Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1]})",
            #    #"Exponential::backgroundPass(mass, lp[0,-5,5])",
            #    #"Exponential::backgroundFail(mass, lf[0,-5,5])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            #vpvPlusQuadratic = cms.vstring(
            #    "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            #    "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            #    "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
            #    "Voigtian::signal1f(mass, mean1, width, sigma1)",
            #    "Voigtian::signal2f(mass, mean2, width, sigma2)",
            #    "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
            #    "Chebychev::backgroundPass(mass, {cPass1[0.,-1,1], cPass2[-0.,-1,1]})",
            #    "Chebychev::backgroundFail(mass, {cFail1[0.,-1,1], cFail2[-0.,-1,1]})",
            #    #"Exponential::backgroundPass(mass, lp[0,-5,5])",
            #    #"Exponential::backgroundFail(mass, lf[0,-5,5])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.99]"
            #),
        ),
    
        Efficiencies = EfficiencySelection,
    )
else:
    process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        InputFileNames = selectedAll,
        InputTreeName = cms.string("fitter_tree"),
        InputDirectoryName = cms.string("goodPATEleToHLT"),
        OutputFileName = cms.string("ElectronEffPlot"+outputFilePrefix+suffix+".root"),
        
        NumCPU = cms.uint32(5),
        SaveWorkspace = cms.bool(False),
        binnedFit = cms.bool(True),
        binsForFit = cms.uint32(40),
        WeightVariable = cms.string(weightVar),
        
        Variables = cms.PSet(
            weight   = cms.vstring("MC event weight", "0", "10000", ""),
            mass = cms.vstring("Tag-Electron Mass", "55", "120", "GeV/c^{2}"),
            probe_gsfEle_et = cms.vstring("electron e_{T}", "0", "1000", "GeV/c"),
            probe_gsfEle_eta    = cms.vstring("electron #eta", "-2.5", "2.5", ""),
            probe_gsfEle_abseta = cms.vstring("electron |#eta|", "0", "2.5", ""),
            #probe_gsfEle_phi    = cms.vstring("electron #phi at vertex", "-3.1416", "3.1416", ""),
            #probe_gsfEle_charge = cms.vstring("electron charge", "-2.5", "2.5", ""),
            #tag_gsfEle_pt = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
            nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
            #probe_gsfEle_ecaliso    = cms.vstring("Probe ecal iso", "-2", "9999999", ""),
            #probe_gsfEle_hcaliso    = cms.vstring("Probe hcal iso", "-2", "9999999", ""),
            #probe_gsfEle_trackiso    = cms.vstring("Probe trk iso", "-2", "9999999", ""),
            #tag_gsfEle_ecaliso = cms.vstring("Tag ecal iso", "-2", "9999999", ""),
            #tag_gsfEle_hcaliso = cms.vstring("Tag hcal iso", "-2", "9999999", ""),
            #tag_gsfEle_trackiso = cms.vstring("Tag trk iso", "-2", "9999999", ""),
            d0_v     = cms.vstring("electron d0_{vertex}"  , "-20", "20", "cm"),
            #d0_b     = cms.vstring("electron d0_{beamspot}", "-20", "20", "cm"),
            dz_v     = cms.vstring("electron dz_{vertex}"  , "-20", "20", "cm"),
            #dz_b     = cms.vstring("electron dz_{beamspot}", "-20", "20", "cm"),
            drjet  = cms.vstring("electron-jet_{pt>30} #DeltaR", "0", "10000000000", ""),
            #njet   = cms.vstring("number of jets_{pt>30}", "0", "100", ""),
            #tag_d0_v     = cms.vstring("Tag electron d0_{vertex}"  , "-20", "20", "cm"),
            #tag_d0_b     = cms.vstring("Tag electron d0_{beamspot}", "-20", "20", "cm"),
            #tag_dz_v     = cms.vstring("Tag electron dz_{vertex}"  , "-20", "20", "cm"),
            #tag_dz_b     = cms.vstring("Tag electron dz_{beamspot}", "-20", "20", "cm"),
            tag_ht        = cms.vstring("Event HT", "0", "600", "GeV"),
            tag_met       = cms.vstring("Event MET", "0", "600", "GeV"),
            #tag_passingHLT_Ele15_HT250_PFMHT25 = cms.vstring("Event passing HLT_Ele15_HT250_PFMHT25", "-0.5", "1.5", ""),
            #tag_passingHLT_Ele15_HT250_PFMHT40 = cms.vstring("Event passing HLT_Ele15_HT250_PFMHT40", "-0.5", "1.5", ""),
            #tag_HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT   = cms.vstring("Tag fired HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*", "0", "2", ""),
            reliso        = cms.vstring("Probe Rel. Isolation", "0",  "10", ""),
            absdeltapt    = cms.vstring("Probe Rel. Isolation", "-10000",  "10000", "GeV/c"),
            stlep         = cms.vstring("Probe ST", "0",  "10000", "GeV"),
            # 2012 Cross Triggers
            tag_passingHLT_CleanPFHT350_Ele5_PFMET45      = cms.vstring("Event passing HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",     "0", "2", ""),
            tag_passingHLT_CleanPFHT350_Ele5_PFMET50      = cms.vstring("Event passing HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",     "0", "2", ""),
            tag_passingHLT_CleanPFNoPUHT350_Ele5_PFMET45  = cms.vstring("Event passing HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*", "0", "2", ""),
            tag_passingHLT_CleanPFNoPUHT350_Ele5_PFMET50  = cms.vstring("Event passing HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*", "0", "2", ""),
            tag_passingHLT_CleanPFHT300_Ele15_PFMET45     = cms.vstring("Event passing HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",    "0", "2", ""),
            tag_passingHLT_CleanPFHT300_Ele15_PFMET50     = cms.vstring("Event passing HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",    "0", "2", ""),
            tag_passingHLT_CleanPFNoPUHT300_Ele15_PFMET45 = cms.vstring("Event passing HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","0", "2", ""),
            tag_passingHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.vstring("Event passing HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*","0", "2", ""),
            tag_passingHLT_CleanPFHT300_Ele40             = cms.vstring("Event passing HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*",                              "0", "2", ""),
            tag_passingHLT_CleanPFHT300_Ele60             = cms.vstring("Event passing HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*",                              "0", "2", ""),
            tag_passingHLT_CleanPFNoPUHT300_Ele40         = cms.vstring("Event passing HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*",                          "0", "2", ""),
            tag_passingHLT_CleanPFNoPUHT300_Ele60         = cms.vstring("Event passing HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*",                          "0", "2", ""),
            tag_passingHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30    = cms.vstring("Event passing HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v*",  "0", "2", ""),
        ),
    
        Categories = cms.PSet(
            #tag_Mu24 = cms.vstring("MC true", "dummy[pass=1,fail=0]"),
            mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
            ##probe_passingGOOD   = cms.vstring("electronID('simpleEleId80cIso') == 7", "dummy[pass=1,fail=0]"),
            ##probe_passingGOODNoIso   = cms.vstring("electronID('simpleEleId80cIso') == 5", "dummy[pass=1,fail=0]"),
            ##probe_passingID   = cms.vstring("electronID('simpleEleId80cIso') == 5 or 7", "dummy[pass=1,fail=0]"),
            #HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.vstring("Electron passing HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200", "dummy[pass=1,fail=0]"), 
            #HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Electron passing HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            #HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            #HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250  = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250 ", "dummy[pass=1,fail=0]"), 
            ##HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix  = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix ", "dummy[pass=1,fail=0]"),  
            #HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL        = cms.vstring("Electron passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL       ", "dummy[pass=1,fail=0]"),  
            ###HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele17_CaloIdL_CaloIsoVL                        = cms.vstring("Electron passing HLT_Ele17_CaloIdL_CaloIsoVL                       ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.vstring("Electron passing HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL      ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele25_WP80_PFMT40                              = cms.vstring("Electron passing HLT_Ele25_WP80_PFMT40                             ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele27_WP70_PFMT40_PFMHT20                      = cms.vstring("Electron passing HLT_Ele27_WP70_PFMT40_PFMHT20                     ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Electron passing HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele32_WP70_PFMT50                              = cms.vstring("Electron passing HLT_Ele32_WP70_PFMT50                             ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Electron passing HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Electron passing HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele45_CaloIdVT_TrkIdT                          = cms.vstring("Electron passing HLT_Ele45_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele52_CaloIdVT_TrkIdT                          = cms.vstring("Electron passing HLT_Ele52_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele65_CaloIdVT_TrkIdT                          = cms.vstring("Electron passing HLT_Ele65_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele8                                           = cms.vstring("Electron passing HLT_Ele8                                          ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele8_CaloIdL_CaloIsoVL                         = cms.vstring("Electron passing HLT_Ele8_CaloIdL_CaloIsoVL                        ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                   = cms.vstring("Electron passing HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                  ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele8_CaloIdL_TrkIdVL                           = cms.vstring("Electron passing HLT_Ele8_CaloIdL_TrkIdVL                          ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL        = cms.vstring("Electron passing HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
            ###HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL        = cms.vstring("Electron passing HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
            #matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.vstring("Probe matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25", "dummy[pass=1,fail=0]"),
            #matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.vstring("Probe matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40", "dummy[pass=1,fail=0]"),
            #HT350_Ele30_CaloIdT_TrkIdT                         = cms.vstring("Electron passing HLT_HT350_Ele30_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            #HT400_Ele60_CaloIdT_TrkIdT                         = cms.vstring("Electron passing HLT_HT400_Ele60_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            #tag_HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.vstring("Tag passing HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200", "dummy[pass=1,fail=0]"), 
            #tag_HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Tag passing HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            #tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200 ", "dummy[pass=1,fail=0]"), 
            #tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250  = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250 ", "dummy[pass=1,fail=0]"), 
            ##tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix  = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix ", "dummy[pass=1,fail=0]"),  
            #tag_HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL        = cms.vstring("Tag passing HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL       ", "dummy[pass=1,fail=0]"),  
            ###tag_HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele17_CaloIdL_CaloIsoVL                        = cms.vstring("Tag passing HLT_Ele17_CaloIdL_CaloIsoVL                       ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.vstring("Tag passing HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL      ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele25_WP80_PFMT40                              = cms.vstring("Tag passing HLT_Ele25_WP80_PFMT40                             ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele27_WP70_PFMT40_PFMHT20                      = cms.vstring("Tag passing HLT_Ele27_WP70_PFMT40_PFMHT20                     ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Tag passing HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele32_WP70_PFMT50                              = cms.vstring("Tag passing HLT_Ele32_WP70_PFMT50                             ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.vstring("Tag passing HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL     ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.vstring("Tag passing HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT        ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele45_CaloIdVT_TrkIdT                          = cms.vstring("Tag passing HLT_Ele45_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele52_CaloIdVT_TrkIdT                          = cms.vstring("Tag passing HLT_Ele52_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele65_CaloIdVT_TrkIdT                          = cms.vstring("Tag passing HLT_Ele65_CaloIdVT_TrkIdT                         ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele8                                           = cms.vstring("Tag passing HLT_Ele8                                          ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele8_CaloIdL_CaloIsoVL                         = cms.vstring("Tag passing HLT_Ele8_CaloIdL_CaloIsoVL                        ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                   = cms.vstring("Tag passing HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                  ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele8_CaloIdL_TrkIdVL                           = cms.vstring("Tag passing HLT_Ele8_CaloIdL_TrkIdVL                          ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL        = cms.vstring("Tag passing HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
            ###tag_HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL        = cms.vstring("Tag passing HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL       ", "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.vstring("Tag matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25", "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.vstring("Tag matched to Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40", "dummy[pass=1,fail=0]"),
            #tag_HT350_Ele30_CaloIdT_TrkIdT                         = cms.vstring("Tag passing HLT_HT350_Ele30_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            #tag_HT400_Ele60_CaloIdT_TrkIdT                         = cms.vstring("Tag passing HLT_HT400_Ele60_CaloIdT_TrkIdT                    ", "dummy[pass=1,fail=0]"),
            # 2012 Triggers
            HLT_Ele22_CaloIdL_CaloIsoVL                                         = cms.vstring("Electron passing HLT_Ele22_CaloIdL_CaloIsoVL_v*",                                        "dummy[pass=1,fail=0]"),
            HLT_Ele27_CaloIdL_CaloIsoVL                                         = cms.vstring("Electron passing HLT_Ele27_CaloIdL_CaloIsoVL_v*",                                        "dummy[pass=1,fail=0]"),
            HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL                        = cms.vstring("Electron passing HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",                       "dummy[pass=1,fail=0]"),
            HLT_Ele27_WP80                                                      = cms.vstring("Electron passing HLT_Ele27_WP80_v*",                                                     "dummy[pass=1,fail=0]"),
            HLT_Ele27_WP80_PFMET_MT50                                           = cms.vstring("Electron passing HLT_Ele27_WP80_PFMET_MT50_v*",                                          "dummy[pass=1,fail=0]"),
            #HLT_Ele27_WP80_CentralPFJet80                                       = cms.vstring("Electron passing HLT_Ele27_WP80_CentralPFJet80_v*",                                      "dummy[pass=1,fail=0]"),
            #HLT_Ele27_WP80_WCandPt80                                            = cms.vstring("Electron passing HLT_Ele27_WP80_WCandPt80_v*",                                           "dummy[pass=1,fail=0]"),
            HLT_Ele30_CaloIdVT_TrkIdT                                           = cms.vstring("Electron passing HLT_Ele30_CaloIdVT_TrkIdT_v*",                                          "dummy[pass=1,fail=0]"),
            HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL                        = cms.vstring("Electron passing HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",                       "dummy[pass=1,fail=0]"),
            HLT_Ele65_CaloIdVT_TrkIdT                                           = cms.vstring("Electron passing HLT_Ele65_CaloIdVT_TrkIdT_v*",                                          "dummy[pass=1,fail=0]"),
            HLT_Ele80_CaloIdVT_TrkIdT                                           = cms.vstring("Electron passing HLT_Ele80_CaloIdVT_TrkIdT_v*",                                          "dummy[pass=1,fail=0]"),
            HLT_Ele80_CaloIdVT_GsfTrkIdT                                        = cms.vstring("Electron passing HLT_Ele80_CaloIdVT_GsfTrkIdT_v*",                                       "dummy[pass=1,fail=0]"),
            HLT_Ele90_CaloIdVT_GsfTrkIdT                                        = cms.vstring("Electron passing HLT_Ele90_CaloIdVT_GsfTrkIdT_v*",                                       "dummy[pass=1,fail=0]"),
            HLT_Ele100_CaloIdVT_TrkIdT                                          = cms.vstring("Electron passing HLT_Ele100_CaloIdVT_TrkIdT_v*",                                         "dummy[pass=1,fail=0]"),
            HLT_Ele8_CaloIdT_TrkIdVL_Jet30                                      = cms.vstring("Electron passing HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v*",                                     "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45      = cms.vstring("Electron matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",    "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50      = cms.vstring("Electron matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",    "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45  = cms.vstring("Electron matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50  = cms.vstring("Electron matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*","dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.vstring("Electron matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",   "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.vstring("Electron matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",   "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET4_v*","dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET5_v*","dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT                               = cms.vstring("Electron matched HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT                               = cms.vstring("Electron matched HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT                           = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            #matchedHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT                           = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            HLT_CleanPFHT350_Ele5_PFMET45                                        = cms.vstring("Electron matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",    "dummy[pass=1,fail=0]"),
            HLT_CleanPFHT350_Ele5_PFMET50                                        = cms.vstring("Electron matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",    "dummy[pass=1,fail=0]"),
            HLT_CleanPFNoPUHT350_Ele5_PFMET45                                    = cms.vstring("Electron matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","dummy[pass=1,fail=0]"),
            HLT_CleanPFNoPUHT350_Ele5_PFMET50                                    = cms.vstring("Electron matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*","dummy[pass=1,fail=0]"),
            HLT_CleanPFHT300_Ele15_PFMET45                                       = cms.vstring("Electron matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",   "dummy[pass=1,fail=0]"),
            HLT_CleanPFHT300_Ele15_PFMET50                                       = cms.vstring("Electron matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",   "dummy[pass=1,fail=0]"),
            HLT_CleanPFNoPUHT300_Ele15_PFMET45                                   = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET4_v*","dummy[pass=1,fail=0]"),
            HLT_CleanPFNoPUHT300_Ele15_PFMET50                                   = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET5_v*","dummy[pass=1,fail=0]"),
            HLT_CleanPFHT300_Ele40                                               = cms.vstring("Electron matched HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            HLT_CleanPFHT300_Ele60                                               = cms.vstring("Electron matched HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            HLT_CleanPFNoPUHT300_Ele40                                           = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            HLT_CleanPFNoPUHT300_Ele60                                           = cms.vstring("Electron matched HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            HLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30                                      = cms.vstring("Electron matched HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v*", "dummy[pass=1,fail=0]"),
            tag_HLT_Ele22_CaloIdL_CaloIsoVL                                         = cms.vstring("Tag passing HLT_Ele22_CaloIdL_CaloIsoVL_v*",                                        "dummy[pass=1,fail=0]"),
            tag_HLT_Ele27_CaloIdL_CaloIsoVL                                         = cms.vstring("Tag passing HLT_Ele27_CaloIdL_CaloIsoVL_v*",                                        "dummy[pass=1,fail=0]"),
            tag_HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL                        = cms.vstring("Tag passing HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",                       "dummy[pass=1,fail=0]"),
            tag_HLT_Ele27_WP80                                                      = cms.vstring("Tag passing HLT_Ele27_WP80_v*",                                                     "dummy[pass=1,fail=0]"),
            tag_HLT_Ele27_WP80_PFMET_MT50                                           = cms.vstring("Tag passing HLT_Ele27_WP80_PFMET_MT50_v*",                                          "dummy[pass=1,fail=0]"),
            #tag_HLT_Ele27_WP80_CentralPFJet80                                       = cms.vstring("Tag passing HLT_Ele27_WP80_CentralPFJet80_v*",                                      "dummy[pass=1,fail=0]"),
            #tag_HLT_Ele27_WP80_WCandPt80                                            = cms.vstring("Tag passing HLT_Ele27_WP80_WCandPt80_v*",                                           "dummy[pass=1,fail=0]"),
            tag_HLT_Ele30_CaloIdVT_TrkIdT                                           = cms.vstring("Tag passing HLT_Ele30_CaloIdVT_TrkIdT_v*",                                          "dummy[pass=1,fail=0]"),
            tag_HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL                        = cms.vstring("Tag passing HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",                       "dummy[pass=1,fail=0]"),
            tag_HLT_Ele65_CaloIdVT_TrkIdT                                           = cms.vstring("Tag passing HLT_Ele65_CaloIdVT_TrkIdT_v*",                                          "dummy[pass=1,fail=0]"),
            tag_HLT_Ele80_CaloIdVT_TrkIdT                                           = cms.vstring("Tag passing HLT_Ele80_CaloIdVT_TrkIdT_v*",                                          "dummy[pass=1,fail=0]"),
            tag_HLT_Ele80_CaloIdVT_GsfTrkIdT                                        = cms.vstring("Tag passing HLT_Ele80_CaloIdVT_GsfTrkIdT_v*",                                       "dummy[pass=1,fail=0]"),
            tag_HLT_Ele90_CaloIdVT_GsfTrkIdT                                        = cms.vstring("Tag passing HLT_Ele90_CaloIdVT_GsfTrkIdT_v*",                                       "dummy[pass=1,fail=0]"),
            tag_HLT_Ele100_CaloIdVT_TrkIdT                                          = cms.vstring("Tag passing HLT_Ele100_CaloIdVT_TrkIdT_v*",                                         "dummy[pass=1,fail=0]"),
            tag_HLT_Ele8_CaloIdT_TrkIdVL_Jet30                                      = cms.vstring("Tag passing HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v*",                                     "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45      = cms.vstring("Tag matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",    "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50      = cms.vstring("Tag matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",    "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45  = cms.vstring("Tag matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50  = cms.vstring("Tag matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*","dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     = cms.vstring("Tag matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",   "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     = cms.vstring("Tag matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",   "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET4_v*","dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET5_v*","dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT                               = cms.vstring("Tag matched HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT                               = cms.vstring("Tag matched HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT                           = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT                           = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFHT350_Ele5_PFMET45                                        = cms.vstring("Tag matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",    "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFHT350_Ele5_PFMET50                                        = cms.vstring("Tag matched HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",    "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFNoPUHT350_Ele5_PFMET45                                    = cms.vstring("Tag matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFNoPUHT350_Ele5_PFMET50                                    = cms.vstring("Tag matched HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*","dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFHT300_Ele15_PFMET45                                       = cms.vstring("Tag matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",   "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFHT300_Ele15_PFMET50                                       = cms.vstring("Tag matched HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",   "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFNoPUHT300_Ele15_PFMET45                                   = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET4_v*","dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFNoPUHT300_Ele15_PFMET50                                   = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET5_v*","dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFHT300_Ele40                                               = cms.vstring("Tag matched HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFHT300_Ele60                                               = cms.vstring("Tag matched HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*",                             "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFNoPUHT300_Ele40                                           = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_CleanPFNoPUHT300_Ele60                                           = cms.vstring("Tag matched HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*",                         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30                                      = cms.vstring("Tag matched HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v*", "dummy[pass=1,fail=0]"),

        ),
        Cuts = cms.PSet(
            #combRelIso15 = cms.vstring("comb. rel. isolation < 0.15", "combRelIso", "0.15"),
        ),
     
        PDFs = cms.PSet(
            voigtPlusExpo = cms.vstring(
                "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
                "Exponential::backgroundPass(mass, lp[0,-5,5])",
                "Exponential::backgroundFail(mass, lf[0,-5,5])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
            vpvPlusExpo = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",     
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",    
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",                         
                "Voigtian::signal1f(mass, mean1, width, sigma1)",                              
                "Voigtian::signal2f(mass, mean2, width, sigma2)",                              
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",                         
                "Exponential::backgroundPass(mass, lp[-0.0001.,-1,0.1])",
                "Exponential::backgroundFail(mass, lf[-0.0001.,-1,0.1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
            vpvPlusExpo2 = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
                "Voigtian::signal1f(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2f(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
                "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
                "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
            vpvPlusExpoPassFail = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",     
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",    
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",                         
                "Voigtian::signal1f(mass, mean1, width, sigma1)",                              
                "Voigtian::signal2f(mass, mean2, width, sigma2)",                              
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",                         
                "Exponential::backgroundPass(mass, l[-0.0001.,-1,0.1])",
                "Exponential::backgroundFail(mass, l)",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
            vpvPlusExpoMin70 = cms.vstring(
                "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
                "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
                "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
                "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
                "efficiency[0.9,0.7,1]",
                "signalFractionInPassing[0.9]"
            ),
             voigtPlusQuadratic = cms.vstring(
                "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
                "Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1]})",
                "Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1]})",
                #"Exponential::backgroundPass(mass, lp[0,-5,5])",
                #"Exponential::backgroundFail(mass, lf[0,-5,5])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
            vpvPlusQuadratic = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
                "Voigtian::signal1f(mass, mean1, width, sigma1)",
                "Voigtian::signal2f(mass, mean2, width, sigma2)",
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
                "Chebychev::backgroundPass(mass, {cPass1[0.,-1,1], cPass2[-0.,-1,1]})",
                "Chebychev::backgroundFail(mass, {cFail1[0.,-1,1], cFail2[-0.,-1,1]})",
                #"Exponential::backgroundPass(mass, lp[0,-5,5])",
                #"Exponential::backgroundFail(mass, lf[0,-5,5])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.99]"
            ),
        ),
    
        Efficiencies = EfficiencySelection,
    )

process.fit = cms.Path(
    process.TagProbeFitTreeAnalyzer
)

