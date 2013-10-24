import FWCore.ParameterSet.Config as cms

import sys
import os
import ROOT

isData = True
#suffix = "_lessdata"
#suffix = "_FastSim"
#suffix = "_lessdata_EB_EE"
#suffix = "_FastSim_EB_EE"
#suffix = "_noGOOD"
suffix = "_All2012"

#main_dir = "/home/jkarancs/gridout/LeptonEfficiency/Ele_ID_130112"
#main_dir = "/home/jkarancs/gridout/LeptonEfficiency/ID_lessdata/Ele_ID_130112"
main_dir = "/home/jkarancs/gridout/LeptonEfficiency/ID_lessdata/new/Ele_ID_130110"

pathNamesData = [
    main_dir+"/Data/SingleElectron_Run2012A-13Jul2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012A-recover-06Aug2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012B-13Jul2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012C-24Aug2012-v1/",
    main_dir+"/Data/SingleElectron_Run2012C-PromptReco-v2/",
    main_dir+"/Data/SingleElectron_Run2012D-PromptReco-v1/",
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
    output = "EleIDEffPlotData"+suffix+".root"
    weightVar = ""   
    theUnbinned = cms.vstring("mass")
    subdir  = ""
else:
    pathNames = pathNamesMC
    output = "EleIDEffPlotMC"+suffix+".root"
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


ET_BINS  = cms.PSet( probe_gsfEle_et  = cms.vdouble( 10, 20, 30, 40, 60, 80, 150 ) )

PT_BINS  = cms.PSet( probe_gsfEle_pt  = cms.vdouble( 10, 20, 30, 40, 60, 80, 150 ) )

PT20_BIN = cms.PSet( probe_gsfEle_pt  = cms.vdouble( 20, 200 ) )

ET_ETA_POG_BINS  = cms.PSet(
    probe_gsfEle_et  = cms.vdouble( 10, 15, 20, 30, 40, 50, 200 ),
    probe_gsfEle_abseta = cms.vdouble( 0, 0.8, 1.4442, 1.556, 2.0, 2.5 ),
)

EB_EE_BINS = cms.PSet( probe_gsfEle_abseta = cms.vdouble( 0, 1.5, 2.5 ) )

ETA_BINS = cms.PSet(
    probe_gsfEle_pt  = cms.vdouble( 20, 200 ),
    probe_gsfEle_eta = cms.vdouble( -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5 ),
)


NVTX_BINS  = cms.PSet(
    probe_gsfEle_pt  = cms.vdouble( 20, 200 ),
    nVertices = cms.vdouble(0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 27.5, 30.5, 35.5, 40.5),    
)

NJET_BINS  = cms.PSet(
    probe_gsfEle_pt  = cms.vdouble( 20, 200 ),
    njet = cms.vdouble(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5),
)

#BinToPDFmap = cms.vstring("vpvPlusExpo","*pt_bin3*","vpvPlusExpo","*pt_bin4*","vpvPlusExpo","*pt_bin5*","vpvPlusExpo"),   

ID_ET = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring(#"probe_isRA4","pass", #Obsolete: passes if passingGOOD passes
                                             "probe_passingGOOD","pass",
                                             "probe_passConvRej","pass",
                                             "d0_v002pos","below",
                                             "d0_v002neg","above",
                                             "dz_v01pos","below",
                                             "dz_v01neg","above",
                                             "reliso_015","below",
                                             "drjet_03","above",
                                             "absdeltapt_10pos","below",
                                             "absdeltapt_10000neg","above"),
    UnbinnedVariables = theUnbinned,
    BinnedVariables = cms.PSet(ET_BINS, EB_EE_BINS),
    BinToPDFmap = cms.vstring("vpvPlusExpo"),
)

ID_PT = ID_ET.clone(BinnedVariables = cms.PSet(PT_BINS, EB_EE_BINS))

ID_ETA = ID_ET.clone(BinnedVariables = cms.PSet(ETA_BINS))

ID_PT20 = ID_ET.clone(BinnedVariables = cms.PSet(PT20_BIN, EB_EE_BINS))

ID_ETA = ID_ET.clone(BinnedVariables = cms.PSet(ETA_BINS))

ID_NVTX = ID_ET.clone(BinnedVariables = cms.PSet(NVTX_BINS, EB_EE_BINS))

ID_NJET = ID_ET.clone(BinnedVariables = cms.PSet(NJET_BINS, EB_EE_BINS))

ID_POG_ET_ETA = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("probe_passingGOOD","pass",
                                             "probe_passConvRej","pass",
                                             "probe_isRA4","pass",
                                             "d0_v002pos","below",
                                             "d0_v002neg","above",
                                             "dz_v01pos","below",
                                             "dz_v01neg","above",
                                             "reliso_015","below"),
    UnbinnedVariables = theUnbinned,
    BinnedVariables = cms.PSet(ET_ETA_POG_BINS),
    BinToPDFmap = cms.vstring("vpvPlusExpo"),
)


