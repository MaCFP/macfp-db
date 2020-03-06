
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
    ax.plot(x_data,y_data,label=kwargs.get('data_label'),color=kwargs.get('marker_color'),
        marker=kwargs.get('marker_style'),linestyle=kwargs.get('line_style'))

    # if error range is passed, add it to the plot
    if kwargs.get('y_error_absolute'):
        ax.fill_between(x_data,y_data-kwargs.get('y_error_absolute'),y_data+kwargs.get('y_error_absolute'),
            alpha=0.1,color=kwargs.get('marker_color'))

    if kwargs.get('y_error_relative'):
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

    fig.tight_layout(pad=0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.95, 0.95])

    # plt.show()
    # plt.savefig(plot_fname)

    return fig