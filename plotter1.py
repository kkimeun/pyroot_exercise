import ROOT
import os
from collections import OrderedDict
class plotter:
    def __init__(self,_name):
        self.name=_name
        self._mydict=OrderedDict()
    def AddHist(self,_path,_name,_title):
        _h=self.tfile.Get(_path)
        self._mydict[_name]={
            "hist":_h.Clone(),
            "name":_name,
            "title":_title
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
        #return h3
        self._mydict[p]['hratio']=hratio.Clone()

    def Draw(self):
        self.DrawNoRatio()

    def DrawNoRatio(self):
        ##---No RatioPlot--##
        self.canvas=ROOT.TCanvas("c1","c1",800,800)
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist'].Draw()
            else:
                self._mydict[p]['hist'].Draw('sames')
        self._mydict[p]['hist'].SetStats(0)
        self.leg=ROOT.TLegend(0.1, 0.7, 0.3, 0.9)
        for p in self._mydict:
            self.leg.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
            self.leg.SetTextSize(0.05)
        self.leg.Draw()
        os.system("mkdir -p output")
        self.canvas.SaveAs("output/"+self.name+".pdf")
    def DrawRatio(self):
        self.canvas2=ROOT.TCanvas("c2","c2",800,800)
        self.pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        self.pad1.SetBottomMargin(0)
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
        ##--legend
        self.leg2=ROOT.TLegend(0.1, 0.7, 0.3, 0.9)
        for p in self._mydict:
            self.leg2.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
            self.leg2.SetTextSize(0.05)
        self.leg2.Draw()
        ##--create pad2
        self.canvas2.cd()    
        self.pad2=ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        self.pad2.SetTopMargin(0)
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
                self._mydict[p]['hratio'].Draw()
            else:
                self._mydict[p]['hratio'].Draw('sames')
            i+=1
            self._mydict[p]['hratio'].SetTitle("")
            self._mydict[p]['hratio'].SetLineColor(1)
            self._mydict[p]['hratio'].GetYaxis().SetNdivisions(8)
            self._mydict[p]['hratio'].GetYaxis().SetLabelSize(0.1)
            self._mydict[p]['hratio'].GetXaxis().SetLabelSize(0.1)
        
        self.canvas2.cd()
        self.canvas2.SaveAs("output/ratio__"+self.name+".pdf")

    def SetTitle(self,_canvastitle):
        self.canvas.SetTitle(_canvastitle)
        self.canvas2.SetTitle(_canvastitle)
    def SetLineColor(self,_name, _color):
        self._mydict[_name]['hist'].SetLineColor(_color)
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
    myplotter.SetLineColor('sbar',2)
    myplotter.SetLineColor('s',4)
    ##--NorRatioPlot
    myplotter.DrawNoRatio()
    ##--RatioPlot
    myplotter.SetDeno("s")
    myplotter.DrawRatio()
    

        
