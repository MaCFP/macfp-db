#!/usr/bin/python3
#McGrattan
#8 August 2023

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
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
    "Sim_1": ['red', '--', 'Sim. 2.0 cm'],
    "Sim_2": ['yellow', '--', 'Sim. 1.0 cm'],
    "Sim_3": ['green', '--', 'Sim. 0.5 cm']}


E = pd.read_csv('../../../Experimental_Data/Burner_steadyHF_Width_multi-layer.csv', sep=',')
x = np.array([-25, -15, 0, 15, 25])
y = np.array([20, 50, 75, 100])

M1 = pd.read_csv('Preliminary_Results/Marinite_60_kW_1_cm_devc.csv', sep=',', skiprows=1)
M2 = pd.read_csv('Preliminary_Results/Marinite_60_kW_2_cm_devc.csv', sep=',', skiprows=1)
M5 = pd.read_csv('Preliminary_Results/Marinite_60_kW_5_mm_devc.csv', sep=',', skiprows=1)

X, Y = np.meshgrid(x, y, indexing='xy')
Z = E.loc[1:4,"HF_y-25":"HF_y25"].values[:].astype(float)

Z1 = np.zeros((4,5))
Z1[0,:] = M1.loc[50,"HF_y-25z20":"HF_y25z20"].values[:].astype(float)
Z1[1,:] = M1.loc[50,"HF_y-25z50":"HF_y25z50"].values[:].astype(float)
Z1[2,:] = M1.loc[50,"HF_y-25z75":"HF_y25z75"].values[:].astype(float)
Z1[3,:] = M1.loc[50,"HF_y-25z100":"HF_y25z100"].values[:].astype(float)

Z2 = np.zeros((4,5))
Z2[0,:] = M2.loc[50,"HF_y-25z20":"HF_y25z20"].values[:].astype(float)
Z2[1,:] = M2.loc[50,"HF_y-25z50":"HF_y25z50"].values[:].astype(float)
Z2[2,:] = M2.loc[50,"HF_y-25z75":"HF_y25z75"].values[:].astype(float)
Z2[3,:] = M2.loc[50,"HF_y-25z100":"HF_y25z100"].values[:].astype(float)

Z5 = np.zeros((4,5))
Z5[0,:] = M5.loc[50,"HF_y-25z20":"HF_y25z20"].values[:].astype(float)
Z5[1,:] = M5.loc[50,"HF_y-25z50":"HF_y25z50"].values[:].astype(float)
Z5[2,:] = M5.loc[50,"HF_y-25z75":"HF_y25z75"].values[:].astype(float)
Z5[3,:] = M5.loc[50,"HF_y-25z100":"HF_y25z100"].values[:].astype(float)

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

CS2 = ax.contour(X, Y, Z2, levels, linewidths=contour_line_widths,
                 colors=cont_info["Sim_3"][0],
                 linestyles=cont_info["Sim_3"][1])
ax.clabel(CS2, inline=True, fmt='%1.0f', fontsize=font_size_contours,
          colors=cont_info["Sim_3"][0])

CS1 = ax.contour(X, Y, Z1, levels, linewidths=contour_line_widths,
                 colors=cont_info["Sim_2"][0],
                 linestyles=cont_info["Sim_2"][1])
ax.clabel(CS1, inline=True, fmt='%1.0f', fontsize=font_size_contours,
          colors=cont_info["Sim_2"][0])

CS5 = ax.contour(X, Y, Z5, levels, linewidths=contour_line_widths,
                 colors=cont_info["Sim_1"][0],
                 linestyles=cont_info["Sim_1"][1])
ax.clabel(CS5, inline=True, fmt='%1.0f', fontsize=font_size_contours,
          colors=cont_info["Sim_1"][0])

plt.xlabel('Width [cm]', fontsize=font_size_axis)
plt.ylabel('Height [cm]', fontsize=font_size_axis)

# Add instituion and revision label
inst_label_x = 0.025
default_stamp_fontsize = 10
institute_label='NIST'
revision_label='MaCFP-3, Tsukuba, 2023'
# if len(str(ymax))>abs(axis_exponent_max) or len(str(ymin))>abs(axis_exponent_min):
    # inst_label_x = 0.06 # else the institute label overlays the exponential notation multiplier
plt.gca().text(inst_label_x,1.01, institute_label, fontsize=default_stamp_fontsize, transform=plt.gca().transAxes)
plt.gca().text(0.975,       1.01, revision_label, fontsize=default_stamp_fontsize, ha='right', transform=plt.gca().transAxes)


ax.set_xlim(-30,30)
ax.set_ylim(0,140)

exp_line    = mlines.Line2D([], [], color=cont_info["Exp"][0],
                            linestyle=cont_info["Exp"][1],
                            label=cont_info["Exp"][2])
sim5mm_line = mlines.Line2D([], [], color=cont_info["Sim_1"][0],
                            linestyle=cont_info["Sim_1"][1],
                            label=cont_info["Sim_1"][2])
sim1cm_line = mlines.Line2D([], [], color=cont_info["Sim_2"][0],
                            linestyle=cont_info["Sim_2"][1],
                            label=cont_info["Sim_2"][2])
sim2cm_line = mlines.Line2D([], [], color=cont_info["Sim_3"][0],
                            linestyle=cont_info["Sim_3"][1],
                            label=cont_info["Sim_3"][2])

ax.legend(handles=[exp_line,sim5mm_line,sim1cm_line,sim2cm_line])

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Preliminary_Results/Plots/Burner_heat_flux_contour.pdf', bbox_inches='tight')

# plt.show()
