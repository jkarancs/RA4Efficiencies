## /*****************************************************************************
##  Code taken form 
##  V04-01-01      PhysicsTools/TagAndProbe
##  and modified to run with SUSYPat recipie for 2011 RA4 electron TP-studies 
##  by Wolfgang Kiesenhofer (HEPHY Vienna)
##  *****************************************************************************/

import FWCore.ParameterSet.Config as cms

def initTP(process, MC_flag):

    process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
    process.load("Configuration.StandardSequences.Geometry_cff")
    process.load('FWCore.MessageService.MessageLogger_cfi')
    process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
    #process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
      
    process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")
               
    ELECTRON_ET_CUT_MIN = 5.0 # was 10.0
    ELECTRON_COLL = "gsfElectrons"
    #ELECTRON_CUTS = "ecalDrivenSeed==1 && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
    ELECTRON_CUTS = "ecalDrivenSeed==1 && abs(superCluster.eta) <= 2.5  && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
        
    SUPERCLUSTER_COLL_EB = "correctedHybridSuperClusters"#"hybridSuperClusters"
    SUPERCLUSTER_COLL_EE = "correctedMulti5x5SuperClustersWithPreshower"#"multi5x5SuperClustersWithPreshower"
    if MC_flag:
        SUPERCLUSTER_COLL_EB = "correctedHybridSuperClusters"
        SUPERCLUSTER_COLL_EE = "correctedMulti5x5SuperClustersWithPreshower"
    SUPERCLUSTER_CUTS = "abs(eta)<2.5 &&  et>" + str(ELECTRON_ET_CUT_MIN)
    
    
    JET_COLL = "ak5PFJets"
    JET_CUTS =  "abs(eta)<2.6 && chargedHadronEnergyFraction>0 && electronEnergyFraction<0.1 && nConstituents>1 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99"
    
    ########################
    
    
    ##   ____                         ____ _           _            
    ##  / ___| _   _ _ __   ___ _ __ / ___| |_   _ ___| |_ ___ _ __ 
    ##  \___ \| | | | '_ \ / _ \ '__| |   | | | | / __| __/ _ \ '__|
    ##   ___) | |_| | |_) |  __/ |  | |___| | |_| \__ \ ||  __/ |   
    ##  |____/ \__,_| .__/ \___|_|   \____|_|\__,_|___/\__\___|_|   
    ##  
    
    #  SuperClusters  ################
    process.superClusters = cms.EDProducer("SuperClusterMerger",
       src = cms.VInputTag(cms.InputTag( SUPERCLUSTER_COLL_EB ,""),
                           cms.InputTag( SUPERCLUSTER_COLL_EE ,"") )  
    )
    
    process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
       src = cms.InputTag("superClusters"),
       particleType = cms.int32(11),
    )
    
    #   Get the above SC's Candidates and place a cut on their Et and eta
    process.goodSuperClusters = cms.EDFilter("CandViewSelector",
          src = cms.InputTag("superClusterCands"),
          cut = cms.string( SUPERCLUSTER_CUTS ),
          filter = cms.bool(True)
    )
                                             
    
    #### remove real jets (with high hadronic energy fraction) from SC collection
    ##### this improves the purity of the probe sample without affecting efficiency    
    process.JetsToRemoveFromSuperCluster = cms.EDFilter("CaloJetSelector",   
        src = cms.InputTag("ak5CaloJets"),
        cut = cms.string('pt>5 && energyFractionHadronic > 0.15')
    )
    process.goodSuperClustersClean = cms.EDProducer("CandViewCleaner",
        srcObject = cms.InputTag("goodSuperClusters"),
        module_label = cms.string(''),
        srcObjectsToRemove = cms.VInputTag(cms.InputTag("JetsToRemoveFromSuperCluster")),
        deltaRMin = cms.double(0.1)
    )
    
    
    process.sc_sequence = cms.Sequence(
        process.superClusters +
        process.superClusterCands +
        process.goodSuperClusters +
        process.JetsToRemoveFromSuperCluster +
        process.goodSuperClustersClean
    )
    
    
    ##    ____      __ _____ _           _                   
    ##   / ___|___ / _| ____| | ___  ___| |_ _ __ ___  _ __  
    ##  | |  _/ __| |_|  _| | |/ _ \/ __| __| '__/ _ \| '_ \ 
    ##  | |_| \__ \  _| |___| |  __/ (__| |_| | | (_) | | | |
    ##   \____|___/_| |_____|_|\___|\___|\__|_|  \___/|_| |_|
    ##  
    #  GsfElectron ################ 
    process.goodElectrons = cms.EDFilter("GsfElectronRefSelector",
        src = cms.InputTag( ELECTRON_COLL ),
        cut = cms.string( ELECTRON_CUTS )    
    )
        
    process.GsfMatchedSuperClusterCands = cms.EDProducer("ElectronMatchedCandidateProducer",
       src     = cms.InputTag("goodSuperClustersClean"),
       ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
       deltaR =  cms.untracked.double(0.3)
    )
    
    # 2012 SingleElectron Triggers
    # HLT_Ele22_CaloIdL_CaloIsoVL
    # HLT_Ele27_CaloIdL_CaloIsoVL
    # HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    # HLT_Ele27_WP80
    # HLT_Ele27_WP80_PFMET_MT50
    # #HLT_Ele27_WP80_CentralPFJet80
    # #HLT_Ele27_WP80_WCandPt80
    # HLT_Ele30_CaloIdVT_TrkIdT
    # HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
    # HLT_Ele65_CaloIdVT_TrkIdT
    # HLT_Ele80_CaloIdVT_TrkIdT
    # HLT_Ele80_CaloIdVT_GsfTrkIdT
    # HLT_Ele90_CaloIdVT_GsfTrkIdT
    # HLT_Ele100_CaloIdVT_TrkIdT
    # 2012 EleHad Triggers                                                 Filter
    # HLT_Ele8_CaloIdT_TrkIdVL_Jet30              
    # HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45      hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET45
    # HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50      hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET50
    # HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45  hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET45
    # HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50  hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET50
    # HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45     hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET45
    # HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50     hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET50
    # HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET45
    # HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50 hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET50
    # HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT                               hltElectron40CaloIdTTrkIdTCleanedPFHT300
    # HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT                               hltElectron60CaloIdTTrkIdTCleanedPFHT300
    # HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT                           hltElectron40CaloIdTTrkIdTCleanedPFHT300NoPU
    # HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT                           hltElectron60CaloIdTTrkIdTCleanedPFHT300NoPU

    process.goodPATElectrons = cms.EDFilter("PATElectronRefSelector",
        src = cms.InputTag("cleanPatElectronsTriggerMatch"),
        #cut = cms.string("electronID('simpleEleId80relIso') == 7 && p4().Pt() > 10 && abs(eta) < 2.5"),
        cut = cms.string("(isEB||isEE) && (abs(eta())<= 2.5) "
                         "&& (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1)"
                         "&& ( (isEB"
                         "      && (sigmaIetaIeta<0.01)"
                         "      && ( abs(deltaPhiSuperClusterTrackAtVtx)<0.06 )"
                         "      && ( abs(deltaEtaSuperClusterTrackAtVtx)<0.004 )"
                         "      && (hadronicOverEm<0.12)"
                         "      )"
                         "     || (isEE"
                         "         && (sigmaIetaIeta<0.03)"
                         "         && ( abs(deltaPhiSuperClusterTrackAtVtx)<0.03 )"
                         "         && ( abs(deltaEtaSuperClusterTrackAtVtx)<0.007 )"
                         "         && (hadronicOverEm<0.1) "
                         "         )"
                         "    )"
                         "&& passConversionVeto"),
    )
    
    process.goodPATElectronsNoIso = cms.EDFilter("PATElectronRefSelector",
        src = cms.InputTag("cleanPatElectronsTriggerMatch"),
        cut = cms.string("(electronID('simpleEleId80relIso') == 5 || electronID('simpleEleId80relIso') == 7) && p4().Pt() > 10 && abs(eta) < 2.5"),
    )
    
    MATCHED_Ele15_HT250_PFMHT25 = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_v*",0,0).empty() && !triggerObjectMatchesByFilter("hltEle15CaloIdTCaloIsoVLTrkIdTTrkIsoVLTrackIsoFilterEG5HTT75").empty())'
    MATCHED_Ele15_HT250_PFMHT40 = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_v*",0,0).empty() && !triggerObjectMatchesByFilter("hltEle15CaloIdTCaloIsoVLTrkIdTTrkIsoVLTrackIsoFilterEG5HTT75").empty())'


    #MATCHED_CleanPFHT350_Ele5_PFMET45      = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"     ,0,0).empty() && !triggerObjectMatchesByFilter("hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET45").empty())'
    #MATCHED_CleanPFHT350_Ele5_PFMET50      = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"     ,0,0).empty() && !triggerObjectMatchesByFilter("hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET50").empty())'
    #MATCHED_CleanPFNoPUHT350_Ele5_PFMET45  = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*" ,0,0).empty() && !triggerObjectMatchesByFilter("hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET45").empty())'
    #MATCHED_CleanPFNoPUHT350_Ele5_PFMET50  = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*" ,0,0).empty() && !triggerObjectMatchesByFilter("hltEle5CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET50").empty())'
    #MATCHED_CleanPFHT300_Ele15_PFMET45     = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"    ,0,0).empty() && !triggerObjectMatchesByFilter("hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET45").empty())'
    #MATCHED_CleanPFHT300_Ele15_PFMET50     = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"    ,0,0).empty() && !triggerObjectMatchesByFilter("hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350PFMET50").empty())'
    #MATCHED_CleanPFNoPUHT300_Ele15_PFMET45 = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",0,0).empty() && !triggerObjectMatchesByFilter("hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET45").empty())'
    #MATCHED_CleanPFNoPUHT300_Ele15_PFMET50 = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",0,0).empty() && !triggerObjectMatchesByFilter("hltElectron15CaloIdTCaloIsoVLTrkIdTTrkIsoVLCleanedPFHT350NoPUPFMET50").empty())'
    #MATCHED_CleanPFHT300_Ele40             = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*"                              ,0,0).empty() && !triggerObjectMatchesByFilter("hltElectron40CaloIdTTrkIdTCleanedPFHT300").empty())'
    #MATCHED_CleanPFHT300_Ele60             = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*"                              ,0,0).empty() && !triggerObjectMatchesByFilter("hltElectron60CaloIdTTrkIdTCleanedPFHT300").empty())'
    #MATCHED_CleanPFNoPUHT300_Ele40         = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*"                          ,0,0).empty() && !triggerObjectMatchesByFilter("hltElectron40CaloIdTTrkIdTCleanedPFHT300NoPU").empty())'
    #MATCHED_CleanPFNoPUHT300_Ele60         = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*"                          ,0,0).empty() && !triggerObjectMatchesByFilter("hltElectron60CaloIdTTrkIdTCleanedPFHT300NoPU").empty())'

    #MATCHED_CleanPFHT350_Ele5_PFMET45      = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"     ,0,1).empty())'
    #MATCHED_CleanPFHT350_Ele5_PFMET50      = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"     ,0,1).empty())'
    #MATCHED_CleanPFNoPUHT350_Ele5_PFMET45  = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*" ,0,1).empty())'
    #MATCHED_CleanPFNoPUHT350_Ele5_PFMET50  = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*" ,0,1).empty())'
    #MATCHED_CleanPFHT300_Ele15_PFMET45     = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"    ,0,1).empty())'
    #MATCHED_CleanPFHT300_Ele15_PFMET50     = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"    ,0,1).empty())'
    #MATCHED_CleanPFNoPUHT300_Ele15_PFMET45 = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",0,1).empty())'
    #MATCHED_CleanPFNoPUHT300_Ele15_PFMET50 = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",0,1).empty())'
    #MATCHED_CleanPFHT300_Ele40             = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*"                              ,0,1).empty())'
    #MATCHED_CleanPFHT300_Ele60             = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*"                              ,0,1).empty())'
    #MATCHED_CleanPFNoPUHT300_Ele40         = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*"                          ,0,1).empty())'
    #MATCHED_CleanPFNoPUHT300_Ele60         = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*"                          ,0,1).empty())'

    
    TRIGGER_OR =  '!triggerObjectMatchesByType("TriggerElectron").empty() && (!triggerObjectMatchesByPath("HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele32_WP70_PFMT50_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele25_WP80_PFMT40_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele52_CaloIdVT_TrkIdT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele65_CaloIdVT_TrkIdT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_CaloIdL_TrkIdVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_CaloIdL_CaloIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele45_CaloIdVT_TrkIdT_v*",1,0).empty() ||'
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*",1,0).empty() ||'
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele32_WP70_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_WP80_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_HT350_Ele30_CaloIdT_TrkIdT_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_HT400_Ele60_CaloIdT_TrkIdT_v*",1,0).empty() || '
    TRIGGER_OR += MATCHED_Ele15_HT250_PFMHT25 + ' || '
    TRIGGER_OR += MATCHED_Ele15_HT250_PFMHT40 + ' || '
    # 2012 SingleElectron Triggers
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele22_CaloIdL_CaloIsoVL_v*"                 ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_CaloIdL_CaloIsoVL_v*"                 ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_WP80_v*"                              ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_WP80_PFMET_MT50_v*"                   ,1,0).empty() || '
    #TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_WP80_CentralPFJet80_v*"               ,1,0).empty() || '
    #TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele27_WP80_WCandPt80_v*"                    ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele30_CaloIdVT_TrkIdT_v*"                   ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele65_CaloIdVT_TrkIdT_v*"                   ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele80_CaloIdVT_TrkIdT_v*"                   ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele100_CaloIdVT_TrkIdT_v*"                  ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele80_CaloIdVT_GsfTrkIdT_v*"                ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele90_CaloIdVT_GsfTrkIdT_v*"                ,0,1).empty() || '
    # 2012 EleHad Triggers
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v*"              ,1,0).empty() || '
    #TRIGGER_OR += MATCHED_CleanPFHT350_Ele5_PFMET45 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFHT350_Ele5_PFMET50 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFNoPUHT350_Ele5_PFMET45 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFNoPUHT350_Ele5_PFMET50 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFHT300_Ele15_PFMET45 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFHT300_Ele15_PFMET50 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFNoPUHT300_Ele15_PFMET45 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFNoPUHT300_Ele15_PFMET50 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFHT300_Ele40 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFHT300_Ele60 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFNoPUHT300_Ele40 + ' || '
    #TRIGGER_OR += MATCHED_CleanPFNoPUHT300_Ele60 + ' || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"     ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"     ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*" ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*" ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"    ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"    ,0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",0,1).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*"                              ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*"                              ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*"                          ,1,0).empty() || '
    TRIGGER_OR += '!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*"                          ,1,0).empty() '
    TRIGGER_OR += ')'

    #MATCHED_Ele27_WP80            = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_Ele27_WP80_v*"           ,0,0).empty() && !triggerObjectMatchesByFilter("hltEle27WP80TrackIsoFilter").empty())'
    #MATCHED_Ele30_CaloIdVT_TrkIdT = '(!triggerObjectMatchesByType("TriggerElectron").empty() && !triggerObjectMatchesByPath("HLT_Ele30_CaloIdVT_TrkIdT_v*",0,0).empty() && !triggerObjectMatchesByFilter("hltEle30CaloIdVTTrkIdTDphiFilter").empty())'
    #TRIGGER_OR  = MATCHED_Ele30_CaloIdVT_TrkIdT + ' || '
    #TRIGGER_OR += MATCHED_Ele27_WP80

    all_triggers = cms.PSet(
        # trigger present in summer2011
        HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.string('!triggerObjectMatchesByPath("HLT_Ele42_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"     ,1,0).empty()'),
        HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.string('!triggerObjectMatchesByPath("HLT_Ele42_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*"        ,1,0).empty()'),
        HLT_Ele32_WP70_PFMT50                              = cms.string('!triggerObjectMatchesByPath("HLT_Ele32_WP70_PFMT50_v*"                             ,1,0).empty()'),
        HLT_Ele27_WP70_PFMT40_PFMHT20                      = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_WP70_PFMT40_PFMHT20_v*"                     ,1,0).empty()'),
        HLT_Ele25_WP80_PFMT40                              = cms.string('!triggerObjectMatchesByPath("HLT_Ele25_WP80_PFMT40_v*"                             ,1,0).empty()'),
        HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.string('!triggerObjectMatchesByPath("HLT_Ele25_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"      ,1,0).empty()'),
        HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*"        ,1,0).empty()'),
        HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL      = cms.string('!triggerObjectMatchesByPath("HLT_Ele32_CaloIdVL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"     ,1,0).empty()'),
        HLT_Ele52_CaloIdVT_TrkIdT                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele52_CaloIdVT_TrkIdT_v*"                         ,1,0).empty()'),
        HLT_Ele65_CaloIdVT_TrkIdT                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele65_CaloIdVT_TrkIdT_v*"                         ,1,0).empty()'),
        HLT_Ele8                                           = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_v*"                                          ,1,0).empty()'),
        HLT_Ele8_CaloIdL_TrkIdVL                           = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_CaloIdL_TrkIdVL_v*"                          ,1,0).empty()'),
        HLT_Ele8_CaloIdL_CaloIsoVL_Jet40                   = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v*"                  ,1,0).empty()'),
        HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL        = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"       ,1,0).empty()'),
        HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL        = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*"       ,1,0).empty()'),
        HLT_Ele17_CaloIdL_CaloIsoVL                        = cms.string('!triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_v*"                       ,1,0).empty()'),
        HLT_Ele8_CaloIdL_CaloIsoVL                         = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_CaloIdL_CaloIsoVL_v*"                        ,1,0).empty()'),
        HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.string('!triggerObjectMatchesByPath("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*"        ,1,0).empty()'),
        HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL = cms.string('!triggerObjectMatchesByPath("HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*",1,0).empty()'),
        HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200 = cms.string('!triggerObjectMatchesByPath("HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v*",1,0).empty()'),
        HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.string('!triggerObjectMatchesByPath("HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*" ,1,0).empty()'),
        HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT         = cms.string('!triggerObjectMatchesByPath("HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*"        ,1,0).empty()'),
        HLT_Ele45_CaloIdVT_TrkIdT                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele45_CaloIdVT_TrkIdT_v*"                         ,1,0).empty()'),
        HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200  = cms.string('!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*" ,1,0).empty()'),
        HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250  = cms.string('!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*" ,1,0).empty()'),
        HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HTmix  = cms.string('!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v*" ,1,0).empty() || !triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_v*",1,0).empty()'),
        
        # new for winter
        HLT_Ele32_WP70                                     = cms.string('!triggerObjectMatchesByPath("HLT_Ele32_WP70_v*"                                    ,1,0).empty()'),
        HLT_Ele27_WP80                                     = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_WP80_v*"                                    ,1,0).empty()'),
        HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL        = cms.string('!triggerObjectMatchesByPath("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_v*"       ,1,0).empty()'),
        HT350_Ele30_CaloIdT_TrkIdT                         = cms.string('!triggerObjectMatchesByPath("HLT_HT350_Ele30_CaloIdT_TrkIdT_v*"                    ,1,0).empty()'),
        HT400_Ele60_CaloIdT_TrkIdT                         = cms.string('!triggerObjectMatchesByPath("HLT_HT400_Ele60_CaloIdT_TrkIdT_v*"                    ,1,0).empty()'),
        
        matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25 = cms.string(MATCHED_Ele15_HT250_PFMHT25),
        matchedHLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40 = cms.string(MATCHED_Ele15_HT250_PFMHT40),
        
        # 2012 SingleElectron Triggers
        HLT_Ele22_CaloIdL_CaloIsoVL                        = cms.string('!triggerObjectMatchesByPath("HLT_Ele22_CaloIdL_CaloIsoVL_v*"                       ,1,0).empty()'),
        HLT_Ele27_CaloIdL_CaloIsoVL                        = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_CaloIdL_CaloIsoVL_v*"                       ,1,0).empty()'),
        HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"      ,1,0).empty()'),
        #HLT_Ele27_WP80                                     = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_WP80_v*"                                    ,1,0).empty()'),
        HLT_Ele27_WP80_PFMET_MT50                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_WP80_PFMET_MT50_v*"                         ,1,0).empty()'),
        #HLT_Ele27_WP80_CentralPFJet80                      = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_WP80_CentralPFJet80_v*"                     ,1,0).empty( ),'
        #HLT_Ele27_WP80_WCandPt80                           = cms.string('!triggerObjectMatchesByPath("HLT_Ele27_WP80_WCandPt80_v*"                          ,1,0).empty( ),'
        HLT_Ele30_CaloIdVT_TrkIdT                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele30_CaloIdVT_TrkIdT_v*"                         ,1,0).empty()'),
        HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL       = cms.string('!triggerObjectMatchesByPath("HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"      ,1,0).empty()'),
        #HLT_Ele65_CaloIdVT_TrkIdT                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele65_CaloIdVT_TrkIdT_v*"                         ,1,0).empty()'),
        HLT_Ele80_CaloIdVT_TrkIdT                          = cms.string('!triggerObjectMatchesByPath("HLT_Ele80_CaloIdVT_TrkIdT_v*"                         ,1,0).empty()'),
        HLT_Ele100_CaloIdVT_TrkIdT                         = cms.string('!triggerObjectMatchesByPath("HLT_Ele100_CaloIdVT_TrkIdT_v*"                        ,1,0).empty()'),
        HLT_Ele80_CaloIdVT_GsfTrkIdT                       = cms.string('!triggerObjectMatchesByPath("HLT_Ele80_CaloIdVT_GsfTrkIdT_v*"                      ,0,1).empty()'),
        HLT_Ele90_CaloIdVT_GsfTrkIdT                       = cms.string('!triggerObjectMatchesByPath("HLT_Ele90_CaloIdVT_GsfTrkIdT_v*"                      ,0,1).empty()'),
        # 2012 EleHad Triggers                                                                                                                              
        HLT_Ele8_CaloIdT_TrkIdVL_Jet30                     = cms.string('!triggerObjectMatchesByPath("HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v*"                    ,1,0).empty()'),
        
        ############################################################
        #   DO NOT USE LONG VARIABLE NAMES - THERE'S A BUG ! ! !   #
        ############################################################
        #matchedHLT_CleanPFHT350_Ele5_PFMET45      = cms.string(MATCHED_CleanPFHT350_Ele5_PFMET45),
        #matchedHLT_CleanPFHT350_Ele5_PFMET50      = cms.string(MATCHED_CleanPFHT350_Ele5_PFMET50),
        #matchedHLT_CleanPFNoPUHT350_Ele5_PFMET45  = cms.string(MATCHED_CleanPFNoPUHT350_Ele5_PFMET45),
        #matchedHLT_CleanPFNoPUHT350_Ele5_PFMET50  = cms.string(MATCHED_CleanPFNoPUHT350_Ele5_PFMET50),
        #matchedHLT_CleanPFHT300_Ele15_PFMET45     = cms.string(MATCHED_CleanPFHT300_Ele15_PFMET45),
        #matchedHLT_CleanPFHT300_Ele15_PFMET50     = cms.string(MATCHED_CleanPFHT300_Ele15_PFMET50),
        #matchedHLT_CleanPFNoPUHT300_Ele15_PFMET45 = cms.string(MATCHED_CleanPFNoPUHT300_Ele15_PFMET45),
        #matchedHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.string(MATCHED_CleanPFNoPUHT300_Ele15_PFMET50),
        #matchedHLT_CleanPFHT300_Ele40             = cms.string(MATCHED_CleanPFHT300_Ele40),
        #matchedHLT_CleanPFHT300_Ele60             = cms.string(MATCHED_CleanPFHT300_Ele60),
        #matchedHLT_CleanPFNoPUHT300_Ele40         = cms.string(MATCHED_CleanPFNoPUHT300_Ele40),
        #matchedHLT_CleanPFNoPUHT300_Ele60         = cms.string(MATCHED_CleanPFNoPUHT300_Ele60),

        HLT_CleanPFHT350_Ele5_PFMET45                      = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"     ,0,1).empty()'),
        HLT_CleanPFHT350_Ele5_PFMET50                      = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"     ,0,1).empty()'),
        HLT_CleanPFNoPUHT350_Ele5_PFMET45                  = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*" ,0,1).empty()'),
        HLT_CleanPFNoPUHT350_Ele5_PFMET50                  = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*" ,0,1).empty()'),
        HLT_CleanPFHT300_Ele15_PFMET45                     = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"    ,0,1).empty()'),
        HLT_CleanPFHT300_Ele15_PFMET50                     = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"    ,0,1).empty()'),
        HLT_CleanPFNoPUHT300_Ele15_PFMET45                 = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",0,1).empty()'),
        HLT_CleanPFNoPUHT300_Ele15_PFMET50                 = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",0,1).empty()'),
        HLT_CleanPFHT300_Ele40                             = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*"                              ,0,1).empty()'),
        HLT_CleanPFHT300_Ele60                             = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*"                              ,0,1).empty()'),
        HLT_CleanPFNoPUHT300_Ele40                         = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*"                          ,0,1).empty()'),
        HLT_CleanPFNoPUHT300_Ele60                         = cms.string('!triggerObjectMatchesByPath("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*"                          ,0,1).empty()'),
    )

    process.tagPATElectrons = cms.EDFilter("PATElectronRefSelector",
        src = cms.InputTag("cleanPatElectronsTriggerMatch"),
        cut = cms.string( "electronID('simpleEleId80cIso') == 7 && p4().Pt() > 10 && abs(eta) < 2.5")
        #cut = cms.string( "electronID('simpleEleId80cIso') == 7 && p4().Pt() > 10 && abs(eta) < 2.5 && (" + PASS_HLT_Ele30_CaloIdVT_TrkIdT + ")")
    )

    process.GSFPassingGoodPat = cms.EDProducer("MatchGsfElectronsToPAT",
        electrons   = cms.InputTag("goodElectrons"),
        pat = cms.InputTag("goodPATElectrons"),
        patCut = cms.string("pt>0"),
        matchByReference = cms.bool(False)
    )

    process.GsfPassingCleanPat = cms.EDProducer("MatchGsfElectronsToPAT",
        electrons   = cms.InputTag(ELECTRON_COLL),
        pat = cms.InputTag("cleanPatElectronsTriggerMatch"),
        patCut = cms.string("pt>0"),
        matchByReference = cms.bool(False)
    )

    process.GSFPassingGoodPatNoIso = cms.EDProducer("MatchGsfElectronsToPAT",
        electrons   = cms.InputTag("goodElectrons"),
        pat = cms.InputTag("goodPATElectronsNoIso"),
        patCut = cms.string("pt>0"),
        matchByReference = cms.bool(False)
    )

