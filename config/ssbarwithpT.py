import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"s_sbar with electron pT using NNPDF31",
    "input":_maindir+"/mg_output/histos_ssbarwithpT.root",
    "hist":OrderedDict({
        #"e":{"path":"pT_e","name":"e","title":"e","color":6},
        "e, x>0.03":{"path":"pT_e_x>0.03","name":"e, x>0.03","title":"e, x>0.03","color":2},
        "e, x<0.03":{"path":"pT_e_x<0.03","name":"e, x<0.03","title":"e, x<0.03","color":4},
    }),
    "title":"pp->l vl with electron pT using NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"pT(e)",
    "ytitle":"Event",
    "deno":"e, x<0.03",

}
