import FWCore.ParameterSet.Config as cms

#   ___ ____ ____    ____ _  _ ___     ___  ____ ____ ___  ____ 
#    |  |__| | __    |__| |\ | |  \    |__] |__/ |  | |__] |___ 
#    |  |  | |__]    |  | | \| |__/    |    |  \ |__| |__] |___ 
    ################################################################################################################################                                                            

def initTP(process, mcInfo=False):

    process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
    process.load("Configuration.StandardSequences.MagneticField_cff")
    process.load("Configuration.StandardSequences.Geometry_cff")
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.load("Geometry.CommonDetUnit.globalTrackingGeometry_cfi")
    process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi")
    process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")
    process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi")
    ################################################################################################################################
 
#   ____ _  _ ___ ____ 
#   |    |  |  |  [__  
#   |___ |__|  |  ___] 

# Old Tag Cuts:
# isGlobalMuon()
# numberOfMatches() >= 2
# abs(eta()) <= 2.4                                           (recommended <= 2.1)
#+ abs(track.d0) < 2
#+ abs(track.dz) < 30
#
# Old Probe Cuts:
# isGood('AllTrackerMuons')
# isGood('GlobalMuonPromptTight')                             (Has normChi2 <= 10, at least 1 Muon system hits, isGlobalMuon)
# globalTrack().chi2()/globalTrack()->ndof() <= 10            (within isGood('GlobalMuonPromptTight'))
# globalTrack().hitPattern().numberOfValidMuonHits() > 0      (within isGood('GlobalMuonPromptTight'))
# numberOfMatches() >= 2
# innerTrack().hitPattern().pixelLayersWithMeasurement() >= 1 (Also cutting on this during Plotting?)
# globalTrack().hitPattern().numberOfValidTrackerHits() >= 11
# pt > 5                                                      (recommended >= 20, but this is a probe cut and thus lower)
# abs(eta()) < 2.4                                            (recommended <= 2.1)

# Old Cuts done during Efficiency Fitting:
# reco::deltaR(pat::Muon, pat::Jet) > 0.3                     (Plot: drjet > 0.3)
# (hcalIso() + ecalIso() + trackIso())/pt() < 0.10            (Plot: reliso  < 0.1)
# abs(innerTrack().vertex().z() - PV.z()) < 1.0               (Plot: (dz_v) < 1.0, cut: line 5xx)
# innerTrack().d0 (correct to beamspot) < 0.02                (Plot: (d0_b) < 0.02, cut: abs(dB()))
# abs(reco_pt - pf_pt) / reco_pt < 0.20                       (Plot: deltaPtRecoPF < 0.2)
# innerTrack().hitPattern().pixelLayersWithMeasurement() > 1  (Plot: pixlayer > 1, recommended >= 1)
# GlobalTrack_ptErr()/mus_pt()^2 < 0.001                      (Plot: ptErrorByPt2 < 0.001)



# New Tag Cuts:
# isGlobalMuon() 
# isPFMuon()
# numberOfMatchedStations() > 1
# abs(eta()) <= 2.4
#+ abs(track.d0) < 2
#+ abs(track.dz) < 30
#
# New Probe Cuts:
# isGood('GlobalMuonPromptTight')                             (isGlobalMuon, Has normChi2 <= 10, at least 1 Muon system hits)
#// globalTrack().chi2()/globalTrack()->ndof() <= 10          (within isGood('GlobalMuonPromptTight'))
#// globalTrack().hitPattern().numberOfValidMuonHits() > 0    (within isGood('GlobalMuonPromptTight'))
# numberOfMatchedStations() > 1
# innerTrack().hitPattern().numberOfValidPixelHits() > 0
# track().hitPattern().trackerLayersWithMeasurement() > 5
# pt() > 5                                                    (recommended >= 20, but this is a probe cut and thus lower)
# abs(eta()) <= 2.4

# New Cuts done during Efficiency Fitting:
# deltaR(muon, jet) > 0.3                                     (Plot: drjet > 0.3)
# (pfIsolationR03().sumChargedHadronPt + max(0., pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - 0.5*pfIsolationR03().sumPUPt ) ) / pt() < 0.12    (Plot: pfreliso < 0.12)
# abs(innerTrack()->dxy(vertexPosition)) < 0.02               (Plot: abs(d0_v) < 0.02, or cut: abs(dB()) < 0.02)
# abs(innerTrack()->dz(vertexPosition)) < 0.5                 (Plot: abs(dz_v) < 0.5, line: 5xx)
# abs(pt() - (*ipfMu).pt()) < 0.5                             (Plot: absdeltaPtRecoPF < 0.5 GeV)

