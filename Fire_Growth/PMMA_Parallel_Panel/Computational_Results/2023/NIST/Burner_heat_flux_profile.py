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

plt.close('all')

# read data from csv file
E = pd.read_csv('../../../Experimental_Data/Burner_HF_Centerline_sand_multi-layer.csv', sep=',')
M1 = pd.read_csv('Preliminary_Results/Marinite_60_kW_1_cm_devc.csv', sep=',', skiprows=1)
M2 = pd.read_csv('Preliminary_Results/Marinite_60_kW_2_cm_devc.csv', sep=',', skiprows=1)
M5 = pd.read_csv('Preliminary_Results/Marinite_60_kW_5_mm_devc.csv', sep=',', skiprows=1)

y = np.array([20,50,75,100])
Exp_Name = ['Exp (20 s)','Exp (40 s)','Exp (60 s)','Exp (80 s)']
FDS1_Name = ['FDS (20 s, 1 cm)','FDS (40 s, 1 cm)','FDS (60 s, 1 cm)','FDS (80 s, 1 cm)']
FDS2_Name = ['FDS (20 s, 2 cm)','FDS (40 s, 2 cm)','FDS (60 s, 2 cm)','FDS (80 s, 2 cm)']
FDS5_Name = ['FDS (20 s, 5 mm)','FDS (40 s, 5 mm)','FDS (60 s, 5 mm)','FDS (80 s, 5 mm)']
y1 = np.linspace(1,243, num=50, endpoint=True)

color=['green','red','purple','brown']

FDS_row=[10,20,30,40]

f = macfp.plot_to_fig(x_data=[0,1], y_data=[0,1], marker_style='None',line_style='None')

for irow in range(0,4):
    x = E.loc[irow+1,"HF_z20":"HF_z100"].values[:].astype(float)
    f = macfp.plot_to_fig(x_data=x, y_data=y, data_label=Exp_Name[irow],
                          x_min=0,x_max=80,
                          y_min=0,y_max=180,
                          x_label='Heat Flux [kW/m²]',
                          y_label='Height [cm]',
                          marker_style='o',
                          marker_edge_color=color[irow],
                          marker_fill_color=color[irow],
                          line_style=' ',
                          show_legend=True,
                          figure_right_adjust=0,
                          legend_fontsize=10,
                          figure_handle=f)

    plt.errorbar(x[0],y[0],xerr=2,capsize=4,ecolor=color[irow])
    plt.errorbar(x[1],y[1],xerr=1,capsize=4,ecolor=color[irow])
    plt.errorbar(x[2],y[2],xerr=.5,capsize=4,ecolor=color[irow])

    x1 = M1.loc[FDS_row[irow],"Flux-1":"Flux-50"].values[:].astype(float)
    x2 = M2.loc[FDS_row[irow],"Flux-1":"Flux-50"].values[:].astype(float)
    x5 = M5.loc[FDS_row[irow],"Flux-1":"Flux-50"].values[:].astype(float)
    
    f = macfp.plot_to_fig(x_data=x5, y_data=y1, data_label=FDS5_Name[irow],
                          x_min=0,x_max=80,
                          y_min=0,y_max=180,
                          x_label='Heat Flux [kW/m²]',
                          y_label='Height [cm]',
                          line_color=color[irow],
                          line_style='-',
                          show_legend=True,
                          figure_right_adjust=0,
                          legend_fontsize=10,
                          figure_handle=f)
    f = macfp.plot_to_fig(x_data=x1, y_data=y1, data_label=FDS1_Name[irow],
                          x_min=0,x_max=80,
                          y_min=0,y_max=180,
                          x_label='Heat Flux [kW/m²]',
                          y_label='Height [cm]',
                          line_color=color[irow],
                          line_style='--',
                          show_legend=True,
                          figure_right_adjust=0,
                          legend_fontsize=10,
                          figure_handle=f)
    f = macfp.plot_to_fig(x_data=x2, y_data=y1, data_label=FDS2_Name[irow],
                          x_min=0,x_max=80,
                          y_min=0,y_max=180,
                          x_label='Heat Flux [kW/m²]',
                          y_label='Height [cm]',
                          line_color=color[irow],
                          line_style='-.',
                          show_legend=True,
                          figure_right_adjust=0,
                          legend_fontsize=10,
                          figure_handle=f)


# fig.tight_layout(pad=1.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Preliminary_Results/Plots/Burner_heat_flux_profile.pdf')

# plt.show()
