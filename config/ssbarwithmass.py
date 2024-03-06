import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"invariant mass of (lepton + neutrino) distribution using NNPDF31",
    "input":_maindir+"/mg_output/histos_invariantmass.root",
    "hist":OrderedDict({
        "lv":{"path":"m_lv","name":"lv","title":"lv","color":3},
        "lv, x>0.0003":{"path":"m_lv_x>0.0003","name":"lv, x>0.0003","title":"lv, x>0.0003","color":2},
        "lv, x<0.0003":{"path":"m_lv_x<0.0003","name":"lv, x<0.0003","title":"lv, x<0.0003","color":4},
    }),
    "hratio":OrderedDict({
        "lv":{"path":"m_lv","name":"lv","title":"lv","color":3},
        "lv, x>0.0003":{"path":"m_lv_x>0.0003","name":"lv, x>0.0003","title":"lv, x>0.0003","color":2},
        "lv, x<0.0003":{"path":"m_lv_x<0.0003","name":"lv, x<0.0003","title":"lv, x<0.0003","color":4},
     }),
    "title":"invariant mass of (lepton + neutrino) distribution using NNPDF31_nnlo_hessian_pdfas",
    "xtitle":"M(lv)",
    "ytitle":"Event",
    "deno":"lv, x<0.0003",

}
