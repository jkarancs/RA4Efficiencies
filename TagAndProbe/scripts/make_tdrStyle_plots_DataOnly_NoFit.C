#include <iomanip> 

void make_tdrStyle_plots_NoFit(std::string fn_data, std::string hn_data, std::string cn_name, std::string cn_title, std::string x_title, std::string y_title) {
  setTDRStyle();
  tdrGrid(true);
  gROOT->SetStyle("tdrStyle");
  
  TFile fdata(fn_data.c_str());
  TCanvas* can_data = (TCanvas*)fdata.Get(hn_data.c_str());
  TGraphAsymmErrors *data = can_data->GetPrimitive("hxy_fit_eff");
    
  Eff_pt = new TCanvas(cn_name.c_str(), cn_title.c_str(),200,10,600,600);
  //Eff_pt->Draw();
  data->GetXaxis()->SetTitle(x_title.c_str());
  data->GetYaxis()->SetTitle(y_title.c_str());
  //data->GetXaxis()->SetLabelSize(0.04);
  data->GetXaxis()->SetTitleSize(0.05);
  data->GetYaxis()->SetTitleSize(0.06);
  data->GetYaxis()->SetRangeUser(0, 1.1);
  data->SetMarkerStyle(20);
  data->SetMarkerSize(2);
  data->Draw("AP");

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
