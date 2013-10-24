#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 42X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV10
#

# Starting with a skeleton process which gets imported with the following line
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.outpath = cms.EndPath()

#-- Meta data to be logged in DBS ---------------------------------------------
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /RA4Efficiencies/TagAndProbe/python/RA4_TP_ZMuMu/runTnP_Data.py,v $'),
    annotation = cms.untracked.string('SUSY pattuple definition')
)

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
#-- Message Logger ------------------------------------------------------------
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(
    limit = cms.untracked.int32(-1),
    reportEvery = cms.untracked.int32(1)
    )
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')

#options.output = "SUSYPAT.root"
options.maxEvents = -1
#  for SusyPAT configuration 
options.register('mcInfo', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")

options.register('GlobalTag', "GR_P_V41_AN2::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
if options.mcInfo:
    options.GlobalTag="START53_V7F::All"

options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
if not options.mcInfo:
    options.jetCorrections.append('L2L3Residual')

options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
options.register('hltSelection', 'HLT_Mu*', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.hltSelection.append('HLT_IsoMu*')
## 2011 Triggers
#options.hltSelection.append('HLT_Mu8_HT200_v*')
#options.hltSelection.append('HLT_Mu15_HT200_v*')
#options.hltSelection.append('HLT_Mu30_HT200_v*')
#options.hltSelection.append('HLT_Mu40_HT200_v*')
#options.hltSelection.append('HLT_Mu40_HT300_v*')
#options.hltSelection.append('HLT_HT250_Mu15_PFMHT20_v*')
#options.hltSelection.append('HLT_HT250_Mu15_PFMHT40_v*')
#options.hltSelection.append('HLT_HT300_Mu15_PFMHT40_v*')
# 2012 Triggers
options.hltSelection.append('HLT_Mu40_HT200_v*')
options.hltSelection.append('HLT_Mu40_FJHT200_v*')
options.hltSelection.append('HLT_Mu40_PFHT350_v*')
options.hltSelection.append('HLT_Mu40_PFNoPUHT350_v*')
options.hltSelection.append('HLT_Mu60_PFHT350_v*')
options.hltSelection.append('HLT_Mu60_PFNoPUHT350_v*')
options.hltSelection.append('HLT_PFHT350_Mu15_PFMET45_v*')
options.hltSelection.append('HLT_PFNoPUHT350_Mu15_PFMET45_v*')
options.hltSelection.append('HLT_PFHT350_Mu15_PFMET50_v*')
options.hltSelection.append('HLT_PFNoPUHT350_Mu15_PFMET50_v*')
options.hltSelection.append('HLT_PFHT400_Mu5_PFMET45_v*')
options.hltSelection.append('HLT_PFNoPUHT400_Mu5_PFMET45_v*')
options.hltSelection.append('HLT_PFHT400_Mu5_PFMET50_v*')
options.hltSelection.append('HLT_PFNoPUHT400_Mu5_PFMET50_v*')

options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
#options.register('addKeep', 'keep *_*TriggerMatch_*_*', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")

#options.register('files', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "List of input files")
options.files.append('file:/data/jkarancs/data/SingleMu__Run2012A-13Jul2012-v1__AOD/E4B1E118-69D2-E111-A562-00266CFFC13C.root')
#options.files.append('file:/data/jkarancs/data/SingleMu__Run2011B-19Nov2011-v1__AOD/742BBF97-6E17-E111-8A7E-001F29C49312.root')

#-- Input Source --------------------------------------------------------------
if options.files:
    process.source.fileNames = cms.untracked.vstring (options.files)

process.maxEvents.input = options.maxEvents
# Due to problem in production of LM samples: same event number appears multiple times
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')


#-- Calibration tag -----------------------------------------------------------
if options.GlobalTag:
    process.GlobalTag.globaltag = options.GlobalTag

# define trigger match
# just a basic working example... has to be tuned!
process.muonTriggerMatchHLTMuons = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    src     = cms.InputTag( 'cleanPatMuons' ),
    matched = cms.InputTag( 'patTrigger' ),
    matchedCuts = cms.string( 'type("TriggerMuon") && ('
                              ## 2011 Triggers
                              #'(hasFilterLabel("hltL1Mu0HTT50L3MuFiltered8") && path("HLT_Mu8_HT200_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1Mu0HTT50L3MuFiltered15") && path("HLT_Mu15_HT200_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1Mu0HTT50L3MuFiltered30") && path("HLT_Mu30_HT200_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1Mu0HTT50L3MuFiltered40") && path("HLT_Mu40_HT200_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1Mu0HTT50L2QualL3MuFiltered40") && path("HLT_Mu40_HT300_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1HTT100singleMuL3PreFiltered15") && path("HLT_HT250_Mu15_PFMHT20_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1HTT100singleMuL3PreFiltered15") && path("HLT_HT250_Mu15_PFMHT40_v*",0,0)) || '
                              #'(hasFilterLabel("hltL1HTT100singleMuL3PreFiltered15") && path("HLT_HT300_Mu15_PFMHT40_v*",0,0)) ||'
                              # 2012 Triggers
                              # Mu*
                              '(hasFilterLabel("hltL3fL1sMu3L3Filtered5") && path("HLT_Mu5_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu3L3Filtered8") && path("HLT_Mu8_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu7L3Filtered12") && path("HLT_Mu12_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu12L3Filtered17") && path("HLT_Mu17_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16L1f0L2f16QL3Filtered24Q") && path("HLT_Mu24_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16L1f0L2f16QL3Filtered30Q") && path("HLT_Mu30_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16L1f0L2f16QL3Filtered40Q") && path("HLT_Mu40_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu7L1fEta2p1L2fEta2p1f7L3FilteredEta2p1Filtered15") && path("HLT_Mu15_eta2p1_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q") && path("HLT_Mu24_eta2p1_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered30Q") && path("HLT_Mu30_eta2p1_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q") && path("HLT_Mu40_eta2p1_v*",0,0)) || '
                              '(hasFilterLabel("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered50Q") && path("HLT_Mu50_eta2p1_v*",0,0)) || '
                              # IsoMu*
                              '(hasFilterLabel("hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15") && path("HLT_IsoMu24_v*",0,0)) || '
                              '(hasFilterLabel("hltL3crIsoL1sMu16L1f0L2f16QL3f30QL3crIsoRhoFiltered0p15") && path("HLT_IsoMu30_v*",0,0)) || '
                              '((hasFilterLabel("hltL3crIsoL1sMu12Eta2p1L1f0L2f12QL3f15QL3crIsoFiltered10") || hasFilterLabel("hltL3crIsoL1sMu12Eta2p1L1f0L2f12QL3f15QL3crIsoRhoFiltered0p15")) && path("HLT_IsoMu15_eta2p1_L1ETM20_v*",0,0)) || '
                              '((hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoFiltered10") || hasFilterLabel(" hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoRhoFiltered0p15")) && path("HLT_IsoMu20_eta2p1_v*",0,0)) || '
                              '((hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10") || hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15")) && path("HLT_IsoMu24_eta2p1_v*",0,0)) || '
                              '((hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoFiltered10") || hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoRhoFiltered0p15")) && path("HLT_IsoMu30_eta2p1_v*",0,0)) || '
                              '((hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoFiltered10") || hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoRhoFiltered0p15")) && path("HLT_IsoMu34_eta2p1_v*",0,0)) || '
                              '((hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoFiltered10") || hasFilterLabel("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoRhoFiltered0p15")) && path("HLT_IsoMu40_eta2p1_v*",0,0)) || '
                              # Cross Triggers
                              '(hasFilterLabel("hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40") && path("HLT_Mu40_HT200_v*",0,0)) || '
                              '(hasFilterLabel("hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40") && path("HLT_Mu40_FJHT200_v*",0,0)) || '
                              '(hasFilterLabel("hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40") && path("HLT_Mu40_PFHT350_v*",0,0)) || '
                              '(hasFilterLabel("hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40") && path("HLT_Mu40_PFNoPUHT350_v*",0,0)) || '
                              '(hasFilterLabel("hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered60") && path("HLT_Mu60_PFHT350_v*",0,0)) || '
                              '(hasFilterLabel("hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered60") && path("HLT_Mu60_PFNoPUHT350_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered15") && path("HLT_PFHT350_Mu15_PFMET45_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered15") && path("HLT_PFNoPUHT350_Mu15_PFMET45_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered15") && path("HLT_PFHT350_Mu15_PFMET50_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered15") && path("HLT_PFNoPUHT350_Mu15_PFMET50_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered5") && path("HLT_PFHT400_Mu5_PFMET45_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered5") && path("HLT_PFNoPUHT400_Mu5_PFMET45_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered5") && path("HLT_PFHT400_Mu5_PFMET50_v*",0,0)) || '
                              '(hasFilterLabel("hltL1HTT150singleMuL3PreFiltered5") && path("HLT_PFNoPUHT400_Mu5_PFMET50_v*",0,0))'
                              ')'),
    maxDPtRel   = cms.double( 0.5 ), # no effect here
    maxDeltaR   = cms.double( 0.5 ),
    resolveAmbiguities    = cms.bool( True ),
    resolveByMatchQuality = cms.bool( True )
)

############################# START SUSYPAT specifics ####################################
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands
#Apply SUSYPAT
addDefaultSUSYPAT(process,options.mcInfo,options.hltName,options.jetCorrections,options.mcVersion,options.jetTypes,options.doValidation,options.doExtensiveMatching,options.doSusyTopProjection)

process.load('PhysicsTools.PatAlgos.triggerLayer1.triggerMatcher_cfi')

#from PhysicsTools.PatAlgos.triggerLayer1.triggerMatcher_cfi import cleanMuonTriggerMatchHLTMu20
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger( process, hltProcess = options.hltName, sequence =  "susyPatDefaultSequence") # This is optional and can be omitted.
switchOnTriggerMatchEmbedding( process, [ 'muonTriggerMatchHLTMuons' ], hltProcess = options.hltName, sequence =  "susyPatDefaultSequence")

SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )
############################## END SUSYPAT specifics ####################################

#-- HLT selection ------------------------------------------------------------
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
if options.hltSelection:
    process.hltFilter = hlt.hltHighLevel.clone(
        HLTPaths = cms.vstring(options.hltSelection),
        TriggerResultsTag = cms.InputTag("TriggerResults","",options.hltName),
        throw = False
    )
    process.susyPatDefaultSequence.replace(process.eventCountProducer, process.eventCountProducer * process.hltFilter)


#-- Filter --------------------------------------------------------------
process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                    applyfilter = cms.untracked.bool(True),
                                    debugOn = cms.untracked.bool(False),
                                    numtrack = cms.untracked.uint32(10),
                                    thresh = cms.untracked.double(0.25)
                                    )
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
             vertexCollection = cms.InputTag('offlinePrimaryVertices'),
             minimumNDOF = cms.uint32(4) ,
             maxAbsZ = cms.double(24),
             maxd0 = cms.double(2)
                                           )
