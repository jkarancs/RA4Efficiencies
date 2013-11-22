#include <iomanip> 

void make_tdrStyle_plots(std::string fn_data, std::string hn_data, std::string cn_name, std::string cn_title, std::string x_title, std::string y_title) {
  setTDRStyle();
  tdrGrid(true);
  gROOT->SetStyle("tdrStyle");
  
  TFile fdata(fn_data.c_str());
  TCanvas* can_data = (TCanvas*)fdata.Get(hn_data.c_str());
  TGraphAsymmErrors *data = can_data->GetPrimitive("hxy_fit_eff");
    
  Eff_pt = new TCanvas(cn_name.c_str(), cn_title.c_str(),200,10,600,600);
  Eff_pt->Draw();
  data->GetXaxis()->SetTitle(x_title.c_str());
  data->GetYaxis()->SetTitle(y_title.c_str());
  data->GetXaxis()->SetTitleSize(0.05);
  data->GetYaxis()->SetTitleSize(0.06);
  data->GetYaxis()->SetRangeUser(0, 1.1);
  data->SetMarkerStyle(20);
  data->SetMarkerSize(1);
  data->Draw("AP");

  TF1* f = new TF1("turnon", "[0]/(1+exp(([1]-x)/[2]))", data->GetXaxis()->GetXmin(), data->GetXaxis()->GetXmax());
  f->SetParLimits(0, 0.5, 1);
  f->SetParLimits(1, 5, 70);
  f->SetParLimits(2, 0, 9);
  //f->SetParLimits(1, -100, 70);
  //f->SetParLimits(2, 0, 100);
  f->SetLineColor(1);
  f->SetLineWidth(2);
  data->Fit("turnon","RMQ");
  //gStyle->SetOptFit(1);
  
  std::stringstream ss1;
  ss1<<"#epsilon_{Plateau}  "<<std::setprecision(4)<<f->GetParameter(0)<<" #pm "<<f->GetParError(0);
  std::stringstream ss2;
  ss2<<"Turnon  "<<std::setprecision(4)<<f->GetParameter(1)<<" #pm "<<f->GetParError(1)<<" ";
  std::stringstream ss3;
  ss3<<"Width  "<<std::setprecision(4)<<f->GetParameter(2)<<" #pm "<<f->GetParError(2)<<" ";

  TPaveStats *ptstats = new TPaveStats(0.7, 0.88, 1, 1,"brNDC");
  ptstats->SetName("stats");
  ptstats->SetBorderSize(1);
  ptstats->SetFillColor(0);
  ptstats->SetTextAlign(11);
  ptstats->SetTextFont(42);
  ptstats->SetTextSize(0.025);
  TText *text = ptstats->AddText(ss1.str().c_str());
  text = ptstats->AddText(ss2.str().c_str());
  text = ptstats->AddText(ss3.str().c_str());
  ptstats->SetOptStat(0);
  ptstats->SetOptFit(1);
  ptstats->Draw();
  data->GetListOfFunctions()->Add(ptstats);
  ptstats->SetParent(data->GetListOfFunctions());

  TLegend *leg = new TLegend(0.7,0.2,0.9,0.4,"");
  leg->AddEntry(data, "Data", "lp");
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetTextSize(0.04);
  leg->Draw();

  Eff_pt->UseCurrentStyle();
  data->SetMarkerColor(1);
  data->SetMarkerStyle(20);
  data->SetLineColor(1);
  data->SetMaximum(1.1);
  data->SetMinimum(0.);

  fdata.Close();
}
