
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
    # print(x_data)
    # print(y_data)
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

    if kwargs.get('figure_handle'):
        fig = kwargs.get('figure_handle')
        ax = kwargs.get('axes_handle')
        plt.figure(fig.number)
    else:
        fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(8,6))

    ax.plot(x_data,y_data,label=kwargs.get('data_label'),color=kwargs.get('marker_color'),
        marker=kwargs.get('marker_style'),linestyle=kwargs.get('line_style'))

    if kwargs.get('y_error_absolute'):
        ax.fill_between(x_data,y_data-kwargs.get('y_error_absolute'),y_data+kwargs.get('y_error_absolute'),
            alpha=0.1,color=kwargs.get('marker_color'))

    if kwargs.get('y_error_relative'):
        ax.fill_between(x_data,y_data*(1.-kwargs.get('y_error_relative')),y_data*(1.+kwargs.get('y_error_relative')),
            alpha=0.1,color=kwargs.get('marker_color'))

    ax.set_xlim(kwargs.get('x_min'),kwargs.get('x_max'))
    ax.set_ylim(kwargs.get('y_min'),kwargs.get('y_max'))
    ax.set_xticks(np.linspace(start = kwargs.get('x_min'), stop = kwargs.get('x_max'), num = kwargs.get('x_nticks'), endpoint=True))
    ax.set_yticks(np.linspace(start = kwargs.get('y_min'), stop = kwargs.get('y_max'), num = kwargs.get('y_nticks'), endpoint=True))
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=0, fontsize=16 )
    plt.setp( ax.yaxis.get_majorticklabels(), rotation=0, fontsize=16 )

    plt.xlabel(kwargs.get('x_label'), fontsize=18)
    plt.ylabel(kwargs.get('y_label'), fontsize=18)

    if kwargs.get('show_legend'):
        plt.legend(fontsize=16)

    # # plot title
    # ax.text(-0.45, 0.9, 'Sandia Helium Plume', fontsize=18)
    # ax.text(-0.45, 0.85, '$z$ = 0.2 m', fontsize=18)

    fig.tight_layout(pad=0, h_pad=0.0, w_pad=0.0, rect=[0.10, 0.10, 0.95, 0.95])

    # plt.show()
    # plt.savefig(plot_fname)

    return fig, ax