#probe_gsfEle_eta = cms.vdouble(-2.5, 2.5),
#d0_v = cms.vdouble(-0.02, 0.02),
#dz_v = cms.vdouble(-0.1, 0.1),
#reliso = cms.vdouble(0., 0.15),
#drjet = cms.vdouble(0.3, 7),
#absdeltapt = cms.vdouble(-10000., 5.0),


Efficiencies = cms.PSet(
    ID_et = cms.PSet(ID_ET),
    ID_eta = cms.PSet(ID_ETA),
    ID_nvtx = cms.PSet(ID_NVTX),
    ID_njet = cms.PSet(ID_NJET),
    ID_pt = cms.PSet(ID_PT),
    ID_pt20 = cms.PSet(ID_PT20),
    #ID_POG_et_eta = cms.PSet(ID_POG_ET_ETA),
)

process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    InputFileNames = selectedAll,
    InputDirectoryName = cms.string("GsfElectronToIdPATTag"),
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
        probe_gsfEle_et = cms.vstring("electron E_{T}", "0", "1000", "GeV"),
        probe_gsfEle_pt = cms.vstring("electron p_{T}", "0", "1000", "GeV/c"),
        probe_gsfEle_eta    = cms.vstring("electron #eta", "-2.5", "2.5", ""),
        probe_gsfEle_abseta = cms.vstring("electron |#eta|", "0", "2.5", ""),
        #probe_gsfEle_phi    = cms.vstring("electron #phi at vertex", "-3.1416", "3.1416", ""),
        #probe_gsfEle_charge = cms.vstring("electron charge", "-2.5", "2.5", ""),
        tag_gsfEle_et = cms.vstring("Tag E_{T}", "0", "1000", "GeV/c"),
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
        njet   = cms.vstring("number of jets_{pt>40}", "0", "100", ""),
        absdeltapt = cms.vstring("|Reco pt - PF pt|", "0", "9999999", "Gev/c"),
        reliso = cms.vstring("Rel. Iso. ", "0", "9999999", ""),
    ),
    
    Categories = cms.PSet(
        probe_passingGOOD = cms.vstring("GsfEle passing as PatEle", "dummy[pass=1,fail=0]"),
        probe_passConvRej = cms.vstring("Passing Conversion rejection", "dummy[pass=1,fail=0]"),
        probe_isRA4 = cms.vstring("RA4 Cuts, not comprehensive", "dummy[pass=1,fail=0]"),
        #mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    ),
    #probe_gsfEle_eta = cms.vdouble(-2.5, 2.5),
    #d0_v = cms.vdouble(-0.02, 0.02),
    #dz_v = cms.vdouble(-0.1, 0.1),
    #reliso = cms.vdouble(0., 0.15),
    #drjet = cms.vdouble(0.3, 7),
    #absdeltapt = cms.vdouble(-10000., 5.0),

    Cuts = cms.PSet(
        d0_v002pos    = cms.vstring("d0 < 0.02", "d0_v", "0.02"),
        d0_v002neg    = cms.vstring("d0 > -0.02", "d0_v", "-0.02"),
        dz_v01neg     = cms.vstring("dz > -0.1", "dz_v", "-0.1"),
        dz_v01pos     = cms.vstring("dz < 0.1", "dz_v", "0.1"),
        drjet_03      = cms.vstring("deltaR (nearest Jet > 0.3", "drjet", "0.3"),
        reliso_015  = cms.vstring("RelIso  < 0.15", "reliso", "0.15"),
        absdeltapt_10pos    = cms.vstring("|delta pt| < 10", "absdeltapt", "10.",),
        absdeltapt_10000neg = cms.vstring("|delta pt| > -10000", "absdeltapt", "-10000.",),
    ),
    
    PDFs = cms.PSet(
        #voigtPlusExpo = cms.vstring(
        #    "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
        #    "Exponential::backgroundPass(mass, lp[0,-5,5])",
        #    "Exponential::backgroundFail(mass, lf[0,-5,5])",
        #    "efficiency[0.9,0,1]",
        #    "signalFractionInPassing[0.9]"
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
        #vpvPlusExpo2 = cms.vstring(
        #    "Voigtian::signal1p(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
        #    "Voigtian::signal2p(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
        #    "SUM::signalPass(vFrac[0.8,0,1]*signal1p, signal2p)",
        #    "Voigtian::signal1f(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
        #    "Voigtian::signal2f(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
        #    "SUM::signalFail(vFrac[0.8,0,1]*signal1f, signal2f)",
        #    "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
        #    "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
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

