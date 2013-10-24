/** \class BasicHLTFilter
 *
 * See header file for documentation
 *
 *  $Date: 2011/10/21 12:17:54 $
 *  $Revision: 1.2 $
 *
 *  \author Martin Grunewald
 *
 */

#include "../interface/BasicHLTFilter.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <cassert>

//
// constructors and destructor
//
BasicHLTFilter::BasicHLTFilter(const edm::ParameterSet& iConfig) :
  HLTFilter (iConfig),
  inputTag_ (iConfig.getParameter<edm::InputTag> ("TriggerResultsTag")),
  triggerNames_(),
  andOr_    (iConfig.getParameter<bool> ("andOr" )),
  n_        (0)

{
  // get names from module parameters, then derive slot numbers
  HLTPathsByName_= iConfig.getParameter<std::vector<std::string > >("HLTPaths");
  n_=HLTPathsByName_.size();
  HLTPathsByIndex_.resize(n_);

  // this is a user/analysis filter: it places no product into the event!

}

BasicHLTFilter::~BasicHLTFilter()
{
}

//
// member functions
//
int BasicHLTFilter::classifyW ( const edm::Event & ev ) const
{
  edm::Handle< reco::GenParticleCollection > gen_p;
  ev.getByLabel ( "genParticles", gen_p );
  int Wtype=-2;
  if ( gen_p.isValid() )
  {
    Wtype=-1;
    for ( reco::GenParticleCollection::const_iterator i=gen_p->begin();
          i!=gen_p->end() ; ++i )
    {
      if ( ( fabs ( i->pdgId() ) == 24 ) && (i->numberOfDaughters()>0) )
      {
        for ( unsigned d=0; d< i->numberOfDaughters() ; d++ )
        {
          if ( i->daughter(d) )
          {
            int dpdg = abs ( i->daughter(d)->pdgId() );
            if ( dpdg == 11 || dpdg == 15 || dpdg == 13 || dpdg < 7 ) Wtype=dpdg;
          }
        }
      }
    }
  }
  return Wtype;
}

// ------------ method called to produce the data  ------------
bool
BasicHLTFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace std;
   using namespace edm;

   const string invalid("@@invalid@@");

   // get hold of TriggerResults Object
   Handle<TriggerResults> trh;
   iEvent.getByLabel(inputTag_,trh);
   if (trh.isValid()) {
     LogDebug("") << "TriggerResults found, number of HLT paths: " << trh->size();
   } else {
     LogDebug("") << "TriggerResults product not found - returning result=false!";
     return false;
   }

   // get hold of trigger names - based on TriggerResults object!
   triggerNames_=iEvent.triggerNames ( *trh );

   unsigned int n(n_);
   for (unsigned int i=0; i!=n; i++) {
     HLTPathsByIndex_[i]=triggerNames_.triggerIndex(HLTPathsByName_[i]);
   }

   // for empty input vectors (n==0), default to all HLT trigger paths!
   if (n==0) {
     n=trh->size();
     HLTPathsByName_.resize(n);
     HLTPathsByIndex_.resize(n);
     for (unsigned int i=0; i!=n; i++) {
       HLTPathsByName_[i]=triggerNames_.triggerName(i);
       HLTPathsByIndex_[i]=i;
     }
   }

   // report on what is finally used
   LogDebug("") << "HLT trigger paths: " + inputTag_.encode()
		<< " - Number requested: " << n
		<< " - andOr mode: " << andOr_;
   if (n>0) {
     LogDebug("") << "  HLT trigger paths requested: index, name and valididty:";
     for (unsigned int i=0; i!=n; i++) {
       bool validity ( (HLTPathsByIndex_[i]<trh->size()) && (HLTPathsByName_[i]!=invalid) );

       LogTrace("") << " " << HLTPathsByIndex_[i]
		    << " " << HLTPathsByName_[i]
		    << " " << validity;

       if (!validity) throw cms::Exception("Configuration")
	 << " BasicHLTFilter [instance: " << *moduleLabel()
	 << " - path: " << *pathName()
	 << "] configured with unknown HLT path name "
	 << i << " " << HLTPathsByName_[i] <<"\n";
     }
   }

   // count number of requested HLT paths which have fired
   unsigned int fired(0);
   for (unsigned int i=0; i!=n; i++) {
     if (HLTPathsByIndex_[i]<trh->size()) {
       if (trh->accept(HLTPathsByIndex_[i])) {
	 fired++;
       }
     }
   }

   // Boolean filter result
   const bool accept( ((!andOr_) && (fired==n)) ||
		      (( andOr_) && (fired!=0)) );
   LogDebug("") << "Accept = " << accept << " fired=" << fired;

   return accept;

}

bool BasicHLTFilter::hltFilter(edm::Event & iEvent, edm::EventSetup const & iSetup, trigger::TriggerFilterObjectWithRefs& filterproduct)
{ return true; }
