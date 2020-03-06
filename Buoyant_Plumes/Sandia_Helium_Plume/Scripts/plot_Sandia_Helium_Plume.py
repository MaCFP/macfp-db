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

# import numpy as np
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


institute = 'NIST'
config_filename = 'NIST_macfp_config.csv'

expdir = '../Experimental_Data/'
cmpdir = '../Computational_Results/2020/' + institute + '/'
pltdir = '../Plots/2020/'

# read the config file
C = pd.read_csv(cmpdir+config_filename,sep=',')

# loop over the rows of the config file
for irow in C.index:
    print(C.values[irow,C.columns.get_loc('Exp_Filename')])
    Exp_Filename = C.values[irow,C.columns.get_loc('Exp_Filename')]

    # read data from exp file
    E = pd.read_csv(expdir+Exp_Filename, sep=',')

    print(C.values[irow,C.columns.get_loc('Exp_x_Col_Name')])
    Exp_x_Col_Name = C.values[irow,C.columns.get_loc('Exp_x_Col_Name')]

    print(C.values[irow,C.columns.get_loc('Exp_y_Col_Name')])
    Exp_y_Col_Name = C.values[irow,C.columns.get_loc('Exp_y_Col_Name')]

    x = E[Exp_x_Col_Name][::2]
    y = E[Exp_y_Col_Name][::2]

    # plot the exp data
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

    # print(C.values[irow,C.columns.get_loc('Plot_Filename')])
    # Plot_Filename = C.values[irow,C.columns.get_loc('Plot_Filename')]

    # plt.savefig(pltdir+Plot_Filename+'.pdf')

    print(C.values[irow,C.columns.get_loc('Cmp_Filename')])
    Cmp_Filename = C.values[irow,C.columns.get_loc('Cmp_Filename')]

    # get the model results
    M = pd.read_csv(cmpdir+Cmp_Filename, sep=',', header=1)

    print(C.values[irow,C.columns.get_loc('Cmp_x_Col_Name')])
    Cmp_x_Col_Name = C.values[irow,C.columns.get_loc('Cmp_x_Col_Name')]

    print(C.values[irow,C.columns.get_loc('Cmp_y_Col_Name')])
    Cmp_y_Col_Name = C.values[irow,C.columns.get_loc('Cmp_y_Col_Name')]

    x = M[Cmp_x_Col_Name][::1]
    y = M[Cmp_y_Col_Name][::1]

    f1 = macfp.plot_to_fig(x_data=x, y_data=y,
        x_label='Radial Position (m)',
        y_label='Helium Mass Fraction',
        data_label='FDS $\Delta x=6$ cm',
        institute_label=institute,
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

    print(C.values[irow,C.columns.get_loc('Plot_Filename')])
    Plot_Filename = C.values[irow,C.columns.get_loc('Plot_Filename')]

    plt.savefig(pltdir+Plot_Filename+'.pdf')



