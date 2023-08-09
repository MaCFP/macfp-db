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
import numpy as np
import pandas as pd

plt.close('all')

E = pd.read_csv('../../../Experimental_Data/Burner_steadyHF_Width_multi-layer.csv', sep=',')
x = np.array([-25, -15, 0, 15, 25])
y = np.array([20, 50, 75, 100])

M1 = pd.read_csv('Preliminary_Results/Marinite_60_kW_1_cm_devc.csv', sep=',', skiprows=1)
M2 = pd.read_csv('Preliminary_Results/Marinite_60_kW_2_cm_devc.csv', sep=',', skiprows=1)

X, Y = np.meshgrid(x, y, indexing='xy')
Z = E.loc[1:4,"HF_y-25":"HF_y25"].values[:].astype(float)

Z1 = np.zeros((4,5))
Z1[0,:] = M1.loc[60,"HF_y-25z20":"HF_y25z20"].values[:].astype(float)
Z1[1,:] = M1.loc[60,"HF_y-25z50":"HF_y25z50"].values[:].astype(float)
Z1[2,:] = M1.loc[60,"HF_y-25z75":"HF_y25z75"].values[:].astype(float)
Z1[3,:] = M1.loc[60,"HF_y-25z100":"HF_y25z100"].values[:].astype(float)

Z2 = np.zeros((4,5))
Z2[0,:] = M2.loc[60,"HF_y-25z20":"HF_y25z20"].values[:].astype(float)
Z2[1,:] = M2.loc[60,"HF_y-25z50":"HF_y25z50"].values[:].astype(float)
Z2[2,:] = M2.loc[60,"HF_y-25z75":"HF_y25z75"].values[:].astype(float)
Z2[3,:] = M2.loc[60,"HF_y-25z100":"HF_y25z100"].values[:].astype(float)

levels = [5, 10, 15, 20, 30, 40, 50, 60]

fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, levels)
ax.clabel(CS, inline=False, fontsize=10, colors='red')

CS1 = ax.contour(X, Y, Z1, levels, colors='white')
ax.clabel(CS1, inline=True, fontsize=10, colors='white')

CS2 = ax.contour(X, Y, Z2, levels, colors='yellow', linestyles='dashed')
ax.clabel(CS2, inline=True, fontsize=10, colors='yellow')

plt.xlabel('Width [cm]', fontsize=16)
plt.ylabel('Height [cm]', fontsize=16)

ax.set_xlim(-30,30)
ax.set_ylim(0,120)

#plt.legend(loc='upper right')

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Preliminary_Results/Plots/Burner_heatflux_colormap.pdf')

# plt.show()
