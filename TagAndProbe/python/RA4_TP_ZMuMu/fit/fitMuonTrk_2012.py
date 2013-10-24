import FWCore.ParameterSet.Config as cms

import sys
import os
import ROOT

isData = False
#suffix = "_lessdata"
suffix = "_FastSim"
#suffix = "_drjet"

#main_dir = "/home/jkarancs/gridout/LeptonEfficiency/Mu_ID_130110"
main_dir = "/home/jkarancs/gridout/LeptonEfficiency/ID_lessdata/Mu_ID_130110"

pathNamesData = [
    main_dir+"/Data/SingleMu_Run2012A-13Jul2012-v1/",
    main_dir+"/Data/SingleMu_Run2012A-recover-06Aug2012-v1/",
    main_dir+"/Data/SingleMu_Run2012B-13Jul2012-v1/",
    main_dir+"/Data/SingleMu_Run2012C-24Aug2012-v1/",
    main_dir+"/Data/SingleMu_Run2012C-PromptReco-v2/",
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
if isData:
    pathNames = pathNamesData
    output = "MuonTrkEffPlotData"+suffix+".root"
    weightVar = ""   
    theUnbinned = cms.vstring("mass")
    subdir  = ""
else:
    pathNames = pathNamesMC
    output = "MuonTrkEffPlotMC"+suffix+".root"
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



print str(len(selectedAll)) + " files added"
           
process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

#- Reco efficiency:
#    * standalone muon hit, pt > 5 GeV, |eta| < 2.4
#    --> van tracker track
#- ID efficiency:
#    * van track, (pt > 5 GeV, |eta| < 2.4, 5 valid hit)
#    --> van global fit
#    --> jo minosegu muon: impakt parameter, pt, eta stb... (RA4 szelekciok)

#ra4idcuts:
# pMu->isGood("GlobalMuonPromptTight") && 
# pMu->isPFMuon() && 
# pMu->track()->hitPattern().trackerLayersWithMeasurement() > 5 && 
# pMu->numberOfMatchedStations() >= 2 && 
# pMu->innerTrack()->hitPattern().numberOfValidPixelHits() > 0 && 
# abs(pMu->eta()) < 2.4;

#additional RA4 cuts:
# d0_v = cms.vdouble(-0.02, 0.02),
# dz_v = cms.vdouble(-0.5, 0.5),
# drjet = cms.vdouble(0.3, 7),
# pfreliso = cms.vdouble(0., 0.12),
# absdeltapt = cms.vdouble(-10000., 5.0),

PT_BINS = cms.PSet( pt  = cms.vdouble( 10, 20, 30, 40, 50, 65, 80, 200 ) )

PT20_BIN = cms.PSet( pt  = cms.vdouble( 20, 200 ) )

ABSETA24_BIN = cms.PSet( abs_eta = cms.vdouble( 0, 2.4 ) )

ETA_BINS = cms.PSet(
    pt  = cms.vdouble( 20, 200 ),
    eta = cms.vdouble( -2.4, -2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.4 ),
)


NVTX_BINS  = cms.PSet(
    pt  = cms.vdouble( 20, 200 ),
    abs_eta = cms.vdouble( 0, 2.4 ),
    tag_nVertices = cms.vdouble(0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 27.5, 30.5, 35.5, 40.5),    
)

NJET_BINS  = cms.PSet(
    pt  = cms.vdouble( 20, 200 ),
    abs_eta = cms.vdouble( 0, 2.4 ),
    njet = cms.vdouble(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5),
)

DRJET_BINS  = cms.PSet(
    pt  = cms.vdouble( 20, 200 ),
    abs_eta = cms.vdouble( 0, 2.4 ),
    drjet = cms.vdouble(0.0, 0.3, 0.6, 0.9, 1.3, 1.7, 2.1, 2.5, 3, 3.5, 4, 4.5),
)

Trk_PT = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("passing","pass"),
    UnbinnedVariables = theUnbinned,
    BinnedVariables = cms.PSet(PT_BINS, ABSETA24_BIN),
    BinToPDFmap = cms.vstring("vpvPlusExpo"),
)
Trk_ETA = Trk_PT.clone(BinnedVariables = cms.PSet(ETA_BINS))

Trk_PT20 = Trk_PT.clone(BinnedVariables = cms.PSet(PT20_BIN, ABSETA24_BIN))

