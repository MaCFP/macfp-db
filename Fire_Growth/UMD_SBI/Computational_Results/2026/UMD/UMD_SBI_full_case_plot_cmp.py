#!/usr/bin/env python3
# Lei Li
# May 2026
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
MACFP_DB = HERE.parents[4]
sys.path.insert(0, str(MACFP_DB / "Utilities"))

import macfp  # noqa: E402

importlib.reload(macfp)  # use for development (while making changes to macfp.py)

os.chdir(HERE)
macfp.dataplot(
    config_filename="UMD_SBI_full_case_cmp_config.csv",
    institute="UMD",
    revision="MaCFP-4, La Rochelle, 2026",
    expdir=str(HERE.parents[2] / "Experimental_Data") + "/",
    cmpdir=str(HERE / "Output") + "/",
    pltdir=str(HERE / "Plots") + "/",
    close_figs=True,
    verbose=True,
    plot_list=["all"],
)

# plt.show()
