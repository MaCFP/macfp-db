#!/usr/bin/env python3
# YM
# March 2026

import sys
import os

# Change to script directory to ensure relative paths work correctly
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Dynamically add Utilities to path
'''script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))))
utilities_path = os.path.join(repo_root, 'Utilities')
sys.path.append(utilities_path)'''

# Old paths (commented out)
sys.path.append('../../../../../../macfp-db/Utilities/')
#sys.path.append('../../../../../../macfp-db-youk/Utilities/')
sys.path.append('../../../../Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py) 
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='UGent_FM_Burner_2026_cmp_config.csv',
               institute='UGent',
               revision='MaCFP-4, La Rochelle, 2026',
               expdir='../../../Experimental_Data/',
               cmpdir='./Computational_results/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

macfp.dataplot(config_filename='UGent_FM_Burner_2026_cmp_config_transient_plots.csv',
               institute='UGent',
               revision='MaCFP-4, La Rochelle, 2026',
               expdir='./Computational_results/', #only to plot the theoretical HRR
               cmpdir='./Computational_results/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

macfp.dataplot(config_filename='UGent_FM_Burner_2026_cmp_config_rms_TC.csv',
               institute='UGent',
               revision='MaCFP-4, La Rochelle, 2026',
               expdir='../../../Experimental_Data/',
               cmpdir='./Computational_results/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
# plt.show()