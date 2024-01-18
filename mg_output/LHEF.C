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

   TFile *newfile = new TFile("histos.root","RECREATE");
   h_x_bbar_log->Write();
   h_x_b_log->Write();
   h_x_g_log->Write();
   h_x_other_log->Write();
   newfile->Close();
   
}
