import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import glob
import os

# ---------------------------------------------------------
# 1. Helper: extract height from column name
# ---------------------------------------------------------
# Accepts:
#   "H=4.004 cm"
#   "H=4.508cm"
#   "5.012"
#   "5.516"
# Returns height in cm (float)
# ---------------------------------------------------------
def parse_height(colname):
    txt = colname.strip()

    # Pattern 1: H=4.004 cm
    m = re.match(r"H\s*=\s*([\d\.]+)\s*cm", txt)
    if m:
        return float(m.group(1))

    # Pattern 2: H=4.508cm
    m = re.match(r"H\s*=\s*([\d\.]+)\s*cm?", txt)
    if m:
        return float(m.group(1))

    # Pattern 3: plain number "5.012", "6.02", etc. → height in cm
    m = re.match(r"([\d\.]+)$", txt)
    if m:
        return float(m.group(1))

    return None  # ignore columns that don't contain data


# ---------------------------------------------------------
# 2. Process velocity files
#       horizontal_velocity_mean_15.2_OC.csv
#       vertical_velocity_mean_15.2_OC.csv
# ---------------------------------------------------------
files = sorted(glob.glob("*velocity_mean_*OC.csv"))

data = {}   # data[OC]['U'] = dataframe, data[OC]['W'] = dataframe

for f in files:
    OC = re.search(r"(\d+\.\d+)_OC", f).group(1)   # "15.2"
    OC = float(OC)

    if OC not in data:
        data[OC] = {}

    if "horizontal" in f:
        data[OC]['U'] = pd.read_csv(f)
    elif "vertical" in f:
        data[OC]['W'] = pd.read_csv(f)


# ---------------------------------------------------------
# 3. Plotting function
# ---------------------------------------------------------
def plot_velocity(df, title, outfile, ylabel):

    # First column = radial position (cm)
    radius = pd.to_numeric(df.iloc[:, 0], errors="coerce").values

    # Extract heights + corresponding columns
    height_cols = []
    for col in df.columns[1:]:
        h = parse_height(col)
        if h is not None:
            height_cols.append((h, col))

    # Sort by height
    height_cols.sort(key=lambda x: x[0])

    plt.figure(figsize=(10, 6))

    for h, col in height_cols:
        y = pd.to_numeric(df[col], errors='coerce').values
        plt.plot(radius, y, marker='o', label=f"{h:.3g} cm")

    plt.title(title)
    plt.xlabel("Distance from center (cm)")
    plt.ylabel(ylabel)
    plt.grid(True, linestyle=":")
    plt.legend(title="Height")
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()


# ---------------------------------------------------------
# 4. Produce plots for each OC level
# ---------------------------------------------------------
for OC in sorted(data.keys()):

    # Horizontal velocity (U)
    if 'U' in data[OC]:
        dfU = data[OC]['U']
        plot_velocity(
            dfU,
            title=f"Horizontal velocity U (mean) — {OC}% OC",
            outfile=f"velocity_U_mean_{OC}_OC.png",
            ylabel="U velocity (m/s)",
        )

    # Vertical velocity (W)
    if 'W' in data[OC]:
        dfW = data[OC]['W']
        plot_velocity(
            dfW,
            title=f"Vertical velocity W (mean) — {OC}% OC",
            outfile=f"velocity_W_mean_{OC}_OC.png",
            ylabel="W velocity (m/s)",
        )

print("Finished generating velocity plots.")

