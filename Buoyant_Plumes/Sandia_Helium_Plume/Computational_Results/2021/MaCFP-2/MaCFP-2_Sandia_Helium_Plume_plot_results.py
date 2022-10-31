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

macfp.dataplot(config_filename='MaCFP-2_Sandia_Helium_Plume_dataplot_config.csv',
               institute='Case 1: Sandia Helium Plume',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots/',
               verbose=True,
               close_figs=True,
               plot_range=range(1000))

# plt.show()