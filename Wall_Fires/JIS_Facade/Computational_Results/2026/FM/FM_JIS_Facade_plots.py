#!/panfs/lux/miniconda3/envs/sciml-torch/bin/python3
"""
FM_JIS_Facade_plots.py

Generates comparison plots between FM fireFoam (0.5-inch uniform grid)
simulation results and the JIS A 1310 façade calibration fire test
experimental data from:

  Sun X. et al., Fire and Materials, 48:411-425, 2024.

Plots produced (saved to ./Plots/):
  1. FM_JIS_Facade_0p5in_HF_profile.png   – Total heat flux vs height
  2. FM_JIS_Facade_0p5in_CHF_profile.png  – Convective heat flux vs height
  3. FM_JIS_Facade_0p5in_RHF_profile.png  – Radiative heat flux vs height
  4. FM_JIS_Facade_0p5in_T_Y0_profile.png – Surface temperature at Y=0

Usage (from this directory):
  python3 FM_JIS_Facade_plots.py

Requires: numpy, pandas, matplotlib
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')          # no display needed
import matplotlib.pyplot as plt

# ─────────────────────────── Paths ───────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXP_DIR    = os.path.normpath(os.path.join(
                 SCRIPT_DIR, '..', '..', '..', 'Experimental_Data'))
SIM_FILE   = os.path.join(SCRIPT_DIR, 'FM_JIS_Facade_0p5in_line.csv')
PLOTS_DIR  = os.path.join(SCRIPT_DIR, 'Plots')
os.makedirs(PLOTS_DIR, exist_ok=True)

# ─────────────────────────── Coordinate offset ───────────────────────────────
# FM simulation z-coordinates originate at the floor.
# Experimental z-coordinates originate at the upper edge of the window opening.
# Window top height from the floor: 1.36 m (from snappyHexMeshDict window
# faceZone box: z = 0.45–1.36 m).  FM gauge alignment check:
#   z_sim=[2.265, 2.865, 3.365, 3.865] → z_exp=[0.905, 1.505, 2.005, 2.505]
#   matches experimental HF gauge heights z_exp=[0.9, 1.5, 2.0, 2.5] m.
H_WINDOW_TOP = 1.36    # metres

# ─────────────────────────── Plot style ──────────────────────────────────────
plt.rcParams.update({
    'font.family'  : 'sans-serif',
    'font.size'    : 10,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'legend.fontsize': 8,
    'figure.dpi'   : 150,
})

COLORS  = {'600': '#1f77b4', '750': '#ff7f0e', '900': '#d62728'}
MARKERS = {'600': 'o', '750': 's', '900': '^'}
POWERS  = ['600', '750', '900']

# ─────────────────────────── Load data ───────────────────────────────────────
print('Loading simulation data:', SIM_FILE)
if not os.path.isfile(SIM_FILE):
    sys.exit(f'ERROR: simulation file not found: {SIM_FILE}')

# Two-row MaCFP header: row 0 = units, row 1 = column names, rows 2+ = data
sim  = pd.read_csv(SIM_FILE, header=1)

# Convert FM z (floor origin) → experimental z (window-top origin)
z_hf = sim['z-HF'].values - H_WINDOW_TOP
z_t  = sim['z-T'].values  - H_WINDOW_TOP

# ── Experimental heat flux (total, on façade surface) ────────────────────────
exp_hf_path = os.path.join(EXP_DIR, 'Sun_FAM_2024_mean_heat_flux.csv')
if not os.path.isfile(exp_hf_path):
    sys.exit(f'ERROR: experimental file not found: {exp_hf_path}')
exp_hf = pd.read_csv(exp_hf_path)
print('Loaded experimental HF:', exp_hf_path)

# ── Experimental temperature (gas, X=0 = façade surface, Y=0 = centerline) ──
exp_t_path = os.path.join(EXP_DIR, 'Sun_FAM_2024_mean_temperature.csv')
if not os.path.isfile(exp_t_path):
    sys.exit(f'ERROR: experimental file not found: {exp_t_path}')
exp_t_all = pd.read_csv(exp_t_path)
exp_t = exp_t_all[exp_t_all['X(m)'] == 0.0].copy().reset_index(drop=True)
print('Loaded experimental temperature (X=0 filter):', exp_t_path)

# ─────────────────────────── Utility ─────────────────────────────────────────
def save_fig(fig, name):
    path = os.path.join(PLOTS_DIR, name)
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  -> Saved: {name}')

# ─────────────────────────────────────────────────────────────────────────────
# Figure 1 – Total heat flux profiles  (FM vs experimental)
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(11, 4.5), sharey=True)
fig.suptitle(
    'JIS A 1310 Façade – Total Heat Flux vs Height\n'
    'FM fireFoam (0.5 in grid) vs Experiment (Sun 2024)',
    fontsize=10)

for ax, pwr in zip(axes, POWERS):
    # FM simulation
    ax.plot(sim[f'HF_{pwr}'], z_hf,
            MARKERS[pwr] + '-', color=COLORS[pwr],
            lw=1.5, ms=5, label='FM fireFoam')
    # Experimental (symbols only)
    ax.plot(exp_hf[f'{pwr}kW(kW/m2)'], exp_hf['Z(m)'],
            'ks', ms=7, mfc='none', mew=1.2, label='Exp (Sun 2024)')
    ax.set_xlabel('Total Heat Flux (kW/m²)')
    ax.set_title(f'{pwr} kW')
    ax.set_xlim(left=0)
    ax.set_ylim(0, 3.0)
    ax.legend(loc='upper right')
    ax.grid(True, ls=':', alpha=0.5)

axes[0].set_ylabel('Height above window top (m)')
fig.tight_layout()
save_fig(fig, 'FM_JIS_Facade_0p5in_HF_profile.png')

# ─────────────────────────────────────────────────────────────────────────────
# Figure 2 – Convective heat flux profiles  (FM only; no experimental data)
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(11, 4.5), sharey=True)
fig.suptitle(
    'JIS A 1310 Façade – Convective Heat Flux vs Height\n'
    'FM fireFoam (0.5 in grid)',
    fontsize=10)

for ax, pwr in zip(axes, POWERS):
    ax.plot(sim[f'CHF_{pwr}'], z_hf,
            MARKERS[pwr] + '-', color=COLORS[pwr],
            lw=1.5, ms=5, label='FM fireFoam')
    ax.set_xlabel('Convective Heat Flux (kW/m²)')
    ax.set_title(f'{pwr} kW')
    ax.set_xlim(left=0)
    ax.set_ylim(0, 3.0)
    ax.legend(loc='upper right')
    ax.grid(True, ls=':', alpha=0.5)

axes[0].set_ylabel('Height above window top (m)')
fig.tight_layout()
save_fig(fig, 'FM_JIS_Facade_0p5in_CHF_profile.png')

# ─────────────────────────────────────────────────────────────────────────────
# Figure 3 – Radiative heat flux profiles  (FM only; no experimental data)
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(11, 4.5), sharey=True)
fig.suptitle(
    'JIS A 1310 Façade – Radiative Heat Flux vs Height\n'
    'FM fireFoam (0.5 in grid)',
    fontsize=10)

for ax, pwr in zip(axes, POWERS):
    ax.plot(sim[f'RHF_{pwr}'], z_hf,
            MARKERS[pwr] + '-', color=COLORS[pwr],
            lw=1.5, ms=5, label='FM fireFoam')
    ax.set_xlabel('Radiative Heat Flux (kW/m²)')
    ax.set_title(f'{pwr} kW')
    ax.set_xlim(left=0)
    ax.set_ylim(0, 3.0)
    ax.legend(loc='upper right')
    ax.grid(True, ls=':', alpha=0.5)

axes[0].set_ylabel('Height above window top (m)')
fig.tight_layout()
save_fig(fig, 'FM_JIS_Facade_0p5in_RHF_profile.png')

# ─────────────────────────────────────────────────────────────────────────────
# Figure 4 – Surface temperature profiles at Y = 0  (FM vs experimental)
# X = 0 m corresponds to the façade surface (distance from wall = 0).
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(11, 4.5), sharey=True)
fig.suptitle(
    'JIS A 1310 Façade – Temperature at X=0, Y=0 vs Height\n'
    'FM fireFoam (0.5 in grid) vs Experiment (Sun 2024)',
    fontsize=10)

# Experimental: keep only points at and above the window top (Z >= 0)
exp_t_pos = exp_t[exp_t['Z(m)'] >= 0.0]

for ax, pwr in zip(axes, POWERS):
    # FM simulation
    ax.plot(sim[f'T_{pwr}_x=0.00_y=0.00'], z_t,
            MARKERS[pwr] + '-', color=COLORS[pwr],
            lw=1.5, ms=5, label='FM fireFoam')
    # Experimental (facade surface, Y=0 centerline, Z >= 0)
    ax.plot(exp_t_pos[f'{pwr}kW(Y=0)'], exp_t_pos['Z(m)'],
            'ks', ms=6, mfc='none', mew=1.2, label='Exp (Sun 2024)')
    ax.set_xlabel('Temperature (°C)')
    ax.set_title(f'{pwr} kW')
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 3.0)
    ax.legend(loc='upper right')
    ax.grid(True, ls=':', alpha=0.5)

axes[0].set_ylabel('Height above window top (m)')
fig.tight_layout()
save_fig(fig, 'FM_JIS_Facade_0p5in_T_Y0_profile.png')

print('\nAll plots saved to:', PLOTS_DIR)
