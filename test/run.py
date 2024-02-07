import os
from plotter import plotter
_maindir = os.getenv("_maindir_pyroot_git")

ttplotter=plotter()
filepath=_maindir+"/mg_output/histos.root"
ttplotter.ReadFile(filepath)
ttplotter.AddHist('log_x_t','t','t')
ttplotter.AddHist('log_x_tbar','tbar','#bar{t}')
ttplotter.SetLineColor('tbar',2)
ttplotter.SetLineColor('t',4)
ttplotter.Draw()
ttplotter.SaveAs("ttbar.pdf")
         

ssplotter=plotter()
filepath=_maindir+"/mg_output/histos_ssbar.root"
ssplotter.ReadFile(filepath)
ssplotter.AddHist('log_x_s','s','s')
ssplotter.AddHist('log_x_sbar','sbar','#bar{s}')
ssplotter.SetLineColor('sbar',2)
ssplotter.SetLineColor('s',4)
ssplotter.Draw()
ssplotter.SaveAs("ssbar.pdf")
       