# Cuts in ELECTRON_CUTS
# (isEB()||isEE()) && abs(superCluster.eta) <= 2.5 
#
# Cuts in ELectron Id Cuts
# gsfTrack().trackerExpectedHitsInner.numberOfHits <= 1
# hadronicOverEm() < 0.12 (EB)  < 0.10 (EE)
# abs(deltaPhiSuperClusterTrackAtVtx()) < 0.06 (EB) < 0.03 (EE)
# abs(deltaEtaSuperClusterTrackAtVtx()) < 0.004 (EB) < 0.007 (EE)
# scSigmaIEtaIEta() <0.01 (EB) <0.03 (EE)

# Cuts done while plotting
# abs(gsfTrack().dxy(vertexPosition)) < 0.02
# abs(gsfTrack().dz(vertexPosition)) < 0.1
# pt>= 20 GeV
#

# //Calculate Aeff corrected isolation values - Do in C++
# Aeff = ElectronEffectiveArea::GetElectronEffectiveArea(ElectronEffectiveArea::kEleGammaAndNeutralHadronIso03, fabs(ele->superCluster()->eta()) , ElectronEffectiveArea::kEleEAFall11MC)
# ev.getByLabel("elPFIsoValueCharged03PFIdPFIso", electronIsoValPFId[0]);
# ev.getByLabel("elPFIsoValueGamma03PFIdPFIso", electronIsoValPFId[1]);
# ev.getByLabel("elPFIsoValueNeutral03PFIdPFIso", electronIsoValPFId[2]);
# //In the event loop do
# edm::Ptr< reco::GsfElectron > gsfel = (edm::Ptr< reco::GsfElectron >) ele->originalObjectRef();
# double charged =  (*(*electronIsoVals)[0])[gsfel];
# double photon = (*(*electronIsoVals)[1])[gsfel];
# double neutral = (*(*electronIsoVals)[2])[gsfel];
#
# charged + max (0., photon + neutral - (*eleRho)*Aeff) < 0.15

