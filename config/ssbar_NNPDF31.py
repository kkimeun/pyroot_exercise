import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"s_sbar with different invariant Mass cut, using NNPDF31",
    "input":_maindir+"/mg_output/histos_invariantmass_390.root",
    #"input":_maindir+"/mg_output/histos_ssbarwithpT.root",
    "input2":_maindir+"/mg_output/histos_invariantmass_5.root",
    "hist":OrderedDict({
        "s_5":{"path":"log_x_s","name":"s_5","title":"s_5","color":4},
	"s_390":{"path":"log_x_s","name":"s_390","title":"s_390","color":2},
        #"sbar":{"path":"log_x_sbar","name":"sbar","title":"#bar{s}","color":2},

    }),


    #"hratio":OrderedDict({
	#"sbar":{"path":"log_x_sbar","name1":"sbar","title":"#bar{s}","color":1},
    #}),

    "title":"pp->l vl with different invariant Mass cut, using NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"log(x)",
    "ytitle":"Event",
    "deno":"s_5",

}
