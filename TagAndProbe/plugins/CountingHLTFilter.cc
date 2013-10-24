#include "./CountingHLTFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TNtuple.h"
// #include "TTree.h"
#include <iostream>

using namespace std;

CountingHLTFilter::CountingHLTFilter ( const edm::ParameterSet & pset ) : hltFilter_ ( BasicHLTFilter ( pset ) ),
  passAll_ ( pset.getParameter<bool>("passAll") ), count_(0), passed_(0), tree_(0),  xsecs_(0),
  XSec_ ( pset.getParameter<double>("xsec") ), normalize_ ( pset.getParameter<double>("normalize") )
{
}

CountingHLTFilter::~CountingHLTFilter() { }

void CountingHLTFilter::endJob()
{
  float ratio = float(passed_)/float(count_);
  float weight = normalize_ * XSec_ * ratio;
  xsecs_->Fill ( float(count_), float(passed_), XSec_, XSec_ * ratio, weight );
  cout << "[CountingHLTFilter] " << passed_ << " / " << count_ << " events passed: w=" << normalize_ 
       << " pb^-1 * " << XSec_ << " pb * " << ratio << " = " << weight << endl;
}

bool CountingHLTFilter::filter ( edm::Event & event, edm::EventSetup const & setup )
{
  // cout << "[CountingHLTFilter] start" << endl;
  count_++;
  bool ret=true;
  if ( !passAll_ ) ret=hltFilter_.filter( event, setup );
  if ( ret ) passed_++;
  // tree_->Fill ( float(ret), 1. );
  int Wtype = hltFilter_.classifyW ( event );
  tree_->Fill ( float(ret), 1., float(Wtype) ); /// needed this for simplified models
  // cout << "[CountingHLTFilter] end" << endl;
  return ret;
}

void CountingHLTFilter::beginJob( ) // const edm::EventSetup & setup )
{
  /*
  setup.getData(pdtHandle_);
  */
  edm::Service<TFileService> fs;
  // tree_ = fs->make<TNtuple>("CountTree","CountTree","passed:count:W"); //< needed this for simplified models
  tree_ = fs->make<TNtuple>("CountTree","CountTree","passed:count:W" );
  xsecs_ = fs->make<TNtuple>("XSecs","XSecs","total:passed:orig:skimmed:weight" );
}

//define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CountingHLTFilter);
