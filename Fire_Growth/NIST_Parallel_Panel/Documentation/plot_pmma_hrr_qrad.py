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

E = pd.read_csv('../Experimental_Data/PMMA_HRR_qrad_R6.csv', sep=',', skiprows=[1])
Time = E["Time"].values[:].astype(float)
HRR  = E["HRR"].values[:].astype(float)
HF   = E["HF"].values[:].astype(float)

fig, ax1 = plt.subplots()

lns1=ax1.plot(Time,HRR,marker='none',linestyle='-',color='steelblue',label='HRR, R6')
ax1.set_xlabel('Time [s]', fontsize=16)
ax1.set_ylabel('HRR [kW]', fontsize=16, color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

ax1.set_xlim(0,600)
ax1.set_ylim(0,4000)

# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
ax2.set_ylim(0,7.5)

lns2=ax2.plot(Time,HF,marker='none',linestyle='--',color='orange',label='HF-RAD, R6')
ax2.set_ylabel('Rad Heat Flux [kW/m2]', fontsize=16, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# put both labels in one legend
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper left')

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('PMMA_HRR_q-rad-only.png') #save as png

# plt.show()
