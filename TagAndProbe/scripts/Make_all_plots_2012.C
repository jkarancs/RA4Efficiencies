void make_ele_plot(std::string trigger, std::string type, bool addMC, double ymin, double ymax, double xmin = -9999, double xmax = -9999) {
  std::string stlep = (type == "st") ? "_stlep" : "";
  // 2012ABC
  //std::string input_data    = (trigger.find("HT300")!=string::npos) ? "ElectronEffPlotDataHad_CleanPFHT300_Ele15_PFMET"+stlep+".root" :
  //  (trigger.find("HT350")!=string::npos) ? "ElectronEffPlotDataHad_CleanPFHT350_Ele5_PFMET"+stlep+".root" :
  //  (trigger.find("_Ele25")!=string::npos) ? "ElectronEffPlotDataHad_Ele25_TriCentralPFNoPUJet30.root" :
  //  (trigger.find("_WP80")!=string::npos) ? "ElectronEffPlotDataSingle2012_Ele27_WP80.root" :
  //  "ElectronEffPlotDataSingle2012.root";
  // 2012D
  //std::string input_data    = (trigger.find("HT300")!=string::npos) ? "ElectronEffPlotDataHad_CleanPFHT300_Ele15_PFMET_2012D.root" :
  //  (trigger.find("HT350")!=string::npos) ? "ElectronEffPlotDataHad_CleanPFHT350_Ele5_PFMET_2012D.root" :
  //  (trigger.find("_Ele25")!=string::npos) ? "ElectronEffPlotDataHad_Ele25_TriCentralPFNoPUJet30_2012D.root" :
  //  (trigger.find("_Ele30")!=string::npos) ? "ElectronEffPlotDataSingle_Ele30_2012D.root" :
  //  (trigger.find("_WP80")!=string::npos) ? "ElectronEffPlotDataSingle2012_Ele27_WP80.root" :
  //  "ElectronEffPlotDataSingle2012.root";
  // All2012
  std::string input_data    = (trigger.find("HT300")!=string::npos) ? "ElectronEffPlotDataHad_CleanPFHT300_Ele15_PFMET_All2012.root" :
    (trigger.find("HT350")!=string::npos) ? "ElectronEffPlotDataHad_CleanPFHT350_Ele5_PFMET_All2012.root" :
    (trigger.find("_Ele25")!=string::npos) ? "ElectronEffPlotDataHad_Ele25_TriCentralPFNoPUJet30_All2012.root" :
    (trigger.find("_Ele30")!=string::npos) ? "ElectronEffPlotDataSingle_Ele30_All2012.root" :
    (trigger.find("_WP80")!=string::npos) ? "ElectronEffPlotDataSingle2012_Ele27_WP80.root" :
    "ElectronEffPlotDataSingle2012.root";
  std::string input_mc      = (trigger.find("HT300")!=string::npos) ? "ElectronEffPlotMC_CleanPFHT300_Ele15_PFMET"+stlep+".root" :
    (trigger.find("HT350")!=string::npos) ? "ElectronEffPlotMC_CleanPFHT350_Ele5_PFMET"+stlep+".root" :
    (trigger.find("_Ele25")!=string::npos) ? "ElectronEffPlotMC_Ele25_TriCentralPFNoPUJet30.root" :
    (trigger.find("_WP80")!=string::npos) ? "ElectronEffPlotMC2012_Ele27_WP80.root" :
    "ElectronEffPlotMC2012.root";    
  std::string tree          = "goodPATEleToHLT";
  std::string type2         = (type == "pt") ? "et" : type;
  std::string variable      = 
    (type == "pt") ? "probe_gsfEle_et" :
    (type == "st") ? "stlep" :
    (type == "eta") ? "probe_gsfEle_eta" :
    (type == "ht")     ? "tag_ht" : 
    (type == "met")    ? "tag_met" :
    (type == "nvtx") ? "nVertices" : type;
  std::string xtitle        = 
    (type == "pt") ? "Probe E_{T} [GeV]" :
    (type == "eta") ? "Probe #eta" :
    (type == "nvtx") ? "N_{Vertices}" :
    (type == "met")    ? "Probe #slash{E}_{T}" :
    (type == "ht")     ? "H_{T} [GeV]" :
    (type == "st")     ? "S_{T} [GeV]" :
    (type == "reliso") ? "Probe Rel. Isolation" : "";
  std::string trigger_short = trigger;
  trigger_short.erase(trigger_short.find("HLT_"),4);
  
  if (trigger_short.find("_CaloIdT"  )!=string::npos) trigger_short.erase(trigger_short.find("_CaloIdT"  ),8);
  if (trigger_short.find("_CaloIdL"  )!=string::npos) trigger_short.erase(trigger_short.find("_CaloIdL"  ),8);
  if (trigger_short.find("_CaloIdVT" )!=string::npos) trigger_short.erase(trigger_short.find("_CaloIdVT" ),9);
  if (trigger_short.find("_CaloIsoVL")!=string::npos) trigger_short.erase(trigger_short.find("_CaloIsoVL"),10);
  if (trigger_short.find("_TrkIdT"   )!=string::npos) trigger_short.erase(trigger_short.find("_TrkIdT"   ),7);
  if (trigger_short.find("_TrkIdVL"  )!=string::npos) trigger_short.erase(trigger_short.find("_TrkIdVL"  ),8);
  if (trigger_short.find("_TrkIsoVL" )!=string::npos) trigger_short.erase(trigger_short.find("_TrkIsoVL" ),9);
  if (trigger_short.find("_TrkIsoT"  )!=string::npos) trigger_short.erase(trigger_short.find("_TrkIsoT"  ),8);
  bool dofit = type.find("pt")!=string::npos;

  std::string trigger_short2 = trigger_short;
  if (trigger_short.find("Ele25" )!=string::npos) trigger_short2 = "Ele25_CaloIsoVL_TriCentralPFNoPUJet30";
  if (trigger_short.find("Ele30" )!=string::npos) trigger_short2 = "Ele30_CaloIdVT_TrkIdT";


  //std::string matched = (trigger.find("HT")!=string::npos||trigger.find("Ele30")!=string::npos) ? "" : "matched";
  std::string matched = (trigger.find("Ele30")!=string::npos) ? "" : "matched";
  
  make_tdrStyle_plots(input_data, tree+"/Eff"+type+trigger+"/fit_eff_plots/"+variable+"_PLOT_tag_"+matched+"HLT_"+trigger_short2+"_pass",
		      input_mc,   tree+"/Eff"+type+trigger+"/fit_eff_plots/"+variable+"_PLOT_tag_"+matched+"HLT_"+trigger_short2+"_pass",
		      trigger_short+"_"+type2, trigger_short+" efficiency vs "+type2, xtitle, "#epsilon_{"+trigger+"}", 
		      ymin, ymax, xmin, xmax, -9999, dofit, addMC);
}

// MET/HT plot az IsoMu24_eta2p1

