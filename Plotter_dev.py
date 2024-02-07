import ROOT
import os
from collections import OrderedDict
#print os.getenv("_maindir_pyroot_git")
_maindir = os.getenv("_maindir_pyroot_git")
filepath=_maindir+"/mg_output/histos.root"
tfile=ROOT.TFile.Open(filepath)
#tfile.ls()

dict_h=OrderedDict({
    "tbar":{
        "path":"log_x_tbar",
        "color":2,
        "name":"#bar{t}",
    },
    "t":{
        "path":"log_x_t",
        "color":4,
        "name":"t",
    },
    "g":{
        "path":"log_x_g",
        "color":6,
        "name":"g",
    },
}
)

for p in dict_h:
    _path=dict_h[p]["path"]
    dict_h[p]['histo']=tfile.Get(_path)
    dict_h[p]['histo'].SetDirectory(0)
    _color=dict_h[p]['color']
    dict_h[p]['histo'].SetLineColor(_color)
    _name=dict_h[p]['name']
    dict_h[p]['histo'].SetName(_name)

c=ROOT.TCanvas()
#print list(dict_h)
for i,p in enumerate(dict_h):
    if i == 0:
      dict_h[p]['histo'].Draw()
    else:
      dict_h[p]['histo'].Draw('sames')

c.SaveAs("output/test.pdf")
