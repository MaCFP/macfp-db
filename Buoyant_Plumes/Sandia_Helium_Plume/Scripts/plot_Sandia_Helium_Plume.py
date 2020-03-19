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

    # define plot parameters and return them in an object called pp
    pp = macfp.define_plot_parameters(C,irow)

    if pp.Plot_Filename!=Plot_Filename_Last:

        # read data from exp file
        # set header to the row where column names are stored (Python is 0 based)
        E = pd.read_csv(expdir+pp.Exp_Filename, header=pp.Exp_Header_Row-1, sep=' *, *', engine='python')

        x = E[pp.Exp_x_Col_Name]
        y = E[pp.Exp_y_Col_Name]

        # plot the exp data
        f = macfp.plot_to_fig(x_data=x, y_data=y,
            data_markevery=pp.Exp_Data_Markevery,
            data_label=pp.Exp_Data_Label,
            y_error_absolute=pp.Exp_Error_Absolute,
            y_error_relative=pp.Exp_Error_Relative,
            x_label=pp.Plot_x_Label,
            y_label=pp.Plot_y_Label,
            marker_style=pp.Exp_Marker_Style,
            marker_color=pp.Exp_Marker_Color,
            marker_size=pp.Exp_Marker_Size,
            line_style=pp.Exp_Line_Style,
            line_color=pp.Exp_Line_Color,
            line_width=pp.Exp_Line_Width,
            x_min=pp.Plot_x_Min,x_max=pp.Plot_x_Max,x_nticks=pp.Plot_x_Nticks,
            y_min=pp.Plot_y_Min,y_max=pp.Plot_y_Max,y_nticks=pp.Plot_y_Nticks,
            show_legend=pp.Plot_Show_Legend,legend_location=pp.Plot_Legend_Location,
            figure_size=(8,6)
            )

        # plt.figure(f.number) # make figure current
        # plt.show()
    else:
        f = f_Last

    # get the model results
    M = pd.read_csv(cmpdir+pp.Cmp_Filename, header=pp.Cmp_Header_Row-1, sep=' *, *', engine='python')

    x = M[pp.Cmp_x_Col_Name]
    y = M[pp.Cmp_y_Col_Name]

    f = macfp.plot_to_fig(x_data=x, y_data=y,
        institute_label=institute,
        figure_handle=f,
        data_markevery=pp.Cmp_Data_Markevery,
        x_label=pp.Plot_x_Label,
        y_label=pp.Plot_y_Label,
        data_label=pp.Cmp_Data_Label,
        marker_style=pp.Cmp_Marker_Style,
        marker_color=pp.Cmp_Marker_Color,
        marker_size=pp.Cmp_Marker_Size,
        line_style=pp.Cmp_Line_Style,
        line_color=pp.Cmp_Line_Color,
        line_width=pp.Cmp_Line_Width,
        x_min=pp.Plot_x_Min,x_max=pp.Plot_x_Max,x_nticks=pp.Plot_x_Nticks,
        y_min=pp.Plot_y_Min,y_max=pp.Plot_y_Max,y_nticks=pp.Plot_y_Nticks,
        show_legend=pp.Plot_Show_Legend,legend_location=pp.Plot_Legend_Location,
        plot_title=pp.Plot_Title,
        plot_subtitle=pp.Plot_Subtitle,
        )

    plt.figure(f.number) # make figure current
    plt.show()

    # create plot directory if it does not exist
    isDir = os.path.isdir(pltdir)
    if not isDir:
        os.mkdir(pltdir)

    plt.savefig(pltdir + pp.Plot_Filename)

    Plot_Filename_Last = pp.Plot_Filename
    f_Last = f

