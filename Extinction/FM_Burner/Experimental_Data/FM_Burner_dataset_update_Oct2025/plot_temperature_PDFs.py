import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import glob

# -------------------------------------------------------
# Discover all PDF files
# -------------------------------------------------------
files = sorted(glob.glob("temperature_PDF_OC*.csv"))

file_info = []
for f in files:
    m = re.search(r"OC(\d+\.\d+)_(\d+\.\d)D", f)
    if not m:
        continue
    OC = float(m.group(1))
    height = float(m.group(2))
    file_info.append((OC, height, f))

# -------------------------------------------------------
# Correct ordering:
#   Heights should be plotted LOWEST (0.5D) at bottom row
#   So we reverse the height sort
# -------------------------------------------------------
OCs = sorted({OC for OC, _, _ in file_info})
heights = sorted({h for _, h, _ in file_info})[::-1]   # reversed here

# -------------------------------------------------------
# FM Burner-style colors and linestyles (0 → 10 cm)
#   EXACT black solid for 0 cm (your requirement)
# -------------------------------------------------------
colors = [
    'black',    # 0 cm
    'red',      # 1 cm
    'blue',     # 2 cm
    'magenta',  # 3 cm
    'green',    # 4 cm
    'orange',   # 5 cm
    'cyan',     # 6 cm
    'purple',   # 7 cm
    'red',      # 8 cm (dashed)
    'blue',     # 9 cm (dotted)
    'black'     # 10 cm
]

linestyles = [
    '-',        # 0 cm black solid
    '-',        # 1 cm red solid
    '--',       # 2 cm blue dashed
    '-.',       # 3 cm magenta dash-dot
    '-',        # 4 cm green solid
    '-',        # 5 cm orange solid
    '-',        # 6 cm cyan solid
    ':',        # 7 cm purple dotted
    '--',       # 8 cm red dashed
    ':',        # 9 cm blue dotted
    ':'         # 10 cm black solid
]


# -------------------------------------------------------
# Build multi-panel figure
# -------------------------------------------------------
fig, axes = plt.subplots(
    len(heights), len(OCs),
    figsize=(10, 14),
    sharex=True, sharey=True
)

for (OC, h, f) in file_info:

    # NEW: correct reversed row index
    row = heights.index(h)
    col = OCs.index(OC)
    ax = axes[row][col]

    df = pd.read_csv(f)
    T = df.iloc[:, 0].values
    radial_cols = df.columns[1:]

    # Extract numeric radii (must be sorted low→high)
    radii = [float(c.replace("cm", "")) for c in radial_cols]

    # Sort indices by radius numeric value
    order = np.argsort(radii)

    for idx in order:
        r = radii[idx]
        colname = radial_cols[idx]
        style_i = int(r)   # radius = index (0–10)

        ax.plot(
            T,
            df[colname].values,
            color=colors[style_i],
            linestyle=linestyles[style_i],
            linewidth=1.1,
            label=f"{r:.0f} cm"
        )

    # Title inside plot (paper-style)
    ax.text(
        0.5, 0.93,
        f"{OC}% OC {h}D",
        fontsize=9,
        ha='center', va='top',
        transform=ax.transAxes,
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.6, pad=1.5)
    )

    ax.set_xlim(300, 2100)
    ax.set_ylim(0.0, 0.004)
    ax.grid(True, linestyle=":")

    if row == len(heights) - 1:
        ax.set_xlabel("Temperature (K)")


# -------------------------------------------------------
# Legend goes in UPPER RIGHT panel now
# -------------------------------------------------------
legend_ax = axes[0][-1]   # row 0, last column
legend_ax.legend(
    title="Radius (cm)",
    loc="upper right",
    fontsize=8,
    title_fontsize=8,
    framealpha=0.9,
    borderpad=0.4
)

# -------------------------------------------------------
# Move global Y label further left to avoid crowding
# -------------------------------------------------------
fig.text(
    0.005, 0.5,   # moved further left (0.01 → 0.005)
    "Probability density function (1/K)",
    va="center",
    rotation="vertical",
    fontsize=11
)

# -------------------------------------------------------
# Tighten subplot spacing
# -------------------------------------------------------
plt.subplots_adjust(
    left=0.08,
    right=0.98,
    top=0.97,
    bottom=0.05,
    wspace=0.12,
    hspace=0.18
)

plt.savefig("Fig8_temperature_PDFs.png", dpi=300)
plt.show()

print("Saved: Fig8_temperature_PDFs.png")
