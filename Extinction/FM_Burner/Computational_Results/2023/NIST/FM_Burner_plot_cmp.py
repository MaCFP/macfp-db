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

macfp.dataplot(config_filename='FM_Burner_cmp_config_eta.csv',
               institute='NIST',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output_Eta/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

macfp.dataplot(config_filename='FM_Burner_cmp_config_C2CO_p6.csv',
               institute='NIST',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output_C2CO_p6/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

macfp.dataplot(config_filename='FM_Burner_cmp_config_C2CO_p9.csv',
               institute='NIST',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output_C2CO_p9/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

# plt.show()