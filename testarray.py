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

mycolor=4
gr.SetFillColorAlpha(mycolor,0.3)
gr.SetMarkerColor(mycolor)
gr.SetMarkerSize(0.3)
gr.SetMarkerStyle(20)
gr.Draw("ap3")

gr.SetTitle("Test")
c.SaveAs("test.pdf")

#print x
#print y
#print z
#print(loaded_array['arr_x'])
