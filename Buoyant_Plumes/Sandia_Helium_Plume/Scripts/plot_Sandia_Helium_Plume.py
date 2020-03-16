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

Plot_Filename_Last = 'None'

# loop over the rows of the config file
for irow in C.index:

    # get parameters from config file
    Exp_Filename   = C.values[irow,C.columns.get_loc('Exp_Filename')]
    Exp_x_Col_Name = C.values[irow,C.columns.get_loc('Exp_x_Col_Name')]
    Exp_y_Col_Name = C.values[irow,C.columns.get_loc('Exp_y_Col_Name')]
    Exp_Data_Label = C.values[irow,C.columns.get_loc('Exp_Data_Label')]
    Exp_Error_Absolute = C.values[irow,C.columns.get_loc('Exp_Error_Absolute')]
    Exp_Error_Relative = C.values[irow,C.columns.get_loc('Exp_Error_Relative')]

    Cmp_Filename   = C.values[irow,C.columns.get_loc('Cmp_Filename')]
    Cmp_x_Col_Name = C.values[irow,C.columns.get_loc('Cmp_x_Col_Name')]
    Cmp_y_Col_Name = C.values[irow,C.columns.get_loc('Cmp_y_Col_Name')]

    Plot_x_Label = C.values[irow,C.columns.get_loc('Plot_x_Label')]
    Plot_y_Label = C.values[irow,C.columns.get_loc('Plot_y_Label')]
    Plot_Filename = C.values[irow,C.columns.get_loc('Plot_Filename')]

    if Plot_Filename!=Plot_Filename_Last:

        # read data from exp file
        # set header to the row where column names are stored (Python is 0 based)
        E = pd.read_csv(expdir+Exp_Filename, sep=',', header=0)

        x = E[Exp_x_Col_Name][::2]
        y = E[Exp_y_Col_Name][::2]

        # plot the exp data
        f = macfp.plot_to_fig(x_data=x, y_data=y,
            data_label=Exp_Data_Label,
            y_error_absolute=Exp_Error_Absolute,
            y_error_relative=Exp_Error_Relative,
            x_label=Plot_x_Label,
            y_label=Plot_y_Label,
            marker_style='o',
            line_style='None',
            x_min=-0.5,x_max=0.5,x_nticks=5,
            y_min=0.0,y_max=1.0,y_nticks=6,
            show_legend=True,legend_location='upper right',
            figure_size=(8,6)
            )

        # plt.figure(f.number) # make figure current
        # plt.show()
    else:
        f = f_Last

    # get the model results
    M = pd.read_csv(cmpdir+Cmp_Filename, sep=',', header=1)

    x = M[Cmp_x_Col_Name][::1]
    y = M[Cmp_y_Col_Name][::1]

    f = macfp.plot_to_fig(x_data=x, y_data=y,
        x_label='Radial Position (m)',
        y_label='Helium Mass Fraction',
        data_label='FDS $\Delta x=6$ cm',
        institute_label=institute,
        figure_handle=f,
        marker_style='',
        line_style='--',
        x_min=-0.5,x_max=0.5,x_nticks=5,
        y_min=0.0,y_max=1.0,y_nticks=6,
        show_legend=True,legend_location='upper right',
        plot_title='Sandia Helium Plume',
        plot_subtitle='$z$ = 0.2 m',
        )

    plt.figure(f.number) # make figure current
    plt.show()

    plt.savefig(pltdir+Plot_Filename+'.pdf')

    Plot_Filename_Last = Plot_Filename
    f_Last = f

