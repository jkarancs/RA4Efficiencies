import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )    


daten=True
useData = "Test" #Single / Had / All / Test
set2012=True

if set2012:
    #main_dir = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120911'
    #main_dir = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120913'
    #main_dir = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120928'
    main_dir = '/home/jkarancs/gridout/LeptonEfficiency/Mu_121203' # MuHad Note plots
    #main_dir = '/home/jkarancs/gridout/LeptonEfficiency/Mu_ID_130110' # IsoMu24_eta2p1 only
else:
    #main_dir = '/home/veszpv/project/CMSSW_4_2_8_patch7/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_111124'
    main_dir = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_111124'

pathNamesData_Single = [
    #main_dir+"/Data/SingleMu_Run2012A-13Jul2012-v1/",
    #main_dir+"/Data/SingleMu_Run2012A-recover-06Aug2012-v1/",
    #main_dir+"/Data/SingleMu_Run2012B-13Jul2012-v1/",
    #main_dir+"/Data/SingleMu_Run2012C-24Aug2012-v1/",
    #main_dir+"/Data/SingleMu_Run2012C-PromptReco-v2/",
    main_dir+"/Data/SingleMu_Run2012D-PromptReco-v1/",
]
pathNamesData_Had = [
    main_dir+"/Data/MuHad_Run2012A-13Jul2012-v1/",
    main_dir+"/Data/MuHad_Run2012A-recover-06Aug2012-v1/",
    main_dir+"/Data/MuHad_Run2012B-13Jul2012-v1/",
    main_dir+"/Data/MuHad_Run2012C-24Aug2012-v1/",
    main_dir+"/Data/MuHad_Run2012C-PromptReco-v2/",
    main_dir+"/Data/MuHad_Run2012D-PromptReco-v1/",
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

if set2012:
    #suffix = "_All2012"
    suffix = "_2012D"
else:
    suffix = "2011"

outputFilePrefix = ""
pathNames = []

if daten:
    suffix = useData + suffix
    outputFilePrefix = "Data"
    pathNames = pathNamesData_Single
    if (useData == "Single"): pathNames = pathNamesData_Single
    if (useData == "Double"): pathNames = pathNamesData_Double
    if (useData == "Had"): pathNames = pathNamesData_Had
    if (useData == "Test"): pathNames = pathNamesData_Had
    #if (useData == "All"): pathNames = pathNamesData_Single + pathNamesData_Double + pathNamesData_Had
    if (useData == "All"): pathNames = pathNamesData_Single + pathNamesData_Had
    weightVar = ""
    unbinnedVarDef = cms.vstring("mass")
    subdir  = ""
else:
    outputFilePrefix = "MC"
    if (useData == "Test"): outputFilePrefix = "MCTest"
    pathNames = pathNamesMC
    weightVar = "weight"   
    unbinnedVarDef = cms.vstring("mass",weightVar)
    subdir  = "vtx_reweighted/"

output="MuonEffPlot"+outputFilePrefix+suffix+".root"

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



#if daten:
#    weightVar=""
#    unbinnedVarDef = cms.vstring("mass")
#    
#    if set2012:
#        #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120911/Data/'
#        #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120913/Data/'
#        #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120928/Data/'
#        path = '/home/jkarancs/gridout/LeptonEfficiency/Mu_121203/Data/'
#        suffix="2012"
#    else:
#        #path = '/home/veszpv/project/CMSSW_4_2_8_patch7/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_111124/Data/'
#        path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_111124/Data/'
#        suffix="2011"
#    
#    bins= []
#    for bin in os.listdir(path):
#        bins.append(str(bin))
#    files = []
#    for bin in bins:
#        for file in os.listdir(path+bin+'/'):
#            files.append(path+bin+'/'+file)
#            print path+bin+'/'+file+"\n"
#    output="./EffPlotData"+suffix+".root"
#else:
#    weightVar="weight"
#    unbinnedVarDef = cms.vstring("mass", "weight")
#    suffix="2012"
#    
#    # 2011
#    #path = '/home/veszpv/project/CMSSW_4_2_8_patch7/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_111027/MC/'
#    #path = '/home/veszpv/project/CMSSW_4_2_8_patch7/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_111124/MC/'
#    # 2012
#    #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120911/MC/'
#    #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120913/MC/'
#    #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/MC_test/'
#    #path = '/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/Mu_120928/MC/'
#    path = '/home/jkarancs/gridout/LeptonEfficiency/Mu_121203/MC/'
#    
#    bins=[]
#    for bin in os.listdir(path):
#        bins.append(str(bin))
#    files = []
#    for bin in bins:
#        if not os.path.exists(path+bin+'/vtx_reweighted/'):
#            continue
#        if bin.partition("_")[0] == "QCD":
#            continue
#        for file in os.listdir(path+bin+'/vtx_reweighted/'):
#            files.append(path+bin+'/vtx_reweighted/'+file)
#            print path+bin+'/vtx_reweighted/'+file+"\n"
#    output="./EffPlotMC"+suffix+".root"


if daten: mc=False
else: mc=True

list=[]
for i in range(-21,24,3):
    list.append(i/10.)




## # 2011
## 
## ##
## ## PT 
## ##
##     
## PT8_BINS = cms.PSet(
##     pt = cms.vdouble(5.0, 6.5, 8.0, 9.5, 11.0, 15.0, 20.0, 50.0, 100.0),
##     #pt = cms.vdouble(5.0, 12.0, 15.0, 20.0, 25.0, 35., 50., 100.0),
##     eta = cms.vdouble(-2.1, 2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## 
## PT10_BINS = cms.PSet(
##     pt = cms.vdouble(5.0, 9.0, 12.0, 14.0, 16.0, 18.0, 21.0, 25.0, 30.0, 36.0, 42.0, 50.0, 58., 100.0),
##     #pt = cms.vdouble(5.0, 12.0, 15.0, 20.0, 25.0, 35., 50., 100.0),
##     eta = cms.vdouble(-2.1, 2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
## )
## 
## 
## PT10_BARREL_BINS = cms.PSet(
##     pt = cms.vdouble(5.0, 9.0, 12.0, 14.0, 16.0, 18.0, 21.0, 25.0, 30.0, 36.0, 42.0, 50.0, 58., 100.0),
##     #pt = cms.vdouble(5.0, 12.0, 15.0, 20.0, 25.0, 35., 50., 100.0),
##     #eta = cms.vdouble(-2.1, 2.1),
##     abs_eta = cms.vdouble(0, 0.8),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## 
## PT10_ENDCAP_BINS = cms.PSet(
##     pt = cms.vdouble(5.0, 9.0, 12.0, 14.0, 16.0, 18.0, 21.0, 25.0, 30.0, 36.0, 42.0, 50.0, 58., 100.0),
##     #pt = cms.vdouble(5.0, 12.0, 15.0, 20.0, 25.0, 35., 50., 100.0),
##     #eta = cms.vdouble(-2.1, 2.1),
##     abs_eta = cms.vdouble(0.8, 2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## 
## PT15_LOWSTAT_BINS = cms.PSet(
##     pt = cms.vdouble(5.0, 14.0, 18.0, 22.0, 26.0, 32.0, 40.0, 50.0, 60., 100.0),
##     #pt = cms.vdouble(5.0, 12.0, 15.0, 20.0, 25.0, 35., 50., 100.0),
##     eta = cms.vdouble(-2.1, 2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## 
## PT30_BINS = cms.PSet(
##     pt = cms.vdouble(15.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60., 100.0),
##     eta = cms.vdouble(-2.1, 2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## 
## PT40_BINS = cms.PSet(
##     pt = cms.vdouble(30, 38, 42.0, 46.0, 50.0, 60., 70., 80.0),
##     #pt = cms.vdouble(5.0, 12.0, 15.0, 20.0, 25.0, 35., 50., 100.0),
##     eta = cms.vdouble(-2.1, 2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## 
## ## Mu8
##     
## Trigger_BIN_Mu8 = cms.PSet(
##     tag_passingHLTMu8 = cms.vdouble(0.5, 1.5),
## )    
## EffptHLTMu8 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu8", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT8_BINS, Trigger_BIN_Mu8),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## Mu15
##     
## Trigger_BIN_Mu15 = cms.PSet(
##     tag_passingHLTMu15 = cms.vdouble(0.5, 1.5),
##     )    
## EffptHLTMu15 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT10_BINS, Trigger_BIN_Mu15),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTMu15Barrel = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT10_BARREL_BINS, Trigger_BIN_Mu15),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTMu15Endcap = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT10_ENDCAP_BINS, Trigger_BIN_Mu15),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTMu15HToff300 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_Mu15, tag_ht = cms.vdouble(300, 1000)),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTMu15_with_PT15_LOWSTAT_BINS = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_Mu15),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTMu15_with_PT30_BINS = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT30_BINS, Trigger_BIN_Mu15),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTMu15_with_PT40_BINS = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("passingHLTMu15", "pass"),# "d0_b002pos", "below", "dz_v1pos", "below", "d0_b002neg", "above","dz_v1neg", "above", "pixlayer1", "above", "relIso10", "below", "deltar03", "above"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT40_BINS, Trigger_BIN_Mu15),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## HT250_Mu15_PFMHT20
##     
## Trigger_BIN_HT250_Mu15_PFMHT20 = cms.PSet(
##     tag_passingHLT_HT250_Mu15_PFMHT20 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_HT250_Mu15_PFMHT20 = cms.vstring("pass"),
## )    
## EffptHLTHT250Mu15PFMHT20 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_HT250_Mu15_PFMHT20", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_HT250_Mu15_PFMHT20),
##     #BinnedVariables = cms.PSet(PT10_BINS, Trigger_BIN_HT250_Mu15_PFMHT20),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## EffptHLTHT250Mu15PFMHT20HToff300 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_HT250_Mu15_PFMHT20", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_HT250_Mu15_PFMHT20, tag_ht = cms.vdouble(300, 1000)),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## HT250_Mu15_PFMHT40
##     
## Trigger_BIN_HT250_Mu15_PFMHT40 = cms.PSet(
##     tag_passingHLT_HT250_Mu15_PFMHT40 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_HT250_Mu15_PFMHT40 = cms.vstring("pass"),
## )    
## EffptHLTHT250Mu15PFMHT40 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_HT250_Mu15_PFMHT40", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_HT250_Mu15_PFMHT40),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## HT300_Mu15_PFMHT40
##     
## Trigger_BIN_HT300_Mu15_PFMHT40 = cms.PSet(
##     tag_passingHLT_HT300_Mu15_PFMHT40 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_HT300_Mu15_PFMHT40 = cms.vstring("pass"),
## )    
## EffptHLTHT300Mu15PFMHT40 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_HT300_Mu15_PFMHT40", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_HT300_Mu15_PFMHT40),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## Mu8_HT200
## 
## Trigger_BIN_Mu8_HT200 = cms.PSet(
##     tag_passingHLT_Mu8_HT200 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_Mu8_HT200 = cms.vstring("pass"),
## )    
## EffptHLTMu8HT200 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu8_HT200", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT8_BINS, Trigger_BIN_Mu8_HT200),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## Mu15_HT200
## 
## Trigger_BIN_Mu15_HT200 = cms.PSet(
##     tag_passingHLT_Mu15_HT200 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_Mu15_HT200 = cms.vstring("pass"),
## )
## EffptHLTMu15HT200 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu15_HT200", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_Mu15_HT200),
##     BinToPDFmap = cms.vstring("vpvPlusExpo"),#"vpvPlusExpo","*pt_bin4*","gaussPlusLinear","*pt_bin5*","vpvPlusQuadratic","*pt_bin6*","vpvPlusQuadratic","*pt_bin7*","vpvPlusQuadratic")
## )
## EffptHLTMu15HT200HToff300 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu15_HT200", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS, Trigger_BIN_Mu15_HT200, tag_ht = cms.vdouble(300, 1000)),
##     BinToPDFmap = cms.vstring("vpvPlusExpo"),#"vpvPlusExpo","*pt_bin4*","gaussPlusLinear","*pt_bin5*","vpvPlusQuadratic","*pt_bin6*","vpvPlusQuadratic","*pt_bin7*","vpvPlusQuadratic")
## )
## 
## ## Mu30_HT200
## 
## Trigger_BIN_Mu30_HT200 = cms.PSet(
##     tag_passingHLT_Mu30_HT200 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_Mu30_HT200 = cms.vstring("pass"),
## )    
## EffptHLTMu30HT200 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu30_HT200", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT30_BINS, Trigger_BIN_Mu30_HT200),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## Mu40_HT200
## 
## Trigger_BIN_Mu40_HT200 = cms.PSet(
##     tag_passingHLT_Mu40_HT200 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_Mu40_HT200 = cms.vstring("pass"),
## )    
## EffptHLTMu40HT200 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_HT200", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT40_BINS, Trigger_BIN_Mu40_HT200),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## ## Mu40_HT300
## 
## Trigger_BIN_Mu40_HT300 = cms.PSet(
##     tag_passingHLT_Mu40_HT300 = cms.vdouble(0.5, 1.5),
##     tag_matchedHLT_Mu40_HT300 = cms.vstring("pass"),
## )    
## EffptHLTMu40HT300 = cms.PSet(
##     EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_HT300", "pass"),
##     UnbinnedVariables = unbinnedVarDef,
##     BinnedVariables = cms.PSet(PT40_BINS, Trigger_BIN_Mu40_HT300),
##     BinToPDFmap = cms.vstring("vpvPlusExpo")
## )
## 
## 
## ##
## ## ETA
## ##
## 
## ETA_HIGHSTAT_BINS = cms.PSet(
##     pt = cms.vdouble(20.0, 200.0),
##     #eta = cms.vdouble(-2.4,-2.0,-1.6,-1.3,-1.0,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0,1.3,1.6,2.0,2.4),
##     eta = cms.vdouble(-2.1,-1.6,-1.3,-1.0,-0.8,-0.6,-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0,1.3,1.6,2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## ETA_LOWSTAT_BINS = cms.PSet(
##     pt = cms.vdouble(20.0, 200.0),
##     eta = cms.vdouble(-2.1,-1.6,-1.2,-0.8,-0.4,0.0,0.4,0.8,1.2,1.6,2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## EffetaHLTMu8 = cms.PSet(EffptHLTMu8)
## EffetaHLTMu8.BinnedVariables = cms.PSet(ETA_HIGHSTAT_BINS, Trigger_BIN_Mu8)
## 
## EffetaHLTMu15 = cms.PSet(EffptHLTMu15)
## EffetaHLTMu15.BinnedVariables = cms.PSet(ETA_HIGHSTAT_BINS, Trigger_BIN_Mu15)
## 
## EffetaHLTMu15_with_ETA_LOWSTAT_BINS = cms.PSet(EffptHLTMu15)
## EffetaHLTMu15_with_ETA_LOWSTAT_BINS.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_Mu15)
## 
## EffetaHLTHT250Mu15PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20)
## EffetaHLTHT250Mu15PFMHT20.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_HT250_Mu15_PFMHT20)
## 
## EffetaHLTHT250Mu15PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40)
## EffetaHLTHT250Mu15PFMHT40.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_HT250_Mu15_PFMHT40)
## 
## EffetaHLTHT300Mu15PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40)
## EffetaHLTHT300Mu15PFMHT40.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_HT300_Mu15_PFMHT40)
## 
## EffetaHLTMu8HT200 = cms.PSet(EffptHLTMu8HT200)
## EffetaHLTMu8HT200.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_Mu8_HT200)
## EffetaHLTMu8HT200.BinnedVariables.pt = cms.vdouble(10.0, 200.0)
## 
## EffetaHLTMu15HT200 = cms.PSet(EffptHLTMu15HT200)
## EffetaHLTMu15HT200.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_Mu15_HT200)
## 
## EffetaHLTMu30HT200 = cms.PSet(EffptHLTMu30HT200)
## EffetaHLTMu30HT200.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_Mu30_HT200)
## EffetaHLTMu30HT200.BinnedVariables.pt = cms.vdouble(30.0, 200.0)
## 
## EffetaHLTMu40HT200 = cms.PSet(EffptHLTMu40HT200)
## EffetaHLTMu40HT200.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_Mu40_HT200)
## EffetaHLTMu40HT200.BinnedVariables.pt = cms.vdouble(42.0, 200.0)
## 
## EffetaHLTMu40HT300 = cms.PSet(EffptHLTMu40HT300)
## EffetaHLTMu40HT300.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS, Trigger_BIN_Mu40_HT300)
## EffetaHLTMu40HT300.BinnedVariables.pt = cms.vdouble(42.0, 200.0)
## 
## ##
## ## HT
## ##
## 
## HT_BINS = cms.PSet(
##     pt = cms.vdouble(20.0, 200.0),
##     eta = cms.vdouble(-2.1,2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
##     tag_ht = cms.vdouble(220., 320., 360., 400., 450, 500, 600., 1000.)
## )
## 
## EffhtHLTMu15 = cms.PSet(EffptHLTMu15)
## EffhtHLTMu15.BinnedVariables = cms.PSet(HT_BINS, Trigger_BIN_Mu15)
## 
## EffhtHLTMu15HT200 = cms.PSet(EffptHLTMu15HT200)
## EffhtHLTMu15HT200.BinnedVariables = cms.PSet(HT_BINS, Trigger_BIN_Mu15_HT200)
## 
## EffhtHLTHT250Mu15PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20)
## EffhtHLTHT250Mu15PFMHT20.BinnedVariables = cms.PSet(HT_BINS, Trigger_BIN_HT250_Mu15_PFMHT20)
## 
## EffhtHLTHT250Mu15PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40)
## EffhtHLTHT250Mu15PFMHT40.BinnedVariables = cms.PSet(HT_BINS, Trigger_BIN_HT250_Mu15_PFMHT40)
## 
## EffhtHLTHT300Mu15PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40)
## EffhtHLTHT300Mu15PFMHT40.BinnedVariables = cms.PSet(HT_BINS, Trigger_BIN_HT300_Mu15_PFMHT40)
## 
## ##
## ## MET
## ##
## 
## MET_BINS = cms.PSet(
##     pt = cms.vdouble(20.0, 200.0),
##     eta = cms.vdouble(-2.1,2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
##     tag_met = cms.vdouble(0., 10., 20., 30., 40., 60., 150.),
## )
## 
## EffmetHLTMu15HToff300 = cms.PSet(EffptHLTMu15)
## EffmetHLTMu15HToff300.BinnedVariables = cms.PSet(MET_BINS, Trigger_BIN_Mu15, tag_ht = cms.vdouble(300, 1000))
## 
## EffmetHLTHT250Mu15PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20)
## EffmetHLTHT250Mu15PFMHT20.BinnedVariables = cms.PSet(MET_BINS, Trigger_BIN_HT250_Mu15_PFMHT20, tag_ht = cms.vdouble(300, 1000))
## 
## EffmetHLTHT250Mu15PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40)
## EffmetHLTHT250Mu15PFMHT40.BinnedVariables = cms.PSet(MET_BINS, Trigger_BIN_HT250_Mu15_PFMHT40, tag_ht = cms.vdouble(300, 1000))
## 
## EffmetHLTHT300Mu15PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40)
## EffmetHLTHT300Mu15PFMHT40.BinnedVariables = cms.PSet(MET_BINS, Trigger_BIN_HT300_Mu15_PFMHT40, tag_ht = cms.vdouble(300, 1000))
## 
## ##
## ## ISOLATION
## ##
## 
## RELISO_BINS = cms.PSet(
##     pt = cms.vdouble(20.0, 200.0),
##     eta = cms.vdouble(-2.1,2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.13, 0.2),
##     drjet = cms.vdouble(0.3, 7),
## )
## 
## EffrelisoHLTMu15 = cms.PSet(EffptHLTMu15)
## EffrelisoHLTMu15.BinnedVariables = cms.PSet(RELISO_BINS, Trigger_BIN_Mu15)
## 
## EffrelisoHLTHT250Mu15PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20)
## EffrelisoHLTHT250Mu15PFMHT20.BinnedVariables = cms.PSet(RELISO_BINS, Trigger_BIN_HT250_Mu15_PFMHT20)
## 
## EffrelisoHLTHT250Mu15PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40)
## EffrelisoHLTHT250Mu15PFMHT40.BinnedVariables = cms.PSet(RELISO_BINS, Trigger_BIN_HT250_Mu15_PFMHT40)
## 
## EffrelisoHLTHT300Mu15PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40)
## EffrelisoHLTHT300Mu15PFMHT40.BinnedVariables = cms.PSet(RELISO_BINS, Trigger_BIN_HT300_Mu15_PFMHT40)
## 
## ##
## ## PILEUP
## ##
## 
## NVTX_BINS = cms.PSet(
##     pt = cms.vdouble(20.0, 200.0),
##     eta = cms.vdouble(-2.1,2.1),
##     d0_b = cms.vdouble(-0.02, 0.02),
##     dz_v = cms.vdouble(-1., 1.),
##     pixlayer = cms.vdouble(1,50),
##     reliso = cms.vdouble(0., 0.1),
##     drjet = cms.vdouble(0.3, 7),
##     tag_nVerticesDA = cms.vdouble(0.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 9.5, 14.5),
## )
## 
## EffnvtxHLTMu15 = cms.PSet(EffptHLTMu15)
## EffnvtxHLTMu15.BinnedVariables = cms.PSet(NVTX_BINS, Trigger_BIN_Mu15)
## 
## EffnvtxHLTHT250Mu15PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20)
## EffnvtxHLTHT250Mu15PFMHT20.BinnedVariables = cms.PSet(NVTX_BINS, Trigger_BIN_HT250_Mu15_PFMHT20)
## 
## EffnvtxHLTHT250Mu15PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40)
## EffnvtxHLTHT250Mu15PFMHT40.BinnedVariables = cms.PSet(NVTX_BINS, Trigger_BIN_HT250_Mu15_PFMHT40)
## 
## EffnvtxHLTHT300Mu15PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40)
## EffnvtxHLTHT300Mu15PFMHT40.BinnedVariables = cms.PSet(NVTX_BINS, Trigger_BIN_HT300_Mu15_PFMHT40)


if set2012:
    ##############
    ##    2012
    ##############
    
    ##
    ## PT
    ##

    CUTS_NOPT_2012 = cms.PSet(
        eta = cms.vdouble(-2.1, 2.1),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.5, 0.5),
        drjet = cms.vdouble(0.3, 7),
        pfreliso = cms.vdouble(0., 0.12),
        absdeltapt = cms.vdouble(-10000, 5.0),
    )
    
    PT10_BINS_2012 = cms.PSet(
        CUTS_NOPT_2012,
        pt = cms.vdouble(5.0, 9.0, 12.0, 14.0, 16.0, 18.0, 21.0, 25.0, 30.0, 36.0, 42.0, 50.0, 58., 100.0),
    )
    PT20_BINS_2012 = cms.PSet(
        CUTS_NOPT_2012,
        pt = cms.vdouble(10.0, 14.0, 17.0, 20.0, 23.0, 26.0, 30.0, 35.0, 41.0, 48.0, 56., 100.0),
    )
    PT40_BINS_2012 = cms.PSet(
        CUTS_NOPT_2012,
        pt = cms.vdouble(30, 38, 42.0, 46.0, 50.0, 60., 70., 80.0),
    )

    PT15_LOWSTAT_BINS_2012 = cms.PSet(
        CUTS_NOPT_2012,
        pt = cms.vdouble(5.0, 14.0, 18.0, 22.0, 26.0, 32.0, 40.0, 50.0, 60., 100.0),
    )

    PT40_BINS_2012 = cms.PSet(
        CUTS_NOPT_2012,
        pt = cms.vdouble(30, 38, 42.0, 46.0, 50.0, 60., 70., 80.0),
    )

    ## Mu8

    Trigger_BIN_Mu8 = cms.PSet(tag_passingHLTMu8 = cms.vdouble(0.5, 1.5))
    
    EffptHLTMu8 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("passingHLTMu8", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT10_BINS_2012, Trigger_BIN_Mu8),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )

    ## IsoMu24

    Trigger_BIN_IsoMu24 = cms.PSet(tag_passingHLTIsoMu24 = cms.vdouble(0.5, 1.5))
    
    EffptHLTIsoMu24 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu24", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT20_BINS_2012, Trigger_BIN_IsoMu24),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )
    
    ## IsoMu24_eta2p1

    Trigger_BIN_IsoMu24_eta2p1 = cms.PSet(tag_passingHLTIsoMu24eta2p1 = cms.vdouble(0.5, 1.5))
    
    EffptHLTIsoMu24eta2p1 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu24eta2p1", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT20_BINS_2012, Trigger_BIN_IsoMu24_eta2p1),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )

    ## IsoMu40_eta2p1

    Trigger_BIN_IsoMu40_eta2p1 = cms.PSet(tag_passingHLTIsoMu40eta2p1 = cms.vdouble(0.5, 1.5))
    
    EffptHLTIsoMu40eta2p1 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu40eta2p1", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT40_BINS_2012, Trigger_BIN_IsoMu40_eta2p1),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )

    ## Mu40_FJHT200
    
    #Trigger_BIN_Mu40_FJHT200 = cms.PSet(
    #    tag_passingHLT_Mu40_FJHT200 = cms.vdouble(0.5, 1.5),
    #    tag_matchedHLT_Mu40_FJHT200 = cms.vstring("pass"),
    #)    
    #EffptHLTMu40FJHT200 = cms.PSet(
    #    EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_FJHT200", "pass"),
    #    UnbinnedVariables = unbinnedVarDef,
    #    BinnedVariables = cms.PSet(PT40_BINS_2012, Trigger_BIN_Mu40_FJHT200),
    #    BinToPDFmap = cms.vstring("vpvPlusExpo")
    #)

    ## PFHT350_Mu15_PFMET50
        
    Trigger_BIN_PFHT350_Mu15_PFMET50 = cms.PSet(
        tag_passingHLT_PFHT350_Mu15_PFMET50 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_PFHT350_Mu15_PFMET50 = cms.vstring("pass"),
    )    
    EffptHLTPFHT350Mu15PFMET50 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_HT350_Mu15_PFMET50", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS_2012, Trigger_BIN_PFHT350_Mu15_PFMET50),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )

    ## PFHT400_Mu5_PFMET45
        
    Trigger_BIN_PFHT400_Mu5_PFMET45 = cms.PSet(
        tag_passingHLT_PFHT400_Mu5_PFMET45 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_PFHT400_Mu5_PFMET45 = cms.vstring("pass"),
    )    
    EffptHLTPFHT400Mu5PFMET45 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_HT400_Mu5_PFMET45", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT15_LOWSTAT_BINS_2012, Trigger_BIN_PFHT400_Mu5_PFMET45),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )
    
    ## Mu40_PFHT350
    
    Trigger_BIN_Mu40_PFHT350 = cms.PSet(
        tag_passingHLT_Mu40_PFHT350 = cms.vdouble(0.5, 1.5),
        tag_matchedHLT_Mu40_PFHT350 = cms.vstring("pass"),
    )    
    EffptHLTMu40PFHT350 = cms.PSet(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_PFHT350", "pass"),
        UnbinnedVariables = unbinnedVarDef,
        BinnedVariables = cms.PSet(PT40_BINS_2012, Trigger_BIN_Mu40_PFHT350),
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )

    ##
    ## ETA
    ##

    CUTS_NOETA_2012 = cms.PSet(
        #pt = cms.vdouble(20.0, 200.0),
        pt = cms.vdouble(40.0, 200.0),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.5, 0.5),
        pfreliso = cms.vdouble(0., 0.12),
        drjet = cms.vdouble(0.3, 7),
    )
    
    ETA_HIGHSTAT_BINS_2012 = cms.PSet(
        CUTS_NOETA_2012,
        eta = cms.vdouble(-2.1,-1.6,-1.3,-1.0,-0.8,-0.6,-0.4,-0.2,0.0,0.2,0.4,0.6,0.8,1.0,1.3,1.6,2.1),
    )
    
    ETA_LOWSTAT_BINS_2012 = cms.PSet(
        CUTS_NOETA_2012,
        #eta = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.6,-0.3,-0.2,0.2,0.3,0.6,0.9,1.2,1.6,2.1,2.4),
        eta = cms.vdouble(-2.1,-1.6,-1.2,-0.9,-0.6,-0.3,-0.2,0.2,0.3,0.6,0.9,1.2,1.6,2.1),
    )

    EffetaHLTMu8 = cms.PSet(EffptHLTMu8)
    EffetaHLTMu8.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS_2012, Trigger_BIN_Mu8)
    
    EffetaHLTIsoMu24 = cms.PSet(EffptHLTIsoMu24)
    EffetaHLTIsoMu24.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS_2012, Trigger_BIN_IsoMu24)

    EffetaHLTIsoMu24eta2p1 = cms.PSet(EffptHLTIsoMu24eta2p1)
    EffetaHLTIsoMu24eta2p1.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS_2012, Trigger_BIN_IsoMu24_eta2p1)

    EffetaHLTIsoMu40eta2p1 = cms.PSet(EffptHLTIsoMu40eta2p1)
    EffetaHLTIsoMu40eta2p1.BinnedVariables = cms.PSet(ETA_LOWSTAT_BINS_2012, Trigger_BIN_IsoMu40_eta2p1)

    ##
    ## NVTX
    ##
    
    NVTX_BINS_2012 = cms.PSet(
        pt = cms.vdouble(40.0, 200.0),
        eta = cms.vdouble(-2.1,2.1),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.5, 0.5),
        pfreliso = cms.vdouble(0., 0.12),
        drjet = cms.vdouble(0.3, 7),
        tag_nVertices = cms.vdouble(0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5),
    )

    EffnvtxHLTIsoMu24eta2p1 = cms.PSet(EffptHLTIsoMu24eta2p1)
    EffnvtxHLTIsoMu24eta2p1.BinnedVariables = cms.PSet(NVTX_BINS_2012, Trigger_BIN_IsoMu24_eta2p1)

    EffnvtxHLTIsoMu40eta2p1 = cms.PSet(EffptHLTIsoMu40eta2p1)
    EffnvtxHLTIsoMu40eta2p1.BinnedVariables = cms.PSet(NVTX_BINS_2012, Trigger_BIN_IsoMu40_eta2p1)

    ###################################
    #       Muon POG Comparison       #
    ###################################
    
    EffTemplate = cms.PSet(
        UnbinnedVariables = unbinnedVarDef,
        BinToPDFmap = cms.vstring("vpvPlusExpo")
    )
    
    CUTS_POG = cms.PSet(
        pt = cms.vdouble(40.0, 200.0),
        eta = cms.vdouble(-2.1, 2.1),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.5, 0.5),
        pfreliso = cms.vdouble(0., 0.12),
        #drjet = cms.vdouble(0.3, 7),
        #absdeltapt = cms.vdouble(-10000, 5.0),
    )
    
    PT24_CUTS_POG = CUTS_POG.clone( pt = cms.vdouble(10, 15, 20, 23, 25, 28, 33, 40, 50,  60, 100) )
    ETA_POG       = CUTS_POG.clone( eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.4) )
    
    ## IsoMu24_eta2p1
    
    BinVar_HLTIsoMu24eta2p1_POG = CUTS_POG.clone(tag_passingHLTIsoMu24eta2p1 = cms.vdouble(0.5, 1.5))
    EffptHLTIsoMu24eta2p1_POG = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu24eta2p1", "pass"),
        BinnedVariables = BinVar_HLTIsoMu24eta2p1_POG.clone( pt = PT24_CUTS_POG.pt )
    )
    EffetaHLTIsoMu24eta2p1_POG = EffptHLTIsoMu24eta2p1_POG.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1_POG.clone(eta = ETA_POG.eta) )
    
    ###################################
    #       Single Muon Triggers      #
    ###################################

    #Mu5
    #Mu12
    #Mu15 (was mainly last year)
    #Mu24
    #IsoMu24
    #IsoMu30
    #IsoMu15_eta2p1_L1ETM20 
    #IsoMu20_eta2p1
    #IsoMu24_eta2p1
    #IsoMu30_eta2p1
    #IsoMu34_eta2p1
    #IsoMu40_eta2p1

    CUTS_2012 = cms.PSet(
        eta = cms.vdouble(-2.4, 2.4),
        d0_v = cms.vdouble(-0.02, 0.02),
        dz_v = cms.vdouble(-0.5, 0.5),
        drjet = cms.vdouble(0.3, 7),
        pfreliso = cms.vdouble(0., 0.12),
        #deltapt = cms.vdouble(0., 5.0),
        absdeltapt = cms.vdouble(-10000, 5.0),
    )
    CUTS_ETA2P1 = CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    
    PT10_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(10.0, 200.0) )
    PT20_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(20.0, 200.0) )
    PT30_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(30.0, 200.0) )
    PT40_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(40.0, 200.0) )
    PT50_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(50.0, 200.0) )
    PT60_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(60.0, 200.0) )
    PT70_CUTS_2012 = CUTS_2012.clone( pt = cms.vdouble(70.0, 200.0) )
    
    PT10_CUTS_ETA2P1 = PT10_CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    PT20_CUTS_ETA2P1 = PT20_CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    PT30_CUTS_ETA2P1 = PT30_CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    PT40_CUTS_ETA2P1 = PT40_CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    PT50_CUTS_ETA2P1 = PT50_CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    PT60_CUTS_ETA2P1 = PT60_CUTS_2012.clone( eta = cms.vdouble(-2.1, 2.1) )
    
    NVTX_BINS   = cms.PSet( tag_nVertices = cms.vdouble(0.5, 4.5, 8.5, 12.5, 16.5, 20.5, 24.5, 28.5, 32.5, 36.5, 40.5) )
    ETA_BINS    = cms.PSet( eta           = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.4) )

    ABSETA_2_BINS  = cms.PSet( abs_eta  = cms.vdouble(0.0, 0.9, 2.4) )

    RELISO_BINS = cms.PSet( pfreliso      = cms.vdouble(0., 0.01, 0.02, 0.04, 0.06, 0.09, 0.12, 0.15, 0.2) )
    HT_BINS     = cms.PSet( tag_ht        = cms.vdouble(100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 1000) )
    MET_BINS    = cms.PSet( tag_met       = cms.vdouble(0, 10, 20, 30, 40, 60, 150) )
    
    PT5_BINS  = cms.PSet( pt = cms.vdouble( 2,  4,  5,  6,  8, 11, 15, 20, 30,  60, 100, 200) )
    PT12_BINS = cms.PSet( pt = cms.vdouble( 5,  8, 10, 12, 14, 17, 20, 25, 30,  40,  60, 100, 200) )
    PT15_BINS = cms.PSet( pt = cms.vdouble( 5,  8, 11, 14, 16, 19, 22, 25, 30,  40,  60, 100, 200) )
    PT20_BINS = cms.PSet( pt = cms.vdouble(10, 13, 16, 19, 21, 24, 27, 30, 35,  40,  50,  60, 100, 200) )
    PT24_BINS = cms.PSet( pt = cms.vdouble(10, 15, 20, 23, 25, 28, 33, 40, 50,  60, 100, 200) )
    PT30_BINS = cms.PSet( pt = cms.vdouble(15, 20, 24, 28, 32, 36, 40, 45, 50,  60, 100, 200) )
    PT34_BINS = cms.PSet( pt = cms.vdouble(15, 25, 29, 32, 36, 40, 45, 50, 55,  60, 100, 200) )
    PT40_BINS = cms.PSet( pt = cms.vdouble(30, 34, 38, 42, 46, 50, 60, 70, 80, 100, 200) )
    PT60_BINS = cms.PSet( pt = cms.vdouble(40, 45, 50, 54, 58, 62, 66, 70, 80, 100, 200) )
    
    ST_BINS   = cms.PSet( stlep = cms.vdouble( 0,  25, 50, 75, 100, 150, 200, 250, 300, 400, 500) )
    
    BinVar_HLTMu5                  = PT10_CUTS_2012.clone(tag_passingHLTMu5                    = cms.vdouble(0.5, 1.5))
    BinVar_HLTMu12                 = PT20_CUTS_2012.clone(tag_passingHLTMu12                   = cms.vdouble(0.5, 1.5))
    BinVar_HLTMu24                 = PT30_CUTS_2012.clone(tag_passingHLTMu24                   = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu24              = PT30_CUTS_2012.clone(tag_passingHLTIsoMu24                = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu30              = PT40_CUTS_2012.clone(tag_passingHLTIsoMu30                = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu15eta2p1L1ETM20 = PT30_CUTS_ETA2P1.clone(tag_passingHLTIsoMu15eta2p1L1ETM20 = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu20eta2p1        = PT30_CUTS_ETA2P1.clone(tag_passingHLTIsoMu20eta2p1        = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu24eta2p1        = PT30_CUTS_ETA2P1.clone(tag_passingHLTIsoMu24eta2p1        = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu30eta2p1        = PT40_CUTS_ETA2P1.clone(tag_passingHLTIsoMu30eta2p1        = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu34eta2p1        = PT50_CUTS_ETA2P1.clone(tag_passingHLTIsoMu34eta2p1        = cms.vdouble(0.5, 1.5))
    BinVar_HLTIsoMu40eta2p1        = PT60_CUTS_ETA2P1.clone(tag_passingHLTIsoMu40eta2p1        = cms.vdouble(0.5, 1.5))
    
    #Mu5
    EffptHLTMu5 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTMu5", "pass"),
        BinnedVariables = BinVar_HLTMu5.clone( pt = PT5_BINS.pt )
    )
    EffstHLTMu5     = EffptHLTMu5.clone( BinnedVariables = BinVar_HLTMu5.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu5    = EffptHLTMu5.clone( BinnedVariables = BinVar_HLTMu5.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu5   = EffptHLTMu5.clone( BinnedVariables = BinVar_HLTMu5.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu5 = EffptHLTMu5.clone( BinnedVariables = BinVar_HLTMu5.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu5     = EffptHLTMu5.clone( BinnedVariables = BinVar_HLTMu5.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu5     = EffptHLTMu5.clone( BinnedVariables = BinVar_HLTMu5.clone(tag_met = MET_BINS.tag_met) )
    
    #Mu12    
    EffptHLTMu12 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTMu12", "pass"),
        BinnedVariables = BinVar_HLTMu12.clone( pt = PT12_BINS.pt )
    )
    EffstHLTMu12     = EffptHLTMu12.clone( BinnedVariables = BinVar_HLTMu12.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu12    = EffptHLTMu12.clone( BinnedVariables = BinVar_HLTMu12.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu12   = EffptHLTMu12.clone( BinnedVariables = BinVar_HLTMu12.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu12 = EffptHLTMu12.clone( BinnedVariables = BinVar_HLTMu12.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu12     = EffptHLTMu12.clone( BinnedVariables = BinVar_HLTMu12.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu12     = EffptHLTMu12.clone( BinnedVariables = BinVar_HLTMu12.clone(tag_met = MET_BINS.tag_met) )
    
    #Mu24    
    EffptHLTMu24 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTMu24", "pass"),
        BinnedVariables = BinVar_HLTMu24.clone( pt = PT24_BINS.pt )
    )
    EffstHLTMu24     = EffptHLTMu24.clone( BinnedVariables = BinVar_HLTMu24.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu24    = EffptHLTMu24.clone( BinnedVariables = BinVar_HLTMu24.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu24   = EffptHLTMu24.clone( BinnedVariables = BinVar_HLTMu24.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu24 = EffptHLTMu24.clone( BinnedVariables = BinVar_HLTMu24.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu24     = EffptHLTMu24.clone( BinnedVariables = BinVar_HLTMu24.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu24     = EffptHLTMu24.clone( BinnedVariables = BinVar_HLTMu24.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu24
    EffptHLTIsoMu24 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu24", "pass"),
        BinnedVariables = BinVar_HLTIsoMu24.clone( pt = PT24_BINS.pt )
    )
    EffstHLTIsoMu24      = EffptHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu24     = EffptHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu24    = EffptHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu24  = EffptHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu24      = EffptHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu24      = EffptHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(tag_met = MET_BINS.tag_met) )

    Effabseta2binsHLTIsoMu24     = EffetaHLTIsoMu24.clone( BinnedVariables = BinVar_HLTIsoMu24.clone(eta = ABSETA_2_BINS.abs_eta) )

    
    #IsoMu30
    EffptHLTIsoMu30 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu30", "pass"),
        BinnedVariables = BinVar_HLTIsoMu30.clone( pt = PT30_BINS.pt )
    )
    EffstHLTIsoMu30      = EffptHLTIsoMu30.clone( BinnedVariables = BinVar_HLTIsoMu30.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu30     = EffptHLTIsoMu30.clone( BinnedVariables = BinVar_HLTIsoMu30.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu30    = EffptHLTIsoMu30.clone( BinnedVariables = BinVar_HLTIsoMu30.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu30  = EffptHLTIsoMu30.clone( BinnedVariables = BinVar_HLTIsoMu30.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu30      = EffptHLTIsoMu30.clone( BinnedVariables = BinVar_HLTIsoMu30.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu30      = EffptHLTIsoMu30.clone( BinnedVariables = BinVar_HLTIsoMu30.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu15_eta2p1_L1ETM20
    EffptHLTIsoMu15eta2p1L1ETM20 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu15eta2p1L1ETM20", "pass"),
        BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone( pt = PT24_BINS.pt )
    )
    EffstHLTIsoMu15eta2p1L1ETM20     = EffptHLTIsoMu15eta2p1L1ETM20.clone( BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu15eta2p1L1ETM20    = EffptHLTIsoMu15eta2p1L1ETM20.clone( BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu15eta2p1L1ETM20   = EffptHLTIsoMu15eta2p1L1ETM20.clone( BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu15eta2p1L1ETM20 = EffptHLTIsoMu15eta2p1L1ETM20.clone( BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu15eta2p1L1ETM20     = EffptHLTIsoMu15eta2p1L1ETM20.clone( BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu15eta2p1L1ETM20     = EffptHLTIsoMu15eta2p1L1ETM20.clone( BinnedVariables = BinVar_HLTIsoMu15eta2p1L1ETM20.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu20_eta2p1
    EffptHLTIsoMu20eta2p1 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu20eta2p1", "pass"),
        BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone( pt = PT20_BINS.pt )
    )
    EffstHLTIsoMu20eta2p1     = EffptHLTIsoMu20eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu20eta2p1    = EffptHLTIsoMu20eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu20eta2p1   = EffptHLTIsoMu20eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu20eta2p1 = EffptHLTIsoMu20eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu20eta2p1     = EffptHLTIsoMu20eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu20eta2p1     = EffptHLTIsoMu20eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu20eta2p1.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu24_eta2p1
    EffptHLTIsoMu24eta2p1 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu24eta2p1", "pass"),
        BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone( pt = PT24_BINS.pt )
    )
    EffstHLTIsoMu24eta2p1     = EffptHLTIsoMu24eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu24eta2p1    = EffptHLTIsoMu24eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu24eta2p1   = EffptHLTIsoMu24eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu24eta2p1 = EffptHLTIsoMu24eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu24eta2p1     = EffptHLTIsoMu24eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu24eta2p1     = EffptHLTIsoMu24eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu24eta2p1.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu30_eta2p1
    EffptHLTIsoMu30eta2p1 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu30eta2p1", "pass"),
        BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone( pt = PT30_BINS.pt )
    )
    EffstHLTIsoMu30eta2p1     = EffptHLTIsoMu30eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu30eta2p1    = EffptHLTIsoMu30eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu30eta2p1   = EffptHLTIsoMu30eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu30eta2p1 = EffptHLTIsoMu30eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu30eta2p1     = EffptHLTIsoMu30eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu30eta2p1     = EffptHLTIsoMu30eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu30eta2p1.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu34_eta2p1
    EffptHLTIsoMu34eta2p1 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu34eta2p1", "pass"),
        BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone( pt = PT34_BINS.pt )
    )
    EffstHLTIsoMu34eta2p1     = EffptHLTIsoMu34eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu34eta2p1    = EffptHLTIsoMu34eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu34eta2p1   = EffptHLTIsoMu34eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu34eta2p1 = EffptHLTIsoMu34eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu34eta2p1     = EffptHLTIsoMu34eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu34eta2p1     = EffptHLTIsoMu34eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu34eta2p1.clone(tag_met = MET_BINS.tag_met) )
    
    #IsoMu40_eta2p1
    EffptHLTIsoMu40eta2p1 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("passingHLTIsoMu40eta2p1", "pass"),
        BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone( pt = PT40_BINS.pt )
    )
    EffstHLTIsoMu40eta2p1     = EffptHLTIsoMu40eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTIsoMu40eta2p1    = EffptHLTIsoMu40eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTIsoMu40eta2p1   = EffptHLTIsoMu40eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTIsoMu40eta2p1 = EffptHLTIsoMu40eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTIsoMu40eta2p1     = EffptHLTIsoMu40eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTIsoMu40eta2p1     = EffptHLTIsoMu40eta2p1.clone( BinnedVariables = BinVar_HLTIsoMu40eta2p1.clone(tag_met = MET_BINS.tag_met) )
    
    
    ###################################
    #       MuHad Cross Triggers      #
    ###################################
    
    #Mu40_HT200
    #Mu40_FJHT200
    #Mu40_PFHT350
    #Mu60_PFHT350
    #Mu40_PFNoPUHT350
    #Mu60_PFNoPUHT350
    #PFHT400_Mu5_PFMET45
    #PFHT400_Mu5_PFMET50
    #PFHT350_Mu15_PFMET45
    #PFHT350_Mu15_PFMET50
    #PFNoPUHT400_Mu5_PFMET45
    #PFNoPUHT400_Mu5_PFMET50
    #PFNoPUHT350_Mu15_PFMET45
    #PFNoPUHT350_Mu15_PFMET50

    BinVar_HLTMu40HT200              = PT50_CUTS_2012.clone( tag_passingHLT_Mu40_HT200               = cms.vdouble(0.5, 1.5), tag_matchedHLT_Mu40_HT200_Run2012       = cms.vstring("pass") )
    BinVar_HLTMu40FJHT200            = PT50_CUTS_2012.clone( tag_passingHLT_Mu40_FJHT200             = cms.vdouble(0.5, 1.5), tag_matchedHLT_Mu40_FJHT200             = cms.vstring("pass") )
    BinVar_HLTMu40PFHT350            = PT50_CUTS_2012.clone( tag_passingHLT_Mu40_PFHT350             = cms.vdouble(0.5, 1.5), tag_matchedHLT_Mu40_PFHT350             = cms.vstring("pass") )
    BinVar_HLTMu60PFHT350            = PT70_CUTS_2012.clone( tag_passingHLT_Mu60_PFHT350             = cms.vdouble(0.5, 1.5), tag_matchedHLT_Mu60_PFHT350             = cms.vstring("pass") )
    BinVar_HLTMu40PFNoPUHT350        = PT50_CUTS_2012.clone( tag_passingHLT_Mu40_PFNoPUHT350         = cms.vdouble(0.5, 1.5), tag_matchedHLT_Mu40_PFNoPUHT350         = cms.vstring("pass") )
    BinVar_HLTMu60PFNoPUHT350        = PT70_CUTS_2012.clone( tag_passingHLT_Mu60_PFNoPUHT350         = cms.vdouble(0.5, 1.5), tag_matchedHLT_Mu60_PFNoPUHT350         = cms.vstring("pass") )
    BinVar_HLTPFHT350Mu15PFMET45     = PT20_CUTS_2012.clone( tag_passingHLT_PFHT350_Mu15_PFMET45     = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFHT350_Mu15_PFMET45     = cms.vstring("pass") )
    BinVar_HLTPFHT350Mu15PFMET50     = PT20_CUTS_2012.clone( tag_passingHLT_PFHT350_Mu15_PFMET50     = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFHT350_Mu15_PFMET50     = cms.vstring("pass") )
    BinVar_HLTPFHT400Mu5PFMET45      = PT10_CUTS_2012.clone( tag_passingHLT_PFHT400_Mu5_PFMET45      = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFHT400_Mu5_PFMET45      = cms.vstring("pass") )
    BinVar_HLTPFHT400Mu5PFMET50      = PT10_CUTS_2012.clone( tag_passingHLT_PFHT400_Mu5_PFMET50      = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFHT400_Mu5_PFMET50      = cms.vstring("pass") )
    BinVar_HLTPFNoPUHT350Mu15PFMET45 = PT20_CUTS_2012.clone( tag_passingHLT_PFNoPUHT350_Mu15_PFMET45 = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFNoPUHT350_Mu15_PFMET45 = cms.vstring("pass") )
    BinVar_HLTPFNoPUHT350Mu15PFMET50 = PT20_CUTS_2012.clone( tag_passingHLT_PFNoPUHT350_Mu15_PFMET50 = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFNoPUHT350_Mu15_PFMET50 = cms.vstring("pass") )
    BinVar_HLTPFNoPUHT400Mu5PFMET45  = PT10_CUTS_2012.clone( tag_passingHLT_PFNoPUHT400_Mu5_PFMET45  = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFNoPUHT400_Mu5_PFMET45  = cms.vstring("pass") )
    BinVar_HLTPFNoPUHT400Mu5PFMET50  = PT10_CUTS_2012.clone( tag_passingHLT_PFNoPUHT400_Mu5_PFMET50  = cms.vdouble(0.5, 1.5), tag_matchedHLT_PFNoPUHT400_Mu5_PFMET50  = cms.vstring("pass") )

    # Mu40_HT200
    EffptHLTMu40HT200 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_HT200_Run2012", "pass"),
        BinnedVariables = BinVar_HLTMu40HT200.clone( pt = PT40_BINS.pt )
    )
    EffstHLTMu40HT200     = EffptHLTMu40HT200.clone( BinnedVariables = BinVar_HLTMu40HT200.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu40HT200    = EffptHLTMu40HT200.clone( BinnedVariables = BinVar_HLTMu40HT200.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu40HT200   = EffptHLTMu40HT200.clone( BinnedVariables = BinVar_HLTMu40HT200.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu40HT200 = EffptHLTMu40HT200.clone( BinnedVariables = BinVar_HLTMu40HT200.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu40HT200     = EffptHLTMu40HT200.clone( BinnedVariables = BinVar_HLTMu40HT200.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu40HT200     = EffptHLTMu40HT200.clone( BinnedVariables = BinVar_HLTMu40HT200.clone(tag_met = MET_BINS.tag_met) )

    # Mu40_FJHT200
    EffptHLTMu40FJHT200 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_FJHT200", "pass"),
        BinnedVariables = BinVar_HLTMu40FJHT200.clone( pt = PT40_BINS.pt )
    )
    EffstHLTMu40FJHT200     = EffptHLTMu40FJHT200.clone( BinnedVariables = BinVar_HLTMu40FJHT200.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu40FJHT200    = EffptHLTMu40FJHT200.clone( BinnedVariables = BinVar_HLTMu40FJHT200.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu40FJHT200   = EffptHLTMu40FJHT200.clone( BinnedVariables = BinVar_HLTMu40FJHT200.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu40FJHT200 = EffptHLTMu40FJHT200.clone( BinnedVariables = BinVar_HLTMu40FJHT200.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu40FJHT200     = EffptHLTMu40FJHT200.clone( BinnedVariables = BinVar_HLTMu40FJHT200.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu40FJHT200     = EffptHLTMu40FJHT200.clone( BinnedVariables = BinVar_HLTMu40FJHT200.clone(tag_met = MET_BINS.tag_met) )
    
    # Mu40_PFHT350
    EffptHLTMu40PFHT350 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_PFHT350", "pass"),
        BinnedVariables = BinVar_HLTMu40PFHT350.clone( pt = PT40_BINS.pt )
    )
    EffstHLTMu40PFHT350     = EffptHLTMu40PFHT350.clone( BinnedVariables = BinVar_HLTMu40PFHT350.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu40PFHT350    = EffptHLTMu40PFHT350.clone( BinnedVariables = BinVar_HLTMu40PFHT350.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu40PFHT350   = EffptHLTMu40PFHT350.clone( BinnedVariables = BinVar_HLTMu40PFHT350.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu40PFHT350 = EffptHLTMu40PFHT350.clone( BinnedVariables = BinVar_HLTMu40PFHT350.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu40PFHT350     = EffptHLTMu40PFHT350.clone( BinnedVariables = BinVar_HLTMu40PFHT350.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu40PFHT350     = EffptHLTMu40PFHT350.clone( BinnedVariables = BinVar_HLTMu40PFHT350.clone(tag_met = MET_BINS.tag_met) )
    
    # Mu60_PFHT350
    EffptHLTMu60PFHT350 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu60_PFHT350", "pass"),
        BinnedVariables = BinVar_HLTMu60PFHT350.clone( pt = PT60_BINS.pt )
    )
    EffstHLTMu60PFHT350     = EffptHLTMu60PFHT350.clone( BinnedVariables = BinVar_HLTMu60PFHT350.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu60PFHT350    = EffptHLTMu60PFHT350.clone( BinnedVariables = BinVar_HLTMu60PFHT350.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu60PFHT350   = EffptHLTMu60PFHT350.clone( BinnedVariables = BinVar_HLTMu60PFHT350.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu60PFHT350 = EffptHLTMu60PFHT350.clone( BinnedVariables = BinVar_HLTMu60PFHT350.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu60PFHT350     = EffptHLTMu60PFHT350.clone( BinnedVariables = BinVar_HLTMu60PFHT350.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu60PFHT350     = EffptHLTMu60PFHT350.clone( BinnedVariables = BinVar_HLTMu60PFHT350.clone(tag_met = MET_BINS.tag_met) )
    
    # PFHT350_Mu15_PFMET45
    EffptHLTPFHT350Mu15PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFHT350_Mu15_PFMET45", "pass"),
        BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone( pt = PT15_BINS.pt )
    )
    EffstHLTPFHT350Mu15PFMET45     = EffptHLTPFHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFHT350Mu15PFMET45    = EffptHLTPFHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFHT350Mu15PFMET45   = EffptHLTPFHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFHT350Mu15PFMET45 = EffptHLTPFHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFHT350Mu15PFMET45     = EffptHLTPFHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFHT350Mu15PFMET45    = EffptHLTPFHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    # PFHT350_Mu15_PFMET50
    EffptHLTPFHT350Mu15PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFHT350_Mu15_PFMET50", "pass"),
        BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone( pt = PT15_BINS.pt )
    )
    EffstHLTPFHT350Mu15PFMET50     = EffptHLTPFHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFHT350Mu15PFMET50    = EffptHLTPFHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFHT350Mu15PFMET50   = EffptHLTPFHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFHT350Mu15PFMET50 = EffptHLTPFHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFHT350Mu15PFMET50     = EffptHLTPFHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFHT350Mu15PFMET50    = EffptHLTPFHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFHT350Mu15PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    # PFHT400_Mu5_PFMET45
    EffptHLTPFHT400Mu5PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFHT400_Mu5_PFMET45", "pass"),
        BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone( pt = PT5_BINS.pt )
    )
    EffstHLTPFHT400Mu5PFMET45     = EffptHLTPFHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFHT400Mu5PFMET45    = EffptHLTPFHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFHT400Mu5PFMET45   = EffptHLTPFHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFHT400Mu5PFMET45 = EffptHLTPFHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFHT400Mu5PFMET45     = EffptHLTPFHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFHT400Mu5PFMET45    = EffptHLTPFHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    # PFHT400_Mu5_PFMET50
    EffptHLTPFHT400Mu5PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFHT400_Mu5_PFMET50", "pass"),
        BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone( pt = PT5_BINS.pt )
    )
    EffstHLTPFHT400Mu5PFMET50     = EffptHLTPFHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFHT400Mu5PFMET50    = EffptHLTPFHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFHT400Mu5PFMET50   = EffptHLTPFHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFHT400Mu5PFMET50 = EffptHLTPFHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFHT400Mu5PFMET50     = EffptHLTPFHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFHT400Mu5PFMET50    = EffptHLTPFHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFHT400Mu5PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    # Mu40_PFNoPUHT350
    EffptHLTMu40PFNoPUHT350 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu40_PFNoPUHT350", "pass"),
        BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone( pt = PT40_BINS.pt )
    )
    EffstHLTMu40PFNoPUHT350     = EffptHLTMu40PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu40PFNoPUHT350    = EffptHLTMu40PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu40PFNoPUHT350   = EffptHLTMu40PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu40PFNoPUHT350 = EffptHLTMu40PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu40PFNoPUHT350     = EffptHLTMu40PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu40PFNoPUHT350     = EffptHLTMu40PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu40PFNoPUHT350.clone(tag_met = MET_BINS.tag_met) )
    
    # Mu60_PFNoPUHT350
    EffptHLTMu60PFNoPUHT350 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_Mu60_PFNoPUHT350", "pass"),
        BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone( pt = PT60_BINS.pt )
    )
    EffstHLTMu60PFNoPUHT350     = EffptHLTMu60PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTMu60PFNoPUHT350    = EffptHLTMu60PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTMu60PFNoPUHT350   = EffptHLTMu60PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTMu60PFNoPUHT350 = EffptHLTMu60PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTMu60PFNoPUHT350     = EffptHLTMu60PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTMu60PFNoPUHT350     = EffptHLTMu60PFNoPUHT350.clone( BinnedVariables = BinVar_HLTMu60PFNoPUHT350.clone(tag_met = MET_BINS.tag_met) )
    
    # PFNoPUHT350_Mu15_PFMET45
    EffptHLTPFNoPUHT350Mu15PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFNoPUHT350_Mu15_PFMET45", "pass"),
        BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone( pt = PT15_BINS.pt )
    )
    EffstHLTPFNoPUHT350Mu15PFMET45     = EffptHLTPFNoPUHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFNoPUHT350Mu15PFMET45    = EffptHLTPFNoPUHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFNoPUHT350Mu15PFMET45   = EffptHLTPFNoPUHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFNoPUHT350Mu15PFMET45 = EffptHLTPFNoPUHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFNoPUHT350Mu15PFMET45     = EffptHLTPFNoPUHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFNoPUHT350Mu15PFMET45    = EffptHLTPFNoPUHT350Mu15PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    # PFNoPUHT350_Mu15_PFMET50
    EffptHLTPFNoPUHT350Mu15PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFNoPUHT350_Mu15_PFMET50", "pass"),
        BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone( pt = PT15_BINS.pt )
    )
    EffstHLTPFNoPUHT350Mu15PFMET50     = EffptHLTPFNoPUHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFNoPUHT350Mu15PFMET50    = EffptHLTPFNoPUHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFNoPUHT350Mu15PFMET50   = EffptHLTPFNoPUHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFNoPUHT350Mu15PFMET50 = EffptHLTPFNoPUHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFNoPUHT350Mu15PFMET50     = EffptHLTPFNoPUHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFNoPUHT350Mu15PFMET50    = EffptHLTPFNoPUHT350Mu15PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT350Mu15PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    # PFNoPUHT400_Mu5_PFMET45
    EffptHLTPFNoPUHT400Mu5PFMET45 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFNoPUHT400_Mu5_PFMET45", "pass"),
        BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone( pt = PT5_BINS.pt )
    )
    EffstHLTPFNoPUHT400Mu5PFMET45     = EffptHLTPFNoPUHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFNoPUHT400Mu5PFMET45    = EffptHLTPFNoPUHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFNoPUHT400Mu5PFMET45   = EffptHLTPFNoPUHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFNoPUHT400Mu5PFMET45 = EffptHLTPFNoPUHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFNoPUHT400Mu5PFMET45     = EffptHLTPFNoPUHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFNoPUHT400Mu5PFMET45    = EffptHLTPFNoPUHT400Mu5PFMET45.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET45.clone(tag_met = MET_BINS.tag_met) )
    
    # PFNoPUHT400_Mu5_PFMET50
    EffptHLTPFNoPUHT400Mu5PFMET50 = EffTemplate.clone(
        EfficiencyCategoryAndState = cms.vstring("matchedHLT_PFNoPUHT400_Mu5_PFMET50", "pass"),
        BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone( pt = PT5_BINS.pt )
    )
    EffstHLTPFNoPUHT400Mu5PFMET50     = EffptHLTPFNoPUHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone(pt = cms.vdouble(0,1000), stlep = ST_BINS.stlep) )
    EffetaHLTPFNoPUHT400Mu5PFMET50    = EffptHLTPFNoPUHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone(eta = ETA_BINS.eta) )
    EffnvtxHLTPFNoPUHT400Mu5PFMET50   = EffptHLTPFNoPUHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone(tag_nVertices = NVTX_BINS.tag_nVertices) )
    EffrelisoHLTPFNoPUHT400Mu5PFMET50 = EffptHLTPFNoPUHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone(pfreliso = RELISO_BINS.pfreliso) )
    EffhtHLTPFNoPUHT400Mu5PFMET50     = EffptHLTPFNoPUHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone(tag_ht = HT_BINS.tag_ht) )
    EffmetHLTPFNoPUHT400Mu5PFMET50    = EffptHLTPFNoPUHT400Mu5PFMET50.clone( BinnedVariables = BinVar_HLTPFNoPUHT400Mu5PFMET50.clone(tag_met = MET_BINS.tag_met) )
    
    ##
    ## Data/MC efficiencies
    ##
    
    TestEfficiencies = cms.PSet(
        #pt_HLTIsoMu24              = cms.PSet(EffptHLTIsoMu24),
        eta_HLTPFHT350Mu15PFMET45    = cms.PSet(EffetaHLTPFHT350Mu15PFMET45),
        
        pt_HLTMu40PFHT350            = cms.PSet(EffptHLTMu40PFHT350),
        #st_HLTMu40PFHT350            = cms.PSet(EffstHLTMu40PFHT350),
        #eta_HLTMu40PFHT350           = cms.PSet(EffetaHLTMu40PFHT350),
        #nvtx_HLTMu40PFHT350          = cms.PSet(EffnvtxHLTMu40PFHT350),
        #reliso_HLTMu40PFHT350        = cms.PSet(EffrelisoHLTMu40PFHT350),
        #ht_HLTMu40PFHT350            = cms.PSet(EffhtHLTMu40PFHT350),
        #met_HLTMu40PFHT350           = cms.PSet(EffmetHLTMu40PFHT350),
    )
    
    DataEfficiencies_Single = cms.PSet(
        # Single Muon Triggers
        #Mu5
        #Mu12
        #Mu24
        #IsoMu24
        #IsoMu30
        #IsoMu15_eta2p1_L1ETM20 
        #IsoMu20_eta2p1
        #IsoMu24_eta2p1
        #IsoMu30_eta2p1
        #IsoMu34_eta2p1
        #IsoMu40_eta2p1
        
        # pt Plots
        #pt_HLTMu5                  = cms.PSet(EffptHLTMu5),
        #pt_HLTMu12                 = cms.PSet(EffptHLTMu12),
        #pt_HLTMu24                 = cms.PSet(EffptHLTMu24),
        #pt_HLTIsoMu24              = cms.PSet(EffptHLTIsoMu24),
        #pt_HLTIsoMu30              = cms.PSet(EffptHLTIsoMu30),
        #pt_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffptHLTIsoMu15eta2p1L1ETM20),
        #pt_HLTIsoMu20eta2p1        = cms.PSet(EffptHLTIsoMu20eta2p1),
        pt_HLTIsoMu24eta2p1        = cms.PSet(EffptHLTIsoMu24eta2p1),
        #pt_HLTIsoMu30eta2p1        = cms.PSet(EffptHLTIsoMu30eta2p1),
        #pt_HLTIsoMu34eta2p1        = cms.PSet(EffptHLTIsoMu34eta2p1),
        #pt_HLTIsoMu40eta2p1        = cms.PSet(EffptHLTIsoMu40eta2p1),
        
        # pt Plots
        #st_HLTMu5                  = cms.PSet(EffstHLTMu5),
        #st_HLTMu12                 = cms.PSet(EffstHLTMu12),
        #st_HLTMu24                 = cms.PSet(EffstHLTMu24),
        #st_HLTIsoMu24              = cms.PSet(EffstHLTIsoMu24),
        #st_HLTIsoMu30              = cms.PSet(EffstHLTIsoMu30),
        #st_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffstHLTIsoMu15eta2p1L1ETM20),
        #st_HLTIsoMu20eta2p1        = cms.PSet(EffstHLTIsoMu20eta2p1),
        st_HLTIsoMu24eta2p1        = cms.PSet(EffstHLTIsoMu24eta2p1),
        #st_HLTIsoMu30eta2p1        = cms.PSet(EffstHLTIsoMu30eta2p1),
        #st_HLTIsoMu34eta2p1        = cms.PSet(EffstHLTIsoMu34eta2p1),
        #st_HLTIsoMu40eta2p1        = cms.PSet(EffstHLTIsoMu40eta2p1),
        
        # eta Plots
        #eta_HLTMu5                  = cms.PSet(EffetaHLTMu5),
        #eta_HLTMu12                 = cms.PSet(EffetaHLTMu12),
        #eta_HLTMu24                 = cms.PSet(EffetaHLTMu24),
        #eta_HLTIsoMu24              = cms.PSet(EffetaHLTIsoMu24),
        #eta_HLTIsoMu30              = cms.PSet(EffetaHLTIsoMu30),
        #eta_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffetaHLTIsoMu15eta2p1L1ETM20),
        #eta_HLTIsoMu20eta2p1        = cms.PSet(EffetaHLTIsoMu20eta2p1),
        eta_HLTIsoMu24eta2p1        = cms.PSet(EffetaHLTIsoMu24eta2p1),
        #eta_HLTIsoMu30eta2p1        = cms.PSet(EffetaHLTIsoMu30eta2p1),
        #eta_HLTIsoMu34eta2p1        = cms.PSet(EffetaHLTIsoMu34eta2p1),
        #eta_HLTIsoMu40eta2p1        = cms.PSet(EffetaHLTIsoMu40eta2p1),
        
        # nvtx Plots
        #nvtx_HLTMu5                  = cms.PSet(EffnvtxHLTMu5),
        #nvtx_HLTMu12                 = cms.PSet(EffnvtxHLTMu12),
        #nvtx_HLTMu24                 = cms.PSet(EffnvtxHLTMu24),
        #nvtx_HLTIsoMu24              = cms.PSet(EffnvtxHLTIsoMu24),
        #nvtx_HLTIsoMu30              = cms.PSet(EffnvtxHLTIsoMu30),
        #nvtx_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffnvtxHLTIsoMu15eta2p1L1ETM20),
        #nvtx_HLTIsoMu20eta2p1        = cms.PSet(EffnvtxHLTIsoMu20eta2p1),
        nvtx_HLTIsoMu24eta2p1        = cms.PSet(EffnvtxHLTIsoMu24eta2p1),
        #nvtx_HLTIsoMu30eta2p1        = cms.PSet(EffnvtxHLTIsoMu30eta2p1),
        #nvtx_HLTIsoMu34eta2p1        = cms.PSet(EffnvtxHLTIsoMu34eta2p1),
        #nvtx_HLTIsoMu40eta2p1        = cms.PSet(EffnvtxHLTIsoMu40eta2p1),
        
        # reliso Plots
        #reliso_HLTMu5                  = cms.PSet(EffrelisoHLTMu5),
        #reliso_HLTMu12                 = cms.PSet(EffrelisoHLTMu12),
        #reliso_HLTMu24                 = cms.PSet(EffrelisoHLTMu24),
        #reliso_HLTIsoMu24              = cms.PSet(EffrelisoHLTIsoMu24),
        #reliso_HLTIsoMu30              = cms.PSet(EffrelisoHLTIsoMu30),
        #reliso_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffrelisoHLTIsoMu15eta2p1L1ETM20),
        #reliso_HLTIsoMu20eta2p1        = cms.PSet(EffrelisoHLTIsoMu20eta2p1),
        reliso_HLTIsoMu24eta2p1        = cms.PSet(EffrelisoHLTIsoMu24eta2p1),
        #reliso_HLTIsoMu30eta2p1        = cms.PSet(EffrelisoHLTIsoMu30eta2p1),
        #reliso_HLTIsoMu34eta2p1        = cms.PSet(EffrelisoHLTIsoMu34eta2p1),
        #reliso_HLTIsoMu40eta2p1        = cms.PSet(EffrelisoHLTIsoMu40eta2p1),
        
        # ht Plots
        #ht_HLTMu5                  = cms.PSet(EffhtHLTMu5),
        #ht_HLTMu12                 = cms.PSet(EffhtHLTMu12),
        #ht_HLTMu24                 = cms.PSet(EffhtHLTMu24),
        #ht_HLTIsoMu24              = cms.PSet(EffhtHLTIsoMu24),
        #ht_HLTIsoMu30              = cms.PSet(EffhtHLTIsoMu30),
        #ht_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffhtHLTIsoMu15eta2p1L1ETM20),
        #ht_HLTIsoMu20eta2p1        = cms.PSet(EffhtHLTIsoMu20eta2p1),
        ht_HLTIsoMu24eta2p1        = cms.PSet(EffhtHLTIsoMu24eta2p1),
        #ht_HLTIsoMu30eta2p1        = cms.PSet(EffhtHLTIsoMu30eta2p1),
        #ht_HLTIsoMu34eta2p1        = cms.PSet(EffhtHLTIsoMu34eta2p1),
        #ht_HLTIsoMu40eta2p1        = cms.PSet(EffhtHLTIsoMu40eta2p1),
        
        # met Plots
        #met_HLTMu5                  = cms.PSet(EffmetHLTMu5),
        #met_HLTMu12                 = cms.PSet(EffmetHLTMu12),
        #met_HLTMu24                 = cms.PSet(EffmetHLTMu24),
        #met_HLTIsoMu24              = cms.PSet(EffmetHLTIsoMu24),
        #met_HLTIsoMu30              = cms.PSet(EffmetHLTIsoMu30),
        #met_HLTIsoMu15eta2p1L1ETM20 = cms.PSet(EffmetHLTIsoMu15eta2p1L1ETM20),
        #met_HLTIsoMu20eta2p1        = cms.PSet(EffmetHLTIsoMu20eta2p1),
        met_HLTIsoMu24eta2p1        = cms.PSet(EffmetHLTIsoMu24eta2p1),
        #met_HLTIsoMu30eta2p1        = cms.PSet(EffmetHLTIsoMu30eta2p1),
        #met_HLTIsoMu34eta2p1        = cms.PSet(EffmetHLTIsoMu34eta2p1),
        #met_HLTIsoMu40eta2p1        = cms.PSet(EffmetHLTIsoMu40eta2p1),
        
        #abseta2bins_HLTIsoMu24              = cms.PSet(Effabseta2binsHLTIsoMu24),
    )
    DataEfficiencies_Had = cms.PSet(
        
        # Cross Triggers
            
        #Mu40_HT200
        #Mu40_FJHT200
        #Mu40_PFHT350
        #Mu60_PFHT350
        #PFHT350_Mu15_PFMET45
        #PFHT350_Mu15_PFMET50
        #PFHT400_Mu5_PFMET45
        #PFHT400_Mu5_PFMET50
        #Mu40_PFNoPUHT350
        #Mu60_PFNoPUHT350
        #PFNoPUHT350_Mu15_PFMET45
        #PFNoPUHT350_Mu15_PFMET50
        #PFNoPUHT400_Mu5_PFMET45
        #PFNoPUHT400_Mu5_PFMET50
        
        # Mu40_HT200
        #pt_HLTMu40HT200            = cms.PSet(EffptHLTMu40HT200),
        #st_HLTMu40HT200            = cms.PSet(EffstHLTMu40HT200),
        #eta_HLTMu40HT200           = cms.PSet(EffetaHLTMu40HT200),
        #nvtx_HLTMu40HT200          = cms.PSet(EffnvtxHLTMu40HT200),
        #reliso_HLTMu40HT200        = cms.PSet(EffrelisoHLTMu40HT200),
        #ht_HLTMu40HT200            = cms.PSet(EffhtHLTMu40HT200),
        #met_HLTMu40HT200           = cms.PSet(EffmetHLTMu40HT200),
        
        # Mu40_FJHT200
        #pt_HLTMu40FJHT200            = cms.PSet(EffptHLTMu40FJHT200),
        #st_HLTMu40FJHT200            = cms.PSet(EffstHLTMu40FJHT200),
        #eta_HLTMu40FJHT200           = cms.PSet(EffetaHLTMu40FJHT200),
        #nvtx_HLTMu40FJHT200          = cms.PSet(EffnvtxHLTMu40FJHT200),
        #reliso_HLTMu40FJHT200        = cms.PSet(EffrelisoHLTMu40FJHT200),
        #ht_HLTMu40FJHT200            = cms.PSet(EffhtHLTMu40FJHT200),
        #met_HLTMu40FJHT200           = cms.PSet(EffmetHLTMu40FJHT200),
        
        # Mu40_PFHT350
        pt_HLTMu40PFHT350            = cms.PSet(EffptHLTMu40PFHT350),
        st_HLTMu40PFHT350            = cms.PSet(EffstHLTMu40PFHT350),
        eta_HLTMu40PFHT350           = cms.PSet(EffetaHLTMu40PFHT350),
        nvtx_HLTMu40PFHT350          = cms.PSet(EffnvtxHLTMu40PFHT350),
        reliso_HLTMu40PFHT350        = cms.PSet(EffrelisoHLTMu40PFHT350),
        ht_HLTMu40PFHT350            = cms.PSet(EffhtHLTMu40PFHT350),
        met_HLTMu40PFHT350           = cms.PSet(EffmetHLTMu40PFHT350),
        
        # Mu40_PFNoPUHT350
        pt_HLTMu40PFNoPUHT350            = cms.PSet(EffptHLTMu40PFNoPUHT350),
        st_HLTMu40PFNoPUHT350            = cms.PSet(EffstHLTMu40PFNoPUHT350),
        eta_HLTMu40PFNoPUHT350           = cms.PSet(EffetaHLTMu40PFNoPUHT350),
        nvtx_HLTMu40PFNoPUHT350          = cms.PSet(EffnvtxHLTMu40PFNoPUHT350),
        reliso_HLTMu40PFNoPUHT350        = cms.PSet(EffrelisoHLTMu40PFNoPUHT350),
        ht_HLTMu40PFNoPUHT350            = cms.PSet(EffhtHLTMu40PFNoPUHT350),
        met_HLTMu40PFNoPUHT350           = cms.PSet(EffmetHLTMu40PFNoPUHT350),
        
        # Mu60_PFHT350
        pt_HLTMu60PFHT350            = cms.PSet(EffptHLTMu60PFHT350),
        st_HLTMu60PFHT350            = cms.PSet(EffstHLTMu60PFHT350),
        eta_HLTMu60PFHT350           = cms.PSet(EffetaHLTMu60PFHT350),
        nvtx_HLTMu60PFHT350          = cms.PSet(EffnvtxHLTMu60PFHT350),
        reliso_HLTMu60PFHT350        = cms.PSet(EffrelisoHLTMu60PFHT350),
        ht_HLTMu60PFHT350            = cms.PSet(EffhtHLTMu60PFHT350),
        met_HLTMu60PFHT350           = cms.PSet(EffmetHLTMu60PFHT350),
        
        # Mu60_PFNoPUHT350
        pt_HLTMu60PFNoPUHT350            = cms.PSet(EffptHLTMu60PFNoPUHT350),
        st_HLTMu60PFNoPUHT350            = cms.PSet(EffstHLTMu60PFNoPUHT350),
        eta_HLTMu60PFNoPUHT350           = cms.PSet(EffetaHLTMu60PFNoPUHT350),
        nvtx_HLTMu60PFNoPUHT350          = cms.PSet(EffnvtxHLTMu60PFNoPUHT350),
        reliso_HLTMu60PFNoPUHT350        = cms.PSet(EffrelisoHLTMu60PFNoPUHT350),
        ht_HLTMu60PFNoPUHT350            = cms.PSet(EffhtHLTMu60PFNoPUHT350),
        met_HLTMu60PFNoPUHT350           = cms.PSet(EffmetHLTMu60PFNoPUHT350),
                
        # PFHT350_Mu15_PFMET45
        pt_HLTPFHT350Mu15PFMET45     = cms.PSet(EffptHLTPFHT350Mu15PFMET45),
        st_HLTPFHT350Mu15PFMET45     = cms.PSet(EffstHLTPFHT350Mu15PFMET45),
        eta_HLTPFHT350Mu15PFMET45    = cms.PSet(EffetaHLTPFHT350Mu15PFMET45),
        nvtx_HLTPFHT350Mu15PFMET45   = cms.PSet(EffnvtxHLTPFHT350Mu15PFMET45),
        reliso_HLTPFHT350Mu15PFMET45 = cms.PSet(EffrelisoHLTPFHT350Mu15PFMET45),
        ht_HLTPFHT350Mu15PFMET45     = cms.PSet(EffhtHLTPFHT350Mu15PFMET45),
        met_HLTPFHT350Mu15PFMET45    = cms.PSet(EffmetHLTPFHT350Mu15PFMET45),
        
        # PFHT350_Mu15_PFMET50
        pt_HLTPFHT350Mu15PFMET50     = cms.PSet(EffptHLTPFHT350Mu15PFMET50),
        st_HLTPFHT350Mu15PFMET50     = cms.PSet(EffstHLTPFHT350Mu15PFMET50),
        eta_HLTPFHT350Mu15PFMET50    = cms.PSet(EffetaHLTPFHT350Mu15PFMET50),
        nvtx_HLTPFHT350Mu15PFMET50   = cms.PSet(EffnvtxHLTPFHT350Mu15PFMET50),
        reliso_HLTPFHT350Mu15PFMET50 = cms.PSet(EffrelisoHLTPFHT350Mu15PFMET50),
        ht_HLTPFHT350Mu15PFMET50     = cms.PSet(EffhtHLTPFHT350Mu15PFMET50),
        met_HLTPFHT350Mu15PFMET50    = cms.PSet(EffmetHLTPFHT350Mu15PFMET50),
        
        # PFHT400_Mu5_PFMET45
        pt_HLTPFHT400Mu5PFMET45      = cms.PSet(EffptHLTPFHT400Mu5PFMET45),
        st_HLTPFHT400Mu5PFMET45      = cms.PSet(EffstHLTPFHT400Mu5PFMET45),
        eta_HLTPFHT400Mu5PFMET45     = cms.PSet(EffetaHLTPFHT400Mu5PFMET45),
        nvtx_HLTPFHT400Mu5PFMET45    = cms.PSet(EffnvtxHLTPFHT400Mu5PFMET45),
        reliso_HLTPFHT400Mu5PFMET45  = cms.PSet(EffrelisoHLTPFHT400Mu5PFMET45),
        ht_HLTPFHT400Mu5PFMET45      = cms.PSet(EffhtHLTPFHT400Mu5PFMET45),
        met_HLTPFHT400Mu5PFMET45     = cms.PSet(EffmetHLTPFHT400Mu5PFMET45),
        
        # PFHT400_Mu5_PFMET50
        pt_HLTPFHT400Mu5PFMET50      = cms.PSet(EffptHLTPFHT400Mu5PFMET50),
        st_HLTPFHT400Mu5PFMET50      = cms.PSet(EffstHLTPFHT400Mu5PFMET50),
        eta_HLTPFHT400Mu5PFMET50     = cms.PSet(EffetaHLTPFHT400Mu5PFMET50),
        nvtx_HLTPFHT400Mu5PFMET50    = cms.PSet(EffnvtxHLTPFHT400Mu5PFMET50),
        reliso_HLTPFHT400Mu5PFMET50  = cms.PSet(EffrelisoHLTPFHT400Mu5PFMET50),
        ht_HLTPFHT400Mu5PFMET50      = cms.PSet(EffhtHLTPFHT400Mu5PFMET50),
        met_HLTPFHT400Mu5PFMET50     = cms.PSet(EffmetHLTPFHT400Mu5PFMET50),
        
        # PFNoPUHT350_Mu15_PFMET45
        pt_HLTPFNoPUHT350Mu15PFMET45     = cms.PSet(EffptHLTPFNoPUHT350Mu15PFMET45),
        st_HLTPFNoPUHT350Mu15PFMET45     = cms.PSet(EffstHLTPFNoPUHT350Mu15PFMET45),
        eta_HLTPFNoPUHT350Mu15PFMET45    = cms.PSet(EffetaHLTPFNoPUHT350Mu15PFMET45),
        nvtx_HLTPFNoPUHT350Mu15PFMET45   = cms.PSet(EffnvtxHLTPFNoPUHT350Mu15PFMET45),
        reliso_HLTPFNoPUHT350Mu15PFMET45 = cms.PSet(EffrelisoHLTPFNoPUHT350Mu15PFMET45),
        ht_HLTPFNoPUHT350Mu15PFMET45     = cms.PSet(EffhtHLTPFNoPUHT350Mu15PFMET45),
        met_HLTPFNoPUHT350Mu15PFMET45    = cms.PSet(EffmetHLTPFNoPUHT350Mu15PFMET45),
        
        # PFNoPUHT350_Mu15_PFMET50
        pt_HLTPFNoPUHT350Mu15PFMET50     = cms.PSet(EffptHLTPFNoPUHT350Mu15PFMET50),
        st_HLTPFNoPUHT350Mu15PFMET50     = cms.PSet(EffstHLTPFNoPUHT350Mu15PFMET50),
        eta_HLTPFNoPUHT350Mu15PFMET50    = cms.PSet(EffetaHLTPFNoPUHT350Mu15PFMET50),
        nvtx_HLTPFNoPUHT350Mu15PFMET50   = cms.PSet(EffnvtxHLTPFNoPUHT350Mu15PFMET50),
        reliso_HLTPFNoPUHT350Mu15PFMET50 = cms.PSet(EffrelisoHLTPFNoPUHT350Mu15PFMET50),
        ht_HLTPFNoPUHT350Mu15PFMET50     = cms.PSet(EffhtHLTPFNoPUHT350Mu15PFMET50),
        met_HLTPFNoPUHT350Mu15PFMET50    = cms.PSet(EffmetHLTPFNoPUHT350Mu15PFMET50),
        
        # PFNoPUHT400_Mu5_PFMET45
        pt_HLTPFNoPUHT400Mu5PFMET45      = cms.PSet(EffptHLTPFNoPUHT400Mu5PFMET45),
        st_HLTPFNoPUHT400Mu5PFMET45      = cms.PSet(EffstHLTPFNoPUHT400Mu5PFMET45),
        eta_HLTPFNoPUHT400Mu5PFMET45     = cms.PSet(EffetaHLTPFNoPUHT400Mu5PFMET45),
        nvtx_HLTPFNoPUHT400Mu5PFMET45    = cms.PSet(EffnvtxHLTPFNoPUHT400Mu5PFMET45),
        reliso_HLTPFNoPUHT400Mu5PFMET45  = cms.PSet(EffrelisoHLTPFNoPUHT400Mu5PFMET45),
        ht_HLTPFNoPUHT400Mu5PFMET45      = cms.PSet(EffhtHLTPFNoPUHT400Mu5PFMET45),
        met_HLTPFNoPUHT400Mu5PFMET45     = cms.PSet(EffmetHLTPFNoPUHT400Mu5PFMET45),
        
        # PFNoPUHT400_Mu5_PFMET50
        pt_HLTPFNoPUHT400Mu5PFMET50      = cms.PSet(EffptHLTPFNoPUHT400Mu5PFMET50),
        st_HLTPFNoPUHT400Mu5PFMET50      = cms.PSet(EffstHLTPFNoPUHT400Mu5PFMET50),
        eta_HLTPFNoPUHT400Mu5PFMET50     = cms.PSet(EffetaHLTPFNoPUHT400Mu5PFMET50),
        nvtx_HLTPFNoPUHT400Mu5PFMET50    = cms.PSet(EffnvtxHLTPFNoPUHT400Mu5PFMET50),
        reliso_HLTPFNoPUHT400Mu5PFMET50  = cms.PSet(EffrelisoHLTPFNoPUHT400Mu5PFMET50),
        ht_HLTPFNoPUHT400Mu5PFMET50      = cms.PSet(EffhtHLTPFNoPUHT400Mu5PFMET50),
        met_HLTPFNoPUHT400Mu5PFMET50     = cms.PSet(EffmetHLTPFNoPUHT400Mu5PFMET50),
    )
    
    if (useData == "Single"):
        DataEfficiencies = DataEfficiencies_Single.clone()
        
    if (useData == "Had"):
        DataEfficiencies = DataEfficiencies_Had.clone()
    if (useData == "All"): 
        DataEfficiencies = cms.PSet(
            DataEfficiencies_Single,
            DataEfficiencies_Had
        )
    
    MCEfficiencies = cms.PSet(
        DataEfficiencies_Single,
        DataEfficiencies_Had
    )

    if (useData == "Test"):
        DataEfficiencies = TestEfficiencies
        MCEfficiencies = TestEfficiencies
    
else:
    DataEfficiencies = cms.PSet(
        #passing_pt_HLT_Mu8 = cms.PSet(EffptHLTMu8),
        passing_pt_HLT_Mu15 = cms.PSet(EffptHLTMu15),
    ##     passing_pt_HLT_Mu15_Barrel = cms.PSet(EffptHLTMu15Barrel),
    ##     passing_pt_HLT_Mu15_Endcap = cms.PSet(EffptHLTMu15Endcap),
        #passing_pt_HLT_Mu15_HToff300 = cms.PSet(EffptHLTMu15HToff300),
        #passing_pt_HLT_Mu15_with_PT15_LOWSTAT_BINS = cms.PSet(EffptHLTMu15_with_PT15_LOWSTAT_BINS),
        #passing_pt_HLT_Mu15_with_PT30_BINS = cms.PSet(EffptHLTMu15_with_PT30_BINS),
        #passing_pt_HLT_Mu15_with_PT40_BINS = cms.PSet(EffptHLTMu15_with_PT40_BINS),
    ##     passing_pt_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20),
    ##     passing_pt_HLT_HT250_Mu15_PFMHT20_HToff300 = cms.PSet(EffptHLTHT250Mu15PFMHT20HToff300),
        #passing_pt_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40),
        #passing_pt_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40),
    ##     passing_pt_HLT_Mu8_HT200 = cms.PSet(EffptHLTMu8HT200),
    ##     passing_pt_HLT_Mu15_HT200_HToff300 = cms.PSet(EffptHLTMu15HT200HToff300),
    ##     passing_pt_HLT_Mu15_HT200 = cms.PSet(EffptHLTMu15HT200),
    ##     passing_pt_HLT_Mu30_HT200 = cms.PSet(EffptHLTMu30HT200),
    ##     passing_pt_HLT_Mu40_HT200 = cms.PSet(EffptHLTMu40HT200),
        #passing_pt_HLT_Mu40_HT300 = cms.PSet(EffptHLTMu40HT300),
    
        #passing_eta_HLT_Mu8 = cms.PSet(EffetaHLTMu8),
        #passing_eta_HLT_Mu15 = cms.PSet(EffetaHLTMu15),
        #passing_eta_HLT_Mu15_with_ETA_LOWSTAT_BINS = cms.PSet(EffetaHLTMu15_with_ETA_LOWSTAT_BINS),
        #passing_eta_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffetaHLTHT250Mu15PFMHT20),
        #passing_eta_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffetaHLTHT250Mu15PFMHT40),
        #passing_eta_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffetaHLTHT300Mu15PFMHT40),
        #passing_eta_HLT_Mu8_HT200 = cms.PSet(EffetaHLTMu8HT200),
        #passing_eta_HLT_Mu15_HT200 = cms.PSet(EffetaHLTMu15HT200),
        #passing_eta_HLT_Mu30_HT200 = cms.PSet(EffetaHLTMu30HT200),
        #passing_eta_HLT_Mu40_HT200 = cms.PSet(EffetaHLTMu40HT200),
        #passing_eta_HLT_Mu40_HT300 = cms.PSet(EffetaHLTMu40HT300),
                                                         
    ##     #passing_ht_HLT_Mu15 = cms.PSet(EffhtHLTMu15),
    ##     passing_ht_HLT_Mu15_HT200 = cms.PSet(EffhtHLTMu15HT200),
    ##     passing_ht_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffhtHLTHT250Mu15PFMHT20),
    ##     #passing_ht_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffhtHLTHT250Mu15PFMHT40),
    ##     #passing_ht_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffhtHLTHT300Mu15PFMHT40),
                                                         
    ##     #passing_met_HLT_Mu15_HToff300 = cms.PSet(EffmetHLTMu15HToff300),
    ##     passing_met_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffmetHLTHT250Mu15PFMHT20),
    ##     #passing_met_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffmetHLTHT250Mu15PFMHT40),
    ##     #passing_met_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffmetHLTHT300Mu15PFMHT40),
    
    ##     passing_reliso_HLT_Mu15 = cms.PSet(EffrelisoHLTMu15),
    ##     passing_reliso_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffrelisoHLTHT250Mu15PFMHT20),
    ##     #passing_reliso_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffrelisoHLTHT250Mu15PFMHT40),
    ##     #passing_reliso_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffrelisoHLTHT300Mu15PFMHT40),
    
    ##     passing_nvtx_HLT_Mu15 = cms.PSet(EffnvtxHLTMu15),
    ##     passing_nvtx_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffnvtxHLTHT250Mu15PFMHT20),
    ##     #passing_nvtx_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffnvtxHLTHT250Mu15PFMHT40),
    ##     #passing_nvtx_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffnvtxHLTHT300Mu15PFMHT40),
    
    )
    
    MCEfficiencies = cms.PSet(
    ##     passing_pt_HLT_Mu8 = cms.PSet(EffptHLTMu8),
    ##     passing_pt_HLT_Mu15 = cms.PSet(EffptHLTMu15),
    ##     passing_pt_HLT_Mu15_HToff300 = cms.PSet(EffptHLTMu15HToff300),
    ##     passing_pt_HLT_Mu15_with_PT15_LOWSTAT_BINS = cms.PSet(EffptHLTMu15_with_PT15_LOWSTAT_BINS),
    ##     passing_pt_HLT_Mu15_with_PT30_BINS = cms.PSet(EffptHLTMu15_with_PT30_BINS),
    ##     passing_pt_HLT_Mu15_with_PT40_BINS = cms.PSet(EffptHLTMu15_with_PT40_BINS),
    ##     #passing_pt_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffptHLTHT250Mu15PFMHT20),
    ##     #passing_pt_HLT_HT250_Mu15_PFMHT20_HToff300 = cms.PSet(EffptHLTHT250Mu15PFMHT20HToff300),
    ##     #passing_pt_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffptHLTHT250Mu15PFMHT40),
    ##     #passing_pt_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffptHLTHT300Mu15PFMHT40),
    ##     passing_pt_HLT_Mu8_HT200 = cms.PSet(EffptHLTMu8HT200),
    ##     #passing_pt_HLT_Mu15_HT200 = cms.PSet(EffptHLTMu15HT200),
    ##     #passing_pt_HLT_Mu30_HT200 = cms.PSet(EffptHLTMu30HT200),
    ##     #passing_pt_HLT_Mu40_HT200 = cms.PSet(EffptHLTMu40HT200),
    ##     #passing_pt_HLT_Mu40_HT300 = cms.PSet(EffptHLTMu40HT300),
    
    ##     passing_eta_HLT_Mu8 = cms.PSet(EffetaHLTMu8),
    ##     passing_eta_HLT_Mu15 = cms.PSet(EffetaHLTMu15),
    ##     passing_eta_HLT_Mu15_with_ETA_LOWSTAT_BINS = cms.PSet(EffetaHLTMu15_with_ETA_LOWSTAT_BINS),
    ## ##     passing_eta_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffetaHLTHT250Mu15PFMHT20),
    ## ##     passing_eta_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffetaHLTHT250Mu15PFMHT40),
    ## ##     #passing_eta_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffetaHLTHT300Mu15PFMHT40),
    ##     passing_eta_HLT_Mu8_HT200 = cms.PSet(EffetaHLTMu8HT200),
    ## ##     passing_eta_HLT_Mu15_HT200 = cms.PSet(EffetaHLTMu15HT200),
    ## ##     passing_eta_HLT_Mu30_HT200 = cms.PSet(EffetaHLTMu30HT200),
    ## ##     passing_eta_HLT_Mu40_HT200 = cms.PSet(EffetaHLTMu40HT200),
    ## ##     #passing_eta_HLT_Mu40_HT300 = cms.PSet(EffetaHLTMu40HT300),
                                                         
    ##    passing_ht_HLT_Mu15 = cms.PSet(EffhtHLTMu15),
    ## ##     passing_ht_HLT_Mu15_HT200 = cms.PSet(EffhtHLTMu15HT200),
    ## ##     passing_ht_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffhtHLTHT250Mu15PFMHT20),
    ## ##     passing_ht_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffhtHLTHT250Mu15PFMHT40),
    ## ##     #passing_ht_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffhtHLTHT300Mu15PFMHT40),
                                                         
    ##     passing_met_HLT_Mu15_HToff300 = cms.PSet(EffmetHLTMu15HToff300),
    ## ##     passing_met_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffmetHLTHT250Mu15PFMHT20),
    ## ##     passing_met_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffmetHLTHT250Mu15PFMHT40),
    ## ##     #passing_met_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffmetHLTHT300Mu15PFMHT40),
    
    ##     passing_reliso_HLT_Mu15 = cms.PSet(EffrelisoHLTMu15),
    ## ##     passing_reliso_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffrelisoHLTHT250Mu15PFMHT20),
    ## ##     passing_reliso_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffrelisoHLTHT250Mu15PFMHT40),
    ## ##     #passing_reliso_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffrelisoHLTHT300Mu15PFMHT40),
    
    ##     passing_nvtx_HLT_Mu15 = cms.PSet(EffnvtxHLTMu15),
    ## ##     passing_nvtx_HLT_HT250_Mu15_PFMHT20 = cms.PSet(EffnvtxHLTHT250Mu15PFMHT20),
    ## ##     passing_nvtx_HLT_HT250_Mu15_PFMHT40 = cms.PSet(EffnvtxHLTHT250Mu15PFMHT40),
    ## ##     #passing_nvtx_HLT_HT300_Mu15_PFMHT40 = cms.PSet(EffnvtxHLTHT300Mu15PFMHT40),
        
    )


if daten:
    EfficiencySelection = DataEfficiencies
else:
    EfficiencySelection = MCEfficiencies

if set2012:
    TriggerVariables = cms.PSet(
        tag_passingHLTMu5                       = cms.vstring("Tag passingHLTMu5",                     "0", "2", ""),
        tag_passingHLTMu12                      = cms.vstring("Tag passingHLTMu12",                    "0", "2", ""),
        tag_passingHLTMu24                      = cms.vstring("Tag passingHLTMu24",                    "0", "2", ""),
        tag_passingHLTIsoMu24                   = cms.vstring("Tag passingHLTIsoMu24",                 "0", "2", ""),
        tag_passingHLTIsoMu30                   = cms.vstring("Tag passingHLTIsoMu30",                 "0", "2", ""),
        tag_passingHLTIsoMu15eta2p1L1ETM20      = cms.vstring("Tag passingHLTIsoMu15eta2p1L1ETM20",    "0", "2", ""),
        tag_passingHLTIsoMu20eta2p1             = cms.vstring("Tag passingHLTIsoMu20eta2p1",           "0", "2", ""),
        tag_passingHLTIsoMu24eta2p1             = cms.vstring("Tag passingHLTIsoMu24eta2p1",           "0", "2", ""),
        tag_passingHLTIsoMu30eta2p1             = cms.vstring("Tag passingHLTIsoMu30eta2p1",           "0", "2", ""),
        tag_passingHLTIsoMu34eta2p1             = cms.vstring("Tag passingHLTIsoMu34eta2p1",           "0", "2", ""),
        tag_passingHLTIsoMu40eta2p1             = cms.vstring("Tag passingHLTIsoMu40eta2p1",           "0", "2", ""),
        #tag_passingHLT_IsoMu24                  = cms.vstring("Tag passing HLT_IsoMu24",                 "0", "2", ""),
        #tag_passingHLT_IsoMu30                  = cms.vstring("Tag passing HLT_IsoMu30",                 "0", "2", ""),
        #tag_passingHLT_IsoMu15_eta2p1_L1ETM20   = cms.vstring("Tag passing HLT_IsoMu15_eta2p1_L1ETM20",  "0", "2", ""),
        #tag_passingHLT_IsoMu20_eta2p1           = cms.vstring("Tag passing HLT_IsoMu20_eta2p1",          "0", "2", ""),
        #tag_passingHLT_IsoMu24_eta2p1           = cms.vstring("Tag passing HLT_IsoMu24_eta2p1",          "0", "2", ""),
        #tag_passingHLT_IsoMu30_eta2p1           = cms.vstring("Tag passing HLT_IsoMu30_eta2p1",          "0", "2", ""),
        #tag_passingHLT_IsoMu34_eta2p1           = cms.vstring("Tag passing HLT_IsoMu34_eta2p1",          "0", "2", ""),
        #tag_passingHLT_IsoMu40_eta2p1           = cms.vstring("Tag passing HLT_IsoMu40_eta2p1",          "0", "2", "")
        tag_passingHLT_Mu40_HT200               = cms.vstring("Tag passing HLT_Mu40_HT200",              "0", "2", ""),
        tag_passingHLT_Mu40_FJHT200             = cms.vstring("Tag passing HLT_Mu40_FJHT200",            "0", "2", ""),
        tag_passingHLT_Mu40_PFHT350             = cms.vstring("Tag passing HLT_Mu40_PFHT350",            "0", "2", ""),
        tag_passingHLT_Mu40_PFNoPUHT350         = cms.vstring("Tag passing HLT_Mu40_PFNoPUHT350",        "0", "2", ""),
        tag_passingHLT_Mu60_PFHT350             = cms.vstring("Tag passing HLT_Mu60_PFHT350",            "0", "2", ""),
        tag_passingHLT_Mu60_PFNoPUHT350         = cms.vstring("Tag passing HLT_Mu60_PFNoPUHT350",        "0", "2", ""),
        tag_passingHLT_PFHT350_Mu15_PFMET45     = cms.vstring("Tag passing HLT_PFHT350_Mu15_PFMET45",    "0", "2", ""),
        tag_passingHLT_PFNoPUHT350_Mu15_PFMET45 = cms.vstring("Tag passing HLT_PFNoPUHT350_Mu15_PFMET45","0", "2", ""),
        tag_passingHLT_PFHT350_Mu15_PFMET50     = cms.vstring("Tag passing HLT_PFHT350_Mu15_PFMET50",    "0", "2", ""),
        tag_passingHLT_PFNoPUHT350_Mu15_PFMET50 = cms.vstring("Tag passing HLT_PFNoPUHT350_Mu15_PFMET50","0", "2", ""),
        tag_passingHLT_PFHT400_Mu5_PFMET45      = cms.vstring("Tag passing HLT_PFHT400_Mu5_PFMET45",     "0", "2", ""),
        tag_passingHLT_PFNoPUHT400_Mu5_PFMET45  = cms.vstring("Tag passing HLT_PFNoPUHT400_Mu5_PFMET45", "0", "2", ""), 
        tag_passingHLT_PFHT400_Mu5_PFMET50      = cms.vstring("Tag passing HLT_PFHT400_Mu5_PFMET50",     "0", "2", ""),
        tag_passingHLT_PFNoPUHT400_Mu5_PFMET50  = cms.vstring("Tag passing HLT_PFNoPUHT400_Mu5_PFMET50", "0", "2", ""),
    )
    TriggerCategories = cms.PSet(
        # 2012
        passingHLTMu5                       = cms.vstring("Probe passingHLTMu5",                      "dummy[pass=1,fail=0]"),
        passingHLTMu12                      = cms.vstring("Probe passingHLTMu12",                     "dummy[pass=1,fail=0]"),
        passingHLTMu24                      = cms.vstring("Probe passingHLTMu24",                     "dummy[pass=1,fail=0]"),
        passingHLTIsoMu24                   = cms.vstring("Probe passingHLTIsoMu24",                  "dummy[pass=1,fail=0]"),
        passingHLTIsoMu30                   = cms.vstring("Probe passingHLTIsoMu30",                  "dummy[pass=1,fail=0]"),
        passingHLTIsoMu15eta2p1L1ETM20      = cms.vstring("Probe passingHLTIsoMu15eta2p1L1ETM20",     "dummy[pass=1,fail=0]"),
        passingHLTIsoMu20eta2p1             = cms.vstring("Probe passingHLTIsoMu20eta2p1",            "dummy[pass=1,fail=0]"),
        passingHLTIsoMu24eta2p1             = cms.vstring("Probe passingHLTIsoMu24eta2p1",            "dummy[pass=1,fail=0]"),
        passingHLTIsoMu30eta2p1             = cms.vstring("Probe passingHLTIsoMu30eta2p1",            "dummy[pass=1,fail=0]"),
        passingHLTIsoMu34eta2p1             = cms.vstring("Probe passingHLTIsoMu34eta2p1",            "dummy[pass=1,fail=0]"),
        passingHLTIsoMu40eta2p1             = cms.vstring("Probe passingHLTIsoMu40eta2p1",            "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu24                  = cms.vstring("Probe matched to HLT_IsoMu24",                 "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu30                  = cms.vstring("Probe matched to HLT_IsoMu30",                 "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu15_eta2p1_L1ETM20   = cms.vstring("Probe matched to HLT_IsoMu15_eta2p1_L1ETM20",  "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu20_eta2p1           = cms.vstring("Probe matched to HLT_IsoMu20_eta2p1",          "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu24_eta2p1           = cms.vstring("Probe matched to HLT_IsoMu24_eta2p1",          "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu24_eta2p1_5e33      = cms.vstring("Probe matched to HLT_IsoMu24_eta2p1 (5e33)",   "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu24_eta2p1_7e33      = cms.vstring("Probe matched to HLT_IsoMu24_eta2p1 (7e33)",   "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu30_eta2p1           = cms.vstring("Probe matched to HLT_IsoMu30_eta2p1",          "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu34_eta2p1           = cms.vstring("Probe matched to HLT_IsoMu34_eta2p1",          "dummy[pass=1,fail=0]"),
        #matchedHLT_IsoMu40_eta2p1           = cms.vstring("Probe matched to HLT_IsoMu40_eta2p1",          "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu24                  = cms.vstring("Tag matched to HLT_IsoMu24",                 "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu30                  = cms.vstring("Tag matched to HLT_IsoMu30",                 "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu15_eta2p1_L1ETM20   = cms.vstring("Tag matched to HLT_IsoMu15_eta2p1_L1ETM20",  "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu20_eta2p1           = cms.vstring("Tag matched to HLT_IsoMu20_eta2p1",          "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu24_eta2p1           = cms.vstring("Tag matched to HLT_IsoMu24_eta2p1",          "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu24_eta2p1_5e33      = cms.vstring("Tag matched to HLT_IsoMu24_eta2p1_5e33",     "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu24_eta2p1_7e33      = cms.vstring("Tag matched to HLT_IsoMu24_eta2p1_7e33",     "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu30_eta2p1           = cms.vstring("Tag matched to HLT_IsoMu30_eta2p1",          "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu34_eta2p1           = cms.vstring("Tag matched to HLT_IsoMu34_eta2p1",          "dummy[pass=1,fail=0]"),
        #tag_matchedHLT_IsoMu40_eta2p1           = cms.vstring("Tag matched to HLT_IsoMu40_eta2p1",          "dummy[pass=1,fail=0]"),
        matchedHLT_Mu40_HT200_Run2012       = cms.vstring("Probe matched to HLT_Mu40_HT200",              "dummy[pass=1,fail=0]"),
        matchedHLT_Mu40_FJHT200             = cms.vstring("Probe matched to HLT_Mu40_FJHT200",            "dummy[pass=1,fail=0]"),
        matchedHLT_Mu40_PFHT350             = cms.vstring("Probe matched to HLT_Mu40_PFHT350",            "dummy[pass=1,fail=0]"),
        matchedHLT_Mu40_PFNoPUHT350         = cms.vstring("Probe matched to HLT_Mu40_PFNoPUHT350",        "dummy[pass=1,fail=0]"),
        matchedHLT_Mu60_PFHT350             = cms.vstring("Probe matched to HLT_Mu60_PFHT350",            "dummy[pass=1,fail=0]"),
        matchedHLT_Mu60_PFNoPUHT350         = cms.vstring("Probe matched to HLT_Mu60_PFNoPUHT350",        "dummy[pass=1,fail=0]"),
        matchedHLT_PFHT350_Mu15_PFMET45     = cms.vstring("Probe matched to HLT_PFHT350_Mu15_PFMET45",    "dummy[pass=1,fail=0]"),
        matchedHLT_PFNoPUHT350_Mu15_PFMET45 = cms.vstring("Probe matched to HLT_PFNoPUHT350_Mu15_PFMET45","dummy[pass=1,fail=0]"),
        matchedHLT_PFHT350_Mu15_PFMET50     = cms.vstring("Probe matched to HLT_PFHT350_Mu15_PFMET50",    "dummy[pass=1,fail=0]"),
        matchedHLT_PFNoPUHT350_Mu15_PFMET50 = cms.vstring("Probe matched to HLT_PFNoPUHT350_Mu15_PFMET50","dummy[pass=1,fail=0]"),
        matchedHLT_PFHT400_Mu5_PFMET45      = cms.vstring("Probe matched to HLT_PFHT400_Mu5_PFMET45",     "dummy[pass=1,fail=0]"),
        matchedHLT_PFNoPUHT400_Mu5_PFMET45  = cms.vstring("Probe matched to HLT_PFNoPUHT400_Mu5_PFMET45", "dummy[pass=1,fail=0]"),
        matchedHLT_PFHT400_Mu5_PFMET50      = cms.vstring("Probe matched to HLT_PFHT400_Mu5_PFMET50",     "dummy[pass=1,fail=0]"),
        matchedHLT_PFNoPUHT400_Mu5_PFMET50  = cms.vstring("Probe matched to HLT_PFNoPUHT400_Mu5_PFMET50", "dummy[pass=1,fail=0]"),
        tag_matchedHLT_Mu40_HT200_Run2012       = cms.vstring("Tag matched to HLT_Mu40_HT200",              "dummy[pass=1,fail=0]"),
        tag_matchedHLT_Mu40_FJHT200             = cms.vstring("Tag matched to HLT_Mu40_FJHT200",            "dummy[pass=1,fail=0]"),
        tag_matchedHLT_Mu40_PFHT350             = cms.vstring("Tag matched to HLT_Mu40_PFHT350",            "dummy[pass=1,fail=0]"),
        tag_matchedHLT_Mu40_PFNoPUHT350         = cms.vstring("Tag matched to HLT_Mu40_PFNoPUHT350",        "dummy[pass=1,fail=0]"),
        tag_matchedHLT_Mu60_PFHT350             = cms.vstring("Tag matched to HLT_Mu60_PFHT350",            "dummy[pass=1,fail=0]"),
        tag_matchedHLT_Mu60_PFNoPUHT350         = cms.vstring("Tag matched to HLT_Mu60_PFNoPUHT350",        "dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFHT350_Mu15_PFMET45     = cms.vstring("Tag matched to HLT_PFHT350_Mu15_PFMET45",    "dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFNoPUHT350_Mu15_PFMET45 = cms.vstring("Tag matched to HLT_PFNoPUHT350_Mu15_PFMET45","dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFHT350_Mu15_PFMET50     = cms.vstring("Tag matched to HLT_PFHT350_Mu15_PFMET50",    "dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFNoPUHT350_Mu15_PFMET50 = cms.vstring("Tag matched to HLT_PFNoPUHT350_Mu15_PFMET50","dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFHT400_Mu5_PFMET45      = cms.vstring("Tag matched to HLT_PFHT400_Mu5_PFMET45",     "dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFNoPUHT400_Mu5_PFMET45  = cms.vstring("Tag matched to HLT_PFNoPUHT400_Mu5_PFMET45", "dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFHT400_Mu5_PFMET50      = cms.vstring("Tag matched to HLT_PFHT400_Mu5_PFMET50",     "dummy[pass=1,fail=0]"),
        tag_matchedHLT_PFNoPUHT400_Mu5_PFMET50  = cms.vstring("Tag matched to HLT_PFNoPUHT400_Mu5_PFMET50", "dummy[pass=1,fail=0]")
    )
    
    process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        InputFileNames = cms.vstring(selectedFiles),
        InputDirectoryName = cms.string("fitHltFromGlb"),
        InputTreeName = cms.string("fitter_tree"),
        #InputTreeName = cms.string("fitter_tree_stlep"),
        OutputFileName = cms.string(output),
        
        NumCPU = cms.uint32(6),
        SaveWorkspace = cms.bool(False),
        binnedFit = cms.bool(True),
        binsForFit = cms.uint32(40),    
        WeightVariable = cms.string(weightVar),
    
        Variables = TriggerVariables.clone(
            mass            = cms.vstring("Tag-Probe Mass",           "70",  "110", "GeV/c^{2}"),
            pt              = cms.vstring("Probe p_{T}",               "0",  "100", "GeV/c"),
            #pterror         = cms.vstring("Probe p_{T} error",         "0",    "1", "GeV/c"),
            eta             = cms.vstring("Probe #eta",             "-2.5",  "2.5", ""),
            abs_eta         = cms.vstring("Probe |#eta|",              "0",  "2.5", ""),
            #trkiso          = cms.vstring("Probe Track Isolation",     "0", "1000", "GeV"),
            #ecaliso         = cms.vstring("Probe ECal Isolation",      "0", "1000", "GeV"),
            #hcaliso         = cms.vstring("Probe HCal Isolation",      "0", "1000", "GeV"),
            #reliso          = cms.vstring("Probe Rel. Isolation",      "0",  "100", ""),
            drjet           = cms.vstring("Probe #DeltaR_{Jet}",       "0",    "7", ""),
            #njet            = cms.vstring("Probe N_{Jet}",             "0",   "20", ""),
            d0_v            = cms.vstring("Probe d0_{vertex}",       "-30",   "30", ""),
            #d0_b            = cms.vstring("Probe d0_{beamspot}",     "-30",   "30", ""),
            dz_v            = cms.vstring("Probe dz_{vertex}",       "-30",   "30", ""),
            #dz_b            = cms.vstring("Probe dz_{beamspot}",     "-30",   "30", ""),
            #pixlayer        = cms.vstring("Probe N_{pixLayer}",        "0",   "10", ""),
            #nmatches        = cms.vstring("Probe N_{matches}",         "0",   "10", ""),
            weight          = cms.vstring("Event Weight",              "0", "1000", ""),
            tag_ht          = cms.vstring("Event HT",                  "0", "1000", "GeV/c"),
            tag_met         = cms.vstring("Event MET",                 "0",  "500", "GeV"),
            tag_nVertices   = cms.vstring("Event N_{Vertices}",        "0",   "50", ""),
            tag_nVerticesDA = cms.vstring("Event pile-up",             "0",   "50", ""),
            #tag_ecaliso     = cms.vstring("Tag ECal Isolation",        "0", "1000", "Gev"),
            #tag_trkiso      = cms.vstring("Tag Track Isolation",       "0", "1000", "Gev"),
            #tag_hcaliso     = cms.vstring("Tag HCal Isolation",        "0", "1000", "Gev"),
            #tag_reliso      = cms.vstring("Tag Rel. Isolation",        "0",  "100", ""),
            #tag_passingHLTMu8                 = cms.vstring("Tag passingHLTMu8",                "0", "2", ""),
            #tag_passingHLTMu15                = cms.vstring("Tag passingHLTMu15",               "0", "2", ""),
            #tag_passingHLT_Mu8_HT200          = cms.vstring("Tag passing HLT_Mu8_HT200",          "0", "2", ""),
            #tag_passingHLT_Mu15_HT200         = cms.vstring("Tag passing HLT_Mu15_HT200",         "0", "2", ""),
            #tag_passingHLT_Mu30_HT200         = cms.vstring("Tag passing HLT_Mu30_HT200",         "0", "2", ""),
            #tag_passingHLT_Mu40_HT200         = cms.vstring("Tag passing HLT_Mu40_HT200",         "0", "2", ""),
            #tag_passingHLT_Mu40_HT300         = cms.vstring("Tag passing HLT_Mu40_HT300",         "0", "2", ""),
            #tag_passingHLT_HT250_Mu15_PFMHT20 = cms.vstring("Tag passing HLT_HT250_Mu15_PFMHT20", "0", "2", ""),
            #tag_passingHLT_HT250_Mu15_PFMHT40 = cms.vstring("Tag passing HLT_HT250_Mu15_PFMHT40", "0", "2", ""),
            #tag_passingHLT_HT300_Mu15_PFMHT40 = cms.vstring("Tag passing HLT_HT300_Mu15_PFMHT40", "0", "2", ""),
            # 2012 Specific Variables
            stlep         = cms.vstring("Probe ST", "0",  "10000", "GeV"),
            pfreliso        = cms.vstring("Probe Rel. Isolation (PF)", "0",  "100", ""),
            #tag_pfreliso    = cms.vstring("Tag Rel. Isolation (PF)",   "0",  "100", ""),
            absdeltapt         = cms.vstring("Probe Delta pt |Reco-PF|",  "0",  "100", "")
            #trklayer        = cms.vstring("Probe N_{trkLayer}",        "0",   "50", ""),
            #validpixhits    = cms.vstring("Probe N_{valid pixHits}",   "0",   "10", ""),
        ),
        
        Categories = TriggerCategories.clone(
            mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]")
            #passingHLTMu8                 = cms.vstring("Probe passingHLTMu8",                "dummy[pass=1,fail=0]"),
            #passingHLTMu15                = cms.vstring("Probe passingHLTMu15",               "dummy[pass=1,fail=0]"),
            #matchedHLT_Mu8_HT200          = cms.vstring("Probe matched to HLT_Mu8_HT200",          "dummy[pass=1,fail=0]"),
            #matchedHLT_Mu15_HT200         = cms.vstring("Probe matched to HLT_Mu15_HT200",         "dummy[pass=1,fail=0]"),
            #matchedHLT_Mu30_HT200         = cms.vstring("Probe matched to HLT_Mu30_HT200",         "dummy[pass=1,fail=0]"),
            #matchedHLT_Mu40_HT200         = cms.vstring("Probe matched to HLT_Mu40_HT200",         "dummy[pass=1,fail=0]"),
            #matchedHLT_Mu40_HT300         = cms.vstring("Probe matched to HLT_Mu40_HT300",         "dummy[pass=1,fail=0]"),
            #matchedHLT_HT250_Mu15_PFMHT20 = cms.vstring("Probe matched to HLT_HT250_Mu15_PFMHT20", "dummy[pass=1,fail=0]"),
            #matchedHLT_HT250_Mu15_PFMHT40 = cms.vstring("Probe matched to HLT_HT250_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
            #matchedHLT_HT300_Mu15_PFMHT40 = cms.vstring("Probe matched to HLT_HT300_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Mu8_HT200          = cms.vstring("Tag matched to HLT_Mu8_HT200",          "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Mu15_HT200         = cms.vstring("Tag matched to HLT_Mu15_HT200",         "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Mu30_HT200         = cms.vstring("Tag matched to HLT_Mu30_HT200",         "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Mu40_HT200         = cms.vstring("Tag matched to HLT_Mu40_HT200",         "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_Mu40_HT300         = cms.vstring("Tag matched to HLT_Mu40_HT300",         "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_HT250_Mu15_PFMHT20 = cms.vstring("Tag matched to HLT_HT250_Mu15_PFMHT20", "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_HT250_Mu15_PFMHT40 = cms.vstring("Tag matched to HLT_HT250_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
            #tag_matchedHLT_HT300_Mu15_PFMHT40 = cms.vstring("Tag matched to HLT_HT300_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
        ),
        
        Cuts = cms.PSet(
            # 2012 Cuts
            #deltar03   = cms.vstring("Delta R > 0.3",      "drjet",   "0.3"),
            #pfrelIso12 = cms.vstring("Rel Isol > 0.12", "pfreliso",  "0.12"),
            #d0_v002pos = cms.vstring("#Delta0 < 0.02",      "d0_v",  "0.02"),
            #dz_v05neg  = cms.vstring("#Deltaz > -1",        "dz_v",  "-0.5"),
            #dz_v05pos  = cms.vstring("#Deltaz < 1",         "dz_v",   "0.5"),
            #d0_v002neg = cms.vstring("#Delta0 > -0.02",     "d0_v", "-0.02"),
        ),
        
        PDFs = cms.PSet(
            #breitWignerPlusExponential = cms.vstring(
            #    "BreitWigner::signal(mass, mean[90.,80.,100.], width[2,1.5,2.5])",
            #    "Exponential::backgroundPass(mass, cPass[0,-1,1])",
            #    "Exponential::backgroundFail(mass, cFail[0,-1,1])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            vpvPlusExpo = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
                "Voigtian::signal1f(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2f(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
                "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
                "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.90]"
            ),
            #vpvPlusQuadratic = cms.vstring(
            #    "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            #    "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            #    "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            #    "Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1]})",
            #    "Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1]})",
            #    #"Exponential::backgroundPass(mass, lp[0,-5,5])",
            #    #"Exponential::backgroundFail(mass, lf[0,-5,5])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]"
            #),
            #                                             
            #gaussPlusLinear = cms.vstring(
            #    "Gaussian::signal(mass, mean[90,80,100], sigma[2,1,3])",
            #    "Chebychev::backgroundPass(mass, cPass[0,-1,1])",
            #    "Chebychev::backgroundFail(mass, cFail[0,-1,1])",
            #    "efficiency[0.9,0,1]",
            #    "signalFractionInPassing[0.9]",
            #),
    
        ),
    
        Efficiencies = EfficiencySelection,
    )
    
else:
    process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        InputFileNames = cms.vstring(selectedFiles),
        InputDirectoryName = cms.string("fitHltFromGlb"),
        InputTreeName = cms.string("fitter_tree"),
        OutputFileName = cms.string(output),
        
        NumCPU = cms.uint32(6),
        SaveWorkspace = cms.bool(False),
        binnedFit = cms.bool(False),
        binsForFit = cms.uint32(40),    
        WeightVariable = cms.string(weightVar),
    
        Variables = cms.PSet(
            mass            = cms.vstring("Tag-Probe Mass",           "70",  "110", "GeV/c^{2}"),
            pt              = cms.vstring("Probe p_{T}",               "0",  "100", "GeV/c"),
            pterror         = cms.vstring("Probe p_{T} error",         "0",    "1", "GeV/c"),
            eta             = cms.vstring("Probe #eta",             "-2.5",  "2.5", ""),
            abs_eta         = cms.vstring("Probe |#eta|",              "0",  "2.5", ""),
            trkiso          = cms.vstring("Probe Track Isolation",     "0", "1000", "GeV"),
            ecaliso         = cms.vstring("Probe ECal Isolation",      "0", "1000", "GeV"),
            hcaliso         = cms.vstring("Probe HCal Isolation",      "0", "1000", "GeV"),
            reliso          = cms.vstring("Probe Rel. Isolation",      "0",  "100", ""),
            drjet           = cms.vstring("Probe #DeltaR_{Jet}",       "0",    "7", ""),
            njet            = cms.vstring("Probe N_{Jet}",             "0",   "20", ""),
            d0_v            = cms.vstring("Probe d0_{vertex}",       "-30",   "30", ""),
            d0_b            = cms.vstring("Probe d0_{beamspot}",     "-30",   "30", ""),
            dz_v            = cms.vstring("Probe dz_{vertex}",       "-30",   "30", ""),
            dz_b            = cms.vstring("Probe dz_{beamspot}",     "-30",   "30", ""),
            pixlayer        = cms.vstring("Probe N_{pixLayer}",        "0",   "10", ""),
            nmatches        = cms.vstring("Probe N_{matches}",         "0",   "10", ""),
            weight          = cms.vstring("Event Weight",              "0", "1000", ""),
            tag_ht          = cms.vstring("Event HT",                  "0", "1000", "GeV/c"),
            tag_met         = cms.vstring("Event MET",                 "0",  "500", "GeV"),
            tag_nVertices   = cms.vstring("Event N_{Vertices}",        "0",   "50", ""),
            tag_nVerticesDA = cms.vstring("Event pile-up",             "0",   "50", ""),
            tag_ecaliso     = cms.vstring("Tag ECal Isolation",        "0", "1000", "Gev"),
            tag_trkiso      = cms.vstring("Tag Track Isolation",       "0", "1000", "Gev"),
            tag_hcaliso     = cms.vstring("Tag HCal Isolation",        "0", "1000", "Gev"),
            tag_reliso      = cms.vstring("Tag Rel. Isolation",        "0",  "100", ""),
            tag_passingHLTMu8                 = cms.vstring("Event passing HLT_Mu8",                "0", "2", ""),
            tag_passingHLTMu15                = cms.vstring("Event passing HLT_Mu15",               "0", "2", ""),
            tag_passingHLT_Mu8_HT200          = cms.vstring("Event passing HLT_Mu8_HT200",          "0", "2", ""),
            tag_passingHLT_Mu15_HT200         = cms.vstring("Event passing HLT_Mu15_HT200",         "0", "2", ""),
            tag_passingHLT_Mu30_HT200         = cms.vstring("Event passing HLT_Mu30_HT200",         "0", "2", ""),
            tag_passingHLT_Mu40_HT200         = cms.vstring("Event passing HLT_Mu40_HT200",         "0", "2", ""),
            tag_passingHLT_Mu40_HT300         = cms.vstring("Event passing HLT_Mu40_HT300",         "0", "2", ""),
            tag_passingHLT_HT250_Mu15_PFMHT20 = cms.vstring("Event passing HLT_HT250_Mu15_PFMHT20", "0", "2", ""),
            tag_passingHLT_HT250_Mu15_PFMHT40 = cms.vstring("Event passing HLT_HT250_Mu15_PFMHT40", "0", "2", ""),
            tag_passingHLT_HT300_Mu15_PFMHT40 = cms.vstring("Event passing HLT_HT300_Mu15_PFMHT40", "0", "2", "")
        ),
    
        Categories = cms.PSet(
            mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
            passingHLTMu8                 = cms.vstring("Probe passing    HLT_Mu8",                "dummy[pass=1,fail=0]"),
            passingHLTMu15                = cms.vstring("Probe passing    HLT_Mu15",               "dummy[pass=1,fail=0]"),
            matchedHLT_Mu8_HT200          = cms.vstring("Probe matched to HLT_Mu8_HT200",          "dummy[pass=1,fail=0]"),
            matchedHLT_Mu15_HT200         = cms.vstring("Probe matched to HLT_Mu15_HT200",         "dummy[pass=1,fail=0]"),
            matchedHLT_Mu30_HT200         = cms.vstring("Probe matched to HLT_Mu30_HT200",         "dummy[pass=1,fail=0]"),
            matchedHLT_Mu40_HT200         = cms.vstring("Probe matched to HLT_Mu40_HT200",         "dummy[pass=1,fail=0]"),
            matchedHLT_Mu40_HT300         = cms.vstring("Probe matched to HLT_Mu40_HT300",         "dummy[pass=1,fail=0]"),
            matchedHLT_HT250_Mu15_PFMHT20 = cms.vstring("Probe matched to HLT_HT250_Mu15_PFMHT20", "dummy[pass=1,fail=0]"),
            matchedHLT_HT250_Mu15_PFMHT40 = cms.vstring("Probe matched to HLT_HT250_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
            matchedHLT_HT300_Mu15_PFMHT40 = cms.vstring("Probe matched to HLT_HT300_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Mu8_HT200          = cms.vstring("Tag matched to HLT_Mu8_HT200",          "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Mu15_HT200         = cms.vstring("Tag matched to HLT_Mu15_HT200",         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Mu30_HT200         = cms.vstring("Tag matched to HLT_Mu30_HT200",         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Mu40_HT200         = cms.vstring("Tag matched to HLT_Mu40_HT200",         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_Mu40_HT300         = cms.vstring("Tag matched to HLT_Mu40_HT300",         "dummy[pass=1,fail=0]"),
            tag_matchedHLT_HT250_Mu15_PFMHT20 = cms.vstring("Tag matched to HLT_HT250_Mu15_PFMHT20", "dummy[pass=1,fail=0]"),
            tag_matchedHLT_HT250_Mu15_PFMHT40 = cms.vstring("Tag matched to HLT_HT250_Mu15_PFMHT40", "dummy[pass=1,fail=0]"),
            tag_matchedHLT_HT300_Mu15_PFMHT40 = cms.vstring("Tag matched to HLT_HT300_Mu15_PFMHT40", "dummy[pass=1,fail=0]")
        ),
    
        Cuts = cms.PSet(
            # 2011 Cuts
            deltar03 = cms.vstring("Delta R > 0.3", "drjet", "0.3"),
            relIso10 = cms.vstring("Rel Isol > 0.10", "reliso", "0.10"),
            d0_b002pos = cms.vstring("#Delta0 < 0.02", "d0_b", "0.02"),
            dz_v1neg = cms.vstring("#Deltaz > -1", "dz_v", "-1."),
            dz_v1pos = cms.vstring("#Deltaz < 1", "dz_v", "1."),
            d0_b002neg = cms.vstring("#Delta0 > -0.02", "d0_b", "-0.02"),
            pixlayer1 = cms.vstring("# Pixlayer hits >  1", "pixlayer", "1."),
            ptError0001 = cms.vstring("p_T error < 0.001", "pterror", "0.001"),
        ),
    
        PDFs = cms.PSet(
            breitWignerPlusExponential = cms.vstring(
                "BreitWigner::signal(mass, mean[90.,80.,100.], width[2,1.5,2.5])",
                "Exponential::backgroundPass(mass, cPass[0,-1,1])",
                "Exponential::backgroundFail(mass, cFail[0,-1,1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
    
            vpvPlusExpo = cms.vstring(
                "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
                "Voigtian::signal1f(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2f(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
                "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
                "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.90]"
            ),
    
            vpvPlusQuadratic = cms.vstring(
                "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
                "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
                "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
                "Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1]})",
                "Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1]})",
                #"Exponential::backgroundPass(mass, lp[0,-5,5])",
                #"Exponential::backgroundFail(mass, lf[0,-5,5])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]"
            ),
                                                         
            gaussPlusLinear = cms.vstring(
                "Gaussian::signal(mass, mean[90,80,100], sigma[2,1,3])",
                "Chebychev::backgroundPass(mass, cPass[0,-1,1])",
                "Chebychev::backgroundFail(mass, cFail[0,-1,1])",
                "efficiency[0.9,0,1]",
                "signalFractionInPassing[0.9]",
            ),
    
        ),
    
        Efficiencies = EfficiencySelection,
    )

process.fitness = cms.Path(
    process.TagProbeFitTreeAnalyzer
)

