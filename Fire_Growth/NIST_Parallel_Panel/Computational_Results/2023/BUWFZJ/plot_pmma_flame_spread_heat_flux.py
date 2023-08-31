#!/usr/bin/python3
# T. Hehnen
# 24 August 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')
# sys.path.append('../../../../../Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.close('all')

hrr_label = ['120 kW', '200 kW', '300 kW', '400 kW', '510 kW', '750 kW', '990 kW', '1500 kW', '1980 kW', '2800 kW']
color = ['black', 'maroon', 'limegreen', 'lightgray', 'blue', 'plum', 'cyan', 'orange', 'darkgreen', 'salmon']

# Heights of measurements and FDS predictions
z = np.array([10, 20, 30, 50, 75, 100, 140, 180, 220])
z_FDS = np.linspace(1,243, num=50, endpoint=True)

E = pd.read_csv('../../../Experimental_Data/PMMA_heatflux.csv', sep=',', skiprows=[1])
E.interpolate(axis=1,method='linear',inplace=True) # fill nan values

M1 = pd.read_csv('../NIST/Preliminary_Results/PMMA_60_kW_1_cm_devc.csv', sep=',', skiprows=1)
M2 = pd.read_csv('../NIST/Preliminary_Results/PMMA_60_kW_2_cm_devc.csv', sep=',', skiprows=1)
M5 = pd.read_csv('../NIST/Preliminary_Results/PMMA_60_kW_5_mm_devc.csv', sep=',', skiprows=1)
H1 = pd.read_csv('../NIST/Preliminary_Results/PMMA_60_kW_1_cm_hrr.csv', sep=',', skiprows=1)
H2 = pd.read_csv('../NIST/Preliminary_Results/PMMA_60_kW_2_cm_hrr.csv', sep=',', skiprows=1)
H5 = pd.read_csv('../NIST/Preliminary_Results/PMMA_60_kW_5_mm_hrr.csv', sep=',', skiprows=1)

exp_rows = np.array([0,1,2,3,4,5,6,7,8,9])
indices1 = np.zeros(10,dtype=int)
indices2 = np.zeros(10,dtype=int)
indices5 = np.zeros(10,dtype=int)
j=-1
for i in exp_rows:
   j=j+1
   indices1[j] = (H1.HRR>E.loc[i,'HRR']).idxmax()
   indices2[j] = (H2.HRR>E.loc[i,'HRR']).idxmax()
   indices5[j] = (H5.HRR>E.loc[i,'HRR']).idxmax()

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

    x1 = M1.loc[indices1[irow],"Flux-1":"Flux-50"].values[:].astype(float)
    x2 = M2.loc[indices2[irow],"Flux-1":"Flux-50"].values[:].astype(float)
    x5 = M5.loc[indices5[irow],"Flux-1":"Flux-50"].values[:].astype(float)

    f = macfp.plot_to_fig(x_data=x5, y_data=z_FDS, data_label=hrr_label[irow],
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

    f = macfp.plot_to_fig(x_data=x1, y_data=z_FDS, data_label=hrr_label[irow],
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

    f = macfp.plot_to_fig(x_data=x2, y_data=z_FDS, data_label=hrr_label[irow],
                          x_min=0,x_max=150,x_nticks=4,
                          y_min=0,y_max=250,
                          x_label='PLACEHOLDER Heat Flux [kW/m²]',
                          y_label='PLACEHOLDER Height [cm]',
                          marker_style='None',
                          line_style='-.',
                          line_color=color[irow],
                          show_legend=True,
                          legend_location='outside',
                          figure_right_adjust=0,
                          legend_fontsize=8,
                          figure_handle=f)

f.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Output/Plots/PMMA_flame_spread_heatflux_BUWFZJ.pdf')

# plt.show()
