#!/usr/bin/env python3
# Meehan
# Aug 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp

macfp.dataplot(
    config_filename='Sandia_Pool_Fires_cmp_config.csv',
    institute='Sandia',
    revision='MaCFP-3, Tsukuba, 2023',
    expdir='../../../Experimental_Data/',
    cmpdir='./Preliminary_Results/',
    pltdir='./Preliminary_Results/Plots/',
    close_figs=True,
    verbose=True,
    plot_list=['all']
)

# plt.show()