//

/*
  \class    	  PatMuonImpactParameter
  \description:
  	  	 produces valuemaps for IP (d0/dz) with respect to beamspot and primary vertex, using the innerTrack of the Muon (value = 999999 if innerTrack doesn't exist)
  	  	 To be used in T&P in the following way:

			 process.impactParameter = cms.EDProducer("PatMuonImpactParameter",
				probes = cms.InputTag("patMuonCollection"),
			 )

			 // in TagProbeFitTreeProducer
			 variables = cms.PSet(
			 	...
				d0_v = cms.InputTag("impactParameter","d0v"),
				d0_b = cms.InputTag("impactParameter","d0b"),
				dz_v = cms.InputTag("impactParameter","dzv"),
				dz_b = cms.InputTag("impactParameter","dzb"),
				...
			 )

*/



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
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "CommonTools/Utils/interface/StringObjectFunction.h"

class PatMuonImpactParameter : public edm::EDProducer {
    public:
        explicit PatMuonImpactParameter(const edm::ParameterSet & iConfig);
        virtual ~PatMuonImpactParameter() ;

        virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);

    private:
        edm::InputTag probes_;            

};

PatMuonImpactParameter::PatMuonImpactParameter(const edm::ParameterSet & iConfig) :
    probes_(iConfig.getParameter<edm::InputTag>("probes"))
{
    produces<edm::ValueMap<float> >("d0v");
    produces<edm::ValueMap<float> >("d0b");
    produces<edm::ValueMap<float> >("dzv");
    produces<edm::ValueMap<float> >("dzb");
}

PatMuonImpactParameter::~PatMuonImpactParameter()
{
}

void PatMuonImpactParameter::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
    using namespace edm;
    using namespace std;

    // read input
    Handle<View<pat::Muon> > probes;
    iEvent.getByLabel(probes_,  probes);
    
    math::XYZPoint beamSpotPosition;
    beamSpotPosition.SetCoordinates(NAN,NAN,NAN);
    Handle<reco::BeamSpot> bsHandle;
    try {
    	iEvent.getByLabel("offlineBeamSpot", bsHandle);
    	if (!bsHandle.isValid() || bsHandle.failedToGet()) {
    		cout << "[PatMuonImpactParameter] BeamSpot not valid!." << endl;
    	} else {
    		beamSpotPosition = bsHandle->position();
    	}
    } catch (cms::Exception & e) {
    	cout  << "[PatMuonImpactParameter] error (BeamSpot): " << e.what() << endl;
    }

    math::XYZPoint vertexPosition(NAN, NAN, NAN);
    Handle<vector<reco::Vertex> > pvHandle;
    try {
      iEvent.getByLabel( "offlinePrimaryVertices", pvHandle );
      if (!pvHandle.isValid() || pvHandle.failedToGet()) {
  		cout << "[PatMuonImpactParameter] PrimaryVertex not valid!." << endl;
      } else {
        vertexPosition = (*pvHandle).size()>0 ? (*pvHandle)[0].position() : math::XYZPoint(NAN,NAN,NAN);
      }
    } catch ( cms::Exception & e ) {
    	cout  << "[PatMuonImpactParameter] error (Vertex): " << e.what() << endl;
    }

    // prepare vector for output
    std::vector<float> d0_v;
    std::vector<float> d0_b;
    std::vector<float> dz_v;
    std::vector<float> dz_b;

    // fill
    View<pat::Muon>::const_iterator probe, endprobes = probes->end();
    for (probe = probes->begin(); probe != endprobes; ++probe) {
    	if (probe->innerTrack().isNonnull()) {
    		d0_v.push_back( probe->innerTrack()->dxy(vertexPosition)   );
    		d0_b.push_back( probe->innerTrack()->dxy(beamSpotPosition) );
    		dz_v.push_back( probe->innerTrack()->vertex().z() - vertexPosition.z()   );
    		dz_b.push_back( probe->innerTrack()->vertex().z() - beamSpotPosition.z() );
    	}
    	else {
//        	cout << "[PatMuonImpactParameter] " << "innerTrack() == 0" << endl;
    		d0_v.push_back( 999999 );
    		d0_b.push_back( 999999 );
    		dz_v.push_back( 999999 );
    		dz_b.push_back( 999999 );
        }
    }



    // convert into ValueMap and store
    std::auto_ptr<ValueMap<float> > vm_d0_v(new ValueMap<float>());
    std::auto_ptr<ValueMap<float> > vm_d0_b(new ValueMap<float>());
    std::auto_ptr<ValueMap<float> > vm_dz_v(new ValueMap<float>());
    std::auto_ptr<ValueMap<float> > vm_dz_b(new ValueMap<float>());
    ValueMap<float>::Filler fill_d0_v(*vm_d0_v);
    ValueMap<float>::Filler fill_d0_b(*vm_d0_b);
    ValueMap<float>::Filler fill_dz_v(*vm_dz_v);
    ValueMap<float>::Filler fill_dz_b(*vm_dz_b);
    fill_d0_v.insert(probes, d0_v.begin(), d0_v.end());
    fill_d0_b.insert(probes, d0_b.begin(), d0_b.end());
    fill_dz_v.insert(probes, dz_v.begin(), dz_v.end());
    fill_dz_b.insert(probes, dz_b.begin(), dz_b.end());
    fill_d0_v.fill();
    fill_d0_b.fill();
    fill_dz_v.fill();
    fill_dz_b.fill();
    iEvent.put(vm_d0_v,"d0v");
    iEvent.put(vm_d0_b,"d0b");
    iEvent.put(vm_dz_v,"dzv");
    iEvent.put(vm_dz_b,"dzb");
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PatMuonImpactParameter);
