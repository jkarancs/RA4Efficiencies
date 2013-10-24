import FWCore.ParameterSet.Config as cms

import sys
import os
import ROOT

isMC = True
suffix = "_FastSim"

main_dir = "/home/jkarancs/gridout/LeptonEfficiency/ID_lessdata/Ele_ID_130112"

pathNamesData = [
    main_dir+"/Data/SingleElectron_Run2012A-13Jul2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012A-recover-06Aug2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012B-13Jul2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012C-24Aug2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012C-PromptReco-v2/",
]

pathNamesMC = [
    # FastSim Sample
    main_dir+"/MC/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball_FastSim/",
    # Standard Model background
    #main_dir+"/MC/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/",
    #main_dir+"/MC/QCD_HT-250To500_TuneZ2star_8TeV-madgraph-pythia6/",
    #main_dir+"/MC/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/",
    #main_dir+"/MC/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/",
    #main_dir+"/MC/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/",
    #main_dir+"/MC/T_s-channel_TuneZ2star_8TeV-powheg-tauola/",
    #main_dir+"/MC/T_t-channel_TuneZ2star_8TeV-powheg-tauola/",
    #main_dir+"/MC/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/",
    #main_dir+"/MC/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/",
    #main_dir+"/MC/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/",
    #main_dir+"/MC/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/",
    #main_dir+"/MC/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/",
    #main_dir+"/MC/WW_TuneZ2star_8TeV_pythia6_tauola/",
    #main_dir+"/MC/WZ_TuneZ2star_8TeV_pythia6_tauola/",
    #main_dir+"/MC/ZZ_TuneZ2star_8TeV_pythia6_tauola/",
]

pathNames = []
if not isMC:
    pathNames = pathNamesData
    output = "EleGsfEffPlotData"+suffix+".root"
    weightVar = ""   
    theUnbinned = cms.vstring("mass")
    subdir  = ""
else:
    pathNames = pathNamesMC
    output = "EleGsfEffPlotMC"+suffix+".root"
    weightVar = "weight"   
    theUnbinned = cms.vstring("mass",weightVar)
    subdir  = "vtx_reweighted/"

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
            #print "   adding file " + dir + file
    for file in selectedFiles:
        selectedAll.append(file)
    print "      " + str(len(selectedFiles)) + " selected files"

#selectedAll = cms.vstring("/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZEE/tpZEE_ID_Data.root")


print str(len(selectedAll)) + " files added"
           
process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )


PT_BINS  = cms.PSet( probe_pt  = cms.vdouble( 10, 20, 30, 40, 60, 80, 150 ) )

ETA_BINS = cms.PSet(
    probe_pt  = cms.vdouble( 20, 200 ),
    probe_eta = cms.vdouble( -2.5, -2.1, -1.6, -1.1, -0.6, 0.0, 0.6, 1.1, 1.6, 2.1, 2.5 ),
)

PT20_BIN = cms.PSet( probe_pt  = cms.vdouble( 20, 200 ) )


ET_BINS  = cms.PSet( probe_et  = cms.vdouble( 10, 20, 30, 40, 60, 80, 150 ) )

ETA_ET20_BINS = cms.PSet(
    probe_et  = cms.vdouble( 20, 200 ),
    probe_eta = cms.vdouble( -2.5, -2.1, -1.6, -1.1, -0.6, 0.0, 0.6, 1.1, 1.6, 2.1, 2.5 ),
)

ABSETA25_BIN = cms.PSet( probe_abseta = cms.vdouble( -2.5, 2.5 ) )



#BinToPDFmap = cms.vstring("vpvPlusExpo","*pt_bin3*","vpvPlusExpo","*pt_bin4*","vpvPlusExpo","*pt_bin5*","vpvPlusExpo"),   

Gsf_PT = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("probe_passingGsf","pass"),
    UnbinnedVariables = theUnbinned,
    BinnedVariables = cms.PSet(PT_BINS, ABSETA25_BIN),
    BinToPDFmap = cms.vstring("vpvPlusExpo"),
)
Gsf_ETA = Gsf_PT.clone(BinnedVariables = cms.PSet(ETA_BINS))