## Implemented new variables:
# trklayer = cms.string("track.hitPattern().trackerLayersWithMeasurement()"),
# validpixhits = cms.string("innerTrack.hitPattern().numberOfValidPixelHits()"),
# pfreliso = cms.string("(pfIsolationR03().sumChargedHadronPt + max(pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - pfIsolationR03().sumPUPt/2,0.0))/pt"),
# absdeltaPtRecoPF: plugins/MatcherUsingTracksMatchInfo.cc:152: removed /pt()

    #TAG_CUTS = "isGlobalMuon() && numberOfMatches() > 1 && abs(eta) < 2.4 && abs(track.d0) < 2 && abs(track.dz) < 30"
    TAG_CUTS = "isGlobalMuon() && isPFMuon() && numberOfMatchedStations() > 1 && abs(eta) <= 2.4 && abs(track.d0) < 2 && abs(track.dz) < 24"
    
    RA4_MUON_ID_CUTS_NONCOMPREHENSIVE = "isGood('GlobalMuonPromptTight') && isPFMuon() && track().hitPattern().trackerLayersWithMeasurement() > 5 && numberOfMatchedStations() >= 2 && innerTrack().hitPattern().numberOfValidPixelHits() > 0 && abs(eta) < 2.4"

    # Rest of the cuts should be applied in the TagProbeFitTreeAnalyzer
    # with efficiency cuts for the ID efficiency
    # or via Binning for Trigger Efficiency:
    # d0_v = cms.vdouble(-0.02, 0.02),
    # dz_v = cms.vdouble(-0.5, 0.5),
    # drjet = cms.vdouble(0.3, 7),
    # pfreliso = cms.vdouble(0., 0.12),
    # absdeltapt = cms.vdouble(-10000., 5.0),
    
    # All 2012 Triggers - SingleMu (+ DoubleMu):
    # HLT_Mu5
    #  HLT_Mu8
    # HLT_Mu12
    # HLT_Mu15_eta2p1
    #  HLT_Mu17
    # HLT_Mu24
    # HLT_Mu24_eta2p1
    # HLT_Mu30
    # HLT_Mu30_eta2p1
    # HLT_Mu40
    # HLT_Mu40_eta2p1
    # HLT_Mu50_eta2p1
    # HLT_IsoMu20_eta2p1
    # HLT_IsoMu24
    # HLT_IsoMu24_eta2p1
    # HLT_IsoMu30
    # HLT_IsoMu30_eta2p1
    # HLT_IsoMu34_eta2p1
    # HLT_IsoMu40_eta2p1

    # 2012 Cross Triggers - MuHad:
    # HLT_Mu40_HT200 (7e33 only)
    # HLT_Mu40_FJHT200
    # HLT_Mu40_PFHT350
    # HLT_Mu40_PFNoPUHT350
    # HLT_Mu60_PFHT350
    # HLT_Mu60_PFNoPUHT350
    # HLT_PFHT350_Mu15_PFMET45
    # HLT_PFNoPUHT350_Mu15_PFMET45
    # HLT_PFHT350_Mu15_PFMET50
    # HLT_PFNoPUHT350_Mu15_PFMET50
    # HLT_PFHT400_Mu5_PFMET45
    # HLT_PFNoPUHT400_Mu5_PFMET45
    # HLT_PFHT400_Mu5_PFMET50
    # HLT_PFNoPUHT400_Mu5_PFMET50

    # MATCHED Any --> Csak az IsoMu24_eta2p1
    # Configban -> Csak IsoMu24_eta2p1

    # 2011 Triggers
    PASS_HLT15="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_Mu15_v*",);
    PASS_HLT8="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_Mu8_v*",);
    MATCHED_Mu8_HT200="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu8_HT200_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT50L3MuFiltered8').empty()"
    MATCHED_Mu15_HT200="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu15_HT200_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT50L3MuFiltered15').empty()"
    MATCHED_Mu30_HT200="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu30_HT200_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT50L3MuFiltered30').empty()"
    MATCHED_Mu40_HT200="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_HT200_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT50L3MuFiltered40').empty()"
    MATCHED_Mu40_HT300="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_HT300_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT50L2QualL3MuFiltered40').empty()"
    MATCHED_HT250_Mu15_PFMHT20="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_HT250_Mu15_PFMHT20_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT100singleMuL3PreFiltered15').empty()"
    MATCHED_HT250_Mu15_PFMHT40="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_HT250_Mu15_PFMHT40_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT100singleMuL3PreFiltered15').empty()"
    MATCHED_HT300_Mu15_PFMHT40="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_HT300_Mu15_PFMHT40_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT100singleMuL3PreFiltered15').empty()"
    # 2012 Triggers
    PASS_Mu5                    ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_Mu5_v*",);
    PASS_Mu12                   ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_Mu12_v*",);
    PASS_Mu24                   ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_Mu24_v*",);
    PASS_IsoMu24                ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu24_v*",);
    PASS_IsoMu30                ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu30_v*",);
    PASS_IsoMu15_eta2p1_L1ETM20 ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu15_eta2p1_L1ETM20_v*",);
    PASS_IsoMu20_eta2p1         ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu20_eta2p1_v*",);
    PASS_IsoMu24_eta2p1         ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu24_eta2p1_v*",);
    PASS_IsoMu30_eta2p1         ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu30_eta2p1_v*",);
    PASS_IsoMu34_eta2p1         ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu34_eta2p1_v*",);
    PASS_IsoMu40_eta2p1         ="!triggerObjectMatchesByPath('%s',1,0).empty()" % ("HLT_IsoMu40_eta2p1_v*",);
    
    MATCHED_IsoMu24                ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu24_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15').empty()"
    MATCHED_IsoMu30                ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu30_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16L1f0L2f16QL3f30QL3crIsoRhoFiltered0p15').empty()"    
    MATCHED_IsoMu15_eta2p1_L1ETM20 ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu15_eta2p1_L1ETM20_v*',0,0).empty() && (!triggerObjectMatchesByFilter('hltL3crIsoL1sMu12Eta2p1L1f0L2f12QL3f15QL3crIsoFiltered10').empty() || !triggerObjectMatchesByFilter('hltL3crIsoL1sMu12Eta2p1L1f0L2f12QL3f15QL3crIsoRhoFiltered0p15').empty())"
    MATCHED_IsoMu20_eta2p1         ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu20_eta2p1_v*',0,0).empty() && (!triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoFiltered10').empty() || !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoRhoFiltered0p15').empty())"
    MATCHED_IsoMu24_eta2p1         ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',0,0).empty() && (!triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10').empty() || !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15').empty())"
    MATCHED_IsoMu24_eta2p1_5e33    ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10').empty()"
    MATCHED_IsoMu24_eta2p1_7e33    ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15').empty()"
    MATCHED_IsoMu30_eta2p1         ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu30_eta2p1_v*',0,0).empty() && (!triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoFiltered10').empty() || !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoRhoFiltered0p15').empty())"
    MATCHED_IsoMu34_eta2p1         ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu34_eta2p1_v*',0,0).empty() && (!triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoFiltered10').empty() || !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoRhoFiltered0p15').empty())"
    MATCHED_IsoMu40_eta2p1         ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_IsoMu40_eta2p1_v*',0,0).empty() && (!triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoFiltered10').empty() || !triggerObjectMatchesByFilter('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoRhoFiltered0p15').empty())"
    #MATCHED_Mu8                    ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu8_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu3L3Filtered8').empty()"
    #MATCHED_Mu17                   ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu17_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu12L3Filtered17').empty()"
    #MATCHED_Mu30                   ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu30_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu16L1f0L2f16QL3Filtered30Q').empty()"
    #MATCHED_Mu40                   ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu16L1f0L2f16QL3Filtered40Q').empty()"
    #MATCHED_Mu15_eta2p1            ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu15_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu7L1fEta2p1L2fEta2p1f7L3FilteredEta2p1Filtered15').empty()"
    #MATCHED_Mu24_eta2p1            ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu24_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q').empty()"
    #MATCHED_Mu30_eta2p1            ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu30_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered30Q').empty()"
    #MATCHED_Mu40_eta2p1            ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q').empty()"
    #MATCHED_Mu50_eta2p1            ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu50_eta2p1_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered50Q').empty()"
    
    MATCHED_Mu40_HT200_Run2012="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_HT200_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40').empty()"
    MATCHED_Mu40_FJHT200="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_FJHT200_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40').empty()"
    MATCHED_Mu40_PFHT350="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_PFHT350_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40').empty()"
    MATCHED_Mu40_PFNoPUHT350="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu40_PFNoPUHT350_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered40').empty()"
    MATCHED_Mu60_PFHT350="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu60_PFHT350_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered60').empty()"
    MATCHED_Mu60_PFNoPUHT350="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_Mu60_PFNoPUHT350_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1Mu0HTT100ORL1Mu4HTT125L2QualL3MuFiltered60').empty()"
    MATCHED_PFHT350_Mu15_PFMET45="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFHT350_Mu15_PFMET45_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered15').empty()"
    MATCHED_PFNoPUHT350_Mu15_PFMET45="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFNoPUHT350_Mu15_PFMET45_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered15').empty()"
    MATCHED_PFHT350_Mu15_PFMET50="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFHT350_Mu15_PFMET50_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered15').empty()"
    MATCHED_PFNoPUHT350_Mu15_PFMET50="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFNoPUHT350_Mu15_PFMET50_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered15').empty()"
    MATCHED_PFHT400_Mu5_PFMET45="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFHT400_Mu5_PFMET45_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered5').empty()"
    MATCHED_PFNoPUHT400_Mu5_PFMET45 ="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFNoPUHT400_Mu5_PFMET45_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered5').empty()"
    MATCHED_PFHT400_Mu5_PFMET50="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFHT400_Mu5_PFMET50_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered5').empty()"
    MATCHED_PFNoPUHT400_Mu5_PFMET50="!triggerObjectMatchesByType('TriggerMuon').empty() && !triggerObjectMatchesByPath('HLT_PFNoPUHT400_Mu5_PFMET50_v*',0,0).empty() && !triggerObjectMatchesByFilter('hltL1HTT150singleMuL3PreFiltered5').empty()"

    MATCHED_ANY  = "(" + "(" + PASS_HLT15 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_HLT8 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu8_HT200 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu15_HT200 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu30_HT200 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu40_HT200 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu40_HT300 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_HT250_Mu15_PFMHT20 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_HT250_Mu15_PFMHT40 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_HT300_Mu15_PFMHT40 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_Mu5 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_Mu12 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_Mu24 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu24 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu30 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu15_eta2p1_L1ETM20 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu20_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu24_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu30_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu34_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + PASS_IsoMu40_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu24 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu30 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu15_eta2p1_L1ETM20 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu20_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu24_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu30_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu34_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_IsoMu40_eta2p1 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu40_HT200_Run2012 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu40_FJHT200 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu40_PFHT350 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu40_PFNoPUHT350 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu60_PFHT350 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_Mu60_PFNoPUHT350 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFHT350_Mu15_PFMET45 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFNoPUHT350_Mu15_PFMET45 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFHT350_Mu15_PFMET50 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFNoPUHT350_Mu15_PFMET50 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFHT400_Mu5_PFMET45 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFNoPUHT400_Mu5_PFMET45 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFHT400_Mu5_PFMET50 + ")"
    MATCHED_ANY += "||"+ "(" + MATCHED_PFNoPUHT400_Mu5_PFMET50  + ")" + ")"
    
    # 2011 Triggers
    PASS_ANY = "(!triggerObjectMatchesByPath('HLT_Mu8_v*'           ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu15_v*'          ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu20_v*'          ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu24_v*'          ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu24_eta2p1_v*'   ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu30_v*'          ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu30_eta2p1_v*'   ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu40_v*'          ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu40_eta2p1_v*'   ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu15_v*'       ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu17_v*'       ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu20_v*'       ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu24_v*'       ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu30_v*'       ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu30_eta2p1_v*',1,0).empty() || "
    # 2012 Triggers
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu5_v*'           ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu15_eta2p1_v*'   ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu17_v*'          ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu24_v*'          ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu24_eta2p1_v*'   ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu30_v*'          ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu30_eta2p1_v*'   ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu40_v*'          ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu40_eta2p1_v*'   ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_Mu50_eta2p1_v*'   ,1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu15_eta2p1_L1ETM20_v*',1,0).empty() || "
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu20_eta2p1_v*',1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu24_v*'       ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu30_v*'       ,1,0).empty() || "
    #PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu30_eta2p1_v*',1,0).empty() ||"
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu34_eta2p1_v*',1,0).empty() ||"
    PASS_ANY += "!triggerObjectMatchesByPath('HLT_IsoMu40_eta2p1_v*',1,0).empty() )"

    HighPtTriggerFlags = cms.PSet(
        # 2011 Triggers
        Mu15                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu15_v*'          ,1,0).empty()"),
        Mu20                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu20_v*'          ,1,0).empty()"),
        Mu24                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu24_v*'          ,1,0).empty()"),
        Mu24_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu24_eta2p1_v*'   ,1,0).empty()"),
        Mu30                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu30_v*'          ,1,0).empty()"),
        Mu30_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu30_eta2p1_v*'   ,1,0).empty()"),
        Mu40                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu40_v*'          ,1,0).empty()"),
        Mu40_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu40_eta2p1_v*'   ,1,0).empty()"),
        IsoMu15                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu15_v*'       ,1,0).empty()"),
        IsoMu15_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu15_eta2p1_v*',1,0).empty()"),
        IsoMu17                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu17_v*'       ,1,0).empty()"),
        IsoMu20                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu20_v*'       ,1,0).empty()"),
        IsoMu24                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_v*'       ,1,0).empty()"),
        IsoMu24_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty()"),
        IsoMu30                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu30_v*'       ,1,0).empty()"),
        IsoMu30_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu30_eta2p1_v*',1,0).empty()"),
        IsoMu24orIsoMu24_eta2p1            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty() || !triggerObjectMatchesByPath('HLT_IsoMu24_v*',1,0).empty()"),
        IsoMu17orIsoMu24orIsoMu24_eta2p1   = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu17_v*'       ,1,0).empty() || !triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty() || !triggerObjectMatchesByPath('HLT_IsoMu24_v*',1,0).empty()"),
        # 2012 Only Triggers
        Mu12                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu12_v*'          ,1,0).empty()"),
        Mu15_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu15_eta2p1_v*'   ,1,0).empty()"),
        Mu17                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu17_v*'          ,1,0).empty()"),
        #Mu24                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu24_v*'          ,1,0).empty()"),
        #Mu24_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu24_eta2p1_v*'   ,1,0).empty()"),
        #Mu30                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu30_v*'          ,1,0).empty()"),
        #Mu30_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu30_eta2p1_v*'   ,1,0).empty()"),
        #Mu40                               = cms.string("!triggerObjectMatchesByPath('HLT_Mu40_v*'          ,1,0).empty()"),
        #Mu40_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu40_eta2p1_v*'   ,1,0).empty()"),
        Mu50_eta2p1                        = cms.string("!triggerObjectMatchesByPath('HLT_Mu50_eta2p1_v*'   ,1,0).empty()"),
        IsoMu15_eta2p1_L1ETM20             = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu15_eta2p1_L1ETM20_v*',1,0).empty()"),
        IsoMu20_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu20_eta2p1_v*',1,0).empty()"),
        #IsoMu24                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_v*'       ,1,0).empty()"),
        #IsoMu24_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu24_eta2p1_v*',1,0).empty()"),
        #IsoMu30                            = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu30_v*'       ,1,0).empty()"),
        #IsoMu30_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu30_eta2p1_v*',1,0).empty()"),
        IsoMu34_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu34_eta2p1_v*',1,0).empty()"),
        IsoMu40_eta2p1                     = cms.string("!triggerObjectMatchesByPath('HLT_IsoMu40_eta2p1_v*',1,0).empty()"),
    ) 
   
   #JET_CUT =  "pt() >= 40.0 && abs(eta()) <= 2.4 && neutralHadronEnergyFraction() < 0.99 && neutralEmEnergyFraction() < 0.99 && getPFConstituents().size() > 1 && chargedHadronEnergyFraction() > 0  && chargedMultiplicity() > 0  && chargedEmEnergyFraction() < 0.99"
    JET_CUT =  "pt() >= 40.0 && abs(eta()) <= 2.4 && neutralHadronEnergyFraction() < 0.99 && neutralEmEnergyFraction() < 0.99 && chargedHadronEnergyFraction() > 0  && chargedMultiplicity() > 0  && chargedEmEnergyFraction() < 0.99 && (chargedMultiplicity() + neutralMultiplicity() + muonMultiplicity()) > 1"

    ################################################################################################################################

