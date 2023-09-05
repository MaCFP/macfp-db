#!/usr/bin/env python3
# McDermott
# Feb 2021

# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
# sys.path.append('../../../../../../macfp-db/Utilities/')
# sys.path.append('/Users/fbraenns/09_TOOLs_Application/MaCFP/00_Repositories/macfp-db_FORK.github/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='FM_Burner_cmp_config.csv',
               institute='UWuppertal',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               # cmpdir='./Output/',
               # cmpdir='../NIST/Output/',
               cmpdir='./Output/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

# plt.show()
