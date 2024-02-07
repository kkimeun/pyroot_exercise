import os
from collections import OrderedDict
_maindir = os.getenv("_maindir_pyroot_git")

conf={
    "name":"t_tbar",
    "input":_maindir+"/mg_output/histos.root",
    "hist":OrderedDict({
        "t":{"path":"log_x_t","name":"t","title":"t","color":4},
        "tbar":{"path":"log_x_tbar","name":"tbar","title":"#bar{t}","color":2},
    }),
    "title":"pp->t#bar{t}",
    "xtitle":"log(x)",
    "ytitle":"Event",
    "deno":"t",

}