#   ___ ____ ____ ____ 
#    |  |__| | __ [__  
#    |  |  | |__] ___] 
                   
    process.tagMuons = cms.EDFilter("PATMuonRefSelector",
        src = cms.InputTag("cleanPatMuonsTriggerMatch"),
        cut = cms.string("pt > 10 && " + TAG_CUTS + " && ("+ PASS_ANY +")"), 
    )
    
    process.tagMuonsHLT = cms.EDFilter("PATMuonRefSelector",
        src = cms.InputTag("cleanPatMuonsTriggerMatch"),
        #cut = cms.string("pt > 10 && " + TAG_CUTS + " && (" + PASS_HLT15 + " || " + PASS_HLT8 + " || " + MATCHED_HT250_Mu15_PFMHT20 + " || " + MATCHED_HT250_Mu15_PFMHT40 + " || " + MATCHED_HT300_Mu15_PFMHT40 + ")"),
        cut = cms.string("pt > 10 && " + TAG_CUTS + " && " + MATCHED_ANY),
    )
    ################################################################################################################################

#   ___  ____ ____ ___  ____ ____ 
#   |__] |__/ |  | |__] |___ [__  
#   |    |  \ |__| |__] |___ ___] 
                         
    # probe1: standalone muon probes
    process.staTracks = cms.EDProducer("TrackViewCandidateProducer", 
        src  = cms.InputTag("standAloneMuons","UpdatedAtVtx"), 
        particleType = cms.string("mu+"),
        cut = cms.string(""),
    )
    process.staProbes = cms.EDFilter("RecoChargedCandidateRefSelector",
        src = cms.InputTag("staTracks"),
        cut = cms.string("pt > 5 && abs(eta) < 2.4"),
    )

    # probe2: tracker muon probes
    process.tkTracks = cms.EDProducer("TrackViewCandidateProducer",
        src = cms.InputTag("generalTracks"),
        particleType = cms.string('mu+'),
        cut = cms.string("pt > 5 && abs(eta) < 2.4 && numberOfValidHits > 5"),
    )
    process.tkProbes = cms.EDFilter("RecoChargedCandidateRefSelector",
        src = cms.InputTag("tkTracks"),
        cut = cms.string("")
    )
    process.matchedGlbMuons = cms.EDFilter("PATMuonRefSelector",
        src = cms.InputTag("cleanPatMuonsTriggerMatch"),
        #cut = cms.string("isGood('GlobalMuonPromptTight') && isGood('AllTrackerMuons')  && globalTrack().hitPattern().numberOfValidTrackerHits() >= 11 && numberOfMatches() >= 2 && innerTrack().hitPattern().pixelLayersWithMeasurement() >= 1 &&   pt > 5 && abs(eta) < 2.4"),
        cut = cms.string(RA4_MUON_ID_CUTS_NONCOMPREHENSIVE),
    )

    ################################################################################################################################

#   _  _ ____ ___ ____ _  _    ____ _  _ ___     ___  ____ ____ ____ 
#   |\/| |__|  |  |    |__|    |__| |\ | |  \    |__] |__| [__  [__  
#   |  | |  |  |  |___ |  |    |  | | \| |__/    |    |  | ___] ___] 

    # passing1: standalone muons passing tracker muons
        # matching1: standalone muons to tracker muons
    process.staToTkMatch = cms.EDProducer("MatcherUsingTracks",
        src     = cms.InputTag("staTracks"), # all standalone muons
        matched = cms.InputTag("tkTracks"),  # to all tk tracks
        algorithm = cms.string("byDirectComparison"), # using parameters at PCA
        srcTrack = cms.string("tracker"),  # 'staTracks' is a 'RecoChargedCandidate', so it thinks
        srcState = cms.string("atVertex"), # it has a 'tracker' track, not a standalone one
        matchedTrack = cms.string("tracker"),
        matchedState = cms.string("atVertex"),
        maxDeltaR        = cms.double(1.),   # large range in DR
        maxDeltaEta      = cms.double(0.2),  # small in eta, which is more precise
        maxDeltaLocalPos = cms.double(100),
        maxDeltaPtRel    = cms.double(3),
        sortBy           = cms.string("deltaR"),
    )

        # passing
    process.staPassingTk = cms.EDProducer("MatchedCandidateSelector",
        src   = cms.InputTag("staProbes"),
        match = cms.InputTag("staToTkMatch"),
    )

    # passing2: tracker muons passing global muons
        # matching2: tracker muons to global muons
    process.tkToGlbMatch = cms.EDProducer("MatcherUsingTracksMatchInfo",
        src     = cms.InputTag("tkTracks"),
        matched = cms.InputTag("matchedGlbMuons"),
        algorithm = cms.string("byDirectComparison"), 
        srcTrack = cms.string("tracker"),             
        srcState = cms.string("atVertex"),            
        matchedTrack = cms.string("tracker"),         
        matchedState = cms.string("atVertex"),        
        maxDeltaR        = cms.double(0.01),  
        maxDeltaLocalPos = cms.double(0.01),  
        maxDeltaPtRel    = cms.double(0.01),
        sortBy           = cms.string("deltaR"),
    )
        # passing
    process.tkPassingGlb = cms.EDProducer("MatchedCandidateSelector",
        src   = cms.InputTag("tkProbes"),
        match = cms.InputTag("tkToGlbMatch"),
    )

    # passing3: global muons passing HLT
        # passing:
#    process.glbPassingHLTMu15 = cms.EDFilter("PATMuonRefSelector",
#        src = cms.InputTag("matchedGlbMuons"),
#        cut = cms.string(PASS_HLT15),
#    )
    ################################################################################################################################

