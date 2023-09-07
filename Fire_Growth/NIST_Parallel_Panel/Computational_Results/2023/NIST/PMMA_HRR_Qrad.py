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

E = pd.read_csv('../../../Experimental_Data/PMMA_HRR_qrad_R6.csv', sep=',', skiprows=[1])
Time = E["Time"].values[:].astype(float)
HRR  = E["HRR"].values[:].astype(float)
HF   = E["HF"].values[:].astype(float)

H1 = pd.read_csv('Preliminary_Results/PMMA_60_kW_1_cm_hrr.csv', sep=',', skiprows=1)
H2 = pd.read_csv('Preliminary_Results/PMMA_60_kW_2_cm_hrr.csv', sep=',', skiprows=1)
H5 = pd.read_csv('Preliminary_Results/PMMA_60_kW_5_mm_hrr.csv', sep=',', skiprows=1)
Time_FDS_1 = H1["Time"].values[:].astype(float)
HRR_FDS_1  = H1["HRR"].values[:].astype(float)
Time_FDS_2 = H2["Time"].values[:].astype(float)
HRR_FDS_2  = H2["HRR"].values[:].astype(float)
Time_FDS_5 = H5["Time"].values[:].astype(float)
HRR_FDS_5  = H5["HRR"].values[:].astype(float)

fig, ax1 = plt.subplots()

lns1=ax1.plot(Time,HRR,marker='None',linestyle='-',color='steelblue',label='HRR, R6')
ax1.set_xlabel('Time [s]', fontsize=16)
ax1.set_ylabel('HRR [kW]', fontsize=16, color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

ax1.set_xlim(0,600)
ax1.set_ylim(0,4000)

lns3=ax1.plot(Time_FDS_5,HRR_FDS_5,marker='None',linestyle='--',color='steelblue',label='FDS 5 mm')
lns4=ax1.plot(Time_FDS_1,HRR_FDS_1,marker='None',linestyle='-.',color='steelblue',label='FDS 1 cm')
lns5=ax1.plot(Time_FDS_2,HRR_FDS_2,marker='None',linestyle=':',color='steelblue',label='FDS 2 cm')

# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
ax2.set_ylim(0,6)

lns2=ax2.plot(Time,HF,marker='None',linestyle='--',color='orange',label='HF-RAD, R6')
ax2.set_ylabel('Rad Heat Flux [kW/m²]', fontsize=16, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# put both labels in one legend
lns = lns1+lns2+lns3+lns4+lns5
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper right')

fig.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Preliminary_Results/Plots/PMMA_HRR_Qrad.pdf')

# plt.show()
