#!/usr/bin/env python
import os
from plotter1 import plotter
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
