from math import sqrt
import ROOT
import os
from collections import OrderedDict
class ESplotter:
    def __init__(self,_name):
        self.name=_name
        self._mydict=OrderedDict()
        self.norm_type=0
    def SetNormType(self,_doNorm):
        self.norm_type=_doNorm
    def AddHist(self,_path,_name,_title):
        _h=self.tfile.Get(_path)
        norm=1
        if self.norm_type==1:
            norm=1/_h.Integral()
        elif self.norm_type==2:
            norm=1/_h.GetMaximum()
        _h.Scale(norm)
        self._mydict[_name]={
            "hist":_h.Clone(),
            "name":_name,
            "title":_title
        }

    def AddHist2(self,_path2,_name2,_title2):
        _h=self.tfile.Get(_path2)
        norm=1
        if self.norm_type==1:
            norm=1/_h.Integral()
        elif self.norm_type==2:
            norm=1/_h.GetMaximum()
        _h.Scale(norm)
        self._mydict[_name]={
            "hist2":_h.Clone(),
            "name2":_name2,
            "title2":_title2
        }

    def GetInfo(self,_name):
        return self._mydict[_name]

    def SetName(self, _name):
        self.name=_name
    def SetDeno(self, _deno):
        self.deno=_deno
    def SetRatioHist(self,p):
        hdeno = self._mydict[self.deno]['hist']
        h = self._mydict[p]['hist'] 
        hratio = h.Clone("hratio")
        hratio.SetStats(0)
        hratio.Divide(hdeno)

        hdeno2 = self._mydict[self.deno2]['hist2']
        h = self._mydict[p]['hist2']
        hratio2 = h.Clone("hratio2")
        hratio2.SetStats(0)
        hratio2.Divide(hdeno2)

        #return h3
        self._mydict[p]['hratio']=hratio.Clone()
        self._mydict[p]['hratio2']=hratio2.clone()
        ##---set Poisson error
        for j in range(1,self._mydict[p]['hratio'].GetNbinsX()+1):
            y=self._mydict[p]['hist'].GetBinContent(j)
            yerr=self._mydict[p]['hist'].GetBinError(j)
            ydeno=self._mydict[self.deno]['hist'].GetBinContent(j)
            ydenoerr=self._mydict[self.deno]['hist'].GetBinError(j)
            if y>0 and ydeno>0:
                total_relerr=sqrt(  (yerr/y)**2+(ydenoerr/ydeno)**2)
                total_err=total_relerr*y/ydeno
            else:
                total_relerr=0.
                total_err=0.
            self._mydict[p]['hratio'].SetBinError(j,total_err)

        for j in range(1,self._mydict[p]['hratio2'].GetNbinsX()+1):
            y=self._mydict[p]['hist2'].GetBinContent(j)
            yerr=self._mydict[p]['hist2'].GetBinError(j)
            ydeno=self._mydict[self.deno2]['hist2'].GetBinContent(j)
            ydenoerr=self._mydict[self.deno2]['hist2'].GetBinError(j)
            if y>0 and ydeno>0:
                total_relerr=sqrt(  (yerr/y)**2+(ydenoerr/ydeno)**2)
                total_err=total_relerr*y/ydeno
            else:
                total_relerr=0.
                total_err=0.
            self._mydict[p]['hratio2'].SetBinError(j,total_err)
            #if y>0:
            #    print "<",j,">"
            #    print "y->",y
            #    print "yerr->",yerr
            #    print "ydeno->",ydeno
            #    print "ydenoerr->",ydenoerr
            #    print "ratio err", self._mydict[p]['hratio'].GetBinError(j)

    def DrawRatio(self):
        self.canvas2=ROOT.TCanvas("c2","c2",800,800)
        self.pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        self.pad1.SetBottomMargin(0.05)
        self.pad1.SetGridx()
        self.pad1.Draw()
        self.pad1.cd()
        ##--draw hist
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist'].Draw()
            else:
                self._mydict[p]['hist'].Draw('sames')
            self._mydict[p]['hist'].SetStats(0)
            self._mydict[p]['hist'].GetYaxis().SetTitle(self.ytitle)
        ##--legend
        self.leg2=ROOT.TLegend(0.1, 0.7, 0.3, 0.9)
        for p in self._mydict:
            self.leg2.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
            self.leg2.SetTextSize(0.05)
        self.leg2.Draw()
        ##--create pad2
        self.canvas2.cd()    
        self.pad2=ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        self.pad2.SetTopMargin(0.2)
        self.pad2.SetBottomMargin(0.2)
        self.pad2.SetGridy()
        self.pad2.Draw()
        self.pad2.cd()
        i=0
        for p in self._mydict:
            if p==self.deno:continue
            self.SetRatioHist(p)
            ##-->Now we have self._mydict[proc]['hratio'] obejcts
            
            if i==0:
                self._mydict[p]['hratio'].Draw("e1")
            else:
                self._mydict[p]['hratio'].Draw('e1sames')
            i+=1
            self._mydict[p]['hratio'].SetTitle("")
            #self._mydict[p]['hratio'].SetLineColor(1)
            self._mydict[p]['hratio'].SetMaximum(1.5)
            self._mydict[p]['hratio'].SetMinimum(0.5)
            self._mydict[p]['hratio'].GetYaxis().SetNdivisions(6)
            self._mydict[p]['hratio'].GetYaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio'].GetXaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio'].GetXaxis().SetTitle(self.xtitle)
            self._mydict[p]['hratio'].GetXaxis().SetTitleSize(0.1)
            self._mydict[p]['hratio'].GetYaxis().SetTitle("Ratio To "+self.deno)
            self._mydict[p]['hratio'].GetYaxis().SetTitleSize(0.06)
        
        self.canvas2.cd()
        self.canvas2.SaveAs("output/ratio__"+self.name+".pdf")

    def DrawRatio2(self):
        self.canvas3=ROOT.TCanvas("c3","c3",800,800)
        self.pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 0.5, 1.0)
        self.pad1.SetBottomMargin(0.05)
        self.pad1.SetGridx()
        self.pad1.Draw()
        self.pad1.cd()
        ##--draw hist
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist'].Draw()
            else:
                self._mydict[p]['hist'].Draw('sames')
            self._mydict[p]['hist'].SetStats(0)
            self._mydict[p]['hist'].GetYaxis().SetTitle(self.ytitle)
        ##--legend
        self.leg2=ROOT.TLegend(0.1, 0.7, 0.3, 0.9)
        for p in self._mydict:
            self.leg2.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
            self.leg2.SetTextSize(0.05)
        self.leg2.Draw()
        ##--create pad2
        self.canvas3.cd()
        self.pad2=ROOT.TPad("pad2", "pad2", 0, 0.05, 0.5, 0.3)
        self.pad2.SetTopMargin(0.2)
        self.pad2.SetBottomMargin(0.2)
        self.pad2.SetGridy()
        self.pad2.Draw()
        self.pad2.cd()
        i=0
        for p in self._mydict:
            if p==self.deno:continue
            self.SetRatioHist(p)
            ##-->Now we have self._mydict[proc]['hratio'] obejcts

            if i==0:
                self._mydict[p]['hratio'].Draw("e1")
            else:
                self._mydict[p]['hratio'].Draw('e1sames')
            i+=1
            self._mydict[p]['hratio'].SetTitle("")
            #self._mydict[p]['hratio'].SetLineColor(1)
            self._mydict[p]['hratio'].SetMaximum(1.5)
            self._mydict[p]['hratio'].SetMinimum(0.5)
            self._mydict[p]['hratio'].GetYaxis().SetNdivisions(6)
            self._mydict[p]['hratio'].GetYaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio'].GetXaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio'].GetXaxis().SetTitle(self.xtitle)
            self._mydict[p]['hratio'].GetXaxis().SetTitleSize(0.1)
            self._mydict[p]['hratio'].GetYaxis().SetTitle("Ratio To "+self.deno)
            self._mydict[p]['hratio'].GetYaxis().SetTitleSize(0.06)

	##--create pad3
        self.canvas3=ROOT.TCanvas("c3","c3",800,800)
        self.pad3 = ROOT.TPad("pad3", "pad3", 0.5, 0.3, 1, 1.0)
        self.pad3.SetBottomMargin(0.05)
        self.pad3.SetGridx()
        self.pad3.Draw()
        self.pad3.cd()
        ##--draw hist
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist2'].Draw()
            else:
                self._mydict[p]['hist2'].Draw('sames')
            self._mydict[p]['hist2'].SetStats(0)
            self._mydict[p]['hist2'].GetYaxis().SetTitle(self.ytitle)
        ##--legend
        self.leg2=ROOT.TLegend(0.1, 0.7, 0.3, 0.9)
        for p in self._mydict:
            self.leg2.AddEntry(self._mydict[p]['hist2'], self._mydict[p]["name2"])
            self.leg2.SetTextSize(0.05)
        self.leg2.Draw()
        ##--create pad4
        self.canvas3.cd()
        self.pad4=ROOT.TPad("pad4", "pad4", 0.5, 0.05, 1, 0.3)
        self.pad4.SetTopMargin(0.2)
        self.pad4.SetBottomMargin(0.2)
        self.pad4.SetGridy()
        self.pad4.Draw()
        self.pad4.cd()
        i=0
        for p in self._mydict:
            if p==self.deno2:continue
            self.SetRatioHist(p)
            ##-->Now we have self._mydict[proc]['hratio'] obejcts

            if i==0:
                self._mydict[p]['hratio2'].Draw("e1")
            else:
                self._mydict[p]['hratio2'].Draw('e1sames')
            i+=1
            self._mydict[p]['hratio2'].SetTitle("")
            #self._mydict[p]['hratio2'].SetLineColor(1)
            self._mydict[p]['hratio2'].SetMaximum(1.5)
            self._mydict[p]['hratio2'].SetMinimum(0.5)
            self._mydict[p]['hratio2'].GetYaxis().SetNdivisions(6)
            self._mydict[p]['hratio2'].GetYaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio2'].GetXaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio2'].GetXaxis().SetTitle(self.xtitle)
            self._mydict[p]['hratio2'].GetXaxis().SetTitleSize(0.1)
            self._mydict[p]['hratio2'].GetYaxis().SetTitle("Ratio To "+self.deno2)
            self._mydict[p]['hratio2'].GetYaxis().SetTitleSize(0.06)

        self.canvas3.cd()
        self.canvas3.SaveAs("output/ratio__"+self.name+".pdf")

    def SetTitle(self,_title):
        for p in self._mydict:
            self._mydict[p]["hist"].SetTitle(_title)
    def SetXTitle(self,_title):
        self.xtitle=_title
        #for p in self._mydict:
        #    self._mydict[p]["hratio"].GetXaxis().SetTitle(_title)
    def SetYTitle(self,_title):
        self.ytitle=_title
        #for p in self._mydict:
        #    self._mydict[p]["hratio"].GetYaxis().SetTitle(_title)
    def SetLineColor(self,_name, _color):
        self._mydict[_name]['hist'].SetLineColor(_color)
	self._mydict[_name]['hist2'].SetLineColor(_color)
    def SaveAs(self, _path):
        self.canvas.SaveAs(_path)
    def ReadFile(self, _filepath):
        self.tfile=ROOT.TFile.Open(_filepath)
    
        
if __name__ == '__main__':
    myplotter=plotter("s_sbar")
    _maindir = os.getenv("_maindir_pyroot_git")
    filepath=_maindir+"/mg_output/histos_ssbar.root"   
    myplotter.ReadFile(filepath)
    myplotter.AddHist('log_x_s','s','s')
    myplotter.AddHist('log_x_sbar','sbar','#bar{s}')

    myplotter.SetTitle("pp->l vl")
    myplotter.SetXTitle("x")
    myplotter.SetYTitle("Events")
    myplotter.SetLineColor('sbar',2)
    myplotter.SetLineColor('s',4)
    ##--NorRatioPlot
    myplotter.DrawNoRatio()
    ##--RatioPlot
    myplotter.SetDeno("s")
    myplotter.DrawRatio()
    

        
