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

macfp.dataplot(config_filename='UGENT_FM_Burner_dataplot_config_21O2.csv',
               institute='UGENT',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
               
macfp.dataplot(config_filename='UGENT_FM_Burner_dataplot_config_17O2.csv',
               institute='UGENT',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
               
macfp.dataplot(config_filename='UGENT_FM_Burner_dataplot_config_15O2.csv',
               institute='UGENT',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

#plt.show()