# !ConversionTools::hasMatchedConversion(*gsfel,hConversions,beamSpotPosition) 
#   Use the gsfel obtained with originalObjectRef; don't use the pat::Electron

# abs(reco - PF) PT < 10 GeV
    
    ##    _____ _           _                     ___    _ 
    ##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
    ##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
    ##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
    ##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
    ##   
    # Electron ID  ######
    process.PassingRA4 = process.goodElectrons.clone()
    process.PassingRA4.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1)"
        #" && passConversionVeto"
        " && ((isEB"
        " && (sigmaIetaIeta<0.01)"
        " && ( abs(deltaPhiSuperClusterTrackAtVtx)<0.06 )"
        " && ( abs(deltaEtaSuperClusterTrackAtVtx)<0.004 )"
        " && (hadronicOverEm<0.12)"
        ")"
        " || (isEE"
        " && (sigmaIetaIeta<0.03)"
        " && ( abs(deltaPhiSuperClusterTrackAtVtx)<0.03 )"
        " && ( abs(deltaEtaSuperClusterTrackAtVtx)<0.007 )"
        " && (hadronicOverEm<0.1) "
        "))"
        )
    
    process.PassingWP95 = process.goodElectrons.clone()
    process.PassingWP95.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1)"
        " && ((isEB"
        " && ( dr03TkSumPt/p4.Pt < 0.15 && dr03EcalRecHitSumEt/p4.Pt < 2.0 && dr03HcalTowerSumEt/p4.Pt < 0.12 )" 
        " && (sigmaIetaIeta<0.01)"
        " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )"
        " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
        " && (hadronicOverEm<0.15)"
        ")"
        " || (isEE"
        " && (dr03TkSumPt/p4.Pt < 0.08 && dr03EcalRecHitSumEt/p4.Pt < 0.06  && dr03HcalTowerSumEt/p4.Pt < 0.05 )"  
        " && (sigmaIetaIeta<0.03)"
        " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )"
        " && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )"
        " && (hadronicOverEm<0.07) "
        "))"
        )
    process.PassingWP90 = process.goodElectrons.clone()
    process.PassingWP90.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))"
        " && ((isEB"
        " && ( dr03TkSumPt/p4.Pt <0.12 && dr03EcalRecHitSumEt/p4.Pt < 0.09 && dr03HcalTowerSumEt/p4.Pt  < 0.1 )"
        " && (sigmaIetaIeta<0.01)"
        " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )"
        " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
        " && (hadronicOverEm<0.12)"
        ")"
        " || (isEE"
        " && ( dr03TkSumPt/p4.Pt <0.05 && dr03EcalRecHitSumEt/p4.Pt < 0.06 && dr03HcalTowerSumEt/p4.Pt  < 0.03 )"
        " && (sigmaIetaIeta<0.03)"
        " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )"
        " && ( -0.009<deltaEtaSuperClusterTrackAtVtx<0.009 )"
        " && (hadronicOverEm<0.05) "
        "))"
        ) 
    process.PassingWP85 = process.goodElectrons.clone()
    process.PassingWP85.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))"
        " && ((isEB"
        " && ( dr03TkSumPt/p4.Pt <0.09 && dr03EcalRecHitSumEt/p4.Pt < 0.08 && dr03HcalTowerSumEt/p4.Pt  < 0.1 )"
        " && (sigmaIetaIeta<0.01)"
        " && ( -0.6<deltaPhiSuperClusterTrackAtVtx<0.6 )"
        " && ( -0.006<deltaEtaSuperClusterTrackAtVtx<0.006 )"
        " && (hadronicOverEm<0.04)"
        ")"
        " || (isEE"
        " && ( dr03TkSumPt/p4.Pt <0.05 && dr03EcalRecHitSumEt/p4.Pt < 0.05 && dr03HcalTowerSumEt/p4.Pt  < 0.025 )"
        " && (sigmaIetaIeta<0.03)"
        " && ( -0.04<deltaPhiSuperClusterTrackAtVtx<0.04 )"
        " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
        " && (hadronicOverEm<0.025) "
        "))"
        ) 
    process.PassingWP80 = process.goodElectrons.clone()
    process.PassingWP80.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))"
        " && ((isEB"
        " && ( dr03TkSumPt/p4.Pt <0.09 && dr03EcalRecHitSumEt/p4.Pt < 0.07 && dr03HcalTowerSumEt/p4.Pt  < 0.1 )"
        " && (sigmaIetaIeta<0.01)"
        " && ( -0.06<deltaPhiSuperClusterTrackAtVtx<0.06 )"
        " && ( -0.004<deltaEtaSuperClusterTrackAtVtx<0.004 )"
        " && (hadronicOverEm<0.04)"
        ")"
        " || (isEE"
        " && ( dr03TkSumPt/p4.Pt <0.04 && dr03EcalRecHitSumEt/p4.Pt < 0.05 && dr03HcalTowerSumEt/p4.Pt  < 0.025 )"
        " && (sigmaIetaIeta<0.03)"
        " && ( -0.03<deltaPhiSuperClusterTrackAtVtx<0.03 )"
        " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
        " && (hadronicOverEm<0.025) "
        "))"
        )     
    
    process.PassingWP70 = process.goodElectrons.clone()
    process.PassingWP70.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))"
        " && ((isEB"
        " && ( dr03TkSumPt/p4.Pt <0.05 && dr03EcalRecHitSumEt/p4.Pt < 0.06 && dr03HcalTowerSumEt/p4.Pt  < 0.03 )"
        " && (sigmaIetaIeta<0.01)"
        " && ( -0.03<deltaPhiSuperClusterTrackAtVtx<0.03 )"
        " && ( -0.004<deltaEtaSuperClusterTrackAtVtx<0.004 )"
        " && (hadronicOverEm<0.025)"
        ")"
        " || (isEE"
        " && ( dr03TkSumPt/p4.Pt <0.025 && dr03EcalRecHitSumEt/p4.Pt < 0.025 && dr03HcalTowerSumEt/p4.Pt  < 0.02 )"
        " && (sigmaIetaIeta<0.03)"
        " && ( -0.02<deltaPhiSuperClusterTrackAtVtx<0.02 )"
        " && ( -0.005<deltaEtaSuperClusterTrackAtVtx<0.005 )"
        " && (hadronicOverEm<0.025) "
        "))"
        ) 
    process.PassingWP60 = process.goodElectrons.clone()
    process.PassingWP60.cut = cms.string(
        process.goodElectrons.cut.value() +
        " && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02))"
        " && ((isEB"
        " && ( dr03TkSumPt/p4.Pt <0.04 && dr03EcalRecHitSumEt/p4.Pt < 0.04 && dr03HcalTowerSumEt/p4.Pt  < 0.03 )"
        " && (sigmaIetaIeta<0.01)"
        " && ( -0.025<deltaPhiSuperClusterTrackAtVtx<0.025 )"
        " && ( -0.004<deltaEtaSuperClusterTrackAtVtx<0.004 )"
        " && (hadronicOverEm<0.025)"
        ")"
        " || (isEE"
        " && ( dr03TkSumPt/p4.Pt <0.025 && dr03EcalRecHitSumEt/p4.Pt < 0.02 && dr03HcalTowerSumEt/p4.Pt  < 0.02 )"
        " && (sigmaIetaIeta<0.03)"
        " && ( -0.02<deltaPhiSuperClusterTrackAtVtx<0.02 )"
        " && ( -0.005<deltaEtaSuperClusterTrackAtVtx<0.005 )"
        " && (hadronicOverEm<0.025) "
        "))"
        ) 
        
                                 
    
    
    ##    _____      _                        _  __     __             
    ##   | ____|_  _| |_ ___ _ __ _ __   __ _| | \ \   / /_ _ _ __ ___ 
    ##   |  _| \ \/ / __/ _ \ '__| '_ \ / _` | |  \ \ / / _` | '__/ __|
    ##   | |___ >  <| ||  __/ |  | | | | (_| | |   \ V / (_| | |  \__ \
    ##   |_____/_/\_\\__\___|_|  |_| |_|\__,_|_|    \_/ \__,_|_|  |___/
    ##   
    ## Here we show how to use a module to compute an external variable
    ## process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
    ## ak5PFResidual.useCondDB = False
    
    process.superClusterDRToNearestJet = cms.EDProducer("DeltaRNearestJetComputer",
        probes = cms.InputTag("goodSuperClusters"),
           # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
           #       this must be the full collection, not the subset by refs.
        objects = cms.InputTag(JET_COLL),
        objectSelection = cms.string(JET_CUTS + " && pt > 20.0"),
    )
    process.JetMultiplicityInSCEvents = cms.EDProducer("CandMultiplicityCounter",
        probes = cms.InputTag("goodSuperClusters"),
        objects = cms.InputTag(JET_COLL),
        objectSelection = cms.string(JET_CUTS + " && pt > 20.0"),
    )
    process.SCConvRejVars = cms.EDProducer("ElectronConversionRejectionVars",
        probes = cms.InputTag("goodSuperClusters")
    )
    process.GsfConvRejVars = process.SCConvRejVars.clone()
    process.GsfConvRejVars.probes = cms.InputTag( ELECTRON_COLL )
   
    process.GsfDRToNearestJet = process.superClusterDRToNearestJet.clone()
    process.GsfDRToNearestJet.probes = cms.InputTag( ELECTRON_COLL )
    process.JetMultiplicityInGsfEvents = process.JetMultiplicityInSCEvents.clone()
    process.JetMultiplicityInGsfEvents.probes = cms.InputTag( ELECTRON_COLL )
    
    process.ext_ToNearestJet_sequence = cms.Sequence(
        #process.ak5PFResidual + 
        process.superClusterDRToNearestJet +
        process.JetMultiplicityInSCEvents +
        process.SCConvRejVars +
        process.GsfDRToNearestJet +
        process.JetMultiplicityInGsfEvents +
        process.GsfConvRejVars
    )
    
    # Rho Corrected Relative Isolation
    process.GSFRelIso = cms.EDProducer("GsfElectronRelIsoProducer",
        ElectronProbes  = cms.InputTag( ELECTRON_COLL ),
        rhoIsoInputTag  = cms.InputTag("kt6PFJetsForIsolation2011", "rho"),
        isoValInputTags = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
                                        cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
                                        cms.InputTag('elPFIsoValueNeutral03PFIdPFIso')),
        isMC            = cms.bool(MC_flag),
    )

    process.PATRelIso = cms.EDProducer("PatElectronRelIsoProducer",
        ElectronProbes  = cms.InputTag("cleanPatElectronsTriggerMatch"),
        rhoIsoInputTag  = cms.InputTag("kt6PFJetsForIsolation2011", "rho"),
        isoValInputTags = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
                                        cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
                                        cms.InputTag('elPFIsoValueNeutral03PFIdPFIso')),
        isMC            = cms.bool(MC_flag),
    )

    # Delta Pt
    
    process.GsfEledeltaPfRecoPt = cms.EDProducer("GsfElectronDeltaPfRecoPt",
        probes = cms.InputTag( ELECTRON_COLL ),
    )
    
    process.deltaPfRecoPt = cms.EDProducer("ElectronDeltaPfRecoPt",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
    )
    

    ##    _____             ____        __ _       _ _   _             
    ##   |_   _|_ _  __ _  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  
    ##     | |/ _` |/ _` | | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \ 
    ##     | | (_| | (_| | | |_| |  __/  _| | | | | | |_| | (_) | | | |
    ##     |_|\__,_|\__, | |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|
    ##              |___/
    ## 
    process.RA4MatchedSuperClusterCandsClean = cms.EDProducer("ElectronMatchedCandidateProducer",
       src     = cms.InputTag("goodSuperClustersClean"),
       ReferenceElectronCollection = cms.untracked.InputTag("PassingRA4"),
       deltaR =  cms.untracked.double(0.3)
    )
    process.WP95MatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.WP95MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWP95")
    process.WP90MatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.WP90MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWP90")
    process.WP85MatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.WP85MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWP85")
    process.WP80MatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.WP80MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWP80")
    process.WP70MatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.WP70MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWP70")
    process.WP60MatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.WP60MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingWP60")    
    process.GSFtoPATMatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.GSFtoPATMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("GSFPassingGoodPat")    
    process.GSFtoPATNoIsoMatchedSuperClusterCandsClean = process.RA4MatchedSuperClusterCandsClean.clone()
    process.GSFtoPATNoIsoMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("GSFPassingGoodPatNoIso")    
    
    process.ele_sequence = cms.Sequence(
        process.goodElectrons +
        process.goodPATElectrons *
        process.goodPATElectronsNoIso *
        (process.GSFPassingGoodPat +
         process.GsfPassingCleanPat +
         process.GSFPassingGoodPatNoIso) +
        process.tagPATElectrons +
        process.GsfMatchedSuperClusterCands +
        process.PassingRA4 +
        process.PassingWP95 +
        process.PassingWP90 +
        process.PassingWP85 +
        process.PassingWP80 +
        process.PassingWP70 +
        process.PassingWP60 +
        process.RA4MatchedSuperClusterCandsClean +
        process.WP95MatchedSuperClusterCandsClean +
        process.WP90MatchedSuperClusterCandsClean +
        process.WP85MatchedSuperClusterCandsClean +
        process.WP80MatchedSuperClusterCandsClean +
        process.WP70MatchedSuperClusterCandsClean +
        process.WP60MatchedSuperClusterCandsClean +
        process.GSFtoPATMatchedSuperClusterCandsClean +
        process.GSFtoPATNoIsoMatchedSuperClusterCandsClean
    )
    
    
    ##    _____ ___   ____    ____       _          
    ##   |_   _( _ ) |  _ \  |  _ \ __ _(_)_ __ ___ 
    ##     | | / _ \/\ |_) | | |_) / _` | | '__/ __|
    ##     | || (_>  <  __/  |  __/ (_| | | |  \__ \
    ##     |_| \___/\/_|     |_|   \__,_|_|_|  |___/
    ##                                              
    ##   
    #  Tag & probe selection ######
    process.tagPATSC = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("tagPATElectrons@+ goodSuperClustersClean@-"),
        checkCharge = cms.bool(False),                           
        cut   = cms.string("40 < mass < 1000"),
    )
    process.tagPATGsf = process.tagPATSC.clone()
    process.tagPATGsf.decay = cms.string("tagPATElectrons@+ goodElectrons@-")
    process.tagPATGoodPATElectron = process.tagPATSC.clone()
    process.tagPATGoodPATElectron.decay = cms.string("tagPATElectrons@+ goodPATElectrons@-")

    process.allTagsAndProbes = cms.Sequence(
        process.tagPATSC +
        process.tagPATGsf +
        process.tagPATGoodPATElectron
    )
 
    #JET_CUT =  "pt() >= 40.0 && abs(eta()) <= 2.4 && neutralHadronEnergyFraction() < 0.99 && neutralEmEnergyFraction() < 0.99 && getPFConstituents().size() > 1 && chargedHadronEnergyFraction() > 0  && chargedMultiplicity() > 0  && chargedEmEnergyFraction() < 0.99"
    JET_CUT =  "pt() >= 40.0 && abs(eta()) <= 2.4 && neutralHadronEnergyFraction() < 0.99 && neutralEmEnergyFraction() < 0.99 && chargedHadronEnergyFraction() > 0  && chargedMultiplicity() > 0  && chargedEmEnergyFraction() < 0.99 && (chargedMultiplicity() + neutralMultiplicity() + muonMultiplicity()) > 1"
    
    process.selectedJets = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("cleanPatJetsAK5PF"),
        cut = cms.string( JET_CUT ), # <= anpassen
    )

    process.GSFdRToNearestPATJet = cms.EDProducer("minCutDeltaRNearestPatJetComputer",
        probes = cms.InputTag(ELECTRON_COLL),
        objects = cms.InputTag("selectedJets"),
        minDeltaR = cms.double(0.3),
        objectSelection = cms.InputTag(""),
    )
    process.GSFJetMultiplicity = cms.EDProducer("PatJetMultiplicityCounter",
        probes = cms.InputTag(ELECTRON_COLL),
        objects = cms.InputTag("selectedJets"),
        minDeltaR = cms.double(0.3),
        objectSelection = cms.InputTag(""),
    )

    process.PATdRToNearestPATJet = process.GSFdRToNearestPATJet.clone(
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
    )
    process.PATJetMultiplicity = process.GSFJetMultiplicity.clone(
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
    )
    

    process.nverticesModule = cms.EDProducer("VertexMultiplicityCounter", 
        probes = cms.InputTag(ELECTRON_COLL),
        objects = cms.InputTag("offlinePrimaryVertices"),
        #objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
        objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
    )
    process.nverticesModulePAT = process.nverticesModule.clone(
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
    )
 
    process.GSFImpactParameter = cms.EDProducer("GsfElectronImpactParameter",
        probes = cms.InputTag(ELECTRON_COLL),
    )
     
    process.PATImpactParameter = cms.EDProducer("PatElectronImpactParameter",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
    )
    