#   ___ ____ ____    _  _    ___  ____ ____ ___  ____    ___  ____ _ ____ ____ 
#    |  |__| | __    |\ |    |__] |__/ |  | |__] |___    |__] |__| | |__/ [__  
#    |  |  | |__]    | \|    |    |  \ |__| |__] |___    |    |  | | |  \ ___] 

    # T&P Pair1: globalmuons & standalone muons 
    process.tpGlbSta = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("tagMuons@+ staProbes@-"), # charge coniugate states are implied
        cut   = cms.string("40 < mass < 140"),
    )

    # T&P Pair2: global muons & tracker muons
    process.tpGlbTk = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("tagMuons@+ tkProbes@-"), # charge coniugate states are implied
        cut   = cms.string("50 < mass < 130"),
    )

    # T&P Pair3: global muons & global muons
    process.tpGlbGlb = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string("tagMuonsHLT@+ matchedGlbMuons@-"), # charge coniugate states are implied
        cut   = cms.string("50 < mass < 130"),
    )
    ################################################################################################################################

#   _  _ ____    _  _ ____ ___ ____ _  _ ____ ____ 
#   |\/| |       |\/| |__|  |  |    |__| |___ [__  
#   |  | |___    |  | |  |  |  |___ |  | |___ ___] 
                                               
    if mcInfo:
        # MC muon matches
        process.muMcMatch = cms.EDProducer("MCTruthDeltaRMatcherNew",
            pdgId = cms.vint32(13),
            src = cms.InputTag("cleanPatMuonsTriggerMatch"),
            distMin = cms.double(0.3),
            matched = cms.InputTag("genParticles")
        )
        # MC tracker muon matches & standalone muon matches
        process.tkMcMatch  = process.muMcMatch.clone(src = "tkTracks")
        process.staMcMatch = process.muMcMatch.clone(src = "staTracks", distMin = 0.6)

    ################################################################################################################################

#   T R I G G E R   P A S S E S

    # 2011 Triggers

    process.flagPassHLTMu8HT200 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu8_HT200_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTMu15HT200 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu15_HT200_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTMu30HT200 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu30_HT200_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTMu40HT200 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu40_HT200_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTMu40HT300 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu40_HT300_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTHT250Mu15PFMHT20 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_HT250_Mu15_PFMHT20_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTHT250Mu15PFMHT40 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_HT250_Mu15_PFMHT40_v.*"),
        andOr = cms.bool(True)
    )
    
    
    process.flagPassHLTHT300Mu15PFMHT40 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_HT300_Mu15_PFMHT40_v.*"),
        andOr = cms.bool(True)
    )

    # 2012 Triggers
    process.flagPassHLTIsoMu24 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu24_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu30 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu30_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu15eta2p1L1ETM20 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu15_eta2p1_L1ETM20_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu20eta2p1 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu20_eta2p1_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu24eta2p1 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu24_eta2p1_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu30eta2p1 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu30_eta2p1_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu34eta2p1 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu34_eta2p1_v.*"),
        andOr = cms.bool(True)
    )
    process.flagPassHLTIsoMu40eta2p1 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_IsoMu40_eta2p1_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTMu8HT200 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu8_HT200_v.*"),
        andOr = cms.bool(True)
    )

    #process.flagPassHLTMu40HT200 = cms.EDProducer("HLTResultProducer",
    #    probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
    #    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    #    HLTPaths = cms.vstring("HLT_Mu40_HT200_v.*"),
    #    andOr = cms.bool(True)
    #)

    process.flagPassHLTMu40FJHT200 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu40_FJHT200_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTMu40PFHT350 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu40_PFHT350_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTMu40PFNoPUHT350 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu40_PFNoPUHT350_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTMu60PFHT350 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu60_PFHT350_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTMu60PFNoPUHT350 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_Mu60_PFNoPUHT350_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFHT350Mu15PFMET45 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFHT350_Mu15_PFMET45_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFNoPUHT350Mu15PFMET45 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFNoPUHT350_Mu15_PFMET45_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFHT350Mu15PFMET50 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFHT350_Mu15_PFMET50_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFNoPUHT350Mu15PFMET50 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFNoPUHT350_Mu15_PFMET50_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFHT400Mu5PFMET45 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFHT400_Mu5_PFMET45_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFNoPUHT400Mu5PFMET45 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFNoPUHT400_Mu5_PFMET45_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFHT400Mu5PFMET50 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFHT400_Mu5_PFMET50_v.*"),
        andOr = cms.bool(True)
    )

    process.flagPassHLTPFNoPUHT400Mu5PFMET50 = cms.EDProducer("HLTResultProducer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
        HLTPaths = cms.vstring("HLT_PFNoPUHT400_Mu5_PFMET50_v.*"),
        andOr = cms.bool(True)
    )

    ################################################################################################################################
    
    #   M E T
    process.glbMet = cms.EDProducer("PatMetAssociator",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        metTag = cms.InputTag("patMETsPF"),
    )
    
    ###############################################################################################################################
    
    #   S T
    process.stComp = cms.EDProducer("PatMetSTComputer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        metTag = cms.InputTag("patMETsPF"),
    )

    ################################################################################################################################

#   _ _  _ ___  ____ ____ ___    ___  ____ ____ ____ _  _ ____ ___ ____ ____ 
#   | |\/| |__] |__| |     |     |__] |__| |__/ |__| |\/| |___  |  |___ |__/ 
#   | |  | |    |  | |___  |     |    |  | |  \ |  | |  | |___  |  |___ |  \ 
                                                                         
   
    process.trkImpactParameter = cms.EDProducer("ChargedCandidateImpactParameter",
        probes = cms.InputTag("tkTracks"),
    )
    
    process.staImpactParameter = cms.EDProducer("ChargedCandidateImpactParameter",
        probes = cms.InputTag("staTracks"),
    )
 
    process.glbImpactParameter = cms.EDProducer("PatMuonImpactParameter",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
    )
 
    ################################################################################################################################

#    _ ____ ___ ____ 
#    | |___  |  [__  
#   _| |___  |  ___] 
                 
   
    
    process.selectedJets = cms.EDFilter("PATJetSelector",
        src = cms.InputTag("cleanPatJetsAK5PF"),
        cut = cms.string( JET_CUT ), # <= anpassen
    )

    # jets - tracker
    process.trkdRToNearestJet = cms.EDProducer("minCutDeltaRNearestPatJetComputer",
        probes = cms.InputTag("tkTracks"),
        objects = cms.InputTag("selectedJets"),
        minDeltaR = cms.double(0.1),
        objectSelection = cms.InputTag(""),
    )
    process.trkJetMultiplicity = cms.EDProducer("PatJetMultiplicityCounter",
        probes = cms.InputTag("tkTracks"),
        objects = cms.InputTag("selectedJets"),
        minDeltaR = cms.double(0.1),
        objectSelection = cms.InputTag(""),
    )
    process.trkHT = cms.EDProducer("PatJetHTComputer",
        probes = cms.InputTag("tkTracks"),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )
    

    # jets - standalone
    process.stadRToNearestJet = cms.EDProducer("minCutDeltaRNearestPatJetComputer",
        probes = cms.InputTag("staTracks"),
        objects = cms.InputTag("selectedJets"),
        minDeltaR = cms.double(0.1),
        objectSelection = cms.InputTag(""),
    )
    process.staJetMultiplicity = cms.EDProducer("PatJetMultiplicityCounter",
        probes = cms.InputTag("staTracks"),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )
    process.staHT = cms.EDProducer("PatJetHTComputer",
        probes = cms.InputTag("staTracks"),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )
    
    
    # jets - global
    process.glbdRToNearestJet = cms.EDProducer("minCutDeltaRNearestPatJetComputer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        objects = cms.InputTag("selectedJets"),
        minDeltaR = cms.double(0.1),
        objectSelection = cms.InputTag(""),
    )
    process.glbJetMultiplicity = cms.EDProducer("PatJetMultiplicityCounter",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )
    process.glbHT = cms.EDProducer("PatJetHTComputer",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        objects = cms.InputTag("selectedJets"),
        objectSelection = cms.InputTag(""),
    )

    ################################################################################################################################

    #Delta Reco-PF Muon Pt

    process.deltaPfRecoPt = cms.EDProducer("MuonDeltaPfRecoPt",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
    )
    
    ################################################################################################################################

    #VERTICES:
    
    process.nverticesModule = cms.EDProducer("VertexMultiplicityCounter",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        objects = cms.InputTag("offlinePrimaryVertices"),
        objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
    )

    #########################################################################################
    ##        Deterministic Annealing vertices (100um distance; 4.2.X config)              ##
    #########################################################################################
    process.offlinePrimaryVerticesDA100um = cms.EDProducer("PrimaryVertexProducer",
        verbose = cms.untracked.bool(False),
        algorithm = cms.string('AdaptiveVertexFitter'),
        TrackLabel = cms.InputTag("generalTracks"),
        useBeamConstraint = cms.bool(False),
        beamSpotLabel = cms.InputTag("offlineBeamSpot"),
        minNdof  = cms.double(0.0),
        PVSelParameters = cms.PSet(
            #maxDistanceToBeam = cms.double(0.5)
            maxDistanceToBeam = cms.double(1.0)
        ),
        TkFilterParameters = cms.PSet(
            algorithm=cms.string('filter'),
            maxNormalizedChi2 = cms.double(20.0),
            minPixelLayersWithHits=cms.int32(2),
            minSiliconLayersWithHits = cms.int32(5),
            maxD0Significance = cms.double(5.0),
            minPt = cms.double(0.0),
            trackQuality = cms.string("any")
        ),

        TkClusParameters = cms.PSet(
            algorithm   = cms.string("DA"),
            TkDAClusParameters = cms.PSet(
                coolingFactor = cms.double(0.6),  #  moderate annealing speed
                Tmin = cms.double(4.),            #  end of annealing
                vertexSize = cms.double(0.01),    #  ~ resolution / sqrt(Tmin)
                d0CutOff = cms.double(3.),        # downweight high IP tracks 
                dzCutOff = cms.double(4.)         # outlier rejection after freeze-out (T<Tmin)
            )
        )
    )
    process.nverticesDAModule = cms.EDProducer("VertexMultiplicityCounter",
        probes = cms.InputTag("cleanPatMuonsTriggerMatch"),
        objects = cms.InputTag("offlinePrimaryVerticesDA100um"),
        #objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
        objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
    )


    ################################################################################################################################
    
