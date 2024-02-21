import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"electron pT > 200, using NNPDF31",
    "input":_maindir+"/mg_output/histos_ssbarwithpT.root",
    "hist":OrderedDict({
        "e":{"path":"pT_e","name":"e","title":"e","color":6},
        "e, x>0.03":{"path":"pT_e_x>0.03","name":"e, x>0.03","title":"e, x>0.03","color":2},
        "e, x<0.03":{"path":"pT_e_x<0.03","name":"e, x<0.03","title":"e, x<0.03","color":4},
    }),
    "title":"pp->l vl electron pT > 200, using NNPDF23_nlo_as_0119",
    "xtitle":"pT(e)",
    "ytitle":"Event",
    "deno":"e, x<0.03",

}
