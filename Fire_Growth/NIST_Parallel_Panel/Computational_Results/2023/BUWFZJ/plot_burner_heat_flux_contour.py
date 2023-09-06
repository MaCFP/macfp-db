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
import matplotlib.lines as mlines
import numpy as np
import pandas as pd

plt.close('all')


# Define general information.
# ------------------------------
# Basic information about cases.
burner_sim_info = {
    "MaCFP_Burner_04": {
        "FluidCells": "2.0 cm",
        "Color": "brown",
        "LineStyle": "-.",
        "fps": 2},
    "MaCFP_Burner_08": {
        "FluidCells": "1.0 cm",
        "Color": "yellow",
        "LineStyle": "-.",
        "fps": 2},
    "MaCFP_Burner_09": {
        "FluidCells": "0.5 cm",
        "Color": "green",
        "LineStyle": "-.",
        "fps": 2},
#     "MaCFP_Burner_10": {
#         "FluidCells": "0.5 cm",
#         "fps": 2}
}

# Define sim labels for setups to be skipped.
to_be_skipped = []

# Define headers for experiment data extraction.
hf_labels = ["HF_y-25", "HF_y-15", "HF_y0", "HF_y15", "HF_y25"]


# Initialise simulation data collection.
burner_sims = dict()
sim_dir = os.path.join("Output")

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


# Read experiment data.
# ------------------------------
# Read heat flux map to empty panel, from experiment.
burnersteady_hf_path = os.path.join("..", "..", "..", "Experimental_Data",
                                  "Burner_steadyHF_Width_multi-layer.csv")
# First row as header and row with units skipped.
burnersteady_hf_df = pd.read_csv(burnersteady_hf_path, header=0, skiprows=[1])



# Plot experiment data.
# ------------------------------
# Inititialise data label collection.
data_labels = list()

# Set size of the figure.
plt.figure(figsize=(5, 5))

hf_gauge = burnersteady_hf_df[hf_labels].to_numpy()


# Create the mesh of the data.
x = np.array([-25, -15, 0, 15, 25])
y = np.array([20, 50, 75, 100])
X, Y = np.meshgrid(x, y)
Z = hf_gauge

# Define where the iso-lines are located.
levels = [0, 5, 10, 15, 20, 30, 40, 50, 70]
# Edge length of the data set, i.e. lower part of the panel.
extent = [-0.3,0.3, 0.0,1.0]

# Filled areas.
CS = plt.contourf(X, Y, Z, levels,
                  cmap=plt.cm.viridis)

# Define colour bar.
plt.clim(2.0, 65.0)
plt.colorbar().set_label('Gauge Heat Flux [kW/m²]',size=14)


# Contour lines of the gauge heat flux distribution.
contours = plt.contour(X, Y, Z, levels, colors='black')
plt.clabel(contours, levels, inline=True,
           fmt='%1.0f',  # Set number of digits for contour labels.
           fontsize=8)

# Define data label.
data_labels.append(mlines.Line2D([], [], color='k', label='Exp.'))

# Show DEVC locations.
# Height: 20 cm
plt.scatter([-25, -15, 0, 15, 25],
            [20, 20, 20, 20, 20],
            color='k')

# Height: 50 cm
plt.scatter([-25, -15, 0, 15, 25],
            [50, 50, 50, 50, 50],
            color='k')

# Height: 75 cm
plt.scatter([-25, -15, 0, 15, 25],
            [75, 75, 75, 75, 75],
            color='k')

# Height: 100 cm
plt.scatter([-25, -15, 0, 15, 25],
            [100, 100, 100, 100, 100],
            color='k')


# Plot simulation data.
# ------------------------------
# Stupid, but it works...
devc_locations = {
    "z20": 0, "z50": 1, "z75": 2, "z100": 3,
    "y-25": 0, "y-15": 1, "y0": 2, "y15": 3, "y25": 4}

# sim_label = "MaCFP_Burner_01"
for sim_label in burner_sims:
    if sim_label in to_be_skipped:
        #Skip simulation.
        continue

    # Get DEVC data.
    devc_data = burner_sims[sim_label]["DEVC"]

    # Initialise data collection.
    flux_map = np.zeros((4,5))

    for header in list(devc_data):
        # Find heat flux gauges.
        if "HF_" in header:
            y_pos_label = header.split("_")[1]
            z_pos_label = header.split("_")[2]

            # Compute average over last n points.
            flux_avrg = np.average(devc_data[header][160:200])

            # Collect flux average.
            y_pos = devc_locations[y_pos_label]
            z_pos = devc_locations[z_pos_label]
            flux_map[z_pos][y_pos] = flux_avrg

    # Provide data
    hf_gauge = flux_map

    # Create the mesh of the data.
    X, Y = np.meshgrid(x, y)
    Z = hf_gauge

    # Contour lines of the gauge heat flux DEVC distribution.
    color = burner_sim_info[sim_label]["Color"]
    linestyle = burner_sim_info[sim_label]["LineStyle"]
    contours = plt.contour(X, Y, Z, levels,
                           colors=color,
                           linestyles=linestyle)
    plt.clabel(contours, levels, inline=True,
               fmt='%1.0f',  # Set number of digits for contour labels.
               fontsize=8, colors=color)

    # Define data label.
    cell_size = burner_sim_info[sim_label]["FluidCells"]
    ds_label = f"Sim. {cell_size}"
    data_labels.append(mlines.Line2D([], [], color=color, linestyle=linestyle, label=ds_label))



# Plot meta data.
plt.xlabel("Width [cm]")
plt.ylabel("Height [cm]")

plt.xlim(xmin=-32, xmax=32)
plt.ylim(ymin=-2, ymax=142)

# plt.rcParams.update({'font.size': 12})

plt.tight_layout()
plt.legend(handles=data_labels, loc='upper center', fontsize=11)

# Save image.
plot_dir = os.path.join(sim_dir, "Plots", "NIST_Parallel_Panel_Burner_heatflux_colormap_BUWFZJ.pdf")
plt.savefig(plot_dir, dpi=320, bbox_inches='tight')

# plt.show()