#   _ ____ ____ _    ____ ___ _ ____ _  _ ____ 
#   | [__  |  | |    |__|  |  | |  | |\ | [__  
#   | ___] |__| |___ |  |  |  | |__| | \| ___] 
                                            
    
    from RecoMuon.MuonIsolationProducers.trackExtractorBlocks_cff import MIsoTrackExtractorBlock
    process.trkIsoDepositTk = cms.EDProducer("CandIsoDepositProducer",
        src = cms.InputTag("tkTracks"),
        MultipleDepositsFlag = cms.bool(False),
        trackType = cms.string('best'),
        ExtractorPSet = cms.PSet(
            MIsoTrackExtractorBlock
        )
    )
    from RecoMuon.MuonIsolationProducers.caloExtractorByAssociatorBlocks_cff import MIsoCaloExtractorByAssociatorTowersBlock
    process.trkIsoDepositCalByAssociatorTowers = cms.EDProducer("CandIsoDepositProducer",
        src = cms.InputTag("tkTracks"),
        MultipleDepositsFlag = cms.bool(True),
        trackType = cms.string('best'),
        ExtractorPSet = cms.PSet(
            MIsoCaloExtractorByAssociatorTowersBlock
        )
    )

    process.TrackIsolationForTrk = cms.EDProducer("IsolationProducerForTracks",
        highPtTracks = cms.InputTag("tkTracks"),
        tracks = cms.InputTag("tkTracks"),
        isoDeps = cms.InputTag("trkIsoDepositTk"),
        coneSize = cms.double(0.3),
        trackPtMin = cms.double(3.0)
    )
    
    process.TrackIsolationForTrk04 = process.TrackIsolationForTrk.clone(coneSize = cms.double(0.4))

    process.EcalIsolationForTrk = cms.EDProducer("IsolationProducerForTracks",
        highPtTracks = cms.InputTag("tkTracks"),
        tracks = cms.InputTag("tkTracks"),
        isoDeps = cms.InputTag("trkIsoDepositCalByAssociatorTowers","ecal"),
        coneSize = cms.double(0.3),
        trackPtMin = cms.double(3.0)
    )

    process.EcalIsolationForTrk04                 = process.EcalIsolationForTrk.clone(coneSize = cms.double(0.4))

    process.HcalIsolationForTrk = cms.EDProducer("IsolationProducerForTracks",
        highPtTracks = cms.InputTag("tkTracks"),
        tracks = cms.InputTag("tkTracks"),
        isoDeps = cms.InputTag("trkIsoDepositCalByAssociatorTowers","hcal"),
        coneSize = cms.double(0.3),
        trackPtMin = cms.double(3.0)
    )

    process.HcalIsolationForTrk04               = process.HcalIsolationForTrk.clone(coneSize = cms.double(0.4) )

    process.RelIsolationForTrk = cms.EDProducer("RelIsolationProducerForTracks",
        highPtTracks = cms.InputTag("tkTracks"),
        tracks = cms.InputTag("tkTracks"),
        trkisoDeps = cms.InputTag("trkIsoDepositTk"),
        ecalisoDeps = cms.InputTag("trkIsoDepositCalByAssociatorTowers","ecal"),
        hcalisoDeps = cms.InputTag("trkIsoDepositCalByAssociatorTowers","hcal"),
        coneSize = cms.double(0.3),
        trackPtMin = cms.double(3.0)
    )
  
    process.RelIsolationForTrk04                = process.RelIsolationForTrk.clone(coneSize=cms.double(0.4))

    process.staIsoDepositTk                     = process.trkIsoDepositTk.clone( src = cms.InputTag("staTracks") )
    process.staIsoDepositCalByAssociatorTowers  = process.trkIsoDepositCalByAssociatorTowers.clone( src = cms.InputTag("staTracks") )
    process.TrackIsolationForStA                = process.TrackIsolationForTrk.clone( highPtTacks = cms.InputTag("staTracks") )
    process.EcalIsolationForStA                 = process.EcalIsolationForTrk.clone( highPtTacks = cms.InputTag("staTracks") )
    process.HcalIsolationForStA                 = process.HcalIsolationForTrk.clone( highPtTacks = cms.InputTag("staTracks") )
    process.RelIsolationForStA                  = process.RelIsolationForTrk.clone( highPtTacks = cms.InputTag("staTracks") )
    
    process.TrackIsolationForStA.tracks = cms.InputTag("staTracks")
    process.EcalIsolationForStA.tracks = cms.InputTag("staTracks")
    process.HcalIsolationForStA.tracks = cms.InputTag("staTracks")
    process.RelIsolationForStA.tracks = cms.InputTag("staTracks")
    
    process.TrackIsolationForStA.isoDeps = cms.InputTag("staIsoDepositTk")
    process.EcalIsolationForStA.isoDeps = cms.InputTag("staIsoDepositCalByAssociatorTowers","ecal")
    process.HcalIsolationForStA.isoDeps = cms.InputTag("staIsoDepositCalByAssociatorTowers","hcal")
    process.RelIsolationForStA.trkisoDeps = cms.InputTag("staIsoDepositTk")
    
    process.RelIsolationForStA.ecalisoDeps = cms.InputTag("staIsoDepositCalByAssociatorTowers","ecal")
    process.RelIsolationForStA.hcalisoDeps = cms.InputTag("staIsoDepositCalByAssociatorTowers","hcal")
    
    process.TrackIsolationForStA04              = process.TrackIsolationForStA.clone( coneSize=cms.double(0.4) )
    process.EcalIsolationForStA04               = process.EcalIsolationForStA.clone( coneSize = cms.double(0.4) )
    process.HcalIsolationForStA04               = process.HcalIsolationForStA.clone( coneSize = cms.double(0.4) )
    process.RelIsolationForStA04                = process.RelIsolationForStA.clone( coneSize = cms.double(0.4) )
    ################################################################################################################################
   
