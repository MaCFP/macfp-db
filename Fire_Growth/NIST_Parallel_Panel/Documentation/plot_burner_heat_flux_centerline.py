#!/usr/bin/python3
#McDermott
#18 July 2023

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

M = pd.read_csv('../Experimental_Data/Beaulieu_2007_Digitized.csv', sep=',')
x = M["Beaulieu_2007 x"].values[:].astype(float)
y = M["Beaulieu_2007 y"].values[:].astype(float)
f, axh = macfp.plot_to_fig(x_data=x, y_data=y, data_label='Beaulieu, 2007',marker_style='+',marker_size=10,line_style='None')

M = pd.read_csv('../Experimental_Data/Wu_1997_Digitized.csv', sep=',')
x = M["Wu_1997 x"].values[:].astype(float)
y = M["Wu_1997 y"].values[:].astype(float)
f, axh = macfp.plot_to_fig(x_data=x, y_data=y, data_label='Wu, 1997',marker_style='d',marker_size=10,line_style='None',figure_handle=f)

# read data from csv file
E = pd.read_csv('../Experimental_Data/Burner_HF_Centerline_multi-layer.csv', sep=',')

y = np.array([20,50,75,100])
Exp_Name = ['20 s','40 s','60 s','80 s']

for irow in range(1,5):
    x = E.loc[irow,"HF_z20":"HF_z100"].values[:].astype(float)
    f, a = macfp.plot_to_fig(x_data=x, y_data=y, data_label=Exp_Name[irow-1],
                          x_min=0,x_max=80,
                          y_min=0,y_max=180,
                          x_label='Heat Flux [kW/m2]',
                          y_label='Height [cm]',
                          marker_style='o',
                          show_legend=True,
                          figure_handle=f)

    plt.errorbar(x[0],y[0],xerr=2,capsize=4,ecolor=a[0].get_color())
    plt.errorbar(x[1],y[1],xerr=1,capsize=4,ecolor=a[0].get_color())
    plt.errorbar(x[2],y[2],xerr=.5,capsize=4,ecolor=a[0].get_color())

# fig.tight_layout(pad=1.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Burner_heatflux.png') #save as png

# plt.show()
