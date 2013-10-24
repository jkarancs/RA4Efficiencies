import FWCore.ParameterSet.Config as cms

JetMetPath = cms.vstring(
  #'HLT_Jet180',
  #'HLT_Jet140',
#  'HLT_Jet100U',
#  'HLT_Jet70U',
#  'HLT_Jet50U',
#  'HLT_Jet30U',
#  'HLT_QuadJet25U',
#  'HLT_DiJetAve50U',
#  'HLT_MET45',
#  'HLT_MET65',
#  'HLT_MET100'
)

ExtraPath = cms.vstring(
#  'HLT_L1Mu',
#  'HLT_L1MuOpen',
#  'HLT_IsoMu9',
#  'HLT_Mu5',
#  'HLT_Mu9',
#  'HLT_Mu11',
# # 'HLT_Mu15',
#  'HLT_DoubleMu3',
)

countingHLTFilter = cms.EDFilter ( "CountingHLTFilter",
  TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
  saveTags = cms.bool(False),
  HLTPaths = JetMetPath + ExtraPath,
  passAll = cms.bool ( True ),
  xsec = cms.double ( 16.06 ), # cross section
  normalize = cms.double ( 100. ), # normalize weight to 100 pb^-1
  andOr = cms.bool(True)
)

#triggerResultWriter = cms.EDProducer("TriggerResultWriter",
#  name = cms.string ( "Trigger" ),
#  results = cms.InputTag("TriggerResults","","HLT"),
#  verbose = cms.bool ( False ),
#  triggerpath = JetMetPath,
#  additionalpaths = ExtraPath
#)

