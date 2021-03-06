#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

template<typename T>
class HTComputer : public edm::EDProducer {
    public:
        explicit HTComputer(const edm::ParameterSet & iConfig);
        virtual ~HTComputer() ;

        virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);

    private:
        edm::InputTag probes_;
        edm::InputTag objects_;
        StringCutObjectSelector<T,true> objCut_; // lazy parsing, to allow cutting on variables not in reco::Candidate class
};

template<typename T>
HTComputer<T>::HTComputer(const edm::ParameterSet & iConfig) :
    probes_(iConfig.getParameter<edm::InputTag>("probes")),
    objects_(iConfig.getParameter<edm::InputTag>("objects")),
    objCut_(iConfig.existsAs<std::string>("objectSelection") ? iConfig.getParameter<std::string>("objectSelection") : "", true)
{
    produces<edm::ValueMap<float> >();
}


template<typename T>
HTComputer<T>::~HTComputer()
{
}

template<typename T>
void 
HTComputer<T>::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
    using namespace edm;

    // read input
    Handle<View<reco::Candidate> > probes;
    Handle<View<T> > objects;
    iEvent.getByLabel(probes_,  probes);
    iEvent.getByLabel(objects_, objects);
    
    // fill
    float ht = 0.0;
    View<reco::Candidate>::const_iterator probe, endprobes = probes->end(); 
    typename View<T>::const_iterator object, endobjects = objects->end();
    for (object = objects->begin(); object != endobjects; ++object) {
      if ( !(objCut_(*object)) ) continue;
      ht+=object->pt();
    }

    // prepare vector for output    
    std::vector<float> values(probes->size(), ht);

    // convert into ValueMap and store
    std::auto_ptr<ValueMap<float> > valMap(new ValueMap<float>());
    ValueMap<float>::Filler filler(*valMap);
    filler.insert(probes, values.begin(), values.end());
    filler.fill();
    iEvent.put(valMap);
}


typedef HTComputer<pat::Jet>    PatJetHTComputer;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PatJetHTComputer);
