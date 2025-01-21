#!/usr/bin/python3
#McGrattan
#8 August 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

plt.close('all')

hrr_label = ['120 kW', '200 kW', '300 kW', '400 kW', '510 kW', '750 kW', '990 kW', '1500 kW', '1980 kW', '2800 kW']
hrr_label_2p5 = ['2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm', '2.5 cm']
hrr_label_1p3 = ['1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm', '1.3 cm']
color = ['black', 'maroon', 'limegreen', 'lightgray', 'blue', 'plum', 'cyan', 'orange', 'darkgreen', 'salmon']

# Heights of measurements
z = np.array([10, 20, 30, 50, 75, 100, 140, 180, 220])

E = pd.read_csv('../../../Experimental_Data/PMMA_heatflux.csv', sep=',', skiprows=[1])
E.interpolate(axis=1,method='linear',inplace=True) # fill nan values

# HRRs
hrrs = E['HRR'].to_numpy()

M25 = pd.read_csv('./Sim_data/PMMA/unsteadyHF/FMGlobal_PMMA_unsteadyHF_25mm.csv', sep=',').drop([0]).astype(float)
M25['HRR_filtered'] = savgol_filter(M25['HRR'], 41, 3)

M13 = pd.read_csv('./Sim_data/PMMA/unsteadyHF/FMGlobal_PMMA_unsteadyHF_13mm.csv', sep=',').drop([0]).astype(float)
M13['HRR_filtered'] = savgol_filter(M13['HRR'], 41, 3)

hrr_rows={}
for sim, name in zip([M25, M13], ['M25', 'M13']):
    hrr_rows[name] = []
    for hrr in hrrs:
        hrr_rows[name] += [np.argmin(np.abs(sim['HRR_filtered'] - hrr))]

# Dummy plot to define handle
f = macfp.plot_to_fig(x_data=[0,1], y_data=[0,1], marker_style='None',line_style='None')

for irow in range(len(hrr_label)):
   x = E.loc[irow,"HF_z10":"HF_z220"].values[:].astype(float)
   u = E.loc[irow,"u_exp_HF_z10":"u_exp_HF_z220"].values[:].astype(float)
   if hrr_label[irow] in ['400 kW', '750 kW', '990 kW']: continue
   f = macfp.plot_to_fig(x_data=x, y_data=z, data_label=hrr_label[irow],
                        x_min=0,x_max=150,x_nticks=4,
                        y_min=0,y_max=250,
                        x_label='Heat Flux [kW/m²]',
                        y_label='Height [cm]',
                        marker_style='o',
                        marker_edge_color=color[irow],
                        marker_fill_color=color[irow],
                        line_style='None',
                        line_color=color[irow],
                        show_legend=True,
                        legend_location='outside',
                        figure_right_adjust=0,
                        legend_fontsize=8,
                        figure_handle=f)

   plt.errorbar(x,z,linestyle='',xerr=u,capsize=4,ecolor=color[irow])

   window_size = 3
   start_row = max(0, hrr_rows['M25'][irow] - window_size)  
   end_row = min(len(M25), hrr_rows['M25'][irow] + window_size + 1) 
   x25 = M25[start_row:end_row].mean(axis=0).to_numpy()[1:-1]

   start_row = max(0, hrr_rows['M13'][irow] - window_size)  
   end_row = min(len(M13), hrr_rows['M13'][irow] + window_size + 1) 
   x13 = M13[start_row:end_row].mean(axis=0).to_numpy()[1:-1]

   f = macfp.plot_to_fig(x_data=x25, y_data=z, data_label=hrr_label_2p5[irow],
                           x_min=0,x_max=150,x_nticks=4,
                           y_min=0,y_max=250,
                           x_label='Heat Flux [kW/m²]',
                           y_label='Height [cm]',
                           marker_style='None',
                           line_style='-',
                           line_color=color[irow],
                           show_legend=True,
                           legend_location='outside',
                           figure_right_adjust=0,
                           legend_fontsize=8,
                           figure_handle=f)

   f = macfp.plot_to_fig(x_data=x13, y_data=z, data_label=hrr_label_1p3[irow],
                           x_min=0,x_max=150,x_nticks=4,
                           y_min=0,y_max=250,
                           x_label='Heat Flux [kW/m²]',
                           y_label='Height [cm]',
                           marker_style='None',
                           line_style='--',
                           line_color=color[irow],
                           show_legend=True,
                           legend_location='outside',
                           figure_right_adjust=0,
                           legend_fontsize=8,
                           figure_handle=f)

f.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Plots/PMMA_heat_flux_profile.pdf')

# plt.show()
