#ifndef Filter_BasicHLTFilter_h
#define Filter_BasicHLTFilter_h

/** \class BasicHLTFilter
 *
 *  
 *  This class is an BasicHLTFilter (-> EDFilter) implementing filtering on
 *  HLT bits
 *
 *  $Date: 2011/10/21 11:18:05 $
 *  $Revision: 1.3 $
 *
 *  \author Martin Grunewald
 *
 */

#include "HLTrigger/HLTcore/interface/HLTFilter.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include<vector>
#include<string>

//
// class declaration
//

class BasicHLTFilter : public HLTFilter {

  public:

    explicit BasicHLTFilter(const edm::ParameterSet&);
    ~BasicHLTFilter();
    virtual bool filter(edm::Event&, const edm::EventSetup&);
    virtual bool hltFilter(edm::Event&, const edm::EventSetup&, trigger::TriggerFilterObjectWithRefs&);
    virtual int classifyW( const edm::Event & ) const;

  private:

    /// initialize the trigger conditions (call this if the trigger paths have changed)
    void init(const edm::TriggerResults & results);

    /// HLT TriggerResults EDProduct
    edm::InputTag inputTag_;
    /// HLT trigger names
    edm::TriggerNames triggerNames_;

    /// false=and-mode (all requested triggers), true=or-mode (at least one)
    bool andOr_;

    /*
    // user provides: true: HLT Names (vstring), or false: HLT Index (vuint32)
    // bool byName_;
    // disabled: user must always provide names, never indices
    */

    /// number of HLT trigger paths requested in configuration
    unsigned int n_;

    /// list of required HLT triggers by HLT name
    std::vector<std::string > HLTPathsByName_;
    /// list of required HLT triggers by HLT index
    std::vector<unsigned int> HLTPathsByIndex_;

};

#endif //BasicHLTFilter_h