Gsf_PT20 = Gsf_PT.clone(BinnedVariables = cms.PSet(PT20_BIN, ABSETA25_BIN))

Gsf_ET = Gsf_PT.clone(BinnedVariables = cms.PSet(ET_BINS, ABSETA25_BIN))

Gsf_ETA_ET20 = Gsf_PT.clone(BinnedVariables = cms.PSet(ETA_ET20_BINS))


Efficiencies = cms.PSet(
    Gsf_pt  = cms.PSet(Gsf_PT),
    Gsf_eta = cms.PSet(Gsf_ETA),
    Gsf_pt20 = cms.PSet(Gsf_PT20),
    
    Gsf_et = cms.PSet(Gsf_ET),
    Gsf_eta_et20 = cms.PSet(Gsf_ETA_ET20),
)

process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    InputFileNames = selectedAll,
    InputDirectoryName = cms.string("SuperClusterToGsfElectronPATTag"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string(output),
    
    NumCPU = cms.uint32(6),
    SaveWorkspace = cms.bool(False),
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    WeightVariable = cms.string(weightVar),
    
    Variables = cms.PSet(
        weight   = cms.vstring("MC event weight", "0", "100000000", ""),
        mass = cms.vstring("Tag-Electron Mass", "60", "120", "GeV/c^{2}"),
        probe_et = cms.vstring("supercluster E_{T}", "0", "1000", "GeV"),
        probe_pt = cms.vstring("supercluster p_{T}", "0", "1000", "GeV/c"),
        probe_eta    = cms.vstring("supercluster #eta", "-2.5", "2.5", ""),
        probe_abseta = cms.vstring("supercluster |#eta|", "0", "2.5", ""),
        probe_phi    = cms.vstring("supercluster #phi at vertex", "-3.1416", "3.1416", ""),
        tag_et = cms.vstring("Tag E_{T}", "0", "1000", "GeV/c"),
        nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
    ),
    
    Categories = cms.PSet(
        probe_passingGsf = cms.vstring("SuperCluster passing as GsfEle", "dummy[pass=1,fail=0]"),
    ),

    Cuts = cms.PSet(),
    
    PDFs = cms.PSet(
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1p(mass, mean1[90.4,88,93], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2p(mass, mean2[88,85,95], width,        sigma2[4,2,10])",
            "SUM::signalPass(vFrac[0.7,0.,1.]*signal1p, signal2p)",
            "Voigtian::signal1f(mass, mean1, width, sigma1)",
            "Voigtian::signal2f(mass, mean2, width, sigma2)",
            "SUM::signalFail(vFrac*signal1f, signal2f)",
            "Exponential::backgroundPass(mass, lp[1.54097e-03,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-3.23960e-02,-1,0.1])",
            "efficiency[0.9,0.,1.]",
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
            "Voigtian::signal1p(mass, mean1[90.4,88,93], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2p(mass, mean2[88,85,95], width,        sigma2[4,2,10])",
            "SUM::signalPass(vFrac[0.7,0,1]*signal1p, signal2p)",
            "Voigtian::signal1f(mass, mean1, width, sigma1)",
            "Voigtian::signal2f(mass, mean2, width, sigma2)",
            "SUM::signalFail(vFrac*signal1f, signal2f)",
            "Chebychev::backgroundPass(mass, {cPass1[-0.1,-1,1], cPass2[-0.5,-1,1]})",
            "Chebychev::backgroundFail(mass, {cFail1[-0.8,-1,1], cFail2[0.3,-1,1]})",
            #"Exponential::backgroundPass(mass, lp[0,-5,5])",
            #"Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0.,1.]",
            "signalFractionInPassing[0.9]"
        ),
    ),
    
    Efficiencies = Efficiencies,
)

process.fit = cms.Path(process.TagProbeFitTreeAnalyzer)

