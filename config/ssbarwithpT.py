import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"electron pT < 5 using NNPDF31",
    "input":_maindir+"/mg_output/histos_ssbarwithpTEta.root",
    "hist":OrderedDict({
        "e":{"path":"pT_e","name":"e","title":"e","color":1},
        "e, x>0.0003":{"path":"pT_e_x>0.0003","name":"e, x>0.0003","title":"e, x>0.0003","color":2},
        "e, x<0.0003":{"path":"pT_e_x<0.0003","name":"e, x<0.0003","title":"e, x<0.0003","color":4},
    }),
    "hratio":OrderedDict({
	"e":{"path":"pT_e","name":"e","title":"e","color":1},
	"e, x>0.0003":{"path":"pT_e_x>0.0003","name":"e, x>0.0003","title":"e, x>0.0003","color":2},
	"e, x<0.0003":{"path":"pT_e_x<0.0003","name":"e, x<0.0003","title":"e, x<0.0003","color":4},
     }),
    "title":"pp->l vl electron pT < 5 using NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"pT(e)",
    "ytitle":"Event",
    "deno":"e, x<0.0003",

}
