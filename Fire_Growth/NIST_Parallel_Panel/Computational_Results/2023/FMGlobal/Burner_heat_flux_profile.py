#!/usr/bin/python3
# Modified from McGrattan
# Sept 2023

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
M25 = pd.read_csv('Sim_data/Burner/unsteadyHF/FMGlobal_Burner_unsteadyHF_25mm.csv', sep=',').drop([0]).astype(float)
M13 = pd.read_csv('Sim_data/Burner/unsteadyHF/FMGlobal_Burner_unsteadyHF_13mm.csv', sep=',').drop([0]).astype(float)
M6 = pd.read_csv('Sim_data/Burner/unsteadyHF/FMGlobal_Burner_unsteadyHF_6mm.csv', sep=',').drop([0]).astype(float)

# Heights
y = np.array([20,50,75,100])

# Times
times = [20, 40, 60, 80]

# Labels
Exp_Name = ['Exp (20s)','Exp (40s)','Exp (60s)','Exp (80s)']
sim25_Name = ['Sim (20s, 25mm)','Sim (40s, 25mm)','Sim (60s, 25mm)','Sim (80s, 25mm)']
sim13_Name = ['Sim (20s, 13mm)','Sim (40s, 13mm)','Sim (60s, 13mm)','Sim (80s, 13mm)']
sim6_Name = ['Sim (20s, 6mm)','Sim (40s, 6mm)','Sim (60s, 6mm)','Sim (80s, 6mm)']

color=['green','red','purple','brown']

time_rows={}
for sim, name in zip([M25, M13, M6], ['M25', 'M13', 'M6']):
    time_rows[name] = []
    for time in times:
        time_rows[name] += [np.argmin(np.abs(sim['Time'] - time))]

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

    window_size = 5
    start_row = max(0, time_rows['M25'][irow] - window_size)  
    end_row = min(len(M25), time_rows['M25'][irow] + window_size + 1) 
    x25 = M25[start_row:end_row].mean(axis=0).to_numpy()[1:]

    start_row = max(0, time_rows['M13'][irow] - window_size)  
    end_row = min(len(M13), time_rows['M13'][irow] + window_size + 1) 
    x13 = M13[start_row:end_row].mean(axis=0).to_numpy()[1:]

    start_row = max(0, time_rows['M6'][irow] - window_size)  
    end_row = min(len(M6), time_rows['M6'][irow] + window_size + 1) 
    x6 = M6[start_row:end_row].mean(axis=0).to_numpy()[1:]
    
    f = macfp.plot_to_fig(x_data=x25, y_data=y, data_label=sim25_Name[irow],
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
    f = macfp.plot_to_fig(x_data=x13, y_data=y, data_label=sim13_Name[irow],
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
    f = macfp.plot_to_fig(x_data=x6, y_data=y, data_label=sim6_Name[irow],
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

plt.savefig('Plots/Burner_heat_flux_profile.pdf')

# plt.show()