#   ___  ____ ____ ____ _  _ ____ ___ ____ ____ ____ 
#   |__] |__| |__/ |__| |\/| |___  |  |___ |__/ [__  
#   |    |  | |  \ |  | |  | |___  |  |___ |  \ ___] 
                                                 

    commonStuff = cms.PSet(
        arbitration = cms.string("OneProbe"),
        addRunLumiInfo = cms.bool(True),
    )
    
    trackCommonStuff = cms.PSet(
        variables = cms.PSet(
            eta = cms.string("eta()"),
            abs_eta = cms.string("abs(eta())"),
            pt  = cms.string("pt()"),
            phi  = cms.string("phi()"),
            d0 = cms.string("track.d0()"),
            dz = cms.string("track.dz()"),
            trkiso  = cms.InputTag("TrackIsolationForTrk"),
            ecaliso = cms.InputTag("EcalIsolationForTrk"),
            hcaliso = cms.InputTag("HcalIsolationForTrk"),
            reliso = cms.InputTag("RelIsolationForTrk"),
            trkiso04  = cms.InputTag("TrackIsolationForTrk04"),
            ecaliso04 = cms.InputTag("EcalIsolationForTrk04"),
            hcaliso04 = cms.InputTag("HcalIsolationForTrk04"),
            reliso04 = cms.InputTag("RelIsolationForTrk04"),
            drjet = cms.InputTag("trkdRToNearestJet"),
            njet = cms.InputTag("trkJetMultiplicity"),
            d0_v = cms.InputTag("trkImpactParameter","d0v"),
            d0_b = cms.InputTag("trkImpactParameter","d0b"),
            dz_v = cms.InputTag("trkImpactParameter","dzv"),
            dz_b = cms.InputTag("trkImpactParameter","dzb"),
            ptErrorByPt2 = cms.InputTag("tkToGlbMatch", "ptErrByPt2"),
            pixlayer = cms.string("track.hitPattern().pixelLayersWithMeasurement()"),
            deltapt     = cms.InputTag("tkToGlbMatch", "deltaPtRecoPF"),
            absdeltapt  = cms.InputTag("tkToGlbMatch", "absdeltaPtRecoPF"),
            pfreliso    = cms.InputTag("tkToGlbMatch", "pfreliso"),
            ra4idcuts = cms.InputTag("tkToGlbMatch", "ra4idcuts"), #Not comprehensive
        ),
        flags = cms.PSet(
            passing = cms.InputTag("tkPassingGlb"),
        ),
        tagVariables = cms.PSet(
            ecaliso = cms.string("ecalIso()"),
            hcaliso = cms.string("hcalIso()"),
            reliso = cms.string("( trackIso() + ecalIso() + hcalIso() )/pt()"),
            trkiso  = cms.string("trackIso()"),
            nVertices   = cms.InputTag("nverticesModule"),
            nVerticesDA = cms.InputTag("nverticesDAModule"),
        ),
        tagFlags = cms.PSet(
            HighPtTriggerFlags, 
        ),
    )

    staCommonStuff = cms.PSet(
        variables = cms.PSet(
            eta = cms.string("eta()"),
            abs_eta = cms.string("abs(eta())"),
            pt  = cms.string("pt()"),
            phi  = cms.string("phi()"),
            d0 = cms.string("track.d0()"),
            dz = cms.string("track.dz()"),
            validhits = cms.string("track.numberOfValidHits()"),
            trkiso  = cms.InputTag("TrackIsolationForStA"),
            ecaliso = cms.InputTag("EcalIsolationForStA"),
            hcaliso = cms.InputTag("HcalIsolationForStA"),
            reliso = cms.InputTag("RelIsolationForStA"),
            trkiso04  = cms.InputTag("TrackIsolationForStA04"),
            ecaliso04 = cms.InputTag("EcalIsolationForStA04"),
            hcaliso04 = cms.InputTag("HcalIsolationForStA04"),
            reliso04 = cms.InputTag("RelIsolationForStA04"),
            drjet = cms.InputTag("stadRToNearestJet"),
            njet = cms.InputTag("staJetMultiplicity",),
            d0_v = cms.InputTag("staImpactParameter","d0v"),
            d0_b = cms.InputTag("staImpactParameter","d0b"),
            dz_v = cms.InputTag("staImpactParameter","dzv"),
            dz_b = cms.InputTag("staImpactParameter","dzb"),
        ),
        flags = cms.PSet(
            passing = cms.InputTag("staPassingTk"),
        ),
        tagVariables = cms.PSet(
            ecaliso = cms.string("ecalIso()"),
            hcaliso = cms.string("hcalIso()"),
            reliso = cms.string("( trackIso() + ecalIso() + hcalIso() )/pt()"),
            trkiso  = cms.string("trackIso()"),
            nVertices   = cms.InputTag("nverticesModule"),
            nVerticesDA = cms.InputTag("nverticesDAModule"),
        ),
        tagFlags = cms.PSet(
            HighPtTriggerFlags,
        ),
    )

    muonCommonStuff = cms.PSet(
        variables = cms.PSet(
            eta = cms.string("eta()"),
            abs_eta = cms.string("abs(eta())"),
            pt  = cms.string("pt()"),
            stlep = cms.InputTag("stComp"),
            phi  = cms.string("phi()"),
            d0 = cms.string("track.d0()"),
            dz = cms.string("track.dz()"),
            trkiso  = cms.string("trackIso()"),
            ecaliso = cms.string("ecalIso()"),
            hcaliso = cms.string("hcalIso()"),
            reliso = cms.string("( trackIso() + ecalIso() + hcalIso() )/pt()"),
            drjet = cms.InputTag("glbdRToNearestJet"),
            njet = cms.InputTag("glbJetMultiplicity"),
            d0_v = cms.InputTag("glbImpactParameter","d0v"),
            d0_b = cms.InputTag("glbImpactParameter","d0b"),
            dz_v = cms.InputTag("glbImpactParameter","dzv"),
            dz_b = cms.InputTag("glbImpactParameter","dzb"),
            pterror = cms.string("globalTrack().ptError()"),  
            validhits = cms.string("globalTrack().hitPattern().numberOfValidTrackerHits()"),
            validpixhits = cms.string("innerTrack.hitPattern().numberOfValidPixelHits()"),
            trklayer = cms.string("track.hitPattern().trackerLayersWithMeasurement()"),
            pixlayer = cms.string("track.hitPattern().pixelLayersWithMeasurement()"),
            nmatched = cms.string("numberOfMatchedStations()"),
            pfreliso = cms.string("(pfIsolationR03().sumChargedHadronPt + max(pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - pfIsolationR03().sumPUPt/2,0.0))/pt"),
            absdeltapt = cms.InputTag("deltaPfRecoPt","absdeltapt"),
        ),
        flags = cms.PSet(
            # 2011
            passingHLTMu15                      = cms.string(PASS_HLT15),
            passingHLTMu8                       = cms.string(PASS_HLT8),
            matchedHLT_Mu8_HT200                = cms.string(MATCHED_Mu8_HT200),
            matchedHLT_Mu15_HT200               = cms.string(MATCHED_Mu15_HT200),
            matchedHLT_Mu30_HT200               = cms.string(MATCHED_Mu30_HT200),
            matchedHLT_Mu40_HT200               = cms.string(MATCHED_Mu40_HT200),
            matchedHLT_Mu40_HT300               = cms.string(MATCHED_Mu40_HT300),
            matchedHLT_HT250_Mu15_PFMHT20       = cms.string(MATCHED_HT250_Mu15_PFMHT20),
            matchedHLT_HT250_Mu15_PFMHT40       = cms.string(MATCHED_HT250_Mu15_PFMHT40),
            matchedHLT_HT300_Mu15_PFMHT40       = cms.string(MATCHED_HT300_Mu15_PFMHT40),
            # 2012
            passingHLTMu5                       = cms.string(PASS_Mu5),
            passingHLTMu12                      = cms.string(PASS_Mu12),
            passingHLTMu24                      = cms.string(PASS_Mu24),
            passingHLTIsoMu24                   = cms.string(PASS_IsoMu24),
            passingHLTIsoMu30                   = cms.string(PASS_IsoMu30),
            passingHLTIsoMu15eta2p1L1ETM20      = cms.string(PASS_IsoMu15_eta2p1_L1ETM20),
            passingHLTIsoMu20eta2p1             = cms.string(PASS_IsoMu20_eta2p1),
            passingHLTIsoMu24eta2p1             = cms.string(PASS_IsoMu24_eta2p1),
            passingHLTIsoMu30eta2p1             = cms.string(PASS_IsoMu30_eta2p1),
            passingHLTIsoMu34eta2p1             = cms.string(PASS_IsoMu34_eta2p1),
            passingHLTIsoMu40eta2p1             = cms.string(PASS_IsoMu40_eta2p1),
            matchedHLT_IsoMu24                  = cms.string(MATCHED_IsoMu24),
            matchedHLT_IsoMu30                  = cms.string(MATCHED_IsoMu30),
            matchedHLT_IsoMu15_eta2p1_L1ETM20   = cms.string(MATCHED_IsoMu15_eta2p1_L1ETM20),
            matchedHLT_IsoMu20_eta2p1           = cms.string(MATCHED_IsoMu20_eta2p1),
            matchedHLT_IsoMu24_eta2p1           = cms.string(MATCHED_IsoMu24_eta2p1),
            matchedHLT_IsoMu24_eta2p1_5e33      = cms.string(MATCHED_IsoMu24_eta2p1_5e33),
            matchedHLT_IsoMu24_eta2p1_7e33      = cms.string(MATCHED_IsoMu24_eta2p1_7e33),
            matchedHLT_IsoMu30_eta2p1           = cms.string(MATCHED_IsoMu30_eta2p1),
            matchedHLT_IsoMu34_eta2p1           = cms.string(MATCHED_IsoMu34_eta2p1),
            matchedHLT_IsoMu40_eta2p1           = cms.string(MATCHED_IsoMu40_eta2p1),
            matchedHLT_Mu40_HT200_Run2012       = cms.string(MATCHED_Mu40_HT200_Run2012),
            matchedHLT_Mu40_FJHT200             = cms.string(MATCHED_Mu40_FJHT200),
            matchedHLT_Mu40_PFHT350             = cms.string(MATCHED_Mu40_PFHT350),
            matchedHLT_Mu40_PFNoPUHT350         = cms.string(MATCHED_Mu40_PFNoPUHT350),
            matchedHLT_Mu60_PFHT350             = cms.string(MATCHED_Mu60_PFHT350),
            matchedHLT_Mu60_PFNoPUHT350         = cms.string(MATCHED_Mu60_PFNoPUHT350),
            matchedHLT_PFHT350_Mu15_PFMET45     = cms.string(MATCHED_PFHT350_Mu15_PFMET45),
            matchedHLT_PFNoPUHT350_Mu15_PFMET45 = cms.string(MATCHED_PFNoPUHT350_Mu15_PFMET45),
            matchedHLT_PFHT350_Mu15_PFMET50     = cms.string(MATCHED_PFHT350_Mu15_PFMET50),
            matchedHLT_PFNoPUHT350_Mu15_PFMET50 = cms.string(MATCHED_PFNoPUHT350_Mu15_PFMET50),
            matchedHLT_PFHT400_Mu5_PFMET45      = cms.string(MATCHED_PFHT400_Mu5_PFMET45),
            matchedHLT_PFNoPUHT400_Mu5_PFMET45  = cms.string(MATCHED_PFNoPUHT400_Mu5_PFMET45), 
            matchedHLT_PFHT400_Mu5_PFMET50      = cms.string(MATCHED_PFHT400_Mu5_PFMET50),
            matchedHLT_PFNoPUHT400_Mu5_PFMET50  = cms.string(MATCHED_PFNoPUHT400_Mu5_PFMET50), 
        ),
        tagFlags= cms.PSet(
            HighPtTriggerFlags,
            # 2011
            passingHLTMu15                      = cms.string(PASS_HLT15),
            passingHLTMu8                       = cms.string(PASS_HLT8),
            matchedHLT_Mu8_HT200                = cms.string(MATCHED_Mu8_HT200),
            matchedHLT_Mu15_HT200               = cms.string(MATCHED_Mu15_HT200),
            matchedHLT_Mu30_HT200               = cms.string(MATCHED_Mu30_HT200),
            matchedHLT_Mu40_HT200               = cms.string(MATCHED_Mu40_HT200),
            matchedHLT_Mu40_HT300               = cms.string(MATCHED_Mu40_HT300),
            matchedHLT_HT250_Mu15_PFMHT20       = cms.string(MATCHED_HT250_Mu15_PFMHT20),
            matchedHLT_HT250_Mu15_PFMHT40       = cms.string(MATCHED_HT250_Mu15_PFMHT40),
            matchedHLT_HT300_Mu15_PFMHT40       = cms.string(MATCHED_HT300_Mu15_PFMHT40),
            # 2012
            passingHLTMu5                       = cms.string(PASS_Mu5),
            passingHLTMu12                      = cms.string(PASS_Mu12),
            passingHLTMu24                      = cms.string(PASS_Mu24),
            passingHLTIsoMu24                   = cms.string(PASS_IsoMu24),
            passingHLTIsoMu30                   = cms.string(PASS_IsoMu30),
            passingHLTIsoMu15eta2p1L1ETM20      = cms.string(PASS_IsoMu15_eta2p1_L1ETM20),
            passingHLTIsoMu20eta2p1             = cms.string(PASS_IsoMu20_eta2p1),
            passingHLTIsoMu24eta2p1             = cms.string(PASS_IsoMu24_eta2p1),
            passingHLTIsoMu30eta2p1             = cms.string(PASS_IsoMu30_eta2p1),
            passingHLTIsoMu34eta2p1             = cms.string(PASS_IsoMu34_eta2p1),
            passingHLTIsoMu40eta2p1             = cms.string(PASS_IsoMu40_eta2p1),
            matchedHLT_IsoMu24                  = cms.string(MATCHED_IsoMu24),
            matchedHLT_IsoMu30                  = cms.string(MATCHED_IsoMu30),
            matchedHLT_IsoMu15_eta2p1_L1ETM20   = cms.string(MATCHED_IsoMu15_eta2p1_L1ETM20),
            matchedHLT_IsoMu20_eta2p1           = cms.string(MATCHED_IsoMu20_eta2p1),
            matchedHLT_IsoMu24_eta2p1           = cms.string(MATCHED_IsoMu24_eta2p1),
            matchedHLT_IsoMu24_eta2p1_5e33      = cms.string(MATCHED_IsoMu24_eta2p1_5e33),
            matchedHLT_IsoMu24_eta2p1_7e33      = cms.string(MATCHED_IsoMu24_eta2p1_7e33),            
            matchedHLT_IsoMu30_eta2p1           = cms.string(MATCHED_IsoMu30_eta2p1),
            matchedHLT_IsoMu34_eta2p1           = cms.string(MATCHED_IsoMu34_eta2p1),
            matchedHLT_IsoMu40_eta2p1           = cms.string(MATCHED_IsoMu40_eta2p1),            
            matchedHLT_Mu40_HT200_Run2012       = cms.string(MATCHED_Mu40_HT200_Run2012),
            matchedHLT_Mu40_FJHT200             = cms.string(MATCHED_Mu40_FJHT200),
            matchedHLT_Mu40_PFHT350             = cms.string(MATCHED_Mu40_PFHT350),
            matchedHLT_Mu40_PFNoPUHT350         = cms.string(MATCHED_Mu40_PFNoPUHT350),
            matchedHLT_Mu60_PFHT350             = cms.string(MATCHED_Mu60_PFHT350),
            matchedHLT_Mu60_PFNoPUHT350         = cms.string(MATCHED_Mu60_PFNoPUHT350),
            matchedHLT_PFHT350_Mu15_PFMET45     = cms.string(MATCHED_PFHT350_Mu15_PFMET45),
            matchedHLT_PFNoPUHT350_Mu15_PFMET45 = cms.string(MATCHED_PFNoPUHT350_Mu15_PFMET45),
            matchedHLT_PFHT350_Mu15_PFMET50     = cms.string(MATCHED_PFHT350_Mu15_PFMET50),
            matchedHLT_PFNoPUHT350_Mu15_PFMET50 = cms.string(MATCHED_PFNoPUHT350_Mu15_PFMET50),
            matchedHLT_PFHT400_Mu5_PFMET45      = cms.string(MATCHED_PFHT400_Mu5_PFMET45),
            matchedHLT_PFNoPUHT400_Mu5_PFMET45  = cms.string(MATCHED_PFNoPUHT400_Mu5_PFMET45), 
            matchedHLT_PFHT400_Mu5_PFMET50      = cms.string(MATCHED_PFHT400_Mu5_PFMET50),
            matchedHLT_PFNoPUHT400_Mu5_PFMET50  = cms.string(MATCHED_PFNoPUHT400_Mu5_PFMET50), 
         ),
        tagVariables = cms.PSet(
            ecaliso = cms.string("ecalIso()"),
            hcaliso = cms.string("hcalIso()"),
            reliso = cms.string("( trackIso() + ecalIso() + hcalIso() )/pt()"),
            pfreliso = cms.string("(pfIsolationR03().sumChargedHadronPt + max(pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - pfIsolationR03().sumPUPt/2,0.0))/pt"),
            trkiso  = cms.string("trackIso()"),
            nVertices   = cms.InputTag("nverticesModule"),
            nVerticesDA = cms.InputTag("nverticesDAModule"),
            ht = cms.InputTag("glbHT"),
            met = cms.InputTag("glbMet"),
            # 2011
            passingHLT_Mu8_HT200                = cms.InputTag("flagPassHLTMu8HT200"),
            passingHLT_Mu15_HT200               = cms.InputTag("flagPassHLTMu15HT200"),
            passingHLT_Mu30_HT200               = cms.InputTag("flagPassHLTMu30HT200"),
            passingHLT_Mu40_HT200               = cms.InputTag("flagPassHLTMu40HT200"),
            passingHLT_Mu40_HT300               = cms.InputTag("flagPassHLTMu40HT300"),
            passingHLT_HT250_Mu15_PFMHT20       = cms.InputTag("flagPassHLTHT250Mu15PFMHT20"),
            passingHLT_HT250_Mu15_PFMHT40       = cms.InputTag("flagPassHLTHT250Mu15PFMHT40"),
            passingHLT_HT300_Mu15_PFMHT40       = cms.InputTag("flagPassHLTHT300Mu15PFMHT40"),
            # 2012
            passingHLT_IsoMu24                  = cms.InputTag("flagPassHLTIsoMu24"),
            passingHLT_IsoMu30                  = cms.InputTag("flagPassHLTIsoMu30"),
            passingHLT_IsoMu15_eta2p1_L1ETM20   = cms.InputTag("flagPassHLTIsoMu15eta2p1L1ETM20"),
            passingHLT_IsoMu20_eta2p1           = cms.InputTag("flagPassHLTIsoMu20eta2p1"),
            passingHLT_IsoMu24_eta2p1           = cms.InputTag("flagPassHLTIsoMu24eta2p1"),
            passingHLT_IsoMu30_eta2p1           = cms.InputTag("flagPassHLTIsoMu30eta2p1"),
            passingHLT_IsoMu34_eta2p1           = cms.InputTag("flagPassHLTIsoMu34eta2p1"),
            passingHLT_IsoMu40_eta2p1           = cms.InputTag("flagPassHLTIsoMu40eta2p1"),
            #passingHLT_Mu40_HT200               = cms.InputTag("flagPassHLTMu40HT200"),
            passingHLT_Mu40_FJHT200             = cms.InputTag("flagPassHLTMu40FJHT200"),
            passingHLT_Mu40_PFHT350             = cms.InputTag("flagPassHLTMu40PFHT350"),
            passingHLT_Mu40_PFNoPUHT350         = cms.InputTag("flagPassHLTMu40PFNoPUHT350"),
            passingHLT_Mu60_PFHT350             = cms.InputTag("flagPassHLTMu60PFHT350"),
            passingHLT_Mu60_PFNoPUHT350         = cms.InputTag("flagPassHLTMu60PFNoPUHT350"),
            passingHLT_PFHT350_Mu15_PFMET45     = cms.InputTag("flagPassHLTPFHT350Mu15PFMET45"),
            passingHLT_PFNoPUHT350_Mu15_PFMET45 = cms.InputTag("flagPassHLTPFNoPUHT350Mu15PFMET45"),
            passingHLT_PFHT350_Mu15_PFMET50     = cms.InputTag("flagPassHLTPFHT350Mu15PFMET50"),
            passingHLT_PFNoPUHT350_Mu15_PFMET50 = cms.InputTag("flagPassHLTPFNoPUHT350Mu15PFMET50"),
            passingHLT_PFHT400_Mu5_PFMET45      = cms.InputTag("flagPassHLTPFHT400Mu5PFMET45"),
            passingHLT_PFNoPUHT400_Mu5_PFMET45  = cms.InputTag("flagPassHLTPFNoPUHT400Mu5PFMET45"), 
            passingHLT_PFHT400_Mu5_PFMET50      = cms.InputTag("flagPassHLTPFHT400Mu5PFMET50"),
            passingHLT_PFNoPUHT400_Mu5_PFMET50  = cms.InputTag("flagPassHLTPFNoPUHT400Mu5PFMET50"), 
        ),
    )

    mcTruthCommonStuff = cms.PSet(
        isMC = cms.bool(mcInfo),
        makeMCUnbiasTree = cms.bool(False),
        checkMotherInUnbiasEff = cms.bool(True),
        tagMatches = cms.InputTag("muMcMatch"),
        motherPdgId = cms.vint32(22, 23),
    )
   ################################################################################################################################    

