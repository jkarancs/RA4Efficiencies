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
    version = cms.untracked.string('$Revision: 1.3 $'),
    name = cms.untracked.string('$Source: /RA4Efficiencies/TagAndProbe/python/RA4_TP_ZEE/runTnP_MC.py,v $'),
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
options.register('mcInfo', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")

options.register('GlobalTag', "FT_53_V6_AN2::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
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

# Triggers in the EleHad Dataset (They conflict - Use separately):
# HT300_Ele15_MET45
options.register('hltSelection', 'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*'    , VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.hltSelection.append(     'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*'    )
options.hltSelection.append(     'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*')
options.hltSelection.append(     'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*')
# HT350_Ele5_MET45
#options.hltSelection.append(     'HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*'                              )
#options.hltSelection.append(     'HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*'                              )
#options.hltSelection.append(     'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*'                          )
#options.hltSelection.append(     'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*'                          )
# HT300_Ele40
#options.hltSelection.append(     'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*'     )
#options.hltSelection.append(     'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*'     )
#options.hltSelection.append(     'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*' )
#options.hltSelection.append(     'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*' )
# Ele25_TriCentralPFJet30
#options.hltSelection.append(     'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v*'  )
#options.hltSelection.append(     'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v*'                         )
#options.hltSelection.append(     'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFNoPUJet30_v*'                     )
#options.hltSelection.append(     'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v*'        )
#options.hltSelection.append(     'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFNoPUJet30_v*'    )

options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
#options.register('addKeep', 'keep *_*TriggerMatch_*_*', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")

#options.register('files', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "List of input files")
options.files.append('file:/data/jkarancs/MC/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball__Summer12-PU_S7_START52_V9-v2__AODSIM/FC73DFC5-709B-E111-92DB-001A6478950C.root')

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
process.electronTriggerMatchHLTElectrons = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    src     = cms.InputTag( 'cleanPatElectrons' ),
    matched = cms.InputTag( 'patTrigger' ),
    matchedCuts = cms.string('type( "TriggerElectron" ) && ('
                             # Triggers in the EleHad Dataset (They conflict - Use separately):
                             # HT300_Ele15_MET45
                             'path("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"    ,0,1) || '
                             'path("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"    ,0,1) || '
                             'path("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*",0,1) || '
                             'path("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",0,1)  '
                             # HT350_Ele5_MET45
                             #'path("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*"     ,0,1) || '
                             #'path("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*"     ,0,1) || '
                             #'path("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*" ,0,1) || '
                             #'path("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*" ,0,1) '
                             # HT300_Ele40
                             #'path("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v*"                              ,0,1) || '
                             #'path("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v*"                              ,0,1) || '
                             #'path("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v*"                          ,0,1) || '
                             #'path("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v*"                          ,0,1) '
                             # Ele25_TriCentralPFJet30
                             #'path("HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v*" ,0,1) || '
                             #'path("HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v*"                        ,0,1) || '
                             #'path("HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFNoPUJet30_v*"                    ,0,1) || '
                             #'path("HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v*"       ,0,1) || '
                             #'path("HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFNoPUJet30_v*"   ,0,1)  '
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
switchOnTriggerMatchEmbedding( process, [ 'electronTriggerMatchHLTElectrons' ], hltProcess = options.hltName, sequence =  "susyPatDefaultSequence")

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
              #process.scrapingVeto *
              process.primaryVertexFilter*
              #process.HBHENoiseFilter*
              process.goodVertices*
              #process.trackingFailureFilter*
              #process.hcalLaserEventFilter*
              #process.hcallasereventfilter2012*
              #process.ecalLaserCorrFilter*
              #process.trkPOGFilters*
              #process.CSCTightHaloFilter*
              #process.eeBadScFilter*
              #process.EcalDeadCellTriggerPrimitiveFilter
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

#-- Egamma Isolation -------------------------------------------------------
#compute rho for 2011 effective area Egamma isolation corrections
from RecoJets.JetProducers.kt4PFJets_cfi import *
process.kt6PFJetsForIsolation2011 = kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True )
process.kt6PFJetsForIsolation2011.Rho_EtaMax = cms.double(2.5)
process.susyPatDefaultSequence += process.kt6PFJetsForIsolation2011

#-- Counting _--------------------------------------------------------------
process.load('RA4Efficiencies/TagAndProbe/HLT_cfi')

#-- My Analyzer _--------------------------------------------------------------
from RA4Efficiencies.TagAndProbe.RA4_TP_ZEE.produceTrees import *
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
process.TFileService = cms.Service("TFileService", fileName = cms.string("tpZEE_MC.root"))
