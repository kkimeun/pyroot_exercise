#!/usr/bin/env python
import os
import sys
from ESplotter import ESplotter
def Run(confpath,normtype=0):
    exec(open(confpath))
    name=conf["name"]
    title=conf["title"]
    xtitle=conf["xtitle"]
    ytitle=conf["ytitle"]
    filepath=conf["input"]
    deno=conf["deno"]
    suffix=""
    if normtype==1:
        suffix="_Norm"
    if normtype==2:
        suffix="_NormToMax"
    myplotter=ESplotter(name+suffix)
    myplotter.SetNormType(normtype)
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
    #myplotter.DrawNoRatio()
    ##--RatioPlot
    myplotter.SetDeno(deno)
    for p in conf["hratio"]:
        p_path=conf["hratio"][p]["path"]
	p_name=conf["hratio"][p]["name"]
	p_title=conf["hratio"][p]["title"]
	p_color=conf["hratio"][p]["color"]
        myplotter.AddHist(p_path,p_name,p_title)
	myplotter.SetLineColor(p,p_color)
    myplotter.SetTitle(title)               
    #myplotter.DrawRatio()
    
    ##---to draw pad3, pad4

    name=conf["name"]
    title=conf["title"]
    xtitle=conf["xtitle"]
    ytitle=conf["ytitle"]
    filepath2=conf["input2"]
    deno2=conf["deno2"]
    suffix=""
    if normtype==1:
        suffix="_Norm"
    if normtype==2:
        suffix="_NormToMax"
    myplotter=ESplotter(name+suffix)
    myplotter.SetNormType(normtype)
    #_maindir = os.getenv("_maindir_pyroot_git")
    myplotter.ReadFile(filepath2)
    for p in conf["hist2"]:
        p_path2=conf["hist2"][p]["path"]
        p_name2=conf["hist2"][p]["name"]
        p_title2=conf["hist2"][p]["title"]
        p_color2=conf["hist2"][p]["color"]
        myplotter.AddHist(p_path2,p_name2,p_title2)
        myplotter.SetLineColor(p,p_color2)
    myplotter.SetTitle(title)
    myplotter.SetXTitle(xtitle)
    myplotter.SetYTitle(ytitle)
    myplotter.SetDeno(deno2)
    for p in conf["hratio2"]:
        p_path2=conf["hratio2"][p]["path"]
        p_name2=conf["hratio2"][p]["name"]
        p_title2=conf["hratio2"][p]["title"]
        p_color2=conf["hratio2"][p]["color"]
        myplotter.AddHist(p_path2,p_name2,p_title2)
        myplotter.SetLineColor(p,p_color2)
    myplotter.SetTitle(title)



if __name__ == '__main__':
    confpath=sys.argv[1]
    #RunWithConfig.py config/ssbar.py
    #-> confpath = "config/ssbar.py"
    Run(confpath)
    Run(confpath,1)
    Run(confpath,2)
