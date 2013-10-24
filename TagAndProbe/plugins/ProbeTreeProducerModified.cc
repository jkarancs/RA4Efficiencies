// -*- C++ -*-
//
// Package:    ProbeTreeProducerModified
// Class:      ProbeTreeProducerModified
// 
/**\class ProbeTreeProducerModified ProbeTreeProducerModified.cc 

 Description: TTree producer based on input probe parameters

 Implementation:
     <Notes on implementation>
*/

#include <memory>
#include <ctype.h>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "PhysicsTools/TagAndProbe/interface/BaseTreeFiller.h"
#include <set>
#include "FWCore/ParameterSet/interface/Registry.h"

#include "DataFormats/Common/interface/Association.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "PhysicsTools/TagAndProbe/interface/TPTreeFiller.h"

class ProbeTreeProducerModified : public edm::EDAnalyzer {
  public:
    explicit ProbeTreeProducerModified(const edm::ParameterSet&);
    ~ProbeTreeProducerModified();

  private:
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob();

    /// InputTag to the collection of all probes
    edm::InputTag probesTag_;

    /// The selector object
    StringCutObjectSelector<reco::Candidate, true> cut_;

    /// Specifies whether this module should filter
    bool filter_;

    /// Name of the reco::Candidate function used for sorting
    std::string sortDescendingBy_;

    /// The StringObjectFunction itself
    StringObjectFunction<reco::Candidate, true> sortFunction_;

    /// The number of first probes used to fill the tree
    int32_t maxProbes_;

    int32_t maxNumOfProbesInEvent_;

    /// The object that actually computes variables and fills the tree for the probe
    std::auto_ptr<tnp::TPTreeFiller> treeFiller_; 

    //---- MC truth information
    /// Is this sample MC?
    bool isMC_; 
    /// InputTag to an edm::Association<reco::GenParticle> from tags & probes to MC truth
    edm::InputTag probeMatches_;
    /// Possible pdgids. If empty, any truth-matched particle will be considered good
    std::set<int32_t> PdgId_;
    /// Return true if ref is not null and has a pdgId inside 'PdgId_'
    bool checkPdgId(const reco::GenParticleRef &ref) const ;
};

ProbeTreeProducerModified::ProbeTreeProducerModified(const edm::ParameterSet& iConfig) :
  probesTag_(iConfig.getParameter<edm::InputTag>("src")),
  cut_(iConfig.existsAs<std::string>("cut") ? iConfig.getParameter<std::string>("cut") : ""),
  filter_(iConfig.existsAs<bool>("filter") ? iConfig.getParameter<bool>("filter") : false),
  sortDescendingBy_(iConfig.existsAs<std::string>("sortDescendingBy") ? iConfig.getParameter<std::string>("sortDescendingBy") : ""),
  sortFunction_(sortDescendingBy_.size()>0 ? sortDescendingBy_ : "pt"), //need to pass a valid default
  maxProbes_(iConfig.existsAs<int32_t>("maxProbes") ? iConfig.getParameter<int32_t>("maxProbes") : -1),
  maxNumOfProbesInEvent_(iConfig.existsAs<int32_t>("maxNumOfProbesInEvent") ? iConfig.getParameter<int32_t>("maxNumOfProbesInEvent") : -1),
  treeFiller_(new tnp::TPTreeFiller(iConfig)),
  isMC_(iConfig.getParameter<bool>("isMC"))
{
    if (isMC_) { 
        // MC matches for probes
        probeMatches_ = iConfig.getParameter<edm::InputTag>("probeMatches");
        // pdgids
        if (iConfig.existsAs<int32_t>("PdgId")) {
            PdgId_.insert(iConfig.getParameter<int32_t>("PdgId"));
        } else {
            std::vector<int32_t> Ids = iConfig.getParameter<std::vector<int32_t> >("PdgId");
            PdgId_.insert(Ids.begin(), Ids.end());
        }
    }
}

ProbeTreeProducerModified::~ProbeTreeProducerModified(){
}

void ProbeTreeProducerModified::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){
  bool result = !filter_;
  edm::Handle<reco::CandidateView> probes;
  iEvent.getByLabel(probesTag_, probes);
  if(!probes.isValid()) return;
  treeFiller_->init(iEvent);
  // on mc we want to load also the MC match info
  edm::Handle<edm::Association<std::vector<reco::GenParticle> > > probeMatches;
  if (isMC_) iEvent.getByLabel(probeMatches_, probeMatches);
  // select probes and calculate the sorting value
  typedef std::pair<reco::CandidateBaseRef, double> Pair;
  std::vector<Pair> selectedProbes;
  for (size_t i = 0; i < probes->size(); ++i){
    const reco::CandidateBaseRef &probe = probes->refAt(i);
    if(cut_(*probe)){
      selectedProbes.push_back(Pair(probe, sortFunction_(*probe)));
    }
  }
  // sort only if a function was provided
  if(sortDescendingBy_.size()>0) sort(selectedProbes.begin(), selectedProbes.end(), boost::bind(&Pair::second, _1) > boost::bind(&Pair::second, _2));

  if (maxNumOfProbesInEvent_>=0 && selectedProbes.size()>(size_t)maxNumOfProbesInEvent_) return;

  // fill the first maxProbes_ into the tree
  for (size_t i = 0; i < (maxProbes_<0 ? selectedProbes.size() : std::min((size_t)maxProbes_, selectedProbes.size())); ++i){
    // on mc, fill mc info (on non-mc, let it to 'true', the treeFiller will ignore it anyway
    bool mcTrue = false;
    if (isMC_) {
      const reco::CandidateBaseRef & probe = selectedProbes[i].first;
      // check mc match
      reco::GenParticleRef mprobe = (*probeMatches)[probe];
      mcTrue = checkPdgId(mprobe);
    }
    treeFiller_->fill(selectedProbes[i].first, -9999, mcTrue, -9999);
    result = true;
  }
  return;

}

bool ProbeTreeProducerModified::checkPdgId(const reco::GenParticleRef &ref) const {
    if (ref.isNull()) return false;
    if (PdgId_.find(abs(ref->pdgId())) != PdgId_.end()) return true;
    return false;
}

void ProbeTreeProducerModified::endJob(){
    // ask to write the current PSet info into the TTree header
    treeFiller_->writeProvenance(edm::getProcessParameterSet());
}

//define this as a plug-in
DEFINE_FWK_MODULE(ProbeTreeProducerModified);

