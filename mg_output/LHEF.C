#define LHEF_cxx
#include "LHEF.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <unordered_map>
void LHEF::Loop()
{
//   In a ROOT session, you can do:
//      root> .L LHEF.C
//      root> LHEF t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;



   TH1D *h_x_g_log = new TH1D("log_x_g","log(x scale)",100,-5,0);
   TH1D *h_x_b_log = new TH1D("log_x_b","x_b",100,-5,0);
   TH1D *h_x_bbar_log = new TH1D("log_x_bbar","x_bbar",100,-5,0);
   TH1D *h_x_other_log = new TH1D("log_x_other","x_other",100,-5,0);


   
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
   
      
      for(unsigned int ip = 0; ip <  Particle_size; ip++){
	double E = Particle_E[ip];
	double px = Particle_Px[ip];
	double py = Particle_Py[ip];
	double pz = Particle_Pz[ip];
	int status = Particle_Status[ip];
	int pid  = Particle_PID[ip];
	if(status==-1){
	  //--gluon x
	  if(pid==21){
	    double _x = E/6500.; // proton energy = 6500GeV, gluon's energy fraction E/6500 == x Bjorken Scale
	    h_x_g_log->Fill(log10(_x));
	    
	  }
	  else if(pid == 5){
	    double _x = E/6500.; // proton energy = 6500GeV, b's energy fraction E/6500 == x Bjorken Scale
	    h_x_b_log->Fill(log10(_x));
	  }

	  else if(pid == -5){
	    double _x = E/6500.; // proton energy = 6500GeV, bar's energy fraction E/6500 == x Bjorken Scale
	    h_x_bbar_log->Fill(log10(_x));
	  }
	  else{
	    double _x = E/6500.; // proton energy = 6500GeV, other's energy fraction E/6500 == x Bjorken Scale
	    h_x_other_log->Fill(log10(_x));
	  }
	}//[END] status==-1
      }//[END]particle loop  
   }//[END]Event Loop

   double _x1=0.1, _y1=0.7, _x2=0.5, _y2=0.9;
   TLegend *leg=new TLegend(_x1,_y1,_x2,_y2);
   leg->AddEntry(h_x_b_log,"b");
   leg->AddEntry(h_x_bbar_log,"#bar{b}");
   leg->Draw();



   TCanvas *cnew = new TCanvas("cnew", "canvas_new", 800, 800);
   TPad *pad1 = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
   pad1->SetBottomMargin(0); // Upper and lower plot are joined
   pad1->SetGridx();         // Vertical grid
   pad1->Draw();             // Draw the upper pad: pad1
   pad1->cd();               // pad1 becomes the current pad
   h_x_bbar_log->SetStats(0);          // No statistics on upper plot
   h_x_bbar_log->Draw();
   h_x_bbar_log->SetLineColor(2);
   h_x_bbar_log->SetTitle("x(b/#bar{b})");
   h_x_b_log->Draw("sames");
   h_x_b_log->SetLineColor(4);
   leg->Draw();
   h_x_b_log->SetStats(0);
   h_x_bbar_log->SetStats(0);
   cnew->cd();          // Go back to the main canvas before defining pad2

   double _ymax=max(h_x_bbar_log->GetMaximum(),h_x_b_log->GetMaximum());
   h_x_bbar_log->SetMaximum(_ymax);
   h_x_b_log->SetMaximum(_ymax);
   TPad *pad2 = new TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
   pad2->SetTopMargin(0);
   pad2->SetBottomMargin(0.2);
   pad2->SetGridx(); // vertical grid
   pad2->Draw();
   pad2->cd();       // pad2 becomes the current pad




   
   TH1D *hratio = (TH1D*)h_x_bbar_log->Clone("hratio");
   hratio->SetLineColor(kBlack);
   hratio->SetMinimum(0.5);  // Define Y ..
   hratio->SetMaximum(1.5); // .. range
   hratio->Sumw2();
   hratio->SetStats(0);      // No statistics on lower plot
   hratio->Divide(h_x_b_log);
   hratio->SetMarkerStyle(21);
   hratio->Draw("ep");       // Draw the ratio plot

   TLine *line = new TLine(-5,1,0,1);//TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
   line->Draw("same");
   line->SetLineColor(2);

   
   hratio->GetYaxis()->SetTitle("#bar{b}/b");
   hratio->GetYaxis()->SetNdivisions(505);
   hratio->GetYaxis()->SetTitleSize(20);
   hratio->GetYaxis()->SetTitleFont(43);
   hratio->GetYaxis()->SetTitleOffset(1.55);
   hratio->GetYaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
   hratio->GetYaxis()->SetLabelSize(15);

   hratio->GetXaxis()->SetTitleSize(20);
   hratio->GetXaxis()->SetTitleFont(43);
   hratio->GetXaxis()->SetTitleOffset(4.);
   hratio->GetXaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
   hratio->GetXaxis()->SetLabelSize(15);
   hratio->SetTitle("");
   cnew->SaveAs("ratio.pdf");
   
}
