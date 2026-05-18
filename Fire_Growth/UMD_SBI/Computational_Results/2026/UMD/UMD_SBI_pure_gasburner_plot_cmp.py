#!/usr/bin/env python3
# Lei Li
# May 2026
import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='UMD_SBI_pure_gasburner_cmp_config.csv',
               institute='UMD',
               revision='MaCFP-4, La Rochelle, 2026',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

# plt.show()
