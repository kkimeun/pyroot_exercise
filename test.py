import ROOT
#ROOT.gSystem.Load("/cvmfs/cms.cern.ch/slc7_amd64_gcc820/external/lhapdf/6.2.3/lib/libLHAPDF.so")
import os
import lhapdf
import numpy as np
from numpy import array
from math import sqrt
#class PDFplotter:

def GetStoSbar(x,q2,lhapdf_name):
    p = lhapdf.mkPDF(lhapdf_name)
    pdgid=3
    Nrep=p.set().size
    #--nominal
    irep=0
    s_pdf=p.xfxQ2(pdgid,x,q2)
    sbar_pdf=p.xfxQ2(-pdgid,x,q2)
    r_nom=s_pdf/sbar_pdf
    sum_dr2=0
    for irep in range(Nrep):
        p = lhapdf.mkPDF(lhapdf_name,irep)
        
        s_pdf=p.xfxQ2(pdgid,x,q2)
        sbar_pdf=p.xfxQ2(-pdgid,x,q2)
        #21, 1e-3, 1e4)
        #print s_pdf/sbar_pdf
        r=s_pdf/sbar_pdf
        dr=r-r_nom
        dr2=dr*dr
        sum_dr2+=dr2
    r_err=sqrt(sum_dr2)
    #return r_nom,r_err
    return s_pdf,sbar_pdf

#def Draw(,):
    #c=ROOT.TCanvas()
    #arr_x =array([0.0003,0.003,0.01])
    #arr_y =array([]}
    #arr_ey=array
    #gr=ROOT.TGraphErrors()
    #N=len(arr_x)
    #for i in range(N):
	#x=arr_x[i]
	#y=arr_y[i]
	#ex=0
	#ey=arr_ey[i]
	#gr.SetPoint(i,x,y)
	#gr.SetPointError(i,0,ey)

    #gr.Draw()
    #gr.SetTitle(
    #os.system("mkdir -p output")
    #c.SaveAs("output/test.pdf")



Q2=1000
lhapdf_name="NNPDF31_nnlo_hessian_pdfas"
#lhapdf_name="CT18ZNNLO"
#lhapdf_name="CT18NNLO"
lhapdf.setVerbosity(0)
#print "<",lhapdf_name,">", "Q2=",Q2
#print "log x",'\t',"x",'\t',"s/s~","\t","err(s/s~)"
#print "--------------------"
#for x in [0.3,0.25,0.2,0.1,0.06,0.05,0.04,0.03,0.02,0.01,0.008,0.005,0.003,0.001,0.0001,0.00001,1e-6,1e-7,1e-8,1e-9,1e-10,1e-11]:
arr_x=[]
arr_y=[]
arr_z=[]
y=np.arange(-5,-1,0.5)
for i in y:
    x= 10**i
    s_pdf,sbar_pdf=GetStoSbar(x,Q2,lhapdf_name)
    #r,r_err=GetStoSbar(x,Q2,lhapdf_name)
    #print x,'\t', s_pdf,"\t",r_err
    #print i,'\t',x,'\t', s_pdf, "\t",sbar_pdf
    arr_x.append(x)
    arr_y.append(s_pdf)
    arr_z.append(sbar_pdf)

print (arr_x)
print (arr_y)
print (arr_z)     
np.savez('arrays.npz',arr_x=arr_x,arr_y=arr_y,arr_z=arr_z)
