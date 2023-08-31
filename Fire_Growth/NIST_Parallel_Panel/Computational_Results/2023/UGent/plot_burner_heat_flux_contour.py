#!/usr/bin/python3
#McGrattan
#31 August 2023

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

E = pd.read_csv('../../../Experimental_Data/Burner_steadyHF_Width_multi-layer.csv', sep=',')
x = np.array([-25, -15, 0, 15, 25])
y = np.array([20, 50, 75, 100])

M2 = pd.read_csv('Output/UGent_Burner_steadyHF_25_mm.csv', sep=',', skiprows=1)
M5 = pd.read_csv('Output/UGent_Burner_steadyHF_50_mm.csv', sep=',', skiprows=1)

X, Y = np.meshgrid(x, y, indexing='xy')
Z = E.loc[1:4,"HF_y-25":"HF_y25"].values[:].astype(float)

Z2 = np.zeros((4,5))
Z2[0,:] = M2.loc[0,"HF_y-25":"HF_y25"].values[:].astype(float)
Z2[1,:] = M2.loc[1,"HF_y-25":"HF_y25"].values[:].astype(float)
Z2[2,:] = M2.loc[2,"HF_y-25":"HF_y25"].values[:].astype(float)
Z2[3,:] = M2.loc[3,"HF_y-25":"HF_y25"].values[:].astype(float)

Z5 = np.zeros((4,5))
Z5[0,:] = M5.loc[0,"HF_y-25":"HF_y25"].values[:].astype(float)
Z5[1,:] = M5.loc[1,"HF_y-25":"HF_y25"].values[:].astype(float)
Z5[2,:] = M5.loc[2,"HF_y-25":"HF_y25"].values[:].astype(float)
Z5[3,:] = M5.loc[3,"HF_y-25":"HF_y25"].values[:].astype(float)

# Define where the lines are located.
levels = [0, 5, 10, 15, 20, 30, 40, 50, 70]
# Edge length of the data set, i.e. lower part of the panel.
extent = [-0.3,0.3, 0.0,1.0]

fig, ax = plt.subplots()
CS = plt.contourf(X, Y, Z, levels, extent=extent, cmap=plt.cm.viridis)

# Define colour bar.
plt.clim(2.0, 65.0)
plt.colorbar().set_label('Gauge Heat Flux [kW/m²]',size=14)

contours = ax.contour(X, Y, Z, levels, colors='gray')
ax.clabel(contours, levels, inline=True, fmt='%1.0f', fontsize=8)

CS5 = ax.contour(X, Y, Z5, levels, colors='red', linestyles='dashed', linewidths=1)
ax.clabel(CS5, inline=True, fmt='%1.0f', fontsize=8, colors='red')

CS2 = ax.contour(X, Y, Z2, levels, colors='green', linestyles='dashed', linewidths=1)
ax.clabel(CS2, inline=True, fmt='%1.0f', fontsize=8, colors='green')

plt.xlabel('Width [cm]', fontsize=16)
plt.ylabel('Height [cm]', fontsize=16)

ax.set_xlim(-30,30)
ax.set_ylim(0,140)

exp_line    = mlines.Line2D([], [], color='gray', label='exp')
sim50mm_line = mlines.Line2D([], [], color='red', linestyle='--', label='sim 50 mm')
sim25mm_line = mlines.Line2D([], [], color='green', linestyle='--', label='sim 25 mm')

ax.legend(handles=[exp_line,sim25mm_line,sim50mm_line])

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Plots/UGent_NIST_Parallel_Panel_HF_contours.pdf')

# plt.show()
