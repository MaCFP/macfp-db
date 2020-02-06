#!/usr/bin/python
#McDermott
#4 Feb 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'],'size':16})

plt.close('all')

# read data from _hrr file
M = pd.read_csv('Output_temperature_PDF.csv', sep=',')

# build column lists
L = ['Temperature (K)','Temperature PDF (1/K)']
Z = ['1.0D','1.5D','2.0D','2.5D','3.0D','3.5D']
R = ['0 cm','1 cm','2 cm','3 cm','4 cm','5 cm','6 cm','7 cm','8 cm','9 cm','10 cm','11 cm']

C = [] # empty list
for i in range(len(Z)):
    for j in range(len(R)):
        for k in range(len(L)):
            C.append(L[k]+' '+Z[i]+' radius: '+R[j])

# write data to a file
# M.to_csv('test.csv',columns=C,index=None)

fig, axs = plt.subplots(nrows=6, ncols=5, sharex=True, sharey=True, gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(10, 6))

# build plots specifically for Ren et al. 2020 Fig 7
for i in range(6):
    for j in range(5):
        C0='Temperature (K) '+Z[i]+' radius: '+R[j]
        C1='Temperature PDF (1/K) '+Z[i]+' radius: '+R[j]
        axs[i,j].plot(M[C0],M[C1])

# hide x labels and tick labels for all but bottom plot.
for ax in axs.flat:
    # print(ax.get_position())
    ax.set_ylim(0,0.0025)
    ax.label_outer()
    ax.set_xticks([500,1000,1500,2000])
    ax.set_yticks([0.0005,0.001,0.0015,0.002])
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=45, fontsize=8 )
    plt.setp( ax.yaxis.get_majorticklabels(), rotation=0,  fontsize=8 )

# common axis labels
fig.text(0.5, 0.04, 'Temperature (K)', ha='center')
fig.text(0.04, 0.5, 'PDF (1/K)', va='center', rotation='vertical')

# radius and height labels
colx0=0.5*(axs[0,0].get_position().x0 + axs[0,0].get_position().x1)-0.01
colx1=0.5*(axs[0,1].get_position().x0 + axs[0,1].get_position().x1)-0.015
colx2=0.5*(axs[0,2].get_position().x0 + axs[0,2].get_position().x1)-0.015
colx3=0.5*(axs[0,3].get_position().x0 + axs[0,3].get_position().x1)-0.02
colx4=0.5*(axs[0,4].get_position().x0 + axs[0,4].get_position().x1)-0.02

fig.text(colx0, 0.95, 'r = 0 cm', ha='center')
fig.text(colx1, 0.95, 'r = 1 cm', ha='center')
fig.text(colx2, 0.95, 'r = 2 cm', ha='center')
fig.text(colx3, 0.95, 'r = 3 cm', ha='center')
fig.text(colx4, 0.95, 'r = 4 cm', ha='center')

rowy0=0.5*(axs[0,0].get_position().y0 + axs[0,0].get_position().y1)+0.02
rowy1=0.5*(axs[1,0].get_position().y0 + axs[1,0].get_position().y1)+0.02
rowy2=0.5*(axs[2,0].get_position().y0 + axs[2,0].get_position().y1)+0.02
rowy3=0.5*(axs[3,0].get_position().y0 + axs[3,0].get_position().y1)+0.02
rowy4=0.5*(axs[4,0].get_position().y0 + axs[4,0].get_position().y1)+0.02
rowy5=0.5*(axs[5,0].get_position().y0 + axs[5,0].get_position().y1)+0.02

fig.text(0.89, rowy0, 'z = 1.0 D', ha='left')
fig.text(0.89, rowy1, 'z = 1.5 D', ha='left')
fig.text(0.89, rowy2, 'z = 2.0 D', ha='left')
fig.text(0.89, rowy3, 'z = 2.5 D', ha='left')
fig.text(0.89, rowy4, 'z = 3.0 D', ha='left')
fig.text(0.89, rowy5, 'z = 3.5 D', ha='left')

fig.tight_layout(pad=1.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.show()
