import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"b_bbar",
    "input":_maindir+"/mg_output/histos_bbbar.root",
    "hist":OrderedDict({
        "b":{"path":"log_x_b","name":"b","title":"b","color":4},
        "bbar":{"path":"log_x_bbar","name":"bbar","title":"#bar{b}","color":2},
    }),
    "title":"pp->l+ l- b",
    "xtitle":"log(x)",
    "ytitle":"Event",
    "deno":"b",

}
