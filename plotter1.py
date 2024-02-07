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
    #def Draw(self):
    #    #self.canvas=ROOT.TCanvas()
    #    self.pad=ROOT.TPad()
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
        self.canvas=ROOT.TCanvas()
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist'].Draw()
            else:
                self._mydict[p]['hist'].Draw('sames')
        self._mydict[p]['hist'].SetStats(0)
        self.leg=ROOT.TLegend(0.1, 0.7, 0.5, 0.9)
        for p in self._mydict:
            self.leg.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
        self.leg.Draw()
        os.system("mkdir -p output")
        self.canvas.SaveAs("output/"+self.name+".pdf")
    def DrawRatio(self):
        self.canvas2=ROOT.TCanvas()
        self.pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        self.pad1.SetBottomMargin(0)
        self.pad1.SetGridx()
        self.pad1.cd()
        ##--draw hist
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist'].Draw()
            else:
                self._mydict[p]['hist'].Draw('sames')
            self._mydict[p]['hist'].SetStats(0)
        ##--legend
        self.leg2=ROOT.TLegend(0.1, 0.7, 0.5, 0.9)
        self.leg2.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
        self.leg2.Draw()
        ##--create pad2
        self.canvas2.cd()    
        self.pad2=ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        self.pad2.SetTopMargin(0)
        self.pad2.SetBottomMargin(0.2)
        self.pad2.SetGridx()
        self.pad2.Draw()
        self.pad2.cd()
        
        for i,p in enumerate(self._mydict):
            self.SetRatioHist(p)
            ##-->Now we have self._mydict[proc]['hratio'] obejcts
            if i==0:
                self._mydict[p]['hratio'].Draw()
            else:
                self._mydict[p]['hratio'].Draw('sames')
        self.canvas2.cd()
        self.canvas2.SaveAs("output/ratio__"+self.name+".pdf")

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

    myplotter.SetLineColor('sbar',2)
    myplotter.SetLineColor('s',4)
    ##--NorRatioPlot
    myplotter.DrawNoRatio()
    ##--RatioPlot
    myplotter.SetDeno("s")
    myplotter.DrawRatio()

        