process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')
#process.HBHENoiseFilter.minIsolatedNoiseSumE = cms.double(999999.)
#process.HBHENoiseFilter.minNumIsolatedNoiseChannels = cms.int32(999999)
#process.HBHENoiseFilter.minIsolatedNoiseSumEt = cms.double(999999.)
process.goodVertices = cms.EDFilter(
            "VertexSelector",
            filter = cms.bool(False),
            src = cms.InputTag("offlinePrimaryVertices"),
            cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2")
          )
process.load("RecoMET.METFilters.hcalLaserEventFilter_cfi")
process.hcalLaserEventFilter.vetoByRunEventNumber=cms.untracked.bool(False)
process.hcalLaserEventFilter.vetoByHBHEOccupancy=cms.untracked.bool(True)
process.load("EventFilter.HcalRawToDigi.hcallasereventfilter2012_cfi")
process.load('RecoMET.METFilters.ecalLaserCorrFilter_cfi')
process.load('RecoMET.METFilters.trackingPOGFilters_cff')
process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.load('RecoMET.METAnalyzers.CSCHaloFilter_cfi')
process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')
process.filterSequence = cms.Sequence(
              process.hltFilter *
              process.scrapingVeto *
              process.primaryVertexFilter*
              process.HBHENoiseFilter*
              process.goodVertices*
              process.trackingFailureFilter*
              process.hcalLaserEventFilter*
              process.hcallasereventfilter2012*
              process.ecalLaserCorrFilter*
              process.trkPOGFilters*
              process.CSCTightHaloFilter*
              process.eeBadScFilter*
              process.EcalDeadCellTriggerPrimitiveFilter
          )

