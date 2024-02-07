import ROOT
import os
from collections import OrderedDict
#class plotter:
    def __init__(self):
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
    def Draw(self):
        #self.canvas=ROOT.TCanvas()
        self.pad=ROOT.TPad()
    
    def RatioPlot(self,_name1,_name2):
        h1 = self._mydict[_name1]['hist']
        h2 = self._mydict[_name2]['hist'] 
        h3 = h1.Clone("h3")
        h3.SetStats(0)
        h3.Divide(h2)
        return h3

    
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottommargin(0)
    pad1.SetGridx()
    pad1.cd()

    for i,p in enumerate(self._mydict):
        if i==0:
            self._mydict[p]['hist'].Draw()
        else:
            self._mydict[p]['hist'].Draw('sames')
        self._mydict[p]['hist'].SetStats(0)
        self._mydict[p]['hratio']=self._mydict[p]['hist'].Clone()
        self._mydict[p]['hratio'].Divide(self._mydict[p]['hist'])

        leg=ROOT.TLegend(0.1, 0.7, 0.5, 0.9)
        leg.AddEntry(self._mydict[p]['hist'], self._mydict[p]["name"])
        leg.Draw()
    
    c.cd()    
    pad2=ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2=SetTopMargin(0)
    pad2.SetBottomMargin(0.2)
    pad2.SetGridx()
    pad2.Draw()
    pad2.cd()
    for i,p in enumerate(self._mydict):
        h
                


    def SetLineColor(self,_name, _color):
        self._mydict[_name]['hist'].SetLineColor(_color)
    def SaveAs(self, _path):
        self.canvas.SaveAs(_path)
    def ReadFile(self, _filepath):
        self.tfile=ROOT.TFile.Open(_filepath)

        
if __name__ == '__main__':
    myplotter=plotter()
    _maindir = os.getenv("_maindir_pyroot_git")
    filepath=_maindir+"/mg_output/histos_ssbar.root"   
    myplotter.ReadFile(filepath)
    myplotter.AddHist('log_x_s','s','s')
    myplotter.AddHist('log_x_sbar','sbar','#bar{s}')

    myplotter.SetLineColor('sbar',2)
    myplotter.SetLineColor('s',4)
    myplotter.Draw()
    myplotter.SaveAs("ssbarwithratio.pdf")
        
