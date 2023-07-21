#!/usr/bin/python3
#McDermott
#21 July 2023

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
sys.path.append('../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.close('all')

hrr_label = ['120 kW', '200 kW', '300 kW', '400 kW', '510 kW', '750 kW', '990 kW', '1500 kW', '1980 kW', '2800 kW']
color = ['black', 'maroon', 'limegreen', 'lightgray', 'blue', 'plum', 'cyan', 'orange', 'darkgreen', 'salmon']
z = np.array([10, 20, 30, 50, 75, 100, 140, 180, 220])

E = pd.read_csv('../Experimental_Data/PMMA_heatflux.csv', sep=',', skiprows=[1])
E.interpolate(axis=1,method='linear',inplace=True) # fill nan values
# print(E) # double check that nans are gone

f=0 # will be overwritten
for irow in range(len(hrr_label)):
    x = E.loc[irow,"HF_z10":"HF_z220"].values[:].astype(float)
    u = E.loc[irow,"u_exp_HF_z10":"u_exp_HF_z220"].values[:].astype(float)
    if hrr_label[irow] in ['400 kW', '750 kW', '990 kW']: continue
    f, a = macfp.plot_to_fig(x_data=x, y_data=z, data_label=hrr_label[irow],
                             x_min=0,x_max=150,x_nticks=4,
                             y_min=0,y_max=250,
                             x_label='Heat Flux [kW/m2]',
                             y_label='Height [cm]',
                             marker_style='o',
                             marker_edge_color=color[irow],
                             marker_fill_color=color[irow],
                             line_style='--',
                             line_color=color[irow],
                             show_legend=True,
                             legend_location='lower right',
                             figure_handle=f)
    plt.errorbar(x,z,linestyle='',xerr=u,capsize=4,ecolor=color[irow])


f.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('PMMA_flame_spread_heatflux.png') #save as png

# plt.show()
