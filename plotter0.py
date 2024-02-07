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
        self.canvas=ROOT.TCanvas()
        for i,p in enumerate(self._mydict):
            if i==0:
                self._mydict[p]['hist'].Draw()
            else:
                self._mydict[p]['hist'].Draw('sames')
            self._mydict[p]['hist'].SetStats(0)

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
    myplotter.SaveAs("ssbar.pdf")
        
