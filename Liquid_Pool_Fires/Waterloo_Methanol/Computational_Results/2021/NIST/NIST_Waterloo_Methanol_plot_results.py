#!/usr/bin/env python3
# McDermott
# Feb 2021

# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='NIST_Waterloo_Methanol_dataplot_config_base.csv',
               institute='NIST FDS6.7.5-1004-g197c82469-master',
               expdir='../../../../../Liquid_Pool_Fires/',
               cmpdir='',
               pltdir='./Baseline/Plots/',
               close_figs=True,
               verbose=True,
               plot_range=range(10000))

# macfp.dataplot(config_filename='NIST_Waterloo_Methanol_dataplot_config_dev.csv',
#                institute='NIST FDS6.7.5-1004-g197c82469-master',
#                expdir='../../../../../Liquid_Pool_Fires/',
#                cmpdir='',
#                pltdir='./Development/Plots/',
#                close_figs=True,
#                verbose=True,
#                plot_range=range(10000))

# plt.show()