void make_mu_plot(std::string trigger, std::string type, bool addMC, double ymin, double ymax, double xmin = -9999, double xmax = -9999) {
  // 2012ABC
  //std::string input_data    = (trigger.find("HT")==string::npos) ? "MuonEffPlotDataSingle.root" : 
  //  (trigger.find("NoPU")==string::npos) ? "MuonEffPlotDataHad2012ABonly.root" : "MuonEffPlotDataHadNoPUHT.root";
  // 2012D
  //std::string input_data    = (trigger.find("HT")==string::npos) ? "MuonEffPlotDataSingle_2012D.root" : "MuonEffPlotDataHad_2012D.root";
  // 2012ABCD
  std::string input_data    = (trigger.find("HT")==string::npos) ? "MuonEffPlotDataSingle_All2012.root" : "MuonEffPlotDataHad_All2012.root";
  std::string input_mc      = "MuonEffPlotMC.root";
  std::string tree          = "fitHltFromGlb";
  std::string variable      = 
    (type == "nvtx")   ? "tag_nVertices" :
    (type == "reliso") ? "pfreliso" :
    (type == "ht")     ? "tag_ht" : 
    (type == "st")     ? "stlep" : 
    (type == "met")    ? "tag_met" : type;
  std::string xtitle        = 
    (type == "nvtx")   ? "N_{Vertices}" :
    (type == "reliso") ? "Probe PFReliso (#Delta#beta = 0.3)" :
    (type == "met")    ? "Probe #slash{E}_{T}" :
    (type == "ht")     ? "H_{T} [GeV]" :
    (type == "st")     ? "S_{T} [GeV]" :
    (type == "pt")     ? "Probe p_{T} [GeV/c]" :
    (type == "eta")    ? "Probe #eta" : "";
  std::string trigger2 = trigger;
  while (trigger2.find("_")!=string::npos) trigger2.erase(trigger2.find("_"),1);
  
  // Probe pt>5, the turnon is not seen for Mu5
  bool dofit = type.find("pt")!=string::npos;// && trigger.find("Mu5_")==string::npos;
  
  if (trigger.find("HT")==string::npos) { // SingleMu Triggers
    make_tdrStyle_plots(input_data, tree+"/"+type+"_"+trigger2+"/fit_eff_plots/"+variable+"_PLOT",
			input_mc,   tree+"/"+type+"_"+trigger2+"/fit_eff_plots/"+variable+"_PLOT",
			trigger.erase(0,4)+"_"+type, trigger+" efficiency vs "+type, xtitle, "#epsilon_{HLT_"+trigger+"}", 
			ymin, ymax, xmin, xmax, -9999, dofit, addMC, (type=="reliso") ? 0.04 : 0.05);
  } else { // Cross Triggers
    addMC = (trigger != "HLT_Mu40_HT200") && trigger.find("NoPUHT")==string::npos;
    std::string trigvar = (trigger == "HLT_Mu40_HT200") ? trigger+"_Run2012" : trigger;
    make_tdrStyle_plots(input_data, tree+"/"+type+"_"+trigger2+"/fit_eff_plots/"+variable+"_PLOT_tag_matched"+trigvar+"_pass",
			input_mc,   tree+"/"+type+"_"+trigger2+"/fit_eff_plots/"+variable+"_PLOT_tag_matched"+trigvar+"_pass",
			trigger.erase(0,4)+"_"+type, trigger+" efficiency vs "+type, xtitle, "#epsilon_{HLT_"+trigger+"}", 
			ymin, ymax, xmin, xmax, -9999, dofit, addMC, (type=="reliso") ? 0.04 : 0.05);
  }
}

void make_mu_id_plot(int id, std::string type, double ymin, double ymax, double xmin = -9999, double xmax = -9999) {
  std::string input_data    = (type == "njet") ? "MuonIDEffPlotData_lessdata_njet.root" : "MuonIDEffPlotData.root";
  //std::string input_mc      = (type == "njet") ? "MuonIDEffPlotMC_lessdata_njet.root" : "MuonIDEffPlotMC.root";
  std::string input_mc      = "MuonIDEffPlotMC_FastSim.root";
  std::string tree          = "fitGlbFromTk";
  std::string variable      = (type == "nvtx") ? "tag_nVertices" : type;
  std::string xtitle        = 
    (type == "njet")   ? "N_{Jet}" :
    (type == "nvtx")   ? "N_{Vertices}" :
    (type == "pt")     ? "Probe p_{T} [GeV/c]" :
    (type == "eta")    ? "Probe #eta" : "";
  std::string ID = (id==1) ? "ID1": (id==2) ? "ID2" : "ID";
  std::string ytitle = "#epsilon_{"+ID+"}";
  
  // Probe pt>5, the turnon is not seen for Mu5
  bool dofit = type.find("pt")!=string::npos;
  dofit=0;
  
  std::string passing = (id==2) ? ((type == "njet") ? "_passingID1_pass" : "_passing_pass") : "";
  std::string passing_mc = (id==2) ? "_passingID1_pass" : "";

  make_tdrStyle_plots(input_data, tree+"/"+ID+"_"+type+"/fit_eff_plots/"+variable+"_PLOT"+passing,
		      input_mc,   tree+"/"+ID+"_"+type+"/fit_eff_plots/"+variable+"_PLOT"+passing_mc,
		      ID+"_"+type, ID+" efficiency vs "+type, xtitle, ytitle,
		      ymin, ymax, xmin, xmax, -9999, dofit, 1, 0.05);
}

