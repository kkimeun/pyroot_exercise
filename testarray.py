import numpy as np
import ROOT
from numpy import array

c=ROOT.TCanvas()
loaded_array=np.load('/home/snuintern3/LHAPDFexercise/LHAPDF_exercise/arrays.npz')
arr_logx=loaded_array['arr_logx']
#arr_x=loaded_array['arr_x']
arr_s=loaded_array['arr_s']
arr_sbar=loaded_array['arr_sbar']
arr_serr=loaded_array['arr_serr']
arr_sbarerr=loaded_array['arr_sbarerr']

gr1=ROOT.TGraphErrors()
gr2=ROOT.TGraphErrors()
mg=ROOT.TMultiGraph()
N=len(arr_logx)
for i in range(N):
    logx=arr_logx[i]
    #x=arr_x[i]
    s=arr_s[i]
    sbar=arr_sbar[i]
    ex=0
    ey1=arr_serr[i]
    ey2=arr_sbarerr[i]
    gr1.SetPoint(i,logx,s)
    gr1.SetPointError(i,0,1)
    
    gr2.SetPoint(i,logx,sbar)
    gr2.SetPointError(i,0,ey2)

gr2.SetMarkerColor(2)
gr2.SetMarkerSize(0.5)
gr2.SetMarkerStyle(20)
#gr2.Draw("ap4")
#mycolor=4
#gr.SetFillColorAlpha(mycolor,0.3)
gr1.SetMarkerColor(4)
gr1.SetMarkerSize(0.5)
gr1.SetMarkerStyle(20)
#gr.Draw("ap3")

mg.Add(gr1)
mg.Add(gr2)
mg.Draw("ap3")
mg.SetTitle("Test")
c.SaveAs("test.pdf")

#print x
#print y
#print z
#print(loaded_array['arr_x'])
