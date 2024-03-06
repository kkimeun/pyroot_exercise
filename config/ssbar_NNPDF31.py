import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"s_sbar with lepton pT < 5, using NNPDF31",
    "input":_maindir+"/mg_output/histos_ssbarwithpTEta.root",
    #"input":_maindir+"/mg_output/histos_ssbarwithpT.root",
    "hist":OrderedDict({
        "s":{"path":"log_x_s","name":"s","title":"s","color":4},
        "sbar":{"path":"log_x_sbar","name":"sbar","title":"#bar{s}","color":2},
    }),
    #"hratio":OrderedDict({
	#"sbar":{"path":"log_x_sbar","name1":"sbar","title":"#bar{s}","color":1},
    #}),

    "title":"pp->l vl with lepton pT < 5, using NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"log(x)",
    "ytitle":"Event",
    "deno":"s",

}