Trk_NVTX = Trk_PT.clone(BinnedVariables = cms.PSet(NVTX_BINS))

Trk_NJET = Trk_PT.clone(BinnedVariables = cms.PSet(NJET_BINS))

Trk_DRJET = Trk_PT.clone(BinnedVariables = cms.PSet(DRJET_BINS))


Efficiencies = cms.PSet(
    #Trk_pt  = cms.PSet(Trk_PT),
    #Trk_eta = cms.PSet(Trk_ETA),
    #Trk_pt20 = cms.PSet(Trk_PT20),
    #Trk_nvtx  = cms.PSet(Trk_NVTX),
    #Trk_njet  = cms.PSet(Trk_NJET),
    Trk_drjet  = cms.PSet(Trk_DRJET),
)


#selectedAll = cms.vstring("/home/common/CMSSW/LeptonEfficiency/CMSSW_5_3_3_patch2/src/RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/tpZMuMu_ID_Data.root")

process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    InputFileNames = selectedAll,
    InputDirectoryName = cms.string("fitTkFromSta"),
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
        pt = cms.vstring("electron p_{T}", "0", "1000", "GeV/c"),
        eta = cms.vstring("electron #eta", "-2.5", "2.5", ""),
        abs_eta = cms.vstring("electron |#eta|", "0", "2.5", ""),
        #phi = cms.vstring("electron #phi at vertex", "-3.1416", "3.1416", ""),
        tag_nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
        #ecaliso    = cms.vstring("Probe ecal iso", "-2", "9999999", ""),
        #hcaliso    = cms.vstring("Probe hcal iso", "-2", "9999999", ""),
        #trkiso    = cms.vstring("Probe trk iso", "-2", "9999999", ""),
        #tag_ecaliso = cms.vstring("Tag ecal iso", "-2", "9999999", ""),
        #tag_hcaliso = cms.vstring("Tag hcal iso", "-2", "9999999", ""),
        #tag_trkiso = cms.vstring("Tag trk iso", "-2", "9999999", ""),
        d0_v     = cms.vstring("electron d0_{vertex}"  , "-20", "20", "cm"),
        #d0_b     = cms.vstring("electron d0_{beamspot}", "-20", "20", "cm"),
        dz_v     = cms.vstring("electron dz_{vertex}"  , "-20", "20", "cm"),
        #dz_b     = cms.vstring("electron dz_{beamspot}", "-20", "20", "cm"),
        drjet  = cms.vstring("electron-jet_{pt>30} #DeltaR", "0", "10000000000", ""),
        njet   = cms.vstring("number of jets_{pt>40}", "0", "100", ""),
    ),
    
    Categories = cms.PSet(
        passing = cms.vstring("Sta Probe passing as Track", "dummy[pass=1,fail=0]"),
        #mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    ),

    Cuts = cms.PSet(),
    
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
        #    "Voigtian::signal1f(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
        #    "Voigtian::signal2f(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
        #    "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
        #    "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
        #    "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
        #    "efficiency[0.9,0,1]",
        #    "signalFractionInPassing[0.90]"
        #),
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
        #    "Voigtian::signal1p(mass, mean1[90.4,88,93], width[2.495], sigma1[2,1,3])",
        #    "Voigtian::signal2p(mass, mean2[88,85,95], width,        sigma2[4,2,10])",
        #    "SUM::signalPass(vFrac[0.7,0,1]*signal1p, signal2p)",
        #    "Voigtian::signal1f(mass, mean1, width, sigma1)",
        #    "Voigtian::signal2f(mass, mean2, width, sigma2)",
        #    "SUM::signalFail(vFrac*signal1f, signal2f)",
        #    "Chebychev::backgroundPass(mass, {cPass1[-0.1,-1,1], cPass2[-0.5,-1,1]})",
        #    "Chebychev::backgroundFail(mass, {cFail1[-0.8,-1,1], cFail2[0.3,-1,1]})",
        #    #"Exponential::backgroundPass(mass, lp[0,-5,5])",
        #    #"Exponential::backgroundFail(mass, lf[0,-5,5])",
        #    "efficiency[0.9,0.,1.]",
        #    "signalFractionInPassing[0.9]"
        #),
    ),
    
    Efficiencies = Efficiencies,
)

process.fit = cms.Path(process.TagProbeFitTreeAnalyzer)

