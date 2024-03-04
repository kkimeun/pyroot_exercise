import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"invariant lepton mass distribution using NNPDF31",
    "input":_maindir+"/mg_output/histos_invariantmass.root",
    "hist":OrderedDict({
        "ll":{"path":"m_ll","name":"ll","title":"ll","color":6},
        #"e, x>0.03":{"path":"pT_e_x>0.03","name":"e, x>0.03","title":"e, x>0.03","color":2},
        #"e, x<0.03":{"path":"pT_e_x<0.03","name":"e, x<0.03","title":"e, x<0.03","color":4},
    }),
    "title":"invariant lepton mass distribution using NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"M(ll)",
    "ytitle":"Event",
    "deno":"ll",

}