#   T R I G G E R   P A S S E S
    process.flagPassHLTEle15HT250PFMHT25 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT25_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTEle15HT250PFMHT40 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT250_PFMHT40_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFHT350PFMET45         = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFHT350PFMET50         = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFNoPUHT350PFMET45     = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFNoPUHT350PFMET50     = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFHT300Ele15PFMET45    = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFHT300Ele15PFMET50    = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFNoPUHT300Ele15PFMET45= cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFNoPUHT300Ele15PFMET50= cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFHT300Ele40           = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFHT300Ele60           = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFNoPUHT300Ele40       = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v.*"),
        andOr = cms.bool(True)
    )
    
    process.flagPassHLTCleanPFNoPUHT300Ele60       = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v.*"),
        andOr = cms.bool(True)
    )

    #   M E T
    process.glbMet = cms.EDProducer("PatMetAssociator",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        metTag = cms.InputTag("patMETsPF"),
    )
    process.glbMetGsf = cms.EDProducer("PatMetAssociator",
        probes = cms.InputTag(ELECTRON_COLL),
        metTag = cms.InputTag("patMETsPF"),
    )


    #   S T
    process.stComp = cms.EDProducer("PatMetSTComputer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        metTag = cms.InputTag("patMETsPF"),
    )
    process.stCompGsf = cms.EDProducer("PatMetSTComputer",
        probes = cms.InputTag(ELECTRON_COLL),
        metTag = cms.InputTag("patMETsPF"),
    )

    #   H T
    process.glbHT = cms.EDProducer("PatJetHTComputer",
        probes = cms.InputTag("cleanPatElectronsTriggerMatch"),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )
    process.glbHTGsf = cms.EDProducer("PatJetHTComputer",
        probes = cms.InputTag(ELECTRON_COLL),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )


    process.allHLTResults = cms.Sequence(
        process.flagPassHLTEle15HT250PFMHT25 +
        process.flagPassHLTEle15HT250PFMHT40 +
        process.flagPassHLTCleanPFHT350PFMET45 +
        process.flagPassHLTCleanPFHT350PFMET50 +
        process.flagPassHLTCleanPFNoPUHT350PFMET45 +
        process.flagPassHLTCleanPFNoPUHT350PFMET50 +
        process.flagPassHLTCleanPFHT300Ele15PFMET45 +
        process.flagPassHLTCleanPFHT300Ele15PFMET50 +
        process.flagPassHLTCleanPFNoPUHT300Ele15PFMET45 +
        process.flagPassHLTCleanPFNoPUHT300Ele15PFMET50 +
        process.flagPassHLTCleanPFHT300Ele40 +
        process.flagPassHLTCleanPFHT300Ele60 +
        process.flagPassHLTCleanPFNoPUHT300Ele40 +
        process.flagPassHLTCleanPFNoPUHT300Ele60
    )

    process.allMet = cms.Sequence(
        process.glbMet +
        process.glbMetGsf
    )

    process.allST = cms.Sequence(
        process.stComp +
        process.stCompGsf
    )

    process.allJets = cms.Sequence(
        process.selectedJets*
        (process.GSFdRToNearestPATJet +
        process.PATdRToNearestPATJet +
        process.GSFJetMultiplicity +
        process.PATJetMultiplicity +
        process.glbHT +
        process.glbHTGsf)
    )

    process.allVertex = cms.Sequence(
        process.nverticesModule +
        process.nverticesModulePAT
    )

    process.allImpactParameters = cms.Sequence(
        process.GSFImpactParameter +
        process.PATImpactParameter
    )

    process.allRelIso = cms.Sequence(
        process.GSFRelIso +
        process.PATRelIso
    )

    SUSY_InfoGSF = cms.PSet(
        drjet = cms.InputTag("GSFdRToNearestPATJet"),
        njet = cms.InputTag("GSFJetMultiplicity"),
        d0_v = cms.InputTag("GSFImpactParameter","d0v"),
        d0_b = cms.InputTag("GSFImpactParameter","d0b"),
        dz_v = cms.InputTag("GSFImpactParameter","dzv"),
        dz_b = cms.InputTag("GSFImpactParameter","dzb"),
        nVertices = cms.InputTag("nverticesModule"),
        reliso = cms.InputTag("GSFRelIso","reliso"),
        absdeltapt = cms.InputTag("GsfEledeltaPfRecoPt","absdeltapt"),
    )
    
    SUSY_InfoPAT = cms.PSet(
        drjet = cms.InputTag("PATdRToNearestPATJet"),
        njet = cms.InputTag("PATJetMultiplicity"),
        d0_v = cms.InputTag("PATImpactParameter","d0v"),
        d0_b = cms.InputTag("PATImpactParameter","d0b"),
        dz_v = cms.InputTag("PATImpactParameter","dzv"),
        dz_b = cms.InputTag("PATImpactParameter","dzb"),
        nVertices = cms.InputTag("nverticesModulePAT"),
        reliso = cms.InputTag("PATRelIso","reliso"),
        absdeltapt = cms.InputTag("deltaPfRecoPt","absdeltapt"),
     )
    
    ##    __  __  ____   __  __       _       _               
    ##   |  \/  |/ ___| |  \/  | __ _| |_ ___| |__   ___  ___ 
    ##   | |\/| | |     | |\/| |/ _` | __/ __| '_ \ / _ \/ __|
    ##   | |  | | |___  | |  | | (_| | || (__| | | |  __/\__ \
    ##   |_|  |_|\____| |_|  |_|\__,_|\__\___|_| |_|\___||___/
    ##                                                        
    process.McMatchSC = cms.EDProducer("MCTruthDeltaRMatcherNew",
        matchPDGId = cms.vint32(11),
        src = cms.InputTag("goodSuperClustersClean"),
        distMin = cms.double(0.3),
        matched = cms.InputTag("genParticles")
    )
    process.McMatchGsf = process.McMatchSC.clone()
    process.McMatchGsf.src = cms.InputTag("goodElectrons")
    process.McMatchGSF = process.McMatchSC.clone()
    process.McMatchGSF.src = cms.InputTag(ELECTRON_COLL)
    process.McMatchPATElectron = process.McMatchSC.clone()
    process.McMatchPATElectron.src = cms.InputTag("goodPATElectrons")
    process.McMatchTagPATElectron = process.McMatchSC.clone()
    process.McMatchTagPATElectron.src = cms.InputTag("tagPATElectrons")
    process.McMatchRA4 = process.McMatchSC.clone()
    process.McMatchRA4.src = cms.InputTag("PassingRA4")
    process.McMatchWP95 = process.McMatchSC.clone()
    process.McMatchWP95.src = cms.InputTag("PassingWP95")
    process.McMatchWP90 = process.McMatchSC.clone()
    process.McMatchWP90.src = cms.InputTag("PassingWP90")
    process.McMatchWP85 = process.McMatchSC.clone()
    process.McMatchWP85.src = cms.InputTag("PassingWP85")
    process.McMatchWP80 = process.McMatchSC.clone()
    process.McMatchWP80.src = cms.InputTag("PassingWP80")
    process.McMatchWP70 = process.McMatchSC.clone()
    process.McMatchWP70.src = cms.InputTag("PassingWP70")
    process.McMatchWP60 = process.McMatchSC.clone()
    process.McMatchWP60.src = cms.InputTag("PassingWP60")
        
    process.mc_sequence = cms.Sequence(
       process.McMatchSC +
       process.McMatchGSF +
       process.McMatchGsf +    process.McMatchPATElectron + process.McMatchTagPATElectron +
       process.McMatchRA4 +
       process.McMatchWP95 +
       process.McMatchWP90 +
       process.McMatchWP85 +
       process.McMatchWP80 +
       process.McMatchWP70 +   
       process.McMatchWP60 
    )
    
    ############################################################################
    ##    _____           _       _ ____            _            _   _  ____  ##
    ##   |_   _|_ _  __ _( )_ __ ( )  _ \ _ __ ___ | |__   ___  | \ | |/ ___| ##
    ##     | |/ _` |/ _` |/| '_ \|/| |_) | '__/ _ \| '_ \ / _ \ |  \| | |  _  ##
    ##     | | (_| | (_| | | | | | |  __/| | | (_) | |_) |  __/ | |\  | |_| | ##
    ##     |_|\__,_|\__, | |_| |_| |_|   |_|  \___/|_.__/ \___| |_| \_|\____| ##
    ##              |___/                                                     ##
    ##                                                                        ##
    ############################################################################
    ##    ____                      _     _           
    ##   |  _ \ ___ _   _ ___  __ _| |__ | | ___  ___ 
    ##   | |_) / _ \ | | / __|/ _` | '_ \| |/ _ \/ __|
    ##   |  _ <  __/ |_| \__ \ (_| | |_) | |  __/\__ \
    ##   |_| \_\___|\__,_|___/\__,_|_.__/|_|\___||___/
    ##
    ## I define some common variables for re-use later.
    ## This will save us repeating the same code for each efficiency category
    ZVariablesToStore = cms.PSet(
        eta = cms.string("eta"),
        pt  = cms.string("pt"),
        phi  = cms.string("phi"),
        et  = cms.string("et"),
        e  = cms.string("energy"),
        p  = cms.string("p"),
        px  = cms.string("px"),
        py  = cms.string("py"),
        pz  = cms.string("pz"),
        theta  = cms.string("theta"),    
        vx     = cms.string("vx"),
        vy     = cms.string("vy"),
        vz     = cms.string("vz"),
        rapidity  = cms.string("rapidity"),
        mass  = cms.string("mass"),
        mt  = cms.string("mt"),    
    )   
    
    ProbeVariablesToStore = cms.PSet(
        probe_gsfEle_eta = cms.string("eta"),
        probe_gsfEle_abseta = cms.string("abs(eta)"),
        probe_gsfEle_pt  = cms.string("pt"),
        probe_gsfEle_phi  = cms.string("phi"),
        probe_gsfEle_et  = cms.string("et"),
        probe_gsfEle_e  = cms.string("energy"),
        probe_gsfEle_p  = cms.string("p"),
        probe_gsfEle_px  = cms.string("px"),
        probe_gsfEle_py  = cms.string("py"),
        probe_gsfEle_pz  = cms.string("pz"),
        probe_gsfEle_theta  = cms.string("theta"),    
        probe_gsfEle_charge = cms.string("charge"),
        probe_gsfEle_rapidity  = cms.string("rapidity"),
        probe_gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
        probe_gsfEle_convDist = cms.string("convDist"),
        probe_gsfEle_convDcot = cms.string("convDcot"),
        probe_gsfEle_convRadius = cms.string("convRadius"),        
        probe_gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
        ## super cluster quantities
        probe_sc_energy = cms.string("superCluster.energy"),
        probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
        probe_sc_x      = cms.string("superCluster.x"),
        probe_sc_y      = cms.string("superCluster.y"),
        probe_sc_z      = cms.string("superCluster.z"),
        probe_sc_eta    = cms.string("superCluster.eta"),
        probe_sc_theta  = cms.string("superClusterPosition.theta"),   
        probe_sc_phi    = cms.string("superCluster.phi"),
        probe_sc_size   = cms.string("superCluster.size"), # number of hits
        ## track quantities
        probe_track_p      = cms.string("gsfTrack.p"),
        probe_track_pt     = cms.string("gsfTrack.pt"),    
        probe_track_px     = cms.string("gsfTrack.px"),
        probe_track_py     = cms.string("gsfTrack.py"),
        probe_track_pz     = cms.string("gsfTrack.pz"),
        probe_track_eta    = cms.string("gsfTrack.eta"),
        probe_track_theta  = cms.string("gsfTrack.theta"),   
        probe_track_phi    = cms.string("gsfTrack.phi"),
        probe_track_vx     = cms.string("gsfTrack.vx"),
        probe_track_vy     = cms.string("gsfTrack.vy"),
        probe_track_vz     = cms.string("gsfTrack.vz"),    
        probe_track_dxy    = cms.string("gsfTrack.dxy"),
        probe_track_d0     = cms.string("gsfTrack.d0"),
        probe_track_dsz    = cms.string("gsfTrack.dsz"),
        probe_track_charge = cms.string("gsfTrack.charge"),
        probe_track_qoverp = cms.string("gsfTrack.qoverp"),
        probe_track_normalizedChi2 = cms.string("gsfTrack.normalizedChi2"),
        ## isolation 
        probe_gsfEle_trackiso = cms.string("dr03TkSumPt"),
        probe_gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
        probe_gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
        ## classification, location, etc.    
        probe_gsfEle_classification = cms.string("classification"),
        probe_gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
        probe_gsfEle_bremFraction   = cms.string("fbrem"),
        probe_gsfEle_mva            = cms.string("mva"),        
        probe_gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
        probe_gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
        probe_gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
        probe_gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
        probe_gsfEle_isEB           = cms.string("isEB"),
        probe_gsfEle_isEE           = cms.string("isEE"),
        probe_gsfEle_isGap          = cms.string("isGap"),
        ## Hcal energy over Ecal Energy
        probe_gsfEle_HoverE         = cms.string("hcalOverEcal"),    
        probe_gsfEle_EoverP         = cms.string("eSuperClusterOverP"),
        probe_gsfEle_eSeedClusterOverP = cms.string("eSeedClusterOverP"),    
        ## Cluster shape information
        probe_gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
        probe_gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
        probe_gsfEle_e1x5               = cms.string("e1x5"),
        probe_gsfEle_e2x5Max            = cms.string("e2x5Max"),
        probe_gsfEle_e5x5               = cms.string("e5x5"),
        ## is ECAL driven ? is Track driven ?
        probe_gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
        probe_gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed"),
        #drjet = cms.InputTag("GSFdRToNearestPATJet"),
        #njet = cms.InputTag("GSFJetMultiplicity"),
        #d0_v = cms.InputTag("GSFImpactParameter","d0v"),
        #d0_b = cms.InputTag("GSFImpactParameter","d0b"),
        #dz_v = cms.InputTag("GSFImpactParameter","dzv"),
        #dz_b = cms.InputTag("GSFImpactParameter","dzb"),
        #nVertices   = cms.InputTag("nverticesModule"),
        #absdeltapt = cms.InputTag("deltaPfRecoPt","absdeltapt"),
    )
    
    PATProbeVariablesToStore = ProbeVariablesToStore.clone()
    
    TagVariablesToStore = cms.PSet(
        gsfEle_eta = cms.string("eta"),
        gsfEle_abseta = cms.string("abs(eta)"),
        gsfEle_pt  = cms.string("pt"),
        gsfEle_phi  = cms.string("phi"),
        gsfEle_et  = cms.string("et"),
        gsfEle_e  = cms.string("energy"),
        gsfEle_p  = cms.string("p"),
        gsfEle_px  = cms.string("px"),
        gsfEle_py  = cms.string("py"),
        gsfEle_pz  = cms.string("pz"),
        gsfEle_theta  = cms.string("theta"),    
        gsfEle_charge = cms.string("charge"),
        gsfEle_rapidity  = cms.string("rapidity"),
        gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
        gsfEle_convDist = cms.string("convDist"),
        gsfEle_convDcot = cms.string("convDcot"),
        gsfEle_convRadius = cms.string("convRadius"),     
        gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
        ## super cluster quantities
        sc_energy = cms.string("superCluster.energy"),
        sc_et     = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
        sc_x      = cms.string("superCluster.x"),
        sc_y      = cms.string("superCluster.y"),
        sc_z      = cms.string("superCluster.z"),
        sc_eta    = cms.string("superCluster.eta"),
        sc_theta  = cms.string("superClusterPosition.theta"),      
        sc_phi    = cms.string("superCluster.phi"),
        sc_size   = cms.string("superCluster.size"), # number of hits
        ## track quantities
        track_p      = cms.string("gsfTrack.p"),
        track_pt     = cms.string("gsfTrack.pt"),    
        track_px     = cms.string("gsfTrack.px"),
        track_py     = cms.string("gsfTrack.py"),
        track_pz     = cms.string("gsfTrack.pz"),
        track_eta    = cms.string("gsfTrack.eta"),
        track_theta  = cms.string("gsfTrack.theta"),   
        track_phi    = cms.string("gsfTrack.phi"),
        track_vx     = cms.string("gsfTrack.vx"),
        track_vy     = cms.string("gsfTrack.vy"),
        track_vz     = cms.string("gsfTrack.vz"),    
        track_dxy    = cms.string("gsfTrack.dxy"),
        track_d0     = cms.string("gsfTrack.d0"),
        track_dsz    = cms.string("gsfTrack.dsz"),
        track_charge = cms.string("gsfTrack.charge"),
        track_qoverp = cms.string("gsfTrack.qoverp"),
        track_normalizedChi2 = cms.string("gsfTrack.normalizedChi2"),    
        ## isolation 
        gsfEle_trackiso = cms.string("dr03TkSumPt"),
        gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
        gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
        ## classification, location, etc.    
        gsfEle_classification = cms.string("classification"),
        gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
        gsfEle_bremFraction   = cms.string("fbrem"),
        gsfEle_mva            = cms.string("mva"),        
        gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
        gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
        gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
        gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
        gsfEle_isEB           = cms.string("isEB"),
        gsfEle_isEE           = cms.string("isEE"),
        gsfEle_isGap          = cms.string("isGap"),
        ## Hcal energy over Ecal Energy
        gsfEle_HoverE         = cms.string("hcalOverEcal"),    
        gsfEle_EoverP         = cms.string("eSuperClusterOverP"),
        gsfEle_eSeedClusterOverP = cms.string("eSeedClusterOverP"),  
        ## Cluster shape information
        gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
        gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
        gsfEle_e1x5               = cms.string("e1x5"),
        gsfEle_e2x5Max            = cms.string("e2x5Max"),
        gsfEle_e5x5               = cms.string("e5x5"),
        ## is ECAL driven ? is Track driven ?
        gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
        gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed")
    )
    
    PATTagVariablesToStore = TagVariablesToStore.clone()
    
    CommonStuffForGsfElectronProbe = cms.PSet(
        variables = cms.PSet(ProbeVariablesToStore,SUSY_InfoGSF),
        ignoreExceptions =  cms.bool (False),
        addRunLumiInfo   =  cms.bool (True),
        addEventVariablesInfo   =  cms.bool (True),
        pairVariables =  cms.PSet(ZVariablesToStore),
        pairFlags     =  cms.PSet(
              mass60to120 = cms.string("60 < mass < 120")
        ),
        tagVariables   =  cms.PSet(TagVariablesToStore),
        tagFlags     =  cms.PSet(
              passingGsf = cms.InputTag("goodElectrons"),
              isRA4 = cms.InputTag("PassingRA4"),
              isWP95 = cms.InputTag("PassingWP95"),
              isWP90 = cms.InputTag("PassingWP90"),
              isWP85 = cms.InputTag("PassingWP85"),          
              isWP80 = cms.InputTag("PassingWP80"),
              isWP70 = cms.InputTag("PassingWP70"),
              isWP60 = cms.InputTag("PassingWP60"),
        ),    
    )

    
    CommonStuffForSuperClusterProbe = CommonStuffForGsfElectronProbe.clone()
    CommonStuffForSuperClusterProbe.variables = cms.PSet(
        probe_eta = cms.string("eta"),
        probe_pt  = cms.string("pt"),
        probe_phi  = cms.string("phi"),
        probe_et  = cms.string("et"),
        probe_e  = cms.string("energy"),
        probe_p  = cms.string("p"),
        probe_px  = cms.string("px"),
        probe_py  = cms.string("py"),
        probe_pz  = cms.string("pz"),
        probe_theta  = cms.string("theta"),
    )
    
    tagPATCommonStuffForSuperClusterProbe = CommonStuffForSuperClusterProbe.clone(
        tagFlags = cms.PSet(all_triggers),
        tagVariables = cms.PSet(PATTagVariablesToStore,SUSY_InfoPAT),

    )
    tagPATCommonStuffForGsfElectronProbe = CommonStuffForGsfElectronProbe.clone(
        tagVariables = cms.PSet(PATTagVariablesToStore,SUSY_InfoPAT),                                                                        
        tagFlags = cms.PSet(all_triggers),
    )
  
    if MC_flag:
        tagPATmcTruthCommonStuff = cms.PSet(
            isMC = cms.bool(MC_flag),
            tagMatches = cms.InputTag("McMatchTagPATElectron"),
            motherPdgId = cms.vint32(22,23),
            makeMCUnbiasTree = cms.bool(MC_flag),
            checkMotherInUnbiasEff = cms.bool(MC_flag),
            mcVariables = cms.PSet(
            probe_eta = cms.string("eta"),
            probe_pt  = cms.string("pt"),
            probe_phi  = cms.string("phi"),
            probe_et  = cms.string("et"),
            probe_e  = cms.string("energy"),
            probe_p  = cms.string("p"),
            probe_px  = cms.string("px"),
            probe_py  = cms.string("py"),
            probe_pz  = cms.string("pz"),
            probe_theta  = cms.string("theta"),    
            probe_vx     = cms.string("vx"),
            probe_vy     = cms.string("vy"),
            probe_vz     = cms.string("vz"),   
            probe_charge = cms.string("charge"),
            probe_rapidity  = cms.string("rapidity"),    
            probe_mass  = cms.string("mass"),
            probe_mt  = cms.string("mt"),    
            ),
            mcFlags     =  cms.PSet(
            probe_flag = cms.string("pt>0")
            ),      
            )
    else:
         tagPATmcTruthCommonStuff = cms.PSet(
             isMC = cms.bool(False)
             )
       

    ##    ____   ____       __     ____      __ 
    ##   / ___| / ___|      \ \   / ___|___ / _|
    ##   \___ \| |      _____\ \ | |  _/ __| |_ 
    ##    ___) | |___  |_____/ / | |_| \__ \  _|
    ##   |____/ \____|      /_/   \____|___/_|  
    ##
    ## super cluster --> gsf electron
    process.SuperClusterToGsfElectronPATTag = cms.EDAnalyzer("TagProbeFitTreeProducer",
        ## pick the defaults
        tagPATCommonStuffForSuperClusterProbe, tagPATmcTruthCommonStuff,
        # choice of tag and probe pairs, and arbitration                 
        tagProbePairs = cms.InputTag("tagPATSC"),
        arbitration   = cms.string("Random2"),                      
        flags = cms.PSet(
            probe_passingGsf = cms.InputTag("GsfMatchedSuperClusterCands"),        
            probe_isRA4 = cms.InputTag("RA4MatchedSuperClusterCandsClean"),
            probe_isWP95 = cms.InputTag("WP95MatchedSuperClusterCandsClean"),
            probe_isWP90 = cms.InputTag("WP90MatchedSuperClusterCandsClean"),
            probe_isWP85 = cms.InputTag("WP85MatchedSuperClusterCandsClean"),        
            probe_isWP80 = cms.InputTag("WP80MatchedSuperClusterCandsClean"),
            probe_isWP70 = cms.InputTag("WP70MatchedSuperClusterCandsClean"),
            probe_isWP60 = cms.InputTag("WP60MatchedSuperClusterCandsClean"),
            probe_isGoodPat = cms.InputTag("GSFtoPATMatchedSuperClusterCandsClean"),
            probe_isGoodPatNoIso = cms.InputTag("GSFtoPATNoIsoMatchedSuperClusterCandsClean"),
        ),
        probeMatches  = cms.InputTag("McMatchSC"),
        allProbes     = cms.InputTag("goodSuperClustersClean")
    )
    process.SuperClusterToGsfElectronPATTag.variables.probe_dRjet = cms.InputTag("superClusterDRToNearestJet")
    process.SuperClusterToGsfElectronPATTag.variables.probe_nJets = cms.InputTag("JetMultiplicityInSCEvents")
    process.SuperClusterToGsfElectronPATTag.variables.probe_dist = cms.InputTag("SCConvRejVars","dist")
    process.SuperClusterToGsfElectronPATTag.variables.probe_dcot = cms.InputTag("SCConvRejVars","dcot")
    process.SuperClusterToGsfElectronPATTag.variables.probe_convradius = cms.InputTag("SCConvRejVars","convradius")
    process.SuperClusterToGsfElectronPATTag.variables.probe_passConvRej = cms.InputTag("SCConvRejVars","passConvRej")
 
        
    ##   ____      __       __    ___                 ___    _ 
    ##  / ___|___ / _|      \ \  |_ _|___  ___       |_ _|__| |
    ## | |  _/ __| |_   _____\ \  | |/ __|/ _ \       | |/ _` |
    ## | |_| \__ \  _| |_____/ /  | |\__ \ (_) |  _   | | (_| |
    ##  \____|___/_|        /_/  |___|___/\___/  ( ) |___\__,_|
    ##                                           |/            
    ##  gsf electron --> isolation, electron id  etc.
    process.GsfElectronToIdPATTag = cms.EDAnalyzer("TagProbeFitTreeProducer",
        tagPATmcTruthCommonStuff, tagPATCommonStuffForGsfElectronProbe,
        tagProbePairs = cms.InputTag("tagPATGsf"),
        arbitration   = cms.string("Random2"),
        flags = cms.PSet(
            probe_isRA4 = cms.InputTag("PassingRA4"),
            probe_isWP95 = cms.InputTag("PassingWP95"),
            probe_isWP90 = cms.InputTag("PassingWP90"),
            probe_isWP85 = cms.InputTag("PassingWP85"),        
            probe_isWP80 = cms.InputTag("PassingWP80"),
            probe_isWP70 = cms.InputTag("PassingWP70"),
            probe_isWP60 = cms.InputTag("PassingWP60"),  
            probe_passingGOOD = cms.InputTag("GSFPassingGoodPat"),
            probe_passingGOODNoIso = cms.InputTag("GSFPassingGoodPatNoIso")
        
        ),
        probeMatches  = cms.InputTag("McMatchGsf"),
        allProbes     = cms.InputTag("goodElectrons")
    )
    process.GsfElectronToIdPATTag.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
    process.GsfElectronToIdPATTag.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")
    process.GsfElectronToIdPATTag.variables.probe_dist = cms.InputTag("GsfConvRejVars","dist")
    process.GsfElectronToIdPATTag.variables.probe_dcot = cms.InputTag("GsfConvRejVars","dcot")
    process.GsfElectronToIdPATTag.variables.probe_convradius = cms.InputTag("GsfConvRejVars","convradius")
    process.GsfElectronToIdPATTag.variables.probe_passConvRej = cms.InputTag("GsfConvRejVars","passConvRej")


            
    
    ##    ___    _       __    _   _ _   _____ 
    ##   |_ _|__| |      \ \  | | | | | |_   _|
    ##    | |/ _` |  _____\ \ | |_| | |   | |  
    ##    | | (_| | |_____/ / |  _  | |___| |  
    ##   |___\__,_|      /_/  |_| |_|_____|_|
    ##
    ##  offline selection --> HLT. First specify which quantities to store in the TP tree. 
    if MC_flag:
        HLTmcTruthCommonStuffPAT = cms.PSet(
            isMC = cms.bool(MC_flag),
            tagMatches = cms.InputTag("McMatchTagPATElectron"),
            motherPdgId = cms.vint32(22,23),
            makeMCUnbiasTree = cms.bool(MC_flag),
            checkMotherInUnbiasEff = cms.bool(MC_flag),
            mcVariables = cms.PSet(
              probe_eta = cms.string("eta"),
              probe_phi  = cms.string("phi"),
              probe_et  = cms.string("et"),
              probe_charge = cms.string("charge"),
            ),
            mcFlags     =  cms.PSet(
              probe_flag = cms.string("pt>0")
            ),      
        )
    else:
        HLTmcTruthCommonStuffPAT = cms.PSet(
             isMC = cms.bool(False)
        )
    

    
    
    ##  goodPATElectrons --> HLT
    process.goodPATEleToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
        HLTmcTruthCommonStuffPAT,                                
        variables = cms.PSet(
            SUSY_InfoPAT,
            probe_gsfEle_eta = cms.string("eta"),
            probe_gsfEle_abseta = cms.string("abs(eta)"),
            probe_gsfEle_phi  = cms.string("phi"),
            probe_gsfEle_et  = cms.string("et"),
            probe_gsfEle_charge = cms.string("charge"),
            probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
            probe_sc_eta    = cms.string("superCluster.eta"), 
            probe_sc_phi    = cms.string("superCluster.phi"),
            probe_gsfEle_isEB           = cms.string("isEB"),
            probe_gsfEle_isEE           = cms.string("isEE"),
            probe_gsfEle_isGap          = cms.string("isGap"),
            probe_gsfEle_trackiso = cms.string("dr03TkSumPt"),
            probe_gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
            probe_gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
            probe_gsfEle_stlep    = cms.InputTag("stComp"),
        ),
        ignoreExceptions =  cms.bool (False),
        addRunLumiInfo   =  cms.bool (False),
        addEventVariablesInfo   =  cms.bool (False),                                                        
        tagProbePairs = cms.InputTag("tagPATGoodPATElectron"),
        arbitration   = cms.string("Random2"),
        flags = cms.PSet( 
            all_triggers
        ),
        tagVariables = cms.PSet(
            SUSY_InfoPAT,
            gsfEle_trackiso = cms.string("dr03TkSumPt"),
            gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
            gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
            ht = cms.InputTag("glbHT"),
            met = cms.InputTag("glbMet"),
            passingHLT_Ele15_HT250_PFMHT25 = cms.InputTag("flagPassHLTEle15HT250PFMHT25"),
            passingHLT_Ele15_HT250_PFMHT40 = cms.InputTag("flagPassHLTEle15HT250PFMHT40"),
            passingHLT_CleanPFHT350_Ele5_PFMET45      = cms.InputTag("flagPassHLTCleanPFHT350PFMET45"),
            passingHLT_CleanPFHT350_Ele5_PFMET50      = cms.InputTag("flagPassHLTCleanPFHT350PFMET50"),
            passingHLT_CleanPFNoPUHT350_Ele5_PFMET45  = cms.InputTag("flagPassHLTCleanPFNoPUHT350PFMET45"),
            passingHLT_CleanPFNoPUHT350_Ele5_PFMET50  = cms.InputTag("flagPassHLTCleanPFNoPUHT350PFMET50"),
            passingHLT_CleanPFHT300_Ele15_PFMET45     = cms.InputTag("flagPassHLTCleanPFHT300Ele15PFMET45"),
            passingHLT_CleanPFHT300_Ele15_PFMET50     = cms.InputTag("flagPassHLTCleanPFHT300Ele15PFMET50"),
            passingHLT_CleanPFNoPUHT300_Ele15_PFMET45 = cms.InputTag("flagPassHLTCleanPFNoPUHT300Ele15PFMET45"),
            passingHLT_CleanPFNoPUHT300_Ele15_PFMET50 = cms.InputTag("flagPassHLTCleanPFNoPUHT300Ele15PFMET50"),
            passingHLT_CleanPFHT300_Ele40             = cms.InputTag("flagPassHLTCleanPFHT300Ele40"),
            passingHLT_CleanPFHT300_Ele60             = cms.InputTag("flagPassHLTCleanPFHT300Ele60"),
            passingHLT_CleanPFNoPUHT300_Ele40         = cms.InputTag("flagPassHLTCleanPFNoPUHT300Ele40"),
            passingHLT_CleanPFNoPUHT300_Ele60         = cms.InputTag("flagPassHLTCleanPFNoPUHT300Ele60"),
        ),
        tagFlags = cms.PSet( 
            all_triggers        
        ),

        probeMatches  = cms.InputTag("McMatchPATElectron"),
        allProbes     = cms.InputTag("goodPATElectrons")
    )

    
    process.goodPATEleProbeTree = cms.EDAnalyzer("ProbeTreeProducerModified",
        variables = cms.PSet(
            SUSY_InfoPAT,
            probe_gsfEle_eta = cms.string("eta"),
            probe_gsfEle_abseta = cms.string("abs(eta)"),
            probe_gsfEle_phi  = cms.string("phi"),
            probe_gsfEle_et  = cms.string("et"),
            probe_gsfEle_charge = cms.string("charge"),
            probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
            probe_sc_eta    = cms.string("superCluster.eta"), 
            probe_sc_phi    = cms.string("superCluster.phi"),
            probe_gsfEle_isEB           = cms.string("isEB"),
            probe_gsfEle_isEE           = cms.string("isEE"),
            probe_gsfEle_isGap          = cms.string("isGap"),
            probe_gsfEle_trackiso = cms.string("dr03TkSumPt"),
            probe_gsfEle_ecaliso  = cms.string("dr03EcalRecHitSumEt"),
            probe_gsfEle_hcaliso  = cms.string("dr03HcalTowerSumEt"),
            probe_gsfEle_stlep    = cms.InputTag("stComp"),
            passingHLT_CleanPFHT300_Ele40             = cms.InputTag("flagPassHLTCleanPFHT300Ele40"),
            passingHLT_CleanPFHT300_Ele60             = cms.InputTag("flagPassHLTCleanPFHT300Ele60"),
            passingHLT_CleanPFNoPUHT300_Ele40         = cms.InputTag("flagPassHLTCleanPFNoPUHT300Ele40"),
            passingHLT_CleanPFNoPUHT300_Ele60         = cms.InputTag("flagPassHLTCleanPFNoPUHT300Ele60"),
            ht = cms.InputTag("glbHT"),
            met = cms.InputTag("glbMet"),
        ),
        ignoreExceptions =  cms.bool (False),
        addRunLumiInfo   =  cms.bool (True),
        addEventVariablesInfo   =  cms.bool (True),                                                        
        flags = cms.PSet( 
            #all_triggers
            HLT_Ele30_CaloIdVT_TrkIdT = cms.string('!triggerObjectMatchesByPath("HLT_Ele30_CaloIdVT_TrkIdT_v*",1,0).empty()'),
        ),
        src     = cms.InputTag("goodPATElectrons"),
        # If running on MC set mcTrue to 1 if there exist a matching GenParticle with specified PdgId (11 for Ele)
        isMC = cms.bool(MC_flag),
        PdgId = cms.vint32(11),
        probeMatches  = cms.InputTag("McMatchPATElectron"),
        # Used for Ele40/60 turnon measurement
        #cut = cms.string("!triggerObjectMatchesByPath('HLT_Ele30_CaloIdVT_TrkIdT_v*',1,0).empty()"),
        #maxProbes = cms.int32(1),
        #maxNumOfProbesInEvent = cms.int32(1)                                       
    )

    process.goodGsfEleProbeTree = cms.EDAnalyzer("ProbeTreeProducerModified",
        variables = cms.PSet(
            SUSY_InfoGSF,
            ProbeVariablesToStore,
            probe_gsfEle_stlep    = cms.InputTag("stCompGsf"),
            ht = cms.InputTag("glbHTGsf"),
            met = cms.InputTag("glbMetGsf"),
            probe_dRjet = cms.InputTag("GsfDRToNearestJet"),
            probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents"),
            probe_dist = cms.InputTag("GsfConvRejVars","dist"),
            probe_dcot = cms.InputTag("GsfConvRejVars","dcot"),
            probe_convradius = cms.InputTag("GsfConvRejVars","convradius"),
            probe_passConvRej = cms.InputTag("GsfConvRejVars","passConvRej"),
        ),
        flags = cms.PSet( 
            isRA4 = cms.InputTag("PassingRA4"),
            probe_passingGOOD = cms.InputTag("GSFPassingGoodPat"),
            probe_passingCLEAN = cms.InputTag("GsfPassingCleanPat"),
        ),
        ignoreExceptions =  cms.bool (False),
        addRunLumiInfo   =  cms.bool (True),
        addEventVariablesInfo   =  cms.bool (True),
        src = cms.InputTag(ELECTRON_COLL),
        # If running on MC set mcTrue to 1 if there exist a matching GenParticle with specified PdgId (11 for Ele)
        isMC = cms.bool(MC_flag),
        PdgId = cms.vint32(11),
        probeMatches  = cms.InputTag("McMatchGSF"),
    )

    process.tree_sequence = cms.Sequence(
        process.SuperClusterToGsfElectronPATTag +
        process.GsfElectronToIdPATTag +
        process.goodPATEleToHLT +
        process.goodGsfEleProbeTree
    )    
    
    ##    ____       _   _     
    ##   |  _ \ __ _| |_| |__  
    ##   | |_) / _` | __| '_ \ 
    ##   |  __/ (_| | |_| | | |
    ##   |_|   \__,_|\__|_| |_|
    ##
    
    if MC_flag:
        process.TagAndProbe = cms.Sequence(
            (process.sc_sequence +
             process.ele_sequence + 
             process.ext_ToNearestJet_sequence + 
             process.allTagsAndProbes +
             process.mc_sequence +
             process.allHLTResults +
             process.allMet +
             process.allST +
             process.allJets + 
             process.allVertex +
             process.allImpactParameters +
             process.allRelIso +
             process.deltaPfRecoPt +
             process.GsfEledeltaPfRecoPt) *
            process.tree_sequence
            )
    else:
        process.TagAndProbe = cms.Sequence(
            (process.sc_sequence +
             process.ele_sequence  + 
             process.ext_ToNearestJet_sequence + 
             process.allTagsAndProbes +
             process.allHLTResults +
             process.allMet +
             process.allST +
             process.allJets + 
             process.allVertex +
             process.allImpactParameters +
             process.allRelIso +
             process.deltaPfRecoPt +
             process.GsfEledeltaPfRecoPt) *
            process.tree_sequence
            )
        
