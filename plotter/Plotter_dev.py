import ROOT
import os
from collections import OrderedDict
#print os.getenv("_maindir_pyroot_git")
_maindir = os.getenv("_maindir_pyroot_git")
filepath=_maindir+"/mg_output/histos.root"
tfile=ROOT.TFile.Open(filepath)
#tfile.ls()

dict_h=OrderedDict({
    "bbar":{
        "path":"log_x_bbar",
        "color":2,
        "name":"#bar{b}",
    },
    "b":{
        "path":"log_x_b",
        "color":4,
        "name":"b",
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
for p in dict_h:
    dict_h[p]['histo'].Draw('sames')

c.SaveAs("test.pdf")
