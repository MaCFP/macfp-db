#!/usr/bin/python3
#McDermott
#20 July 2023

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

E = pd.read_csv('../Experimental_Data/Burner_steadyHF_Width_multi-layer.csv', sep=',')
x = np.array([-25, -15, 0, 15, 25])
y = np.array([20, 50, 75, 100])

X, Y = np.meshgrid(x, y, indexing='xy')
Z = E.loc[1:4,"HF_y-25":"HF_y25"].values[:].astype(float)

# Define where the lines are located.
levels = [0, 5, 10, 15, 20, 30, 40, 50, 70]
# Edge length of the data set, i.e. lower part of the panel.
extent = [-0.3,0.3, 0.0,1.0]

fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, levels, extent=extent)

# Contour lines of the gauge heat flux distribution.
contours = plt.contour(X, Y, Z, levels, colors='black')
plt.clabel(contours, levels, inline=True,
           fmt='%1.0f',  # Set number of digits for contour labels.
           fontsize=10)

# add 3 gauge avg
firstlabel=True
for i in range(len(x)):
    for j in range(len(y)):
        if firstlabel:
            plt.plot(x[i],y[j],marker='^',markerfacecolor='black',markeredgecolor='black',linewidth=0,label='3 gauge avg')
            firstlabel=False
        elif x[i]!=0:
            plt.plot(x[i],y[j],marker='^',markerfacecolor='black',markeredgecolor='black')

# add 6 gauge avg
plt.plot(x[2],y[3],marker='*',markerfacecolor='black',markeredgecolor='black',linewidth=0,label='6 gauge avg')
plt.plot(x[2],y[2],marker='*',markerfacecolor='black',markeredgecolor='black',linewidth=0)

# add 12 gauge avg
plt.plot(x[2],y[1],marker='o',markerfacecolor='black',markeredgecolor='black',linewidth=0,label='12 gauge avg')
plt.plot(x[2],y[0],marker='o',markerfacecolor='black',markeredgecolor='black',linewidth=0)

plt.xlabel('Width [cm]', fontsize=16)
plt.ylabel('Height [cm]', fontsize=16)

ax.set_xlim(-30,30)
ax.set_ylim(0,250)

plt.legend(loc='upper right')

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Burner_heatflux_colormap.png') #save as png

# plt.show()
