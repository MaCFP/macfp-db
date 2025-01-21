#!/usr/bin/env python3

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='FMGlobal_NIST_Parallel_Panel_cmp_config.csv',
               institute='FMGlobal',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./Sim_data/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

# plt.show()
