import numpy as np
import ROOT
from numpy import array

c=ROOT.TCanvas()
loaded_array=np.load('/home/snuintern3/LHAPDFexercise/LHAPDF_exercise/arrays.npz')
arr_logx=loaded_array['arr_logx']
#arr_x=loaded_array['arr_x']
arr_y=loaded_array['arr_y']
#arr_z=loaded_array['arr_z']
gr=ROOT.TGraphErrors()
gr2=ROOT.TGraphErrors()
mg=ROOT.TMultiGraph()
N=len(arr_logx)
for i in range(N):
    logx=arr_logx[i]
    #x=arr_x[i]
    y=arr_y[i]
    #z=arr_z[i]
    ex=0
    ey=0
    gr.SetPoint(i,logx,y)
    gr.SetPointError(i,0,ey)
    
    gr2.SetPoint(i,-3,2)
    gr2.SetPointError(i,0,1)
gr2.SetMarkerColor(2)
gr2.SetMarkerSize(0.3)
gr2.SetMarkerStyle(20)
#gr2.Draw("ap4")
#mycolor=4
#gr.SetFillColorAlpha(mycolor,0.3)
gr.SetMarkerColor(4)
gr.SetMarkerSize(0.3)
gr.SetMarkerStyle(20)
#gr.Draw("ap3")

mg.Add(gr)
mg.Add(gr2)
mg.Draw("ap3")
mg.SetTitle("Test")
c.SaveAs("test.pdf")

#print x
#print y
#print z
#print(loaded_array['arr_x'])