#   ____ _ ___    ___ ____ ____ ____    ___  ____ ____ ___  _  _ ____ ____ ____ 
#   |___ |  |      |  |__/ |___ |___    |__] |__/ |  | |  \ |  | |    |___ |__/ 
#   |    |  |      |  |  \ |___ |___    |    |  \ |__| |__/ |__| |___ |___ |  \ 
                                                                               

    # global muon efficieny from tracker muons
    process.fitGlbFromTk = cms.EDAnalyzer("TagProbeFitTreeProducer",
        commonStuff, trackCommonStuff, mcTruthCommonStuff,
        tagProbePairs = cms.InputTag("tpGlbTk"),
        probeMatches  = cms.InputTag("tkMcMatch"),
        allProbes     = cms.InputTag("tkProbes"),
    )
    
    # tracker muon efficiency from standalone muons
    process.fitTkFromSta = cms.EDAnalyzer("TagProbeFitTreeProducer",
        commonStuff, staCommonStuff, mcTruthCommonStuff,
        tagProbePairs = cms.InputTag("tpGlbSta"),
        probeMatches  = cms.InputTag("staMcMatch"),
        allProbes     = cms.InputTag("staProbes"),
    )

    # HLT efficiency from global muons
    process.fitHltFromGlb = cms.EDAnalyzer("TagProbeFitTreeProducer",
        commonStuff, muonCommonStuff, mcTruthCommonStuff,
        tagProbePairs = cms.InputTag("tpGlbGlb"),
        probeMatches  = cms.InputTag("muMcMatch"),
        allProbes     = cms.InputTag("matchedGlbMuons"),
    )
    ##############################################################################################################

