#!/usr/bin/python3
# T. Hehnen
# 24 August 2023

import sys
sys.path.append('../../../../../../macfp-db/Utilities/')

import os
import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.close('all')


# Define general information.
# ------------------------------
# Basic information about cases.
pp_sim_info = {
    "PP_C5_01_cat": {
        "FluidCells": "2.0 cm",
        "LineStyle": "-",
        "fps": 2},
    "PP_C10_03_cat": {
        "FluidCells": "1.0 cm",
        "LineStyle": "--",
        "fps": 2},
    "PP_C20_02_cat": {
        "FluidCells": "0.5 cm",
        "LineStyle": "-.",
        "fps": 2}
}

# Initialise simulation data collection.
pp_sims = dict()
sim_dir = os.path.join("Output")

# Define meta information for the plots.
hrr_label = ['120 kW', '200 kW', '300 kW', '400 kW', '510 kW', '750 kW', '990 kW', '1500 kW', '1980 kW', '2800 kW']
color = ['black', 'maroon', 'limegreen', 'lightgray', 'blue', 'plum', 'cyan', 'orange', 'darkgreen', 'salmon']

# Heights of measurements and FDS predictions.
z_exp = np.array([10, 20, 30, 50, 75, 100, 140, 180, 220])
z_FDS = np.array([20, 50, 75, 100, 125, 150 , 175, 200, 225])

# Heat flux DEVC labels.
hf_devc_labels = ["HF_y0_z20", "HF_y0_z50", "HF_y0_z75", "HF_y0_z100",
                  "Flux-1", "Flux-2", "Flux-3", "Flux-4", "Flux-5"]


# Read experiment data.
# ------------------------------
# Read centre line heat flux to empty panel, from experiment.
exp_heatflux_path = os.path.join("..", "..", "..", "Experimental_Data",
                                 "PMMA_heatflux.csv")
# First row as header and row with units skipped.
exp_heatflux_df = pd.read_csv(exp_heatflux_path, header=0, skiprows=[1])
exp_heatflux_df.interpolate(axis=1, method='linear', inplace=True) # fill nan values


# Read simulation data.
# ------------------------------
# Collect simulation responses.
for sim_label in pp_sim_info:
    # Add dictionary per simulation setup.
    if sim_label not in list(pp_sims):
        # Prevent overwriting existing data ('CHID_hrr' and 'CHID_devc').
        pp_sims[sim_label] = dict()

    # Read 'CHID_devc.csv'-file as Pandas DataFrame.
    devc_path = os.path.join(sim_dir, f"{sim_label}_devc.csv")
    devc_df = pd.read_csv(devc_path, sep=',', header=1)
    pp_sims[sim_label]["DEVC"] = devc_df

    # Read 'CHID_hrr.csv'-file as Pandas DataFrame.
    hrr_path = os.path.join(sim_dir, f"{sim_label}_hrr.csv")
    hrr_df = pd.read_csv(hrr_path, sep=',', header=1)
    pp_sims[sim_label]["HRR"] = hrr_df

    # Find line index for HRR value to extract corresponding DEVC data.
    hrr_exp = exp_heatflux_df.HRR
    indices = list()
    for hrr_exp_val in hrr_exp:
        indices.append((hrr_df.HRR > hrr_exp_val).idxmax())
    pp_sims[sim_label]["Indices"] = indices


# Dummy plot to define handle
f = macfp.plot_to_fig(x_data=[0,1], y_data=[0,1], marker_style='None',line_style='None')

for irow in range(len(hrr_label)):
    # Plot experiment data as target.
    x = exp_heatflux_df.loc[irow,"HF_z10":"HF_z220"].values[:].astype(float)
    u = exp_heatflux_df.loc[irow,"u_exp_HF_z10":"u_exp_HF_z220"].values[:].astype(float)
    if hrr_label[irow] in ['400 kW', '750 kW', '990 kW']: continue
    f = macfp.plot_to_fig(x_data=x, y_data=z_exp, data_label=hrr_label[irow],
                          x_min=0,x_max=150,x_nticks=4,
                          y_min=0,y_max=250,
                          x_label='Heat Flux [kW/m²]',
                          y_label='Height [cm]',
                          marker_style='o',
                          marker_edge_color=color[irow],
                          marker_fill_color=color[irow],
                          line_style='None',
                          line_color=color[irow],
                          show_legend=True,
                          legend_location='outside',
                          figure_right_adjust=0,
                          legend_fontsize=8,
                          figure_handle=f)

    plt.errorbar(x,z_exp,linestyle='',xerr=u,capsize=4,ecolor=color[irow])

    # Plot simulation results for different fluid cell resolution.
    for sim_label in pp_sim_info:
        # Prepare data for plotting.
        sim_df = pp_sims[sim_label]["DEVC"]
        indices = pp_sims[sim_label]["Indices"]
        cell_size = pp_sim_info[sim_label]["FluidCells"]
        data_series_label = f"Sim. {cell_size}"

        x_vals = sim_df.loc[indices[irow], hf_devc_labels].values[:].astype(float)

        f = macfp.plot_to_fig(x_data=x_vals, y_data=z_FDS,
                              data_label=data_series_label,
                              x_min=0,x_max=150,x_nticks=4,
                              y_min=0,y_max=250,
                              x_label='Heat Flux [kW/m²]',
                              y_label='Height [cm]',
                              marker_style='None',
                              line_style=pp_sim_info[sim_label]["LineStyle"],
                              line_color=color[irow],
                              show_legend=True,
                              legend_location='outside',
                              figure_right_adjust=0,
                              legend_fontsize=8,
                              figure_handle=f)


f.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plt.savefig('Output/Plots/NIST_Parallel_Panel_flame_spread_heatflux_BUWFZJ.pdf')

# plt.show()
