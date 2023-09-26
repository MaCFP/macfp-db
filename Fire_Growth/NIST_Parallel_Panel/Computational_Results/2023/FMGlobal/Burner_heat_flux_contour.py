#!/usr/bin/python3
# Modified from McGrattan
# Sept 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import pandas as pd

plt.close('all')


font_size_axis = 13
font_size_contours = 8
contour_line_widths = 1

# Define contour information.
cont_info = {
    "Exp": ['k', '-', 'Exp.'],
    "Sim_1": ['red', '--', 'Sim. 2.5 cm'],
    "Sim_2": ['yellow', '--', 'Sim. 1.3 cm'],
    "Sim_3": ['green', '--', 'Sim. 0.6 cm']}


E = pd.read_csv('../../../Experimental_Data/Burner_steadyHF_Width_multi-layer.csv', sep=',')
x = np.array([-25, -15, 0, 15, 25])
y = np.array([20, 50, 75, 100])

Z25 = pd.read_csv('Sim_data/Burner/steadyHF/FMGlobal_Burner_steadyHF_25mm.csv', sep=',', skiprows=1)
Z13 = pd.read_csv('Sim_data/Burner/steadyHF/FMGlobal_Burner_steadyHF_13mm.csv', sep=',', skiprows=1)
Z6 = pd.read_csv('Sim_data/Burner/steadyHF/FMGlobal_Burner_steadyHF_6mm.csv', sep=',', skiprows=1)

X, Y = np.meshgrid(x, y, indexing='xy')
Z = E.loc[1:4,"HF_y-25":"HF_y25"].values[:].astype(float)

# Define where the lines are located.
levels = [0, 5, 10, 15, 20, 30, 40, 50, 70]
# Edge length of the data set, i.e. lower part of the panel.
extent = [-0.3,0.3, 0.0,1.0]

fig, ax = plt.subplots(figsize=(5, 5))
CS = plt.contourf(X, Y, Z, levels, extent=extent, cmap=plt.cm.viridis)

# Define colour bar.
plt.clim(2.0, 65.0)
plt.colorbar().set_label('Gauge Heat Flux [kW/m²]',size=font_size_axis)


contours = ax.contour(X, Y, Z, levels,
                      colors=cont_info["Exp"][0],
                      linestyles=cont_info["Exp"][1])
ax.clabel(contours, levels, inline=True, fmt='%1.0f', fontsize=font_size_contours)

CS25 = ax.contour(X, Y, Z25, levels, linewidths=contour_line_widths,
                  colors=cont_info["Sim_1"][0],
                  linestyles=cont_info["Sim_1"][1])
ax.clabel(CS25, inline=True, fmt='%1.0f', fontsize=font_size_contours,
          colors=cont_info["Sim_1"][0])

CS13 = ax.contour(X, Y, Z13, levels, linewidths=contour_line_widths,
                  colors=cont_info["Sim_2"][0],
                  linestyles=cont_info["Sim_2"][1])
ax.clabel(CS13, inline=True, fmt='%1.0f', fontsize=font_size_contours,
          colors=cont_info["Sim_2"][0])

CS6 = ax.contour(X, Y, Z6, levels, linewidths=contour_line_widths,
                  colors=cont_info["Sim_3"][0],
                  linestyles=cont_info["Sim_3"][1])
ax.clabel(CS6, inline=True, fmt='%1.0f', fontsize=font_size_contours,
          colors=cont_info["Sim_3"][0])


plt.xlabel('Width [cm]', fontsize=font_size_axis)
plt.ylabel('Height [cm]', fontsize=font_size_axis)

ax.set_xlim(-30,30)
ax.set_ylim(0,140)

exp_line    = mlines.Line2D([], [], color=cont_info["Exp"][0],
                            linestyle=cont_info["Exp"][1],
                            label=cont_info["Exp"][2])
sim25mm_line = mlines.Line2D([], [], color=cont_info["Sim_1"][0],
                            linestyle=cont_info["Sim_1"][1],
                            label=cont_info["Sim_1"][2])
sim13mm_line = mlines.Line2D([], [], color=cont_info["Sim_2"][0],
                            linestyle=cont_info["Sim_2"][1],
                            label=cont_info["Sim_2"][2])
sim6mm_line = mlines.Line2D([], [], color=cont_info["Sim_3"][0],
                            linestyle=cont_info["Sim_3"][1],
                            label=cont_info["Sim_3"][2])

ax.legend(handles=[exp_line,sim25mm_line,sim13mm_line,sim6mm_line])

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Plots/Burner_heat_flux_contour.pdf', bbox_inches='tight')

# plt.show()
