#!/usr/bin/python
#McDermott
#4 Feb 2020

import os
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
C = pd.read_csv(cmpdir+config_filename, sep=' *, *', engine='python')

Plot_Filename_Last = 'None'

# loop over the rows of the config file
for irow in C.index:

    # get parameters from config file
    Exp_Filename         = C.values[irow,C.columns.get_loc('Exp_Filename')]
    Exp_Header_Row       = C.values[irow,C.columns.get_loc('Exp_Header_Row')]
    Exp_x_Col_Name       = C.values[irow,C.columns.get_loc('Exp_x_Col_Name')]
    Exp_y_Col_Name       = C.values[irow,C.columns.get_loc('Exp_y_Col_Name')]
    Exp_Data_Skip        = C.values[irow,C.columns.get_loc('Exp_Data_Skip')]
    Exp_Data_Label       = C.values[irow,C.columns.get_loc('Exp_Data_Label')]
    Exp_Marker_Style     = C.values[irow,C.columns.get_loc('Exp_Marker_Style')]
    Exp_Line_Style       = C.values[irow,C.columns.get_loc('Exp_Line_Style')]
    Exp_Error_Absolute   = C.values[irow,C.columns.get_loc('Exp_Error_Absolute')]
    Exp_Error_Relative   = C.values[irow,C.columns.get_loc('Exp_Error_Relative')]

    Cmp_Filename         = C.values[irow,C.columns.get_loc('Cmp_Filename')]
    Cmp_Header_Row       = C.values[irow,C.columns.get_loc('Cmp_Header_Row')]
    Cmp_x_Col_Name       = C.values[irow,C.columns.get_loc('Cmp_x_Col_Name')]
    Cmp_y_Col_Name       = C.values[irow,C.columns.get_loc('Cmp_y_Col_Name')]
    Cmp_Data_Skip        = C.values[irow,C.columns.get_loc('Cmp_Data_Skip')]
    Cmp_Data_Label       = C.values[irow,C.columns.get_loc('Cmp_Data_Label')]
    Cmp_Marker_Style     = C.values[irow,C.columns.get_loc('Cmp_Marker_Style')]
    Cmp_Line_Style       = C.values[irow,C.columns.get_loc('Cmp_Line_Style')]

    Plot_x_Label         = C.values[irow,C.columns.get_loc('Plot_x_Label')]
    Plot_y_Label         = C.values[irow,C.columns.get_loc('Plot_y_Label')]
    Plot_Title           = C.values[irow,C.columns.get_loc('Plot_Title')]
    Plot_Subtitle        = C.values[irow,C.columns.get_loc('Plot_Subtitle')]
    Plot_x_Min           = C.values[irow,C.columns.get_loc('Plot_x_Min')]
    Plot_x_Max           = C.values[irow,C.columns.get_loc('Plot_x_Max')]
    Plot_x_Tick          = C.values[irow,C.columns.get_loc('Plot_x_Tick')]
    Plot_y_Min           = C.values[irow,C.columns.get_loc('Plot_y_Min')]
    Plot_y_Max           = C.values[irow,C.columns.get_loc('Plot_y_Max')]
    Plot_y_Tick          = C.values[irow,C.columns.get_loc('Plot_y_Tick')]
    Plot_Show_Legend     = C.values[irow,C.columns.get_loc('Plot_Show_Legend')]
    Plot_Legend_Location = C.values[irow,C.columns.get_loc('Plot_Legend_Location')]
    Plot_Filename        = C.values[irow,C.columns.get_loc('Plot_Filename')]
    Plot_Filetype        = C.values[irow,C.columns.get_loc('Plot_Filetype')]

    Plot_x_Nticks = macfp.get_nticks(Plot_x_Min,Plot_x_Max,Plot_x_Tick,C.values[irow,C.columns.get_loc('Plot_x_Nticks')])
    Plot_y_Nticks = macfp.get_nticks(Plot_y_Min,Plot_y_Max,Plot_y_Tick,C.values[irow,C.columns.get_loc('Plot_y_Nticks')])
    if Plot_Legend_Location.isdigit():
        Plot_Legend_Location=int(Plot_Legend_Location)

    if Plot_Filename!=Plot_Filename_Last:

        # read data from exp file
        # set header to the row where column names are stored (Python is 0 based)
        E = pd.read_csv(expdir+Exp_Filename, header=Exp_Header_Row-1, sep=' *, *', engine='python')

        x = E[Exp_x_Col_Name][::Exp_Data_Skip+1]
        y = E[Exp_y_Col_Name][::Exp_Data_Skip+1]

        # plot the exp data
        f = macfp.plot_to_fig(x_data=x, y_data=y,
            data_label=Exp_Data_Label,
            y_error_absolute=Exp_Error_Absolute,
            y_error_relative=Exp_Error_Relative,
            x_label=Plot_x_Label,
            y_label=Plot_y_Label,
            marker_style=Exp_Marker_Style,
            line_style=Exp_Line_Style,
            x_min=Plot_x_Min,x_max=Plot_x_Max,x_nticks=Plot_x_Nticks,
            y_min=Plot_y_Min,y_max=Plot_y_Max,y_nticks=Plot_y_Nticks,
            show_legend=Plot_Show_Legend,legend_location=Plot_Legend_Location,
            figure_size=(8,6)
            )

        # plt.figure(f.number) # make figure current
        # plt.show()
    else:
        f = f_Last

    # get the model results
    M = pd.read_csv(cmpdir+Cmp_Filename, header=Cmp_Header_Row-1, sep=' *, *', engine='python')

    x = M[Cmp_x_Col_Name][::Cmp_Data_Skip+1]
    y = M[Cmp_y_Col_Name][::Cmp_Data_Skip+1]

    f = macfp.plot_to_fig(x_data=x, y_data=y,
        x_label=Plot_x_Label,
        y_label=Plot_y_Label,
        data_label=Cmp_Data_Label,
        institute_label=institute,
        figure_handle=f,
        marker_style=Cmp_Marker_Style,
        line_style=Cmp_Line_Style,
        x_min=Plot_x_Min,x_max=Plot_x_Max,x_nticks=Plot_x_Nticks,
        y_min=Plot_y_Min,y_max=Plot_y_Max,y_nticks=Plot_y_Nticks,
        show_legend=Plot_Show_Legend,legend_location=Plot_Legend_Location,
        plot_title=Plot_Title,
        plot_subtitle=Plot_Subtitle,
        )

    plt.figure(f.number) # make figure current
    plt.show()

    isDir = os.path.isdir(pltdir)
    if not isDir:
        os.mkdir(pltdir)

    plt.savefig(pltdir + Plot_Filename + '.' + Plot_Filetype)

    Plot_Filename_Last = Plot_Filename
    f_Last = f

