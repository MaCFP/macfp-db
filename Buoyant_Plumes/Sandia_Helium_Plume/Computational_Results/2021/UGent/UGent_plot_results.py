#!/usr/bin/env python3
# McDermott
# March 2020

# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='UGent_macfp_config.csv',
               institute='UGent',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots/',
               verbose=True,
               close_figs=True)

# plt.show()