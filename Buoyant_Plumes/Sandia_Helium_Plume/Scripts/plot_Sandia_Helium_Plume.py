#!/usr/bin/python
#McDermott
#4 Feb 2020

import sys
sys.path.append('../../../Utilities/') # relative path of macfp module

import macfp
# need this while macfp is in development
import importlib
importlib.reload(macfp)
# =======================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# rc('font',**{'family':'serif','serif':['Palatino']})

plt.rcParams['mathtext.fontset'] = 'dejavusans' # valid strings are ['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans', 'custom']
plt.rcParams['pdf.compression'] = 6 # 0 to 9 (file size was no smaller with 9)
plt.rcParams['pdf.fonttype'] = 3 # 42 embeds true type fonts into pdf (large file size)
# plt.rcParams['text.usetex'] = True # supports latex math

plt.close('all')

expdir = '../Experimental_Data/'

# read data from _hrr file
M = pd.read_csv(expdir+'Sandia_He_1m_p2.csv', sep=',')

x = M['x (m)'][::2]
y = M['Y He'][::2]

f1 = macfp.plot_to_fig(x_data=x, y_data=y,
    data_label='Exp',
    y_error_absolute=0.08,
    x_label='Radial Position (m)',
    y_label='Helium Mass Fraction',
    marker_style='o',
    line_style='None',
    x_min=-0.5,x_max=0.5,x_nticks=5,
    y_min=0.0,y_max=1.0,y_nticks=6,
    show_legend=True,legend_location='upper right',
    figure_size=(8,6)
    )

plt.figure(f1.number) # make f1 current
plt.show()
plt.savefig('../Plots/test2.pdf')

# read data from _hrr file
M = pd.read_csv(expdir+'Sandia_He_1m_p4.csv', sep=',')

x = M['x (m)'][::2]
y = M['Y He'][::2]

f1 = macfp.plot_to_fig(x_data=x, y_data=y,
    x_label='Radial Position (m)',
    y_label='Helium Mass Fraction',
    data_label='FDS $\Delta x=1$ cm',
    institute_label='NIST',
    figure_handle=f1,
    marker_style='',
    line_style='--',
    x_min=-0.5,x_max=0.5,x_nticks=5,
    y_min=0.0,y_max=1.0,y_nticks=6,
    show_legend=True,legend_location='upper right',
    plot_title='Sandia Helium Plume',
    plot_subtitle='$z$ = 0.2 m'
    )

plt.figure(f1.number) # make f1 current
plt.show()
plt.savefig('../Plots/test3.pdf')

# fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(8,6))

# ax.plot(x,y,marker='o',linestyle='none')
# ax.fill_between(x,y-0.08,y+0.08,alpha=0.1)

# ax.set_ylim(0.,1.)
# ax.set_xlim(-0.5,0.5)
# ax.set_xticks(np.linspace(start = -0.5, stop = 0.5, num = 5, endpoint=True))
# ax.set_yticks(np.linspace(start = 0, stop = 1, num = 6, endpoint=True))
# plt.setp( ax.xaxis.get_majorticklabels(), rotation=0, fontsize=16 )
# plt.setp( ax.yaxis.get_majorticklabels(), rotation=0, fontsize=16 )

# # common axis labels
# plt.xlabel('Radial Position (m)', fontsize=18)
# plt.ylabel('Helium Mass Fraction', fontsize=18)

# # plot title
# ax.text(-0.45, 0.9, 'Sandia Helium Plume', fontsize=18)
# ax.text(-0.45, 0.85, '$z$ = 0.2 m', fontsize=18)

# fig.tight_layout(pad=0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.95, 0.95])

# plt.show()
# plt.savefig('test.pdf')