void Make_all_plots_2012() {
  gROOT->LoadMacro("tdrstyle.C");
  gROOT->LoadMacro("make_tdrStyle_plots.C");
  gROOT->LoadMacro("make_tdrStyle_plots_DataOnly.C");
  gROOT->LoadMacro("make_tdrStyle_plots_DataOnly_NoFit.C");
  gStyle->SetOptTitle(0);

  // SingleElectron Triggers
  std::vector<std::string > ele_triggers;
  //++ //ele_triggers.push_back("HLT_Ele22_CaloIdL_CaloIsoVL");  // Trigger off
  //++ //ele_triggers.push_back("HLT_Ele27_CaloIdL_CaloIsoVL");  // Not exist?
  //++ ele_triggers.push_back("HLT_Ele27_WP80");
  //++ ele_triggers.push_back("HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL");
  ele_triggers.push_back("HLT_Ele30_CaloIdVT_TrkIdT");
  //++ ele_triggers.push_back("HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL");
  //++ ele_triggers.push_back("HLT_Ele65_CaloIdVT_TrkIdT");    // Not enough stat
  //++ ele_triggers.push_back("HLT_Ele80_CaloIdVT_TrkIdT");    // Not enough stat
  //++ //ele_triggers.push_back("HLT_Ele80_CaloIdVT_GsfTrkIdT"); // Tag not matched
  //++ //ele_triggers.push_back("HLT_Ele90_CaloIdVT_GsfTrkIdT"); // Tag not matched
  //++ ele_triggers.push_back("HLT_Ele100_CaloIdVT_TrkIdT");   // Not enough stat
  
  std::vector<std::string > ele_xtriggers;
  ele_xtriggers.push_back("HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30");
  //ele_xtriggers.push_back("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT");
  //ele_xtriggers.push_back("HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT");
  //ele_xtriggers.push_back("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT");
  //ele_xtriggers.push_back("HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT");
  ele_xtriggers.push_back("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45");
  ele_xtriggers.push_back("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50");
  ele_xtriggers.push_back("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45");
  ele_xtriggers.push_back("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50");
  ele_xtriggers.push_back("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45");
  ele_xtriggers.push_back("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50");
  ele_xtriggers.push_back("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45");
  ele_xtriggers.push_back("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50");
  
  // SingleMu Triggers
  std::vector<std::string > mu_triggers;
  //mu_triggers.push_back("HLT_Mu5");  // Not enought stat (Prescaled)
  //mu_triggers.push_back("HLT_Mu12"); // Not enought stat (Prescaled)
  //mu_triggers.push_back("HLT_Mu24");    // Not simulated
  //mu_triggers.push_back("HLT_IsoMu24"); // Not simulated
  //mu_triggers.push_back("HLT_IsoMu30"); // Not simulated
  //mu_triggers.push_back("HLT_IsoMu15_eta2p1_L1ETM20");
  //mu_triggers.push_back("HLT_IsoMu20_eta2p1");
  mu_triggers.push_back("HLT_IsoMu24_eta2p1");
  //mu_triggers.push_back("HLT_IsoMu30_eta2p1");
  //mu_triggers.push_back("HLT_IsoMu34_eta2p1");
  //mu_triggers.push_back("HLT_IsoMu40_eta2p1");

  std::vector<std::string > mu_xtriggers;
  //mu_xtriggers.push_back("HLT_Mu40_HT200"); // Not simulated
  //mu_xtriggers.push_back("HLT_Mu40_FJHT200");
  mu_xtriggers.push_back("HLT_Mu40_PFHT350");
  mu_xtriggers.push_back("HLT_Mu60_PFHT350");
  mu_xtriggers.push_back("HLT_Mu40_PFNoPUHT350"); // No events passing
  mu_xtriggers.push_back("HLT_Mu60_PFNoPUHT350"); // No events passing
  mu_xtriggers.push_back("HLT_PFHT400_Mu5_PFMET45");
  mu_xtriggers.push_back("HLT_PFHT400_Mu5_PFMET50");
  mu_xtriggers.push_back("HLT_PFHT350_Mu15_PFMET45");
  mu_xtriggers.push_back("HLT_PFHT350_Mu15_PFMET50");
  mu_xtriggers.push_back("HLT_PFNoPUHT400_Mu5_PFMET45"); // Not simulated
  mu_xtriggers.push_back("HLT_PFNoPUHT400_Mu5_PFMET50"); // Not simulated
  mu_xtriggers.push_back("HLT_PFNoPUHT350_Mu15_PFMET45"); // Not simulated
  mu_xtriggers.push_back("HLT_PFNoPUHT350_Mu15_PFMET50"); // Not simulated
  
  // Single Lepton Triggers
  // Ele
  for (int i=ele_triggers.size()-1; i>=0; i--) {
    //make_ele_plot(ele_triggers[i],"reliso",i<3, 0,1.2,0,0.25);
    ////make_ele_plot(ele_triggers[i],"nvtx",i<3, 0.5,1.2,0.5, i==0 ? 36.5 : i==1 ? 32.5 : 24.5);
    //make_ele_plot(ele_triggers[i],"nvtx",i<3, 0.5,1.2,0,35);
    //make_ele_plot(ele_triggers[i],"eta",i<3, 0.5,1.2,-2.5,2.5);
    //make_ele_plot(ele_triggers[i],"pt",i<3, 0,1.2,0,i<3 ? 100 : 200);
  }
  
  // Electron Cross Triggers
  for (int i=ele_xtriggers.size()-1; i>=0; i--) {
    if (ele_xtriggers[i].find("NoPU" )!=string::npos) { // For 2012D
      bool addMC = ele_xtriggers[i].find("NoPUHT" )==string::npos;
      //make_ele_plot(ele_xtriggers[i],"met",addMC, 0,1.2,0,150);
      //make_ele_plot(ele_xtriggers[i],"ht",addMC, 0,1.5,100,1000);
      //make_ele_plot(ele_xtriggers[i],"reliso",addMC, 0,1.5,0,0.25);
      //make_ele_plot(ele_xtriggers[i],"nvtx",addMC, 0.5,1.2,0,35);
      //make_ele_plot(ele_xtriggers[i],"eta",addMC, 0.6,1.1,-2.5,2.5);
      //if (ele_xtriggers[i].find("Ele25" )==string::npos) // No ST plot for Ele25
      //	make_ele_plot(ele_xtriggers[i],"st",addMC, 0,1.2,0,500);
      //make_ele_plot(ele_xtriggers[i],"pt",addMC, 0,1.2);
    }
  }

  
  
  // Mu
  for (int i=mu_triggers.size()-1; i>=0; i--) {
    // //bool addMC = (i>0); // IsoMu24, IsoMu24_eta2p1 (former not simulated)
    bool addMC = 1;
    // make_mu_plot(mu_triggers[i],"met",addMC, 0,1.2,0,150);
    // make_mu_plot(mu_triggers[i],"ht",addMC, 0,1.2,100,1000);
    // make_mu_plot(mu_triggers[i],"reliso",addMC, 0,1.2,0,0.2);
    // make_mu_plot(mu_triggers[i],"nvtx",addMC, 0.5,1.1,0,40);
    // make_mu_plot(mu_triggers[i],"eta",addMC, 0.5,1.1,-2.4,2.4);
    // make_mu_plot(mu_triggers[i],"st",addMC, 0,1.2,0,500);
    //make_mu_plot(mu_triggers[i],"pt",addMC, 0,1.2,0,100);
  }
  
  // Cross Triggers 
  // Mu
  double ptmin[12] = { 20, 30, 20, 30, 0, 0, 0, 0, 0, 0, 0, 0 };
  double ptmax[12] = { 200, 200, 200, 200, 100, 100, 100, 100, 100, 100, 100, 100 };
  // NoPu only
  //double ptmin[6] = { 20, 30, 0, 0, 0, 0 };
  //double ptmax[6] = { 200, 200, 100, 100, 100, 100 };
  for (int i=mu_xtriggers.size()-1; i>=0; i--) {
    if (mu_xtriggers[i].find("NoPU" )!=string::npos) { // For 2012D and All2012
      bool addMC = mu_xtriggers[i].find("NoPUHT" )==string::npos;
      //make_mu_plot(mu_xtriggers[i],"met",addMC, 0,1.2,0,150);
      //make_mu_plot(mu_xtriggers[i],"ht",addMC, 0,1.5,100,1000);
      //make_mu_plot(mu_xtriggers[i],"reliso",addMC, 0,1.5,0,0.2);
      //make_mu_plot(mu_xtriggers[i],"nvtx",addMC, 0.5,1.2,0,36);
      //make_mu_plot(mu_xtriggers[i],"eta",addMC, 0.6,1.1,-2.4,2.4);
      //make_mu_plot(mu_xtriggers[i],"st",addMC, 0,1.2,0,500);
      //make_mu_plot(mu_xtriggers[i],"pt",addMC, 0,1.2,ptmin[i],ptmax[i]);
    }
  }
  
  //make_mu_id_plot(2, "njet", 0, 1.2, 0.5, 7.5);
  //make_mu_id_plot(2, "nvtx", 0.7, 1.05, 0, 35);
  //make_mu_id_plot(2, "eta", 0.7, 1.05, -2.4, 2.4);
  //make_mu_id_plot(2, "pt", 0.7, 1.05, 10, 200);
  //make_mu_id_plot(1, "eta", 0.7, 1.05, -2.4, 2.4);
  //make_mu_id_plot(1, "pt", 0.7, 1.05, 20, 200);


  // Ele Cumulative RelIso plots
  /*
  make_tdrStyle_plots("../RA4_TP_ZEE/ElectronEffPlotDataHad_Ele15_cumul_reliso.root", "goodPATEleToHLT/EffcumrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45/fit_eff_plots/reliso_PLOT_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_probe_gsfEle_et_bin0_&_probe_gsfEle_eta_bin0_&_tag_passingHLT_CleanPFHT300_Ele15_PFMET45_bin0_&_tag_matchedHLT_CleanPFHT300_Ele15_PFMET45_pass",
        	      "../RA4_TP_ZEE/ElectronEffPlotMC_Ele15_cumul_reliso.root",      "goodPATEleToHLT/EffcumrelisoHLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45/fit_eff_plots/reliso_PLOT_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_probe_gsfEle_et_bin0_&_probe_gsfEle_eta_bin0_&_tag_passingHLT_CleanPFHT300_Ele15_PFMET45_bin0_&_tag_matchedHLT_CleanPFHT300_Ele15_PFMET45_pass",
        	      "CleanPFHT300_Ele15_PFMET45_cumreliso", "CleanPFHT300_Ele15_PFMET45 efficiency vs cumul. relIso", "Maximum Rel. Isolation", "#epsilon_{CleanPFHT300_Ele15_PFMET45}",
        	      0.9,1.02, 0,0.25, -9999, 0, 1);
  
  
  make_tdrStyle_plots("../RA4_TP_ZEE/ElectronEffPlotDataHad_TriCentral_cumul_reliso.root", "goodPATEleToHLT/EffcumrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30/fit_eff_plots/reliso_PLOT_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_probe_gsfEle_et_bin0_&_probe_gsfEle_eta_bin0_&_tag_passingHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30_bin0_&_tag_matchedHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30_pass",
        	      "../RA4_TP_ZEE/ElectronEffPlotMC_TriCentral_cumul_reliso.root",      "goodPATEleToHLT/EffcumrelisoHLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30/fit_eff_plots/reliso_PLOT_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_probe_gsfEle_et_bin0_&_probe_gsfEle_eta_bin0_&_tag_passingHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30_bin0_&_tag_matchedHLT_Ele25_CaloIsoVL_TriCentralPFNoPUJet30_pass",
        	      "Ele25_TriCentralPFNoPUJet30_cumreliso", "Ele25_TriCentralPFNoPUJet30 efficiency vs cumul. relIso", "Maximum Rel. Isolation", "#epsilon_{Ele25_TriCentralPFNoPUJet30}",
        	      0.9,1.02, 0,0.25, -9999, 0, 1);
  
  // FASTSIM RelIso Test
  make_tdrStyle_plots("../RA4_TP_ZEE/EleIDEffPlotData_RelIsotest3.root","GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
        	      "../RA4_TP_ZEE/EleIDEffPlotMC_RelIsotest3.root",  "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
        	      "ID_eta", "ID efficiency vs eta", "Probe #eta", "#epsilon_{ID}", 0.6,1.1, -2.5,2.5);
  
  // FASTSIM MC
  // Ele ID Efficiency
  /*
  make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin0",
        	      "EleIDEffPlotMC_FastSim.root",  "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin0",
        	      "ID_et_barrel", "ID efficiency vs ET (Barrel)", "Probe E_{T} [GeV]", "#epsilon_{ID}", 0.4,1.1, 20,150, 0.9613, 1,1,0.05,
		      -9999, 0.8,1,    0, -10,10,     20, 0,50); // plateau, turnon, width
  
  make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin1",
        	      "EleIDEffPlotMC_FastSim.root",  "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin1",
        	      "ID_et_endcap", "ID efficiency vs ET (Endcap)", "Probe E_{T} [GeV]", "#epsilon_{ID}", 0.4,1.1, 20,150, 0.9613, 1,1,0.05,
		      -9999, 0.8,1,    0, -10,10,     20, 0,50); // plateau, turnon, width
  
  make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
        	      "EleIDEffPlotMC_FastSim.root",  "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
        	      "ID_eta", "ID efficiency vs eta", "Probe #eta", "#epsilon_{ID}", 0.6,1.1, -2.5,2.5, 0.9613);
  
  make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT",
        	      "EleIDEffPlotMC_FastSim.root",  "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT",
        	      "ID_nvtx", "ID efficiency vs Nvertex", "N_{Vertices}", "#epsilon_{ID}", 0.7,1.05, 0.5,40.5, 0.9613);
  
  make_tdrStyle_plots("EleIDEffPlotData_njet.root", "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT",
        	      "EleIDEffPlotMC_FastSim.root","GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT",
        	      "ID_njet", "ID efficiency vs Njet", "N_{Jet}", "#epsilon_{ID}", 0.7,1.05, 0.5,7.5, 0.9613);
  
  


  // EB/EE Binning
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT_probe_gsfEle_abseta_bin1",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT_probe_gsfEle_abseta_bin1",
        	      "ID_njet_endcap", "ID efficiency vs Njet (Endcap)", "N_{Jet}", "#epsilon_{ID}", 0.5,1.05, 0.5,7.5, 0.8725);
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT_probe_gsfEle_abseta_bin0",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT_probe_gsfEle_abseta_bin0",
        	      "ID_njet_barrel", "ID efficiency vs Njet (Barrel)", "N_{Jet}", "#epsilon_{ID}", 0.7,1.05, 0.5,7.5, 0.99);
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT_probe_gsfEle_abseta_bin1",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT_probe_gsfEle_abseta_bin1",
        	      "ID_nvtx_endcap", "ID efficiency vs Nvertex (Endcap)", "N_{Vertices}", "#epsilon_{ID}", 0.5,1.05, 0.5,35.5, 0.8725);
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT_probe_gsfEle_abseta_bin0",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT_probe_gsfEle_abseta_bin0",
        	      "ID_nvtx_barrel", "ID efficiency vs Nvertex (Barrel)", "N_{Vertices}", "#epsilon_{ID}", 0.7,1.05, 0.5,35.5, 0.99);
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
        	      "ID_eta", "ID efficiency vs eta", "Probe #eta", "#epsilon_{ID}", 0.6,1.1, -2.5,2.5, 0.99);
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin1",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin1",
        	      "ID_et_endcap", "ID efficiency vs ET (Endcap)", "Probe E_{T} [GeV]", "#epsilon_{ID}", 0.5,1.05, 20,150, 0.8725, 1,1,0.05,
		      -9999, 0.8,1,    0, -10,10,     20, 0,50); // plateau, turnon, width
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root", "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin0",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",    "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin0",
        	      "ID_et_barrel", "ID efficiency vs ET (Barrel)", "Probe E_{T} [GeV]", "#epsilon_{ID}", 0.7,1.05, 20,150, 0.99, 1,1,0.05,
		      -9999, 0.8,1,    0, -10,10,     20, 0,50); // plateau, turnon, width
  
  
  // Ele Gsf Efficiency
  make_tdrStyle_plots("EleGsfEffPlotData.root",      "SuperClusterToGsfElectronPATTag/Gsf_pt/fit_eff_plots/probe_pt_PLOT",
        	      "EleGsfEffPlotMC_FastSim.root","SuperClusterToGsfElectronPATTag/Gsf_pt/fit_eff_plots/probe_pt_PLOT",
        	      "Gsf_pt", "Gsf efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{Gsf}", 0.8,1.05, 20,150, 0.9902, 1,1,0.05,
		      0.98, 0.97,1,    0, -100,20,     20, 0,50); // plateau, turnon, width

  make_tdrStyle_plots("EleGsfEffPlotData.root",      "SuperClusterToGsfElectronPATTag/Gsf_eta/fit_eff_plots/probe_eta_PLOT",
        	      "EleGsfEffPlotMC_FastSim.root","SuperClusterToGsfElectronPATTag/Gsf_eta/fit_eff_plots/probe_eta_PLOT",
        	      "Gsf_eta", "Gsf efficiency vs eta", "Probe #eta", "#epsilon_{Gsf}", 0.8,1.05, -2.5,2.5, 0.9902);


  // 1bin plots
  
  //make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID2_pt20/fit_eff_plots/pt_PLOT_passing_pass",
  make_tdrStyle_plots("../RA4_TP_ZMuMu/MuonIDEffPlotData_njet_pt20.root", "fitGlbFromTk/ID2_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0_&_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_passing_pass",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID2_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0_&_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_ra4idcuts_bin0_&_passing_pass",
		      "ID2_pt20", "ID2 efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID2}", 0.7,1.05, 20,200);

  //make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
  make_tdrStyle_plots("../RA4_TP_ZMuMu/MuonIDEffPlotData_njet_pt20.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      "ID1_pt20", "ID1 efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID1}", 0.7,1.05, 20,200);

  make_tdrStyle_plots("EleGsfEffPlotData.root",      "SuperClusterToGsfElectronPATTag/Gsf_pt20/fit_eff_plots/probe_pt_PLOT_probe_abseta_bin0",
        	      "EleGsfEffPlotMC_FastSim.root","SuperClusterToGsfElectronPATTag/Gsf_pt20/fit_eff_plots/probe_pt_PLOT_probe_abseta_bin0",
        	      "Gsf_pt20", "Gsf efficiency in pt bin [20,200]", "Probe p_{T}", "#epsilon_{Gsf}", 0.7,1.05, 20,200);
  
  //make_tdrStyle_plots("../RA4_TP_ZEE/EleIDEffPlotData_pt.root","GsfElectronToIdPATTag/ID_pt20/fit_eff_plots/probe_gsfEle_pt_PLOT_probe_gsfEle_abseta_bin0",
  //      	      "EleIDEffPlotMC_FastSim.root",           "GsfElectronToIdPATTag/ID_pt20/fit_eff_plots/probe_gsfEle_pt_PLOT_probe_gsfEle_abseta_bin0",
  //      	      "ID_pt20", "ID efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID}", 0.7,1.05, 20,200);
  
  make_tdrStyle_plots("EleIDEffPlotData_lessdata_EB_EE.root","GsfElectronToIdPATTag/ID_pt20/fit_eff_plots/probe_gsfEle_abseta_PLOT",
        	      "EleIDEffPlotMC_FastSim_EB_EE.root",   "GsfElectronToIdPATTag/ID_pt20/fit_eff_plots/probe_gsfEle_abseta_PLOT",
        	      "ID_pt20", "ID efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID}", 0.7,1.05, 0,2.5);
  
  make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root", "fitTkFromSta/Trk_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      "MuonTrkEffPlotMC_FastSim.root",    "fitTkFromSta/Trk_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      "Trk_pt20", "Trk efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{Track}", 0.95,1.005, 20,200);

  // Summary      Data              FastSim           Data/FastSim                              Std Bkg MC        Data/Std bkg MC
  // Mu  Trk      0.9908 +- 0.0001  0.9956 +- 0.0001  0.9951 +- 0.0001 (stat.) +- 0.005 (sys.)  0.9955 +- 0.0001  0.9953 +- 0.0001 (stat.) +- 0.005 (sys.)
  // Mu  ID1      0.9422 +- 0.0006  0.9886 +- 0.0002  0.9531 +- 0.0007 (stat.) +- 0.03 (sys.)
  // Mu  ID2      0.9735 +- 0.0005  0.9832 +- 0.0002  0.9902 +- 0.0005 (stat.) +- 0.01 (sys.)
  // Ele Gsf      0.9622 +- 0.0003  0.9718 +- 0.0002  0.9902 +- 0.0004 (stat.) +- 0.01 (sys.)
  // Ele ID       0.8193 +- 0.0011  0.8524 +- 0.0004  0.9613 +- 0.0014 (stat.) +- 0.08 (sys.)
  // Ele ID (EB)  0.8579 +- 0.0004  0.8665 +- 0.0004  0.9900 +- 0.0007 (stat.) +- 0.03 (sys.)
  // Ele ID (EE)  0.7078 +- 0.0009  0.8112 +- 0.0008  0.8725 +- 0.0014 (stat.) +- 0.07?(sys.)

  */
  // All 2012 update
  //make_tdrStyle_plots("../RA4_TP_ZMuMu/MuonIDEffPlotData_All2012.root", "fitGlbFromTk/ID2_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0_&_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_ra4idcuts_bin0_&_passing_pass",
  //      	      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID2_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0_&_absdeltapt_bin0_&_d0_v_bin0_&_drjet_bin0_&_dz_v_bin0_&_ra4idcuts_bin0_&_passing_pass",
  //      	      "ID2_pt20", "ID2 efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID2}", 0.7,1.05, 20,200);
  //
  //make_tdrStyle_plots("../RA4_TP_ZMuMu/MuonIDEffPlotData_2012D.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
  make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      //"MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      "MuonIDEffPlotMC_njet_pt20.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
		      "ID1_pt20", "ID1 efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID1}", 0.7,1.05, 20,200);

  //make_tdrStyle_plots("EleGsfEffPlotData.root",      "SuperClusterToGsfElectronPATTag/Gsf_pt20/fit_eff_plots/probe_pt_PLOT_probe_abseta_bin0",
  //      	      "EleGsfEffPlotMC_FastSim.root","SuperClusterToGsfElectronPATTag/Gsf_pt20/fit_eff_plots/probe_pt_PLOT_probe_abseta_bin0",
  //      	      "Gsf_pt20", "Gsf efficiency in pt bin [20,200]", "Probe p_{T}", "#epsilon_{Gsf}", 0.7,1.05, 20,200);
  
  //make_tdrStyle_plots("../RA4_TP_ZEE/EleIDEffPlotData_All2012.root","GsfElectronToIdPATTag/ID_pt20/fit_eff_plots/probe_gsfEle_abseta_PLOT",
  //      	      "EleIDEffPlotMC_FastSim_EB_EE.root",   "GsfElectronToIdPATTag/ID_pt20/fit_eff_plots/probe_gsfEle_abseta_PLOT",
  //      	      "ID_pt20", "ID efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{ID}", 0.7,1.05, 0,2.5);
  
  //make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root", "fitTkFromSta/Trk_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
  //      	      "MuonTrkEffPlotMC_FastSim.root",    "fitTkFromSta/Trk_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
  //		      "Trk_pt20", "Trk efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{Track}", 0.95,1.005, 20,200);
  
  
  // Summary      Data              FastSim           Data/FastSim                              Std Bkg MC        Data/Std bkg MC
  // Mu  ID1      0.9869 +- 0.0001  0.9886 +- 0.0001  0.9983 +- 0.0002 (stat.) +- 0.03 (sys.)
  // Mu  ID2      0.9715 +- 0.0002  0.9832 +- 0.0002  0.9881 +- 0.0003 (stat.) +- 0.01 (sys.)
  // Ele ID (EB)  0.8573 +- 0.0004  0.8665 +- 0.0004  0.9894 +- 0.0007 (stat.) +- 0.03 (sys.)
  // Ele ID (EE)  0.7072 +- 0.0009  0.8112 +- 0.0008  0.8718 +- 0.0014 (stat.) +- 0.07?(sys.)

  
  
  //Checking ID1 Consistency between 2012A/B/C
  //make_tdrStyle_plots("../RA4_TP_ZMuMu/MuonIDEffPlotData_lessdata_2012A_pt20.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
  //      	      "../RA4_TP_ZMuMu/MuonIDEffPlotData_lessdata_2012C_pt20.root", "fitGlbFromTk/ID1_pt20/fit_eff_plots/pt_PLOT_abs_eta_bin0",
  //      	      "ID1_pt_compare", "ID1 efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{ID1}", 0.9,1.05, 20,150, -9999);
  //make_tdrStyle_plots("../RA4_TP_ZMuMu/MuonIDEffPlotData_lessdata_2012C.root", "fitGlbFromTk/ID1_pt/fit_eff_plots/pt_PLOT",
  //      	      "../RA4_TP_ZMuMu/MuonIDEffPlotData_lessdata_2012ABC.root", "fitGlbFromTk/ID1_pt/fit_eff_plots/pt_PLOT",
  //      	      "ID1_pt_compare", "ID1 efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{ID1}", 0.9,1.05, 20,150, -9999);
  

  // Muon Trk Efficiency
  //make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root",    "fitTkFromSta/Trk_drjet/fit_eff_plots/drjet_PLOT",
  //      	      "MuonTrkEffPlotMC_FastSim_drjet.root", "fitTkFromSta/Trk_drjet/fit_eff_plots/drjet_PLOT",
  //      	      "Trk_drjet", "Trk efficiency vs drjet", "Probe #DeltaR_{Jet}", "#epsilon_{Track}", 0.9,1.02, 0,4.5, 0.9951);
  //
  //make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root", "fitTkFromSta/Trk_njet/fit_eff_plots/njet_PLOT",
  //      	      "MuonTrkEffPlotMC_FastSim.root",    "fitTkFromSta/Trk_njet/fit_eff_plots/njet_PLOT",
  //      	      "Trk_njet", "Trk efficiency vs njet", "N_{Jet}", "#epsilon_{Track}", 0.9,1.02, 0.5,7.5, 0.9951);
  //
  //make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root", "fitTkFromSta/Trk_nvtx/fit_eff_plots/tag_nVertices_PLOT",
  //      	      "MuonTrkEffPlotMC_FastSim.root",    "fitTkFromSta/Trk_nvtx/fit_eff_plots/tag_nVertices_PLOT",
  //      	      "Trk_nvtx", "Trk efficiency vs nvtx", "N_{Vertices}", "#epsilon_{Track}", 0.9,1.02, 0.5,35.5, 0.9951);
  //
  //make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root", "fitTkFromSta/Trk_eta/fit_eff_plots/eta_PLOT",
  //      	      "MuonTrkEffPlotMC_FastSim.root",    "fitTkFromSta/Trk_eta/fit_eff_plots/eta_PLOT",
  //      	      "Trk_eta", "Trk efficiency vs eta", "Probe #eta", "#epsilon_{Track}", 0.9,1.02, -2.4,2.4, 0.9951);
  //
  //make_tdrStyle_plots("MuonTrkEffPlotData_lessdata.root", "fitTkFromSta/Trk_pt/fit_eff_plots/pt_PLOT",
  //      	      "MuonTrkEffPlotMC_FastSim.root",    "fitTkFromSta/Trk_pt/fit_eff_plots/pt_PLOT",
  //      	      "Trk_pt", "Trk efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{Track}", 0.9,1.02, 20,200, 0.9951);
  
  
  /*
  // Muon ID1/ID2 Efficiency
  make_tdrStyle_plots("MuonIDEffPlotData_lessdata_njet.root", "fitGlbFromTk/ID2_njet/fit_eff_plots/njet_PLOT_passingID1_pass",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID2_njet/fit_eff_plots/njet_PLOT_passing_pass",
		      "ID2_njet", "ID2 efficiency vs Njet", "N_{Jet}", "#epsilon_{ID2}", 0.85,1.05, 0.5,7.5, 0.9902);

  make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID2_nvtx/fit_eff_plots/tag_nVertices_PLOT_passing_pass",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID2_nvtx/fit_eff_plots/tag_nVertices_PLOT_passing_pass",
		      "ID2_nvtx", "ID2 efficiency vs Nvertex", "N_{Vertices}", "#epsilon_{ID2}", 0.85,1.05, 0.5,35.5, 0.9902);

  make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID2_eta/fit_eff_plots/eta_PLOT_passing_pass",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID2_eta/fit_eff_plots/eta_PLOT_passing_pass",
		      "ID2_eta", "ID2 efficiency vs eta", "Probe #eta", "#epsilon_{ID2}", 0.85,1.05, -2.4,2.4, 0.9902);

  make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID2_pt/fit_eff_plots/pt_PLOT_passing_pass",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID2_pt/fit_eff_plots/pt_PLOT_passing_pass",
		      "ID2_pt", "ID2 efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{ID2}", 0.85,1.05, 20,200, 0.9902, 1,1,0.05,
		      -9999, 0.8,1,    0, -50,10,     20, 0,50); // plateau, turnon, width
  
  make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID1_eta/fit_eff_plots/eta_PLOT",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID1_eta/fit_eff_plots/eta_PLOT",
		      "ID1_eta", "ID1 efficiency vs eta", "Probe #eta", "#epsilon_{ID1}", 0.8,1.05, -2.4,2.4, 0.9531);
  
  make_tdrStyle_plots("MuonIDEffPlotData.root", "fitGlbFromTk/ID1_pt/fit_eff_plots/pt_PLOT",
		      "MuonIDEffPlotMC_FastSim.root", "fitGlbFromTk/ID1_pt/fit_eff_plots/pt_PLOT",
		      "ID1_pt", "ID1 efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{ID1}", 0.8,1.05, 20,200, 0.9531, 1,1,0.05,
		      -9999, 0.8,1,    0, -50,10,     20, 0,50); // plateau, turnon, width
  */
  // Standard Model Background

  // make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin0",
  //       	      "EleIDEffPlotMC_noNjet.root",   "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin0",
  //      	       "ID_et_barrel", "ID efficiency vs ET (Barrel)", "Probe E_{T} [GeV]", "#epsilon_{ID}", 0,1.2, 10,150, -9999, 1);
  // 
  // make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin1",
  //       	      "EleIDEffPlotMC_noNjet.root",   "GsfElectronToIdPATTag/ID_et/fit_eff_plots/probe_gsfEle_et_PLOT_probe_gsfEle_abseta_bin1",
  //      	       "ID_et_endcap", "ID efficiency vs ET (Endcap)", "Probe E_{T} [GeV]", "#epsilon_{ID}", 0,1.2, 10,150, -9999, 1);
  // 
  // make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
  //       	      "EleIDEffPlotMC_noNjet.root",   "GsfElectronToIdPATTag/ID_eta/fit_eff_plots/probe_gsfEle_eta_PLOT",
  //       	      "ID_eta", "ID efficiency vs eta", "Probe #eta", "#epsilon_{ID}", 0,1.2, -2.5,2.5, -9999);
  // 
  // make_tdrStyle_plots("EleIDEffPlotData_noNjet.root", "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT",
  //       	      "EleIDEffPlotMC_noNjet.root",   "GsfElectronToIdPATTag/ID_nvtx/fit_eff_plots/nVertices_PLOT",
  //       	      "ID_nvtx", "ID efficiency vs Nvertex", "N_{Vertices}", "#epsilon_{ID}", 0,1.2, 0.5,40.5, -9999);
  // 
  // make_tdrStyle_plots("EleIDEffPlotData_njet.root", "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT",
  //       	      "EleIDEffPlotMC_njet.root",   "GsfElectronToIdPATTag/ID_njet/fit_eff_plots/njet_PLOT",
  //       	      "ID_njet", "ID efficiency vs Njet", "N_{Jet}", "#epsilon_{ID}", 0,1.2, 0.5,7.5, -9999);
  // 
  //make_tdrStyle_plots("EleGsfEffPlotData.root", "SuperClusterToGsfElectronPATTag/Gsf_pt/fit_eff_plots/probe_pt_PLOT",
  //      	      "EleGsfEffPlotMC.root",   "SuperClusterToGsfElectronPATTag/Gsf_pt/fit_eff_plots/probe_pt_PLOT",
  //      	      "Gsf_pt", "Gsf efficiency vs pt", "Probe p_{T} [GeV]", "#epsilon_{Gsf}", 0,1.2, 20,150, -9999, 1);
  //
  //make_tdrStyle_plots("EleGsfEffPlotData.root", "SuperClusterToGsfElectronPATTag/Gsf_eta/fit_eff_plots/probe_eta_PLOT",
  //      	      "EleGsfEffPlotMC.root",   "SuperClusterToGsfElectronPATTag/Gsf_eta/fit_eff_plots/probe_eta_PLOT",
  //      	      "Gsf_eta", "Gsf efficiency vs eta", "Probe #eta", "#epsilon_{Gsf}", 0,1.2, 20,150, -9999);
  //
  //make_tdrStyle_plots("EleGsfEffPlotData.root", "SuperClusterToGsfElectronPATTag/Gsf_pt20/fit_eff_plots/probe_pt_PLOT_probe_abseta_bin0",
  //      	      "EleGsfEffPlotMC.root",   "SuperClusterToGsfElectronPATTag/Gsf_pt20/fit_eff_plots/probe_pt_PLOT_probe_abseta_bin0",
  //      	      "Gsf_pt20", "Gsf efficiency in pt bin [20,200]", "Probe p_{T} [GeV]", "#epsilon_{Gsf}", 0,1.2, 20,200, -9999);
  
  
  
  /*
  */
  /*
// SingleMu Triggers
HLT_Mu5  // Not enought stat (Prescaled)
HLT_Mu12 // Not enought stat (Prescaled)
HLT_Mu24 // Not simulated
HLT_IsoMu24 // Not simulated
HLT_IsoMu30 // Not simulated
HLT_IsoMu15_eta2p1_L1ETM20
HLT_IsoMu20_eta2p1
HLT_IsoMu24_eta2p1
HLT_IsoMu30_eta2p1
HLT_IsoMu34_eta2p1
HLT_IsoMu40_eta2p1
  
// MuHad Cross Triggers
HLT_Mu40_HT200 // No events passing
HLT_Mu40_FJHT200
HLT_Mu40_PFHT350
HLT_Mu60_PFHT350
HLT_PFHT400_Mu5_PFMET45
HLT_PFHT400_Mu5_PFMET50
HLT_PFHT350_Mu15_PFMET45
HLT_PFHT350_Mu15_PFMET50
HLT_Mu60_PFNoPUHT350 // No events passing
HLT_Mu40_PFNoPUHT350 // No events passing
HLT_PFNoPUHT400_Mu5_PFMET45 // No events passing
HLT_PFNoPUHT400_Mu5_PFMET50 // No events passing
HLT_PFNoPUHT350_Mu15_PFMET45 // No events passing
HLT_PFNoPUHT350_Mu15_PFMET50 // No events passing
  
// SingleElectron Triggers
HLT_Ele22_CaloIdL_CaloIsoVL  // No Events passing (off)
HLT_Ele27_CaloIdL_CaloIsoVL  // Trigger not exist?
HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
HLT_Ele30_CaloIdVT_TrkIdT
HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL
HLT_Ele65_CaloIdVT_TrkIdT // Not enough stat
HLT_Ele80_CaloIdVT_TrkIdT // Not enough stat
HLT_Ele80_CaloIdVT_GsfTrkIdT // Not exist?
HLT_Ele90_CaloIdVT_GsfTrkIdT // Not exist?
HLT_Ele100_CaloIdVT_TrkIdT // Not enough stat
  */

  // Cross Validation
  /*
  make_tdrStyle_plots("EffPlotMC2012_MuonPogCrossValidation.root",
		      "fitHltFromGlb/pt_HLTIsoMu24eta2p1_POG/fit_eff_plots/pt_PLOT;", 
		      "IsoMu24eta2p1_pt_RA4","HLT_IsoMu24_eta2p1 RA4 (Cross Validation)", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_IsoMu24_eta2p1}");

  make_tdrStyle_plots_NoFit("EffPlotMC2012_MuonPogCrossValidation.root",
			    "fitHltFromGlb/eta_HLTIsoMu24eta2p1_POG/fit_eff_plots/eta_PLOT;", 
			    "IsoMu24eta2p1_eta_RA4","HLT_IsoMu24_eta2p1 RA4 (Cross Validation)", "Probe #eta", "#epsilon_{HLT_IsoMu24_eta2p1}");
  
  make_tdrStyle_plots("EffMc_Muon_POG.root",
		      "tpTree/passing_pt_HLT_IsoMu24_eta2p1_POG/fit_eff_plots/pt_PLOT;", 
		      "IsoMu24eta2p1_pt_POG","HLT_IsoMu24_eta2p1 Muon POG", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_IsoMu24_eta2p1}");

  make_tdrStyle_plots_NoFit("EffMc_Muon_POG.root",
			    "tpTree/passing_eta_HLT_IsoMu24_eta2p1_POG/fit_eff_plots/eta_PLOT;", 
			    "IsoMu24eta2p1_eta_POG","HLT_IsoMu24_eta2p1 Muon POG", "Probe #eta", "#epsilon_{HLT_IsoMu24_eta2p1}");

  // SingleMu Triggers
  // IsoMu24_eta2p1
  make_tdrStyle_plots("EffPlotData2012_IsoMu24eta2p1.root",
		      "fitHltFromGlb/pt_HLTIsoMu24eta2p1/fit_eff_plots/pt_PLOT;", 
		      "IsoMu24eta2p1_pt","HLT_IsoMu24_eta2p1 pt", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_IsoMu24_eta2p1}");
  
  make_tdrStyle_plots_NoFit("EffPlotData2012_IsoMu24eta2p1.root",
			    "fitHltFromGlb/eta_HLTIsoMu24eta2p1/fit_eff_plots/eta_PLOT;", 
			    "IsoMu24eta2p1_eta","HLT_IsoMu24_eta2p1 eta", "Probe #eta", "#epsilon_{HLT_IsoMu24_eta2p1}");  
  
  make_tdrStyle_plots_NoFit("EffPlotData2012_IsoMu24eta2p1.root",
			    "fitHltFromGlb/nvtx_HLTIsoMu24eta2p1/fit_eff_plots/tag_nVertices_PLOT;", 
			    "IsoMu24eta2p1_nvtx","HLT_IsoMu24_eta2p1 nvtx", "N_{Vertices}", "#epsilon_{HLT_IsoMu24_eta2p1}");  
  
  make_tdrStyle_plots_NoFit("EffPlotData2012_IsoMu24eta2p1.root",
			    "fitHltFromGlb/reliso_HLTIsoMu24eta2p1/fit_eff_plots/pfreliso_PLOT;", 
			    "IsoMu24eta2p1_reliso","HLT_IsoMu24_eta2p1 reliso", "Rel. Islation (#Delta#beta = 0.3)", "#epsilon_{HLT_IsoMu24_eta2p1}");
  
  // IsoMu24
  make_tdrStyle_plots("EffPlotData2012_IsoMu24.root",
		      "fitHltFromGlb/pt_HLTIsoMu24/fit_eff_plots/pt_PLOT;", 
		      "IsoMu24_pt","HLT_IsoMu24_ pt", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_IsoMu24}");
  
  make_tdrStyle_plots_NoFit("EffPlotData2012_IsoMu24.root",
			    "fitHltFromGlb/eta_HLTIsoMu24/fit_eff_plots/eta_PLOT;", 
			    "IsoMu24_eta","HLT_IsoMu24_ eta", "Probe #eta", "#epsilon_{HLT_IsoMu24}");  
  
  make_tdrStyle_plots_NoFit("EffPlotData2012_IsoMu24.root",
			    "fitHltFromGlb/nvtx_HLTIsoMu24/fit_eff_plots/tag_nVertices_PLOT;", 
			    "IsoMu24_nvtx","HLT_IsoMu24_ nvtx", "N_{Vertices}", "#epsilon_{HLT_IsoMu24}");  
  
  make_tdrStyle_plots_NoFit("EffPlotData2012_IsoMu24.root",
			    "fitHltFromGlb/reliso_HLTIsoMu24/fit_eff_plots/pfreliso_PLOT;", 
			    "IsoMu24_reliso","HLT_IsoMu24_ reliso", "Rel. Islation (#Delta#beta = 0.3)", "#epsilon_{HLT_IsoMu24}");
  // Mu15
  make_tdrStyle_plots("EffPlotData2012_Mu12.root",
		      "fitHltFromGlb/pt_HLTMu12/fit_eff_plots/pt_PLOT;", 
		      "Mu12_pt","HLT_Mu12 pt", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_Mu12}");

  // Cross Triggers
  // pt plots
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffptHLTMu40PFHT350/fit_eff_plots/pt_PLOT_tag_matchedHLT_Mu40_PFHT350_pass;", 
		      "Mu40PFHT350Eff_pt","HLT_Mu40_PFHT350 efficiency", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_Mu40_PFHT350}");

  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffptHLTMu60PFHT350/fit_eff_plots/pt_PLOT_tag_matchedHLT_Mu60_PFHT350_pass;", 
		      "Mu60PFHT350Eff_pt","HLT_Mu60_PFHT350 efficiency", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_Mu60_PFHT350}");

  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffptHLTPFHT350Mu15PFMET45/fit_eff_plots/pt_PLOT_tag_matchedHLT_PFHT350_Mu15_PFMET45_pass;", 
		      "PFHT350Mu15PFMET45Eff_pt","HLT_PFHT350_Mu15_PFMET45 efficiency", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_PFHT350_Mu15_PFMET45}");

  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffptHLTPFHT400Mu5PFMET45/fit_eff_plots/pt_PLOT_tag_matchedHLT_PFHT400_Mu5_PFMET45_pass;", 
		      "PFHT400Mu5PFMET45Eff_pt","HLT_PFHT400_Mu5_PFMET45 efficiency", "Probe p_{T} (GeV/c)", "#epsilon_{HLT_PFHT400_Mu5_PFMET45}");
  
  // ht plots
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffhtHLTMu40PFHT350/fit_eff_plots/tag_ht_PLOT_tag_matchedHLT_Mu40_PFHT350_pass;", 
		      "Mu40PFHT350Eff_ht","HLT_Mu40_PFHT350 efficiency", "Probe H_{T}", "#epsilon_{HLT_Mu40_PFHT350}");
  
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffhtHLTMu60PFHT350/fit_eff_plots/tag_ht_PLOT_tag_matchedHLT_Mu60_PFHT350_pass;", 
		      "Mu60PFHT350Eff_ht","HLT_Mu60_PFHT350 efficiency", "Probe H_{T}", "#epsilon_{HLT_Mu60_PFHT350}");
  
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffhtHLTPFHT350Mu15PFMET45/fit_eff_plots/tag_ht_PLOT_tag_matchedHLT_PFHT350_Mu15_PFMET45_pass;", 
		      "PFHT350Mu15PFMET45Eff_ht","HLT_PFHT350_Mu15_PFMET45 efficiency", "Probe H_{T}", "#epsilon_{HLT_PFHT350_Mu15_PFMET45}");
  
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffhtHLTPFHT400Mu5PFMET45/fit_eff_plots/tag_ht_PLOT_tag_matchedHLT_PFHT400_Mu5_PFMET45_pass;", 
		      "PFHT400Mu5PFMET45Eff_ht","HLT_PFHT400_Mu5_PFMET45 efficiency", "Probe H_{T}", "#epsilon_{HLT_PFHT400_Mu5_PFMET45}");
  
  // met
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffmetHLTPFHT350Mu15PFMET45/fit_eff_plots/tag_met_PLOT_tag_matchedHLT_PFHT350_Mu15_PFMET45_pass;", 
		      "PFHT350Mu15PFMET45Eff_met","HLT_PFHT350_Mu15_PFMET45 efficiency", "Probe #slash{E}_{T}", "#epsilon_{HLT_PFHT350_Mu15_PFMET45}");
  
  make_tdrStyle_plots("EffPlotData2012_MuHad.root", 
		      "fitHltFromGlb/EffmetHLTPFHT400Mu5PFMET45/fit_eff_plots/tag_met_PLOT_tag_matchedHLT_PFHT400_Mu5_PFMET45_pass;", 
		      "PFHT400Mu5PFMET45Eff_met","HLT_PFHT400_Mu5_PFMET45 efficiency", "Probe #slash{E}_{T}", "#epsilon_{HLT_PFHT400_Mu5_PFMET45}");

  // Electron

  // HLT_Ele27_WP80
  make_tdrStyle_plots("../RA4_TP_ZEE/ElectronEffPlotDataSingle2012.root",
		      "goodPATEleToHLT/EffptHLT_Ele27_WP80/fit_eff_plots/probe_gsfEle_et_PLOT_tag_HLT_Ele27_WP80_pass;", 
		      "HLT_Ele27_WP80_pt","HLT_Ele27_WP80 pt", "Probe E_{T} (GeV)", "#epsilon_{HLT_Ele27_WP80}");

  */
}
