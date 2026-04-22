
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from fdsplotlib import configure_fds_fonts

configure_fds_fonts(usetex=True)

expdir = '../../../Experimental_Data/'
outdir = './Outputs/'
pltdir = './Plots/'

xvals = [0.05,0.10,0.15,0.22]

expdata = pd.read_csv(expdir + 'GHF_processed.csv')

zvals_e = expdata['z']

e35 = expdata[['x5_35','x10_35','x15_35','x22_35']]
e105 = expdata[['x5_105','x10_105','x15_105','x22_105']]
e145 = expdata[['x5_145','x10_145','x15_145','x22_145']]
e185 = expdata[['x5_105','x10_185','x15_185','x22_185']]

Xe, Ze = np.meshgrid(xvals, zvals_e)

fdsp5cm = pd.read_csv(outdir + 'sbi_p5cm_blowing_line.csv', skiprows=1)

zvalsp5 = fdsp5cm['Height']

Xp5, Zp5 = np.meshgrid(xvals, zvalsp5)

fp5_35 = fdsp5cm[['GHF_x05_35','GHF_x10_35','GHF_x15_35','GHF_x22_35']]
fp5_105 = fdsp5cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
fp5_145 = fdsp5cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
fp5_185 = fdsp5cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

fds1cm = pd.read_csv(outdir + 'sbi_1cm_blowing_line.csv', skiprows=1)

zvals1 = fds1cm['Height']

X1, Z1 = np.meshgrid(xvals, zvals1)

f1_35 = fds1cm[['GHF_x05_35','GHF_x10_35','GHF_x15_35','GHF_x22_35']]
f1_105 = fds1cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
f1_145 = fds1cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
f1_185 = fds1cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

fds2cm = pd.read_csv(outdir + 'sbi_2cm_blowing_line.csv', skiprows=1)

zvals2 = fds2cm['Height']

X2, Z2 = np.meshgrid(xvals, zvals2)

f2_35 = fds2cm[['GHF_x05_35','GHF_x10_35','GHF_x15_35','GHF_x22_35']]
f2_105 = fds2cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
f2_145 = fds2cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
f2_185 = fds2cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

fds4cm = pd.read_csv(outdir + 'sbi_4cm_blowing_line.csv', skiprows=1)

zvals4 = fds4cm['Height']

X4, Z4 = np.meshgrid(xvals, zvals4)

f4_35 = fds4cm[['GHF_x05_35','GHF_x10_35','GHF_x15_35','GHF_x22_35']]
f4_105 = fds4cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
f4_145 = fds4cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
f4_185 = fds4cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

custom_levels = np.linspace(0, 80, 9)

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'35 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

# Plot contour maps
contours = []
cs = axes[0].contourf(Xe, Ze, e35, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_35, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_35, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_35, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_35, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')

plt.savefig(pltdir + 't35_contours.pdf')

fig.clear()

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'105 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

contours = []
cs = axes[0].contourf(Xe, Ze, e105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')

plt.savefig(pltdir + 't105_contours.pdf')

fig.clear()

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'145 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

# Plot contour maps
contours = []
cs = axes[0].contourf(Xe, Ze, e145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')


plt.savefig(pltdir + 't145_contours.pdf')

fig.clear()

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'185 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

# Plot contour maps
contours = []
cs = axes[0].contourf(Xe, Ze, e185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')

plt.savefig(pltdir + 't185_contours.pdf')

fig.clear()

fdsp5cm = pd.read_csv(outdir + 'Spyro/sbi_p5cm_spyro_fsri_line.csv', skiprows=1)

zvalsp5 = fdsp5cm['Height']

Xp5, Zp5 = np.meshgrid(xvals, zvalsp5)

fp5_105 = fdsp5cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
fp5_145 = fdsp5cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
fp5_185 = fdsp5cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

fds1cm = pd.read_csv(outdir + 'Spyro/sbi_1cm_spyro_fsri_line.csv', skiprows=1)

zvals1 = fds1cm['Height']

X1, Z1 = np.meshgrid(xvals, zvals1)

f1_105 = fds1cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
f1_145 = fds1cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
f1_185 = fds1cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

fds2cm = pd.read_csv(outdir + 'Spyro/sbi_2cm_spyro_fsri_line.csv', skiprows=1)

zvals2 = fds2cm['Height']

X2, Z2 = np.meshgrid(xvals, zvals2)

f2_105 = fds2cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
f2_145 = fds2cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
f2_185 = fds2cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

fds4cm = pd.read_csv(outdir + 'Spyro/sbi_4cm_spyro_fsri_line.csv', skiprows=1)

zvals4 = fds4cm['Height']

X4, Z4 = np.meshgrid(xvals, zvals4)

f4_105 = fds4cm[['GHF_x05_105','GHF_x10_105','GHF_x15_105','GHF_x22_105']]
f4_145 = fds4cm[['GHF_x05_145','GHF_x10_145','GHF_x15_145','GHF_x22_145']]
f4_185 = fds4cm[['GHF_x05_185','GHF_x10_185','GHF_x15_185','GHF_x22_185']]

custom_levels = np.linspace(0, 80, 9)

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'35 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

# Plot contour maps
fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'105 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

contours = []
cs = axes[0].contourf(Xe, Ze, e105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_105, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')

plt.savefig(pltdir + 't105_spyro_contours.pdf')

fig.clear()

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'145 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

# Plot contour maps
contours = []
cs = axes[0].contourf(Xe, Ze, e145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_145, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')


plt.savefig(pltdir + 't145_spyro_contours.pdf')

fig.clear()

fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
fig.suptitle(f'185 s', fontsize=14)
fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

# Plot contour maps
contours = []
cs = axes[0].contourf(Xe, Ze, e185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[0].set_aspect('equal')
axes[0].set_ylabel('Height (m)')
axes[0].set_title('Exp', fontsize=10)
axes[0].set_xlabel('Distance (m)')
axes[0].set_ylim(0,1.4)

cs = axes[1].contourf(Xp5, Zp5, fp5_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[1].set_aspect('equal')
axes[1].set_title('0.5 cm', fontsize=10)
axes[1].set_ylim(0,1.4)

cs = axes[2].contourf(X1, Z1, f1_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[2].set_aspect('equal')
axes[2].set_title('1 cm', fontsize=10)
axes[2].set_ylim(0,1.4)

cs = axes[3].contourf(X2, Z2, f2_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[3].set_aspect('equal')
axes[3].set_title('2 cm', fontsize=10)
axes[3].set_ylim(0,1.4)

cs = axes[4].contourf(X4, Z4, f4_185, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
contours.append(cs)
axes[4].set_aspect('equal')
axes[4].set_title('4 cm', fontsize=10)
axes[4].set_ylim(0,1.4)

cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
                   fraction=0.05, pad=0.04)
cbar.set_label('Heat Flux (kW/m²)')

plt.savefig(pltdir + 't185_spyro_contours.pdf')

fig.clear()