#   ____ ____ ____ _  _ ____ _  _ ____ ____ ____ 
#   [__  |___ |  | |  | |___ |\ | |    |___ [__  
#   ___] |___ |_\| |__| |___ | \| |___ |___ ___] 
                                                

    process.allTagsAndProbes = cms.Sequence(
        process.tagMuons +
        process.tagMuonsHLT +
        process.matchedGlbMuons * process.tkTracks * process.tkProbes +
        process.staTracks * process.staProbes +
        process.matchedGlbMuons 
    )

    process.allHLTResults = cms.Sequence(
        # 2011
        process.flagPassHLTMu8HT200 +
        process.flagPassHLTMu15HT200 +
        process.flagPassHLTMu30HT200 +
        process.flagPassHLTMu40HT200 +
        process.flagPassHLTMu40HT300 +
        process.flagPassHLTHT250Mu15PFMHT20 +
        process.flagPassHLTHT250Mu15PFMHT40 +
        process.flagPassHLTHT300Mu15PFMHT40 +
        # 2012
        #process.flagPassHLTMu5 +
        #process.flagPassHLTMu12 +
        #process.flagPassHLTMu24 +
        process.flagPassHLTIsoMu24 +
        process.flagPassHLTIsoMu30 +
        process.flagPassHLTIsoMu15eta2p1L1ETM20 +
        process.flagPassHLTIsoMu20eta2p1 +
        process.flagPassHLTIsoMu24eta2p1 +
        process.flagPassHLTIsoMu30eta2p1 +
        process.flagPassHLTIsoMu34eta2p1 +
        process.flagPassHLTIsoMu40eta2p1 +
        #process.flagPassHLTMu40HT200 +
        process.flagPassHLTMu40FJHT200 +
        process.flagPassHLTMu40PFHT350 +
        process.flagPassHLTMu40PFNoPUHT350 +
        process.flagPassHLTMu60PFHT350 +
        process.flagPassHLTMu60PFNoPUHT350 +
        process.flagPassHLTPFHT350Mu15PFMET45 +
        process.flagPassHLTPFNoPUHT350Mu15PFMET45 +
        process.flagPassHLTPFHT350Mu15PFMET50 +
        process.flagPassHLTPFNoPUHT350Mu15PFMET50 +
        process.flagPassHLTPFHT400Mu5PFMET45 +
        process.flagPassHLTPFNoPUHT400Mu5PFMET45 +
        process.flagPassHLTPFHT400Mu5PFMET50 +
        process.flagPassHLTPFNoPUHT400Mu5PFMET50
    )

    process.allMet = cms.Sequence(
        process.glbMet
    )

    process.allST = cms.Sequence(
        process.stComp
    )

    process.allIsolations = cms.Sequence(
        (process.trkIsoDepositTk +
        process.trkIsoDepositCalByAssociatorTowers) *
        (process.TrackIsolationForTrk +
        process.EcalIsolationForTrk +
        process.HcalIsolationForTrk +
        process.RelIsolationForTrk) *
    
        (process.staIsoDepositTk +
        process.staIsoDepositCalByAssociatorTowers) *
        (process.TrackIsolationForStA +
        process.EcalIsolationForStA +
        process.HcalIsolationForStA +
        process.RelIsolationForStA) *

        (process.TrackIsolationForTrk04 +
        process.EcalIsolationForTrk04 +
        process.HcalIsolationForTrk04 +
        process.RelIsolationForTrk04) *

        (process.TrackIsolationForStA04 +
        process.EcalIsolationForStA04 +
        process.HcalIsolationForStA04 +
        process.RelIsolationForStA04) 
    ) 
    
    process.allVertices = cms.Sequence(
        process.nverticesModule +
        process.offlinePrimaryVerticesDA100um *
        process.nverticesDAModule
    )

    process.allJets = cms.Sequence(
        process.selectedJets*
        (process.trkdRToNearestJet +
        process.stadRToNearestJet +
        process.glbdRToNearestJet +
        process.trkJetMultiplicity +
        process.staJetMultiplicity +
        process.glbJetMultiplicity +
        process.trkHT +
        process.staHT +
        process.glbHT)
    )


    process.allPassingProbes = cms.Sequence(
        process.tkToGlbMatch * process.tkPassingGlb +
        process.staToTkMatch * process.staPassingTk 
    )

    process.allTPPairs = cms.Sequence(process.tpGlbTk + process.tpGlbSta + process.tpGlbGlb)
    
    if mcInfo:
        process.allMcMatches = cms.Sequence(process.muMcMatch + process.tkMcMatch + process.staMcMatch)

    process.allTPHistos = cms.Sequence(
        process.allTPPairs   +
        process.fitGlbFromTk +
        process.fitTkFromSta +
        process.fitHltFromGlb 
    )

    process.allImpactParameters = cms.Sequence(
        process.trkImpactParameter +
        process.staImpactParameter +
        process.glbImpactParameter
    )
    
    if mcInfo:
        process.TagAndProbe = cms.Sequence(
            ( process.allTagsAndProbes * process.allPassingProbes +
              process.allHLTResults +
              process.allMet +
              process.allST +
              process.allIsolations +
              process.allVertices +
              process.allJets +
              process.allMcMatches +
              process.deltaPfRecoPt +
              process.allImpactParameters ) *
            process.allTPHistos
        )
        
    if not mcInfo:
        process.TagAndProbe = cms.Sequence(
            ( process.allTagsAndProbes * process.allPassingProbes +
              process.allHLTResults +
              process.allMet +
              process.allST +
              process.allIsolations +
              process.allVertices +
              process.allJets +
              process.deltaPfRecoPt +
              process.allImpactParameters ) *
            process.allTPHistos
        )
