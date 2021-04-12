# McDermott
# 25 March 2021
# power_spectrum.py

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
sys.path.append('../../../../../../macfp-db/Utilities/')

import macfp
import importlib
importlib.reload(macfp)
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
import numpy as np

# get the model results
M1 = pd.read_csv('Baseline/NIST_Methanol_1m_pan_4cm_grid_devc.csv', header=1, sep=' *, *', engine='python')
M2 = pd.read_csv('Baseline/NIST_Methanol_1m_pan_2cm_grid_devc.csv', header=1, sep=' *, *', engine='python')
M3 = pd.read_csv('Baseline/NIST_Methanol_1m_pan_1cm_grid_devc.csv', header=1, sep=' *, *', engine='python')

fs1 = len(M1['Time'])/max(M1['Time'])
fs2 = len(M2['Time'])/max(M2['Time'])
fs3 = len(M3['Time'])/max(M3['Time'])

x1 = M1['w'][M1['Time']>20.]
x2 = M2['w'][M2['Time']>20.]
x3 = M3['w'][M3['Time']>20.]

f1, Pxx_den_1 = signal.periodogram(x1, fs1)
f2, Pxx_den_2 = signal.periodogram(x2, fs2)
f3, Pxx_den_3 = signal.periodogram(x3, fs3)

# plot experimental result
fmeas = np.array([1.37, 1.37])
PSDmeas = np.array([0., 5.])
fh=macfp.plot_to_fig(fmeas, PSDmeas,
                  plot_type='linear',
                  x_min=0.5,x_max=4,y_min=0,y_max=15,
                  x_label='frequency [Hz]',
                  y_label='PSD [V**2/Hz]',
                  line_style='--',
                  line_width=2,
                  line_color='black',
                  institute_label='NIST baseline prescribed MLR',
                  data_label='Exp',
                  plot_title='NIST 1 m Methanol Puffing Frequency',
                  show_legend=True,
                  legend_location='right')

# add error to measuered puffing freq
plt.fill_betweenx(PSDmeas, np.array([1.37, 1.37]), np.array([1.37, 1.37]), color='lightgrey', figure=fh)

fh=macfp.plot_to_fig(f1, Pxx_den_1, plot_type='linear',x_min=0.5,x_max=4,y_min=0,y_max=6,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=4$ cm', line_style='-', line_width=1,line_color='black',  marker_style='o',marker_size=4,marker_edge_color='black', marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')
fh=macfp.plot_to_fig(f2, Pxx_den_2, plot_type='linear',x_min=0.5,x_max=4,y_min=0,y_max=6,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=2$ cm', line_style='-', line_width=1,line_color='magenta',marker_style='^',marker_size=4,marker_edge_color='magenta',marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')
fh=macfp.plot_to_fig(f3, Pxx_den_3, plot_type='linear',x_min=0.5,x_max=4,y_min=0,y_max=6,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=1$ cm', line_style='-.',line_width=1,line_color='red',marker_style='s',marker_size=4,marker_edge_color='red', marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')

# plt.show()

plt.savefig('./Baseline/Plots/NIST_1m_Methanol_puffing_frequency.pdf')

# loglog spectrum
fh2=macfp.plot_to_fig(f3, Pxx_den_3, plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',plot_title='NIST 1 m Methanol Power Spectrum',data_label='FDS $\Delta x=1$ cm',line_style='-', line_width=1,line_color='black',show_legend=True,legend_location='center right',legend_framealpha=1.,institute_label='NIST baseline prescribed MLR')
macfp.plot_to_fig(f3, f3**(-5./3.),plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='f**-5/3',line_style='--', line_width=2,line_color='black',show_legend=True,legend_location='center right',legend_framealpha=1.,figure_handle=fh2)
fnyquist = np.array([0.5*fs3, 0.5*fs3])
macfp.plot_to_fig(fnyquist, PSDmeas,plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='f Nyquist',line_style='--', line_width=1,line_color='red',show_legend=True,legend_location='center right',legend_framealpha=1.,figure_handle=fh2)
macfp.plot_to_fig(fmeas, PSDmeas,plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='f puffing',line_style='--', line_width=1,line_color='green',show_legend=True,legend_location='center right',legend_framealpha=1.,figure_handle=fh2)

# plt.show()

plt.savefig('./Baseline/Plots/NIST_1m_Methanol_Power_Spectrum.pdf')
