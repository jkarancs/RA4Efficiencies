#ifndef Filter_CountingHLTFilter_H
#define Filter_CountingHLTFilter_H
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
// #include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"                                                                               
#include "FWCore/Framework/interface/ESHandle.h"                                                                                               
#include "../interface/BasicHLTFilter.h"

class TH1;
class TNtuple;
// class TTree;

/**
 *  This class filteres based on Martin Grunewald's HLTFilter,
 *  additionally it does event counting, in a separate histo.
 */
class CountingHLTFilter : public edm::EDFilter {
public:
  explicit CountingHLTFilter( const edm::ParameterSet & );
  ~CountingHLTFilter();

  bool filter ( edm::Event&, edm::EventSetup const & );

private:
  void beginJob( ); // const edm::EventSetup & );
  void endJob();
  BasicHLTFilter hltFilter_;
  bool passAll_; //< flag that lets all events pass
  int count_;
  int passed_;
  // edm::ESHandle<ParticleDataTable> pdtHandle_;
  TNtuple * tree_;
  TNtuple * xsecs_; //< tuple to write down the xsec and event weight
  float XSec_; //< original cross section
  float normalize_; //< normalize to that value (in pb^-1)
};
#endif
