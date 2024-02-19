import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"s_sbar with NNPDF31",
    #"input":_maindir+"/mg_output/histos_ssbar_NNPDF31.root",
    "input":_maindir+"/mg_output/histos_ssbarwithpT.root",
    "hist":OrderedDict({
        "s":{"path":"log_x_s","name":"s","title":"s","color":4},
        "sbar":{"path":"log_x_sbar","name":"sbar","title":"#bar{s}","color":2},
    }),
    "title":"pp->l vl with NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"log(x)",
    "ytitle":"Event",
    "deno":"s",

}
