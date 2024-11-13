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
burner_sim_info = {
    "MaCFP_Burner_04": {
        "FluidCells": "2.0 cm",
        "fps": 2},
    "MaCFP_Burner_08": {
        "FluidCells": "1.0 cm",
        "fps": 2},
    "MaCFP_Burner_09": {
        "FluidCells": "0.5 cm",
        "fps": 2},
#     "MaCFP_Burner_10": {
#         "FluidCells": "0.5 cm",
#         "fps": 2}
}

# Initialise simulation data collection.
burner_sims = dict()
sim_dir = os.path.join("Output")


# Device heights, in cm.
heights = [20, 50, 75, 100]
# Interesting times, in s.
desired_times = [20, 40, 60, 80]

# Define headers for experiment data extraction.
hf_labels = ["HF_z20", "HF_z50", "HF_z75", "HF_z100"]
u_hf_labels = ["u_exp_HF_z20", "u_exp_HF_z50", "u_exp_HF_z75", "u_exp_HF_z100"]
# Define headers for simulation data extraction.
devc_labels = ["HF_y0_z20", "HF_y0_z50", "HF_y0_z75", "HF_y0_z100"]

# Define plot elements.
colors = ['black', 'red', 'green', 'blue']
line_styles = ['-', '--', '-.', ':']


# Read experiment data.
# ------------------------------
# Read centre line heat flux to empty panel, from experiment.
centreline_hf_path = os.path.join("..", "..", "..", "Experimental_Data",
                                  "Burner_HF_Centerline_multi-layer.csv")
# First row as header and row with units skipped.
centreline_hf_df = pd.read_csv(centreline_hf_path, header=0, skiprows=[1])


# Read simulation data.
# ------------------------------
# Collect simulation responses.
for sim_label in burner_sim_info:
    # Add dictionary per simulation setup.
    if sim_label not in list(burner_sims):
        # Prevent overwriting existing data ('CHID_hrr' and 'CHID_devc').
        burner_sims[sim_label] = dict()

    # Read 'CHID_devc.csv'-file as Pandas DataFrame.
    devc_path = os.path.join(sim_dir, f"{sim_label}_devc.csv")
    devc_df = pd.read_csv(devc_path, sep=',', header=1)
    burner_sims[sim_label]["DEVC"] = devc_df

    # Simulation response.
    sim_fluxes = list()
    for time_id, desired_time in enumerate(desired_times):
        flux_avrgs = list()
        # Define time window to average over.
        base_frame = desired_time * burner_sim_info[sim_label]["fps"]
        frame_window = 3

        # Go over desired DEVC labels.
        for devc_label in devc_labels:
            # Get CHID_devc data.
            devc_data = burner_sims[sim_label]["DEVC"]

            # Find time window over which to average.
            t_min = int(base_frame - frame_window)
            t_max = int(base_frame + frame_window + 1)
            # Compute average within the above window.
            flux_avrg = np.average(devc_data[devc_label][t_min:t_max].to_numpy())
            flux_avrgs.append(flux_avrg)

        # Collect fluxes per time step.
        sim_fluxes.append(flux_avrgs)

    # Collect fluxes per sim setup.
    burner_sims[sim_label]["Fluxes"] = sim_fluxes


# Create empty figure?
f = macfp.plot_to_fig(x_data=[0,1], y_data=[0,1], marker_style='None',line_style='None')


# Plot experiment data points per time step.
for time_id, time_step in enumerate(centreline_hf_df["Time"]):
    # Get centre line heat flux per time step.
    hf_centre = centreline_hf_df.iloc[time_id][hf_labels].to_numpy()
    # Get related uncertainty.
    hf_u_centre = centreline_hf_df.iloc[time_id][u_hf_labels].to_numpy()

    # Define data series label.
    ds_label = f"Exp ({time_step} s)"

    # Plot experiment data points per time step.
    f = macfp.plot_to_fig(x_data=hf_centre,
                          y_data=heights,
                          data_label=ds_label,
                          x_min=0,x_max=80,
                          y_min=0,y_max=180,
                          x_label='Heat Flux [kW/m²]',
                          y_label='Height [cm]',
                          marker_style='o',
                          marker_edge_color=colors[time_id],
                          marker_fill_color=colors[time_id],
                          line_style=' ',
                          show_legend=True,
                          figure_right_adjust=0,
                          legend_fontsize=10,
                          figure_handle=f)

    # Draw error bars from reported experiment uncertainty, per time step.
    plt.errorbar(hf_centre, heights,
                 xerr=hf_u_centre,
                 capsize=4, fmt=' ',
                 ecolor=colors[time_id])


# Plot simulation data points per time step.
for sim_id, sim_label in enumerate(list(burner_sims)):
    # Get fluid cell size for setup.
    cell_size = burner_sim_info[sim_label]["FluidCells"]

#     burner_sims[sim_label]['Fluxes']
    for time_id, time_step in enumerate(centreline_hf_df["Time"]):
        # Define data series label.
        ds_label = f"Sim ({time_step} s, {cell_size})"
        f = macfp.plot_to_fig(x_data=burner_sims[sim_label]['Fluxes'][time_id],
                              y_data=heights,
                              data_label=ds_label,
                              institute_label='BUW-FZJ',
                              revision_label='MaCFP-3, Tsukuba, 2023',
                              x_min=0,x_max=80,
                              y_min=0,y_max=180,
                              x_label='Heat Flux [kW/m²]',
                              y_label='Height [cm]',
                              line_color=colors[time_id],
                              line_style=line_styles[sim_id],
                              show_legend=True,
                              figure_right_adjust=0,
                              legend_fontsize=10,
                              figure_handle=f)


# fig.tight_layout(pad=1.0, h_pad=0.0, w_pad=0.0, rect=[0.05, 0.05, 0.90, 0.95])

plot_dir = os.path.join(sim_dir, "Plots", "NIST_Parallel_Panel_Burner_heatflux_BUWFZJ.pdf")
plt.savefig(plot_dir)

# plt.show()
