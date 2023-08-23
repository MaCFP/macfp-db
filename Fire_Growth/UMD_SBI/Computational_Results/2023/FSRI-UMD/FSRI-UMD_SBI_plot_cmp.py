#!/usr/bin/env python3
# McGrattan
# Aug 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

macfp.dataplot(config_filename='FSRI-UMD_SBI_Config_Autoupdated.csv',#'FSRI-UMD_SBI_cmp_config_test.csv',
               institute='FSRI-UMD',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list= ['all']) #['FSRI-UMD_SBI_RadHFVertVariation_t105.pdf',
                        #'FSRI-UMD_SBI_RadHFVertVariation_t145.pdf',
                        #'FSRI-UMD_SBI_RadHFVertVariation_t185.pdf']

# plt.show()
