#!/usr/bin/env python
import os
import sys
from ESplotter import ESplotter
confpath=sys.argv[1]
#RunWithConfig.py config/ssbar.py
#-> confpath = "config/ssbar.py"
exec(open(confpath))
name=conf["name"]
title=conf["title"]
xtitle=conf["xtitle"]
ytitle=conf["ytitle"]
filepath=conf["input"]
deno=conf["deno"]
myplotter=ESplotter(name)
#_maindir = os.getenv("_maindir_pyroot_git")
myplotter.ReadFile(filepath)
for p in conf["hist"]:
    p_path=conf["hist"][p]["path"]
    p_name=conf["hist"][p]["name"]
    p_title=conf["hist"][p]["title"]    
    p_color=conf["hist"][p]["color"]
    myplotter.AddHist(p_path,p_name,p_title)
    myplotter.SetLineColor(p,p_color)
myplotter.SetTitle(title)
myplotter.SetXTitle(xtitle)
myplotter.SetYTitle(ytitle)
##--NorRatioPlot
myplotter.DrawNoRatio()
##--RatioPlot
myplotter.SetDeno(deno)
myplotter.DrawRatio()               
