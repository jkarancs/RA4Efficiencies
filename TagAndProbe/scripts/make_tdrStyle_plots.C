#include "TLine.h"

void SetPoint(TGraphAsymmErrors *g, TFile* f, std::string hn_data, std::string repl, int i, double xmin, double xmax) {
  hn_data.replace(hn_data.find("cumreliso"),9,repl);
  TCanvas* c = (TCanvas*)f->Get(hn_data.c_str());
  TGraphAsymmErrors *plot = c->GetPrimitive("hxy_fit_eff");
  
  Double_t x_data, y_data;
  plot->GetPoint(0, x_data, y_data);
  Double_t yh = plot->GetErrorYhigh(0);
  Double_t yl = plot->GetErrorYlow(0);

  g->SetPoint(i,(xmin+xmax)/2,y_data);
  g->SetPointError(i, (xmin+xmax)/2-xmin, xmax-(xmin+xmax)/2, yl, yh);
  
}


void make_tdrStyle_plots(std::string fn_data, std::string hn_data, 
			 std::string fn_mc, std::string hn_mc, 
			 std::string cn_name, std::string cn_title, std::string x_title, std::string y_title, 
			 double ymin, double ymax, double xmin = -9999, double xmax = -9999,
			 double avg = -9999, bool dofit = false, bool addMC = true, double xlabelsize = 0.05,
			 double p1=-9999, double p1min =-9999, double p1max =-9999, 
			 double p2=-9999, double p2min =-9999, double p2max =-9999, 
			 double p3=-9999, double p3min =-9999, double p3max =-9999) {
  setTDRStyle();
  tdrGrid(true);
  gROOT->SetStyle("tdrStyle");

  //std::cout<<fn_data<<","<<hn_data<<std::endl;
  //std::cout<<fn_mc<<","<<hn_mc<<std::endl;
  
  TFile *fdata = TFile::Open(fn_data.c_str());
  TCanvas* can_data;
  TGraphAsymmErrors *data;
  
  if (hn_data.find("cumreliso")!=string::npos) {
    data = new TGraphAsymmErrors(9);
    SetPoint(data, fdata, hn_data, "reliso001", 0, 0.00, 0.01);
    SetPoint(data, fdata, hn_data, "reliso002", 1, 0.01, 0.02);
    SetPoint(data, fdata, hn_data, "reliso004", 2, 0.02, 0.04);
    SetPoint(data, fdata, hn_data, "reliso006", 3, 0.04, 0.06);
    SetPoint(data, fdata, hn_data, "reliso009", 4, 0.06, 0.09);
    SetPoint(data, fdata, hn_data, "reliso012", 5, 0.09, 0.12);
    SetPoint(data, fdata, hn_data, "reliso015", 6, 0.12, 0.15);
    SetPoint(data, fdata, hn_data, "reliso020", 7, 0.15, 0.20);
    SetPoint(data, fdata, hn_data, "reliso025", 8, 0.20, 0.25);
  } else {
    can_data = (TCanvas*)fdata->Get(hn_data.c_str());
    if (can_data==0) {
      std::cout<<"Error: Bad filename/path given: "<<std::endl;
      std::cout<<fn_data<<std::endl;
      std::cout<<hn_data<<std::endl;
      std::cout<<std::endl;    
    } else {
      data = (TGraphAsymmErrors*)can_data->GetPrimitive("hxy_fit_eff");
    }
  }
  
  TGraphAsymmErrors *mc;
  TGraphAsymmErrors *ratio = data->Clone();
  double eff_lastbin_data = 0;
  if (addMC) {
    TFile *fmc = TFile::Open(fn_mc.c_str());
    
    if (hn_mc.find("cumreliso")!=string::npos) {
      mc = new TGraphAsymmErrors(9);
      SetPoint(mc, fmc, hn_mc, "reliso001", 0, 0.00, 0.01);
      SetPoint(mc, fmc, hn_mc, "reliso002", 1, 0.01, 0.02);
      SetPoint(mc, fmc, hn_mc, "reliso004", 2, 0.02, 0.04);
      SetPoint(mc, fmc, hn_mc, "reliso006", 3, 0.04, 0.06);
      SetPoint(mc, fmc, hn_mc, "reliso009", 4, 0.06, 0.09);
      SetPoint(mc, fmc, hn_mc, "reliso012", 5, 0.09, 0.12);
      SetPoint(mc, fmc, hn_mc, "reliso015", 6, 0.12, 0.15);
      SetPoint(mc, fmc, hn_mc, "reliso020", 7, 0.15, 0.20);
      SetPoint(mc, fmc, hn_mc, "reliso025", 8, 0.20, 0.25);
    } else {
      TCanvas* can_mc = fmc->Get(hn_data.c_str());
      if (can_mc==0) {
	std::cout<<"Error: Bad filename/path given: "<<std::endl;
	std::cout<<fn_mc<<std::endl;
	std::cout<<hn_mc<<std::endl;
	std::cout<<std::endl;    
      } else {
	mc = (TGraphAsymmErrors*)can_mc->GetPrimitive("hxy_fit_eff");
      }
    }

    for (Int_t i=0; i<ratio->GetN(); i++) {
      Double_t x_data, y_data;
      data->GetPoint(i, x_data, y_data);
      Double_t xh_data = data->GetErrorXhigh(i);
      Double_t xl_data = data->GetErrorXlow(i);
      Double_t yh_data = data->GetErrorYhigh(i);
      Double_t yl_data = data->GetErrorYlow(i);
      eff_lastbin_data =  y_data;
      Double_t x_mc, y_mc;
      mc->GetPoint(i, x_mc, y_mc);
      Double_t yh_mc = mc->GetErrorYhigh(i);
      Double_t yl_mc = mc->GetErrorYlow(i);
      if (y_mc==0.) continue;
      
      Double_t y_ratio = y_data/y_mc;
      Double_t yh = sqrt((yh_data*yh_data)/(y_data*y_data) + (yh_mc*yh_mc)/(y_mc*y_mc))*y_ratio;
      //yh = TMath::Min(yh, 1.-y_ratio);
      if (y_data==0.) yh = yh_mc;
      Double_t yl = sqrt((yl_data*yl_data)/(y_data*y_data) + (yl_mc*yl_mc)/(y_mc*y_mc))*y_ratio;
      yl = TMath::Min(yl, y_ratio);
      
      ratio->SetPoint(i, x_data, y_ratio);
      ratio->SetPointError(i, xl_data, xh_data, yl, yh);
    }
  }
  
  TCanvas *can = new TCanvas(cn_name.c_str(), cn_title.c_str(),200,10,600,600);
  data->GetXaxis()->SetTitle(x_title.c_str());
  data->GetYaxis()->SetTitle(y_title.c_str());
  if (xmin!=-9999) data->GetXaxis()->SetRangeUser(xmin, xmax);
  /*
  data->GetXaxis()->SetTitleSize(0.05);
  data->GetYaxis()->SetTitleSize(0.06);
  data->GetYaxis()->SetRangeUser(0, 1.1);
  data->SetMarkerStyle(20);
  data->SetMarkerSize(2);
  */
  data->Draw("AP");
  if (addMC) {
    mc->Draw("SAMEP");
    ratio->Draw("SAMEP");
    if (avg != -9999) {
      if (cn_name.find("ID_eta")==string::npos) {
        TLine* line = new TLine((xmin != -9999) ? xmin : data->GetXaxis()->GetXmin(),avg,
      			  (xmax != -9999) ? xmax : data->GetXaxis()->GetXmax(),avg); 
        line->SetLineColor(8);
        line->SetLineWidth(2);
        line->Draw();
      } else {
        TLine* line = new TLine(-2.5,0.8725,-1.5,0.8725); line->SetLineColor(8); line->SetLineWidth(2); line->Draw();	  
        line = new TLine(-1.5,0.99,1.5,0.99); line->SetLineColor(8); line->SetLineWidth(2); line->Draw();	  
        line = new TLine(1.5,0.8725,2.5,0.8725); line->SetLineColor(8); line->SetLineWidth(2); line->Draw();
      }
    }
  }
  
  
  if (dofit) {
    double turnon=0;
    std::string trigger = cn_name;
    if (trigger.find("Mu")!=string::npos) {
      std::stringstream ss;
      for (size_t j=trigger.find("Mu")+2; j<trigger.size(); j++) ss<<trigger[j];
      ss>>turnon;
      trigger.erase(trigger.find("_pt"),3);
    } else if (trigger.find("Ele")!=string::npos) {
      std::stringstream ss;
      for (size_t j=trigger.find("Ele")+3; j<trigger.size(); j++) ss<<trigger[j];
      ss>>turnon;
      trigger.erase(trigger.find("_et"),3);
    }
    
    std::stringstream ss1;
    std::stringstream ss2;
    std::stringstream ss3;
    double max_reached = 0;
    TF1* f;
    //if (trigger.find("Mu5_")==string::npos) {
    f = new TF1("turnon", "[0]/(1+exp(([1]-x)/[2]))", 
      	  (xmin != -9999) ? xmin : data->GetXaxis()->GetXmin(),
      	  (xmax != -9999) ? xmax : data->GetXaxis()->GetXmax());
    f->SetParameter(0, (p1==-9999) ? eff_lastbin_data : p1);
    f->SetParameter(1, (p2==-9999) ? turnon : p2);
    f->SetParameter(2, (p3==-9999) ? 1 : p3);
    if (p1min != 9999) f->SetParLimits(0, (p1min==-9999) ? 0.8 : p1min, (p1max==-9999) ? 1 : p1max);
    if (p2min != 9999) f->SetParLimits(1, (p2min==-9999) ? turnon-5 : p2min, (p2max==-9999) ? turnon+5 : p2max);
    if (p3min != 9999) f->SetParLimits(2, (p3min==-9999) ? 0.5 : p3min, (p3max==-9999) ? 3 : p3max);
    //f->SetParameter(1, -30);
    //f->SetParameter(2, 30);
    //f->SetParLimits(0, 0.9925, 0.9955);
    //f->SetParLimits(1, -10, 10);
    //f->SetParLimits(2, 2, 20);
    //f->SetParLimits(1, -100, 70);
    //f->SetParLimits(2, 0, 100);
    f->SetLineColor(1);
    f->SetLineStyle(2);
    data->Fit("turnon","RMWQ");
    ss1<<"#epsilon_{Plateau}  "<<std::setprecision(3)<<f->GetParameter(0)<<" #pm "<<std::setprecision(1)<<f->GetParError(0);
    ss2<<"Turnon  "<<std::setprecision(3)<<f->GetParameter(1);
    ss3<<"Width  "<<std::setprecision(2)<<f->GetParameter(2);
    
    // std::cout<<"Trigger: "<<trigger<<std::endl;
    // std::cout<<"Eff - Plateau  "<<std::setprecision(4)<<f->GetParameter(0)<<" +- "<<f->GetParError(0)<<std::endl;
    // std::cout<<"Turnon         "<<std::setprecision(4)<<f->GetParameter(1)<<" +- "<<f->GetParError(1)<<std::endl;
    // std::cout<<"Width          "<<std::setprecision(4)<<f->GetParameter(2)<<" +- "<<f->GetParError(2)<<std::endl;
    
    max_reached = f->GetParameter(1) + f->GetParameter(2)*5;
    //} else {
    //  f = new TF1("flat", "[0]", data->GetXaxis()->GetXmin(), data->GetXaxis()->GetXmax());
    //  f->SetLineColor(1);
    //  f->SetLineStyle(2);
    //  f->SetParameter(0, eff_lastbin_data);
    //  f->SetParLimits(0, 0.8, 1);
    //  data->Fit("flat","RMQ");
    //  ss1<<"#epsilon_{Plateau}  "<<std::setprecision(3)<<f->GetParameter(0)<<" #pm "<<std::setprecision(1)<<f->GetParError(0);
    //}
    
    // Find largest deviation from plateau
    double devmax = 0;
    double stdev = 0;
    int n = 0;
    for (Int_t i=0; i<ratio->GetN(); i++) {
      Double_t x_data, y_data;
      data->GetPoint(i, x_data, y_data);
      if (x_data>max_reached&&fabs(y_data-f->GetParameter(0))>devmax) devmax = fabs(y_data-f->GetParameter(0));
      if (x_data>max_reached) {
      stdev += (y_data-f->GetParameter(0))*(y_data-f->GetParameter(0));
      n++;
      }
    }
    printf("%s %*s %.1lf  +-  %.1lf %%\tCut: %d GeV\n", std::string("HLT_"+trigger).c_str(), 35-std::string("HLT_"+trigger).size(), "Eff:", f->GetParameter(0)*100, sqrt(stdev/n)*100, ceil(max_reached));
    
    //TPaveStats *ptstats = new TPaveStats(0.6, (trigger.find("Mu5_")==string::npos) ? 0.85 : 0.95, 0.95, 1,"brNDC");
    TPaveStats *ptstats = new TPaveStats(0.6, 0.85, 0.95, 1,"brNDC");
    ptstats->SetName("stats");
    ptstats->SetBorderSize(1);
    ptstats->SetFillColor(0);
    ptstats->SetTextAlign(11);
    ptstats->SetTextFont(42);
    ptstats->SetTextSize(0.05);
    TText *text = ptstats->AddText(ss1.str().c_str());
    //if (trigger.find("Mu5_")==string::npos) {
    text = ptstats->AddText(ss2.str().c_str());
    text = ptstats->AddText(ss3.str().c_str());
    //}
    ptstats->SetOptStat(0);
    ptstats->SetOptFit(1);
    ptstats->Draw();
    data->GetListOfFunctions()->Add(ptstats);
    ptstats->SetParent(data->GetListOfFunctions());
  }
  
  TLegend *leg = new TLegend(0.4,0.2,0.6,0.4,"");
  leg->AddEntry(data, "Data", "lp");
  if (addMC) {
    leg->AddEntry(mc, "MC", "lp");
    leg->AddEntry(ratio, "Data/MC", "lp");
  }
  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetTextSize(0.04);
  leg->Draw();
  
  can->UseCurrentStyle();
  data->GetXaxis()->SetLabelSize(xlabelsize);
  data->SetMarkerColor(1);
  data->SetMarkerStyle(20);
  data->SetLineColor(1);
  data->SetMaximum(ymax);
  data->SetMinimum(ymin);
  if (addMC) {
    mc->SetMarkerColor(2);
    mc->SetMarkerStyle(21);
    mc->SetLineColor(2);
    ratio->SetMarkerColor(3);
    ratio->SetMarkerStyle(22);
    ratio->SetLineColor(3);
  }
  
  //can->SaveAs(std::string("Plots_C/"    + cn_name + ".C"   ).c_str());
  //can->SaveAs(std::string("Plots_eps/"  + cn_name + ".eps" ).c_str());
  //can->SaveAs(std::string("Plots_png/"  + cn_name + ".png" ).c_str());
  //can->SaveAs(std::string("Plots_root/" + cn_name + ".root").c_str());
  
  if (addMC) fmc->Close();
  fdata->Close();
}