#-- MET Corrections ----------------------------------------------------------
process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
if options.mcInfo:
  process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3"
  process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_mc
else:
  process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3Residual"
  process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_data
process.patPFMETs = process.patMETs.clone(
             metSource = cms.InputTag('pfMet'),
             addMuonCorrections = cms.bool(False),
             #genMETSource = cms.InputTag('genMetTrue'),
             #addGenMET = cms.bool(True)
             )
process.pfType1CorrectedMet.applyType0Corrections = cms.bool(False)
process.pfType1CorrectedMet.srcType1Corrections = cms.VInputTag(
    cms.InputTag('pfJetMETcorr', 'type1') ,
    cms.InputTag('pfMEtSysShiftCorr')  
)
process.patPFMETsTypeIcorrected = process.patPFMETs.clone(
             metSource = cms.InputTag('pfType1CorrectedMet'),
             )

process.susyPatDefaultSequence += process.pfMEtSysShiftCorrSequence
process.susyPatDefaultSequence += process.producePFMETCorrections
process.susyPatDefaultSequence += process.patPFMETsTypeIcorrected

#-- Counting _--------------------------------------------------------------
process.load('RA4Efficiencies/TagAndProbe/HLT_cfi')

#-- My Analyzer _--------------------------------------------------------------
from RA4Efficiencies.TagAndProbe.RA4_TP_ZMuMu.produceTrees import *
initTP(process,options.mcInfo)

#-- Execution path ------------------------------------------------------------
process.out.outputCommands = cms.untracked.vstring('drop *', *SUSY_pattuple_outputCommands )
# analysis path
process.path = cms.Path(
      process.countingHLTFilter*
      process.filterSequence*
      process.susyPatDefaultSequence*
      process.TagAndProbe
)

#-- TFileService --------------------------------------------------------------
process.load ( "PhysicsTools.UtilAlgos.TFileService_cfi")
process.TFileService = cms.Service("TFileService", fileName = cms.string("tpZMuMu_Data.root"))
