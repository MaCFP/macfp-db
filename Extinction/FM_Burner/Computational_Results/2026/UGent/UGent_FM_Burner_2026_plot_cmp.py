#!/usr/bin/env python3
# YM
# March 2026

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
workspace_root = os.path.normpath(os.path.join(current_dir, '../../../../..'))
sys.path.append(os.path.join(workspace_root, 'Utilities'))
os.chdir(current_dir)  # Change to script directory

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='UGent_FM_Burner_2026_cmp_config.csv',
               institute='UGent',
               revision='MaCFP-4, La Rochelle, 2026',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

# plt.show()