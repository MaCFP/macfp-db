#!/usr/bin/python3
# T. Hehnen
# 24 August 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='NIST_Parallel_Panel_BUWFZJ_cmp_config.csv',
               institute='BUW-FZJ',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output/',
               pltdir='./Output/Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

# plt.show()
