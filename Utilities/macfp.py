
"""
macfp.py
by Randy McDermott
Feb 2020

Measurement and Computation of Fire Phenomena (MaCFP)

Collection of functions for plotting and analysis
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_to_fig(x_data,y_data,**kwargs):
    """
    Create a simple x,y plot and return the fig handle
    """
    # # useful debug statements
    # print(x_data)
    # print(y_data)
    # for key, value in kwargs.items():
    #     print ("%s == %s" %(key, value))

    ##### default parameters ######
    default_figure_size = (8,6)
    default_ticklabel_fontsize = 16
    default_axeslabel_fontsize = 18
    default_legend_fontsize = 16
    default_title_fontsize = 18
    default_subtitle_fontsize = 16
    default_stamp_fontsize = 12
    ###############################

    if kwargs.get('figure_size'):
        figure_size=kwargs.get('figure_size')
    else:
        figure_size=default_figure_size

    # if figure handle is passed, append to current figure, else generate a new figure
    if kwargs.get('figure_handle'):
        fig = kwargs.get('figure_handle')
        ax = fig.axes[0]
        plt.figure(fig.number)
    else:
        fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=figure_size)

    # generate the main x,y plot
    ax.plot(x_data,y_data,
        markevery=kwargs.get('data_markevery'),
        label=kwargs.get('data_label'),
        markerfacecolor=kwargs.get('marker_color'),
        markeredgecolor=kwargs.get('marker_color'),
        markeredgewidth=kwargs.get('line_width'),
        marker=kwargs.get('marker_style'),
        markersize=kwargs.get('marker_size'),
        linestyle=kwargs.get('line_style'),
        linewidth=kwargs.get('line_width'),
        color=kwargs.get('line_color'))

    # if error range is passed, add it to the plot
    if kwargs.get('y_error_absolute'):
        if kwargs.get('y_error_absolute')>0.:
            ax.fill_between(x_data,y_data-kwargs.get('y_error_absolute'),y_data+kwargs.get('y_error_absolute'),
                alpha=0.1,color=kwargs.get('marker_color'))

    if kwargs.get('y_error_relative'):
        if kwargs.get('y_error_relative')>0.:
            ax.fill_between(x_data,y_data*(1.-kwargs.get('y_error_relative')),y_data*(1.+kwargs.get('y_error_relative')),
                alpha=0.1,color=kwargs.get('marker_color'))

    # set axes and tick properties
    ax.set_xlim(kwargs.get('x_min'),kwargs.get('x_max'))
    ax.set_ylim(kwargs.get('y_min'),kwargs.get('y_max'))
    ax.set_xticks(np.linspace(start = kwargs.get('x_min'), stop = kwargs.get('x_max'), num = kwargs.get('x_nticks'), endpoint=True))
    ax.set_yticks(np.linspace(start = kwargs.get('y_min'), stop = kwargs.get('y_max'), num = kwargs.get('y_nticks'), endpoint=True))

    if kwargs.get('ticklabel_fontsize'):
        ticklabel_fontsize=kwargs.get('ticklabel_fontsize')
    else:
        ticklabel_fontsize=default_ticklabel_fontsize

    plt.setp( ax.xaxis.get_majorticklabels(), rotation=0, fontsize=ticklabel_fontsize )
    plt.setp( ax.yaxis.get_majorticklabels(), rotation=0, fontsize=ticklabel_fontsize )

    if kwargs.get('axeslabel_fontsize'):
        axeslabel_fontsize=kwargs.get('axeslabel_fontsize')
    else:
        axeslabel_fontsize=default_axeslabel_fontsize

    plt.xlabel(kwargs.get('x_label'), fontsize=axeslabel_fontsize)
    plt.ylabel(kwargs.get('y_label'), fontsize=axeslabel_fontsize)

    if kwargs.get('legend_fontsize'):
        legend_fontsize=kwargs.get('legend_fontsize')
    else:
        legend_fontsize=default_legend_fontsize

    if kwargs.get('show_legend'):
        plt.legend(fontsize=legend_fontsize,loc=kwargs.get('legend_location'))

    # plot titles
    if kwargs.get('title_fontsize'):
        title_fontsize=kwargs.get('title_fontsize')
    else:
        title_fontsize=default_title_fontsize

    if kwargs.get('subtitle_fontsize'):
        subtitle_fontsize=kwargs.get('subtitle_fontsize')
    else:
        subtitle_fontsize=default_subtitle_fontsize

    xmin=kwargs.get('x_min')
    xmax=kwargs.get('x_max')
    xpos=xmin+0.05*(xmax-xmin)
    ymin=kwargs.get('y_min')
    ymax=kwargs.get('y_max')
    ypos1=ymin+0.900*(ymax-ymin)
    ypos2=ymin+0.825*(ymax-ymin)
    ax.text(xpos,ypos1, kwargs.get('plot_title'), fontsize=title_fontsize)
    ax.text(xpos,ypos2, kwargs.get('plot_subtitle'), fontsize=subtitle_fontsize)

    # plot Institute + MaCFP stamp
    ax.text(xmin+0.025*(xmax-xmin),ymax+0.01*(ymax-ymin), kwargs.get('institute_label'), fontsize=default_stamp_fontsize)
    ax.text(xmax-0.025*(xmax-xmin),ymax+0.01*(ymax-ymin), 'MaCFP 2020', fontsize=default_stamp_fontsize, ha='right')

    # note: this absolute method works better than fig.tight_layout(), which may change for each call of the figure
    left_adjust, bottom_adjust = get_subplots_adjust_parameters(ticklabel_fontsize,axeslabel_fontsize)
    if ymin<0:
        left_adjust = left_adjust + 0.025 # account for negative sign

    fig.subplots_adjust(left=left_adjust, bottom=bottom_adjust, right=0.95, top=0.95, wspace=0.2, hspace=0.2)

    return fig


def get_subplots_adjust_parameters(ticklabel_fontsize,axeslabel_fontsize):
    """
    automatically select axes adjustments based on fontsize,
    this is a brute force method, but I could not find a more
    automatic way to do it since tight_layout() is not working
    """
    left_adjust = 0.125
    bottom_adjust = 0.125

    if ticklabel_fontsize + axeslabel_fontsize > 34:
        # determined this adjustment by trial and error
        left_adjust   = 0.125 + 0.006875*(ticklabel_fontsize + axeslabel_fontsize - 34)
        bottom_adjust = 0.125 + 0.001875*(ticklabel_fontsize + axeslabel_fontsize - 34)

    return left_adjust, bottom_adjust



def get_nticks(x_min,x_max,x_tick,nticks):
    """
    converts float x_tick, if it exists, to integer nticks
    """
    if x_tick!='None':
        nticks = int((float(x_max)-float(x_min))/float(x_tick)) + 1

    return nticks


def define_plot_parameters(C,irow):
    """
    gathers parameters from config file
    """
    class plot_parameters:

        Exp_Filename         = C.values[irow,C.columns.get_loc('Exp_Filename')]
        Exp_Header_Row       = C.values[irow,C.columns.get_loc('Exp_Header_Row')]
        Exp_x_Col_Name       = C.values[irow,C.columns.get_loc('Exp_x_Col_Name')]
        Exp_y_Col_Name       = C.values[irow,C.columns.get_loc('Exp_y_Col_Name')]
        Exp_Data_Markevery   = C.values[irow,C.columns.get_loc('Exp_Data_Markevery')]
        Exp_Data_Label       = C.values[irow,C.columns.get_loc('Exp_Data_Label')]
        Exp_Marker_Style     = C.values[irow,C.columns.get_loc('Exp_Marker_Style')]
        Exp_Marker_Color     = C.values[irow,C.columns.get_loc('Exp_Marker_Color')]
        Exp_Marker_Size      = C.values[irow,C.columns.get_loc('Exp_Marker_Size')]
        Exp_Line_Style       = C.values[irow,C.columns.get_loc('Exp_Line_Style')]
        Exp_Line_Color       = C.values[irow,C.columns.get_loc('Exp_Line_Color')]
        Exp_Line_Width       = C.values[irow,C.columns.get_loc('Exp_Line_Width')]
        Exp_Error_Absolute   = C.values[irow,C.columns.get_loc('Exp_Error_Absolute')]
        Exp_Error_Relative   = C.values[irow,C.columns.get_loc('Exp_Error_Relative')]

        Cmp_Filename         = C.values[irow,C.columns.get_loc('Cmp_Filename')]
        Cmp_Header_Row       = C.values[irow,C.columns.get_loc('Cmp_Header_Row')]
        Cmp_x_Col_Name       = C.values[irow,C.columns.get_loc('Cmp_x_Col_Name')]
        Cmp_y_Col_Name       = C.values[irow,C.columns.get_loc('Cmp_y_Col_Name')]
        Cmp_Data_Markevery   = C.values[irow,C.columns.get_loc('Cmp_Data_Markevery')]
        Cmp_Data_Label       = C.values[irow,C.columns.get_loc('Cmp_Data_Label')]
        Cmp_Marker_Style     = C.values[irow,C.columns.get_loc('Cmp_Marker_Style')]
        Cmp_Marker_Color     = C.values[irow,C.columns.get_loc('Cmp_Marker_Color')]
        Cmp_Marker_Size      = C.values[irow,C.columns.get_loc('Cmp_Marker_Size')]
        Cmp_Line_Style       = C.values[irow,C.columns.get_loc('Cmp_Line_Style')]
        Cmp_Line_Color       = C.values[irow,C.columns.get_loc('Cmp_Line_Color')]
        Cmp_Line_Width       = C.values[irow,C.columns.get_loc('Cmp_Line_Width')]

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

        Plot_x_Nticks = get_nticks(Plot_x_Min,Plot_x_Max,Plot_x_Tick,C.values[irow,C.columns.get_loc('Plot_x_Nticks')])
        Plot_y_Nticks = get_nticks(Plot_y_Min,Plot_y_Max,Plot_y_Tick,C.values[irow,C.columns.get_loc('Plot_y_Nticks')])
        if Plot_Legend_Location.isdigit():
            Plot_Legend_Location=int(Plot_Legend_Location)

    return plot_parameters
