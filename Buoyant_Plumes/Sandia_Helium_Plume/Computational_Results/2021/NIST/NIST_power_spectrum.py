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
M1p5 = pd.read_csv('Sandia_He_1m_dx1p5cm_devc.csv', header=1, sep=' *, *', engine='python')
M3   = pd.read_csv('Sandia_He_1m_dx3cm_devc.csv',   header=1, sep=' *, *', engine='python')
M6   = pd.read_csv('Sandia_He_1m_dx6cm_devc.csv',   header=1, sep=' *, *', engine='python')
M10  = pd.read_csv('Sandia_He_1m_dx10cm_devc.csv',  header=1, sep=' *, *', engine='python')
M20  = pd.read_csv('Sandia_He_1m_dx20cm_devc.csv',  header=1, sep=' *, *', engine='python')

fs1p5 = len(M1p5['Time'])/max(M1p5['Time'])
fs3   = len(M3['Time'])/max(M3['Time'])
fs6   = len(M6['Time'])/max(M6['Time'])
fs10  = len(M10['Time'])/max(M10['Time'])
fs20  = len(M20['Time'])/ max(M20['Time'])

x1p5 = M1p5['WVELp6']
x3   = M3['WVELp6']
x6   = M6['WVELp6']
x10  = M10['WVELp6']
x20  = M20['WVELp6']

f1p5, Pxx_den_1p5 = signal.periodogram(x1p5, fs1p5)
f3, Pxx_den_3     = signal.periodogram(x3, fs3)
f6, Pxx_den_6     = signal.periodogram(x6, fs6)
f10, Pxx_den_10   = signal.periodogram(x10, fs10)
f20, Pxx_den_20   = signal.periodogram(x20, fs20)

# plot experimental result
fmeas = np.array([1.37, 1.37])
PSDmeas = np.array([min(Pxx_den_1p5), max(Pxx_den_1p5)])
fh=macfp.plot_to_fig(fmeas, PSDmeas,
                  plot_type='linear',
                  x_min=0,x_max=4,y_min=0,y_max=15,
                  x_label='frequency [Hz]',
                  y_label='PSD [V**2/Hz]',
                  line_style='--',
                  line_width=2,
                  line_color='black',
                  institute_label='NIST Cartesian Geometry',
                  data_label='Exp',
                  plot_title='Sandia 1 m Helium Plume Puffing Frequency',
                  show_legend=True,
                  legend_location='right')

# add error to measuered puffing freq
plt.fill_betweenx(PSDmeas, np.array([1.19, 1.19]), np.array([1.53, 1.53]), color='lightgrey', figure=fh)

fh=macfp.plot_to_fig(f1p5, Pxx_den_1p5,plot_type='linear',x_min=0,x_max=4,y_min=0,y_max=15,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=1.5$ cm',line_style='-', line_width=1,line_color='black',  marker_style='o',marker_size=4,marker_edge_color='black',  marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')
fh=macfp.plot_to_fig(f3, Pxx_den_3,    plot_type='linear',x_min=0,x_max=4,y_min=0,y_max=15,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=3$ cm',  line_style='-', line_width=1,line_color='magenta',marker_style='^',marker_size=4,marker_edge_color='magenta',marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')
fh=macfp.plot_to_fig(f6, Pxx_den_6,    plot_type='linear',x_min=0,x_max=4,y_min=0,y_max=15,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=6$ cm',  line_style='-.',line_width=1,line_color='red',    marker_style='s',marker_size=4,marker_edge_color='red',    marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')
fh=macfp.plot_to_fig(f10, Pxx_den_10,  plot_type='linear',x_min=0,x_max=4,y_min=0,y_max=15,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=10$ cm', line_style=':', line_width=1,line_color='green',  marker_style='*',marker_size=4,marker_edge_color='green',  marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')
fh=macfp.plot_to_fig(f20, Pxx_den_20,  plot_type='linear',x_min=0,x_max=4,y_min=0,y_max=15,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='FDS $\Delta x=20$ cm', line_style=':', line_width=1,line_color='blue',   marker_style='+',marker_size=4,marker_edge_color='blue',   marker_fill_color='None',figure_handle=fh,show_legend=True,legend_location='right')

# plt.show()

plt.savefig('./Plots/NIST_Puffing_frequency.pdf')

# loglog spectrum
fh2=macfp.plot_to_fig(f1p5, Pxx_den_1p5,plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',plot_title='Sandia 1 m Helium Plume Power Spectrum',data_label='FDS $\Delta x=1.5$ cm',line_style='-', line_width=1,line_color='black',show_legend=True,legend_location='lower left',legend_framealpha=1.,institute_label='NIST Cartesian Geometry')
macfp.plot_to_fig(f1p5, f1p5**(-5./3.),plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='f**-5/3',line_style='--', line_width=2,line_color='black',show_legend=True,legend_location='lower left',legend_framealpha=1.,figure_handle=fh2)
fnyquist = np.array([0.5*fs1p5, 0.5*fs1p5])
macfp.plot_to_fig(fnyquist, PSDmeas,plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='f Nyquist',line_style='--', line_width=1,line_color='red',show_legend=True,legend_location='lower left',legend_framealpha=1.,figure_handle=fh2)
macfp.plot_to_fig(fmeas, PSDmeas,plot_type='loglog',x_min=0.5,x_max=1000,y_min=.00001,y_max=100,x_label='frequency [Hz]',y_label='PSD [V**2/Hz]',data_label='f puffing',line_style='--', line_width=1,line_color='green',show_legend=True,legend_location='lower left',legend_framealpha=1.,figure_handle=fh2)

# plt.show()

plt.savefig('./Plots/NIST_Power_Spectrum.pdf')
