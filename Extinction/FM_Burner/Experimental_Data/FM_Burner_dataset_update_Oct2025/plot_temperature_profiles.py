import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import defaultdict

# ---------------------------------------------------------------------------
# Load CSVs (all '--' already removed)
# ---------------------------------------------------------------------------
df_mean = pd.read_csv("temperature_mean.csv")
df_rms  = pd.read_csv("temperature_rms.csv")

# Radius (distance from center)
radius = pd.to_numeric(df_mean.iloc[1:, 0], errors="coerce").values

# ---------------------------------------------------------------------------
# Extract (OC, height, column_rad, column_val) from wide-format column names
#   Mean columns look like:  r_15.2_0.5D (cm)	T_Mean_15.2_0.5D (K)	T_Std_15.2_0.5D(K)	r_15.2_1.0D (cm)	T_Mean_15.2_1.0D (K)	T_Std_15.2_1.0D(K)
#   RMS  columns look like:  r_15.2_0.5D (cm)	T_RMS_15.2_0.5D (K)	T_Std_15.2_0.5D(K)	r_15.2_1.0D (cm)	T_RMS_15.2_1.0D (K)	T_Std_15.2_1.0D(K)
# We:
#   * strip leading/trailing spaces
#   * allow any amount of spaces between tokens
#   * optionally require the "RMS" suffix
# ---------------------------------------------------------------------------
def extract_groups(df,is_rms=False):
    # temporary storage keyed by (OC, height)
    temp = defaultdict(dict)

    # matches: _15.2_0.5D
    pattern = re.compile(r"_(\d+\.\d+)_([\d\.]+)D\b")

    for col in df.columns:
        col_clean = col.strip()

        # exclude STD columns
        if "_Std_" in col_clean:
            continue

        m = pattern.search(col_clean)
        if not m:
            continue

        OC = float(m.group(1))
        height = float(m.group(2))
        key = (OC, height)
        
        if is_rms:
            if col_clean.startswith("r_"):
                temp[key]["r"] = col
            elif col_clean.startswith("T_RMS_"):
                temp[key]["T"] = col
        else:
           if col_clean.startswith("r_"):
               temp[key]["r"] = col
           elif col_clean.startswith("T_Mean_"):
               temp[key]["T"] = col

    # build final groups only when both columns exist
    groups = []
    for (OC, height), cols in temp.items():
        if "r" in cols and "T" in cols:
            groups.append((OC, height, cols["r"], cols["T"]))

    return groups


groups_mean = extract_groups(df_mean,is_rms=False)
groups_rms  = extract_groups(df_rms,is_rms=True)

OCs     = sorted({OC for OC, _, _, _ in groups_mean})
heights = sorted({h  for _, h, _, _ in groups_mean})

print(OCs)
print(heights)

# ---------------------------------------------------------------------------
# Utility: get numeric y-values for a given column
# ---------------------------------------------------------------------------
def get_y(df, col):
    return pd.to_numeric(df[col].iloc[1:], errors="coerce").dropna().values

# ---------------------------------------------------------------------------
# FIGURE 5 — Mean and RMS temperature vs radius for each OC
# ---------------------------------------------------------------------------
fig5 = plt.figure(figsize=(12, 12))

for i, OC in enumerate(OCs):

    # ----- Mean panel -----
    axm = plt.subplot(len(OCs), 2, 2*i + 1)
    for OC_i, h, col_rad, col_val in groups_mean:
        if OC_i == OC:
            radius = get_y(df_mean, col_rad)
            y = get_y(df_mean, col_val)
            axm.plot(radius[:len(y)], y, marker='o', label=f"{h}D")

    axm.set_title(f"Mean {OC}% OC")
    axm.set_xlabel("Distance from center (cm)")
    axm.set_ylabel("Mean temperature (K)")
    axm.set_ylim(200, 1400)
    axm.grid(True, linestyle=":")
    if i == 0:
        axm.legend()

    # ----- RMS panel -----
    axr = plt.subplot(len(OCs), 2, 2*i + 2)
    for OC_i, h, col_rad, col_val in groups_rms:
        if OC_i == OC:
            radius = get_y(df_rms, col_rad)
            y = get_y(df_rms, col_val)
            axr.plot(radius[:len(y)], y, marker='o', label=f"{h}D")

    axr.set_title(f"RMS {OC}% OC")
    axr.set_xlabel("Distance from center (cm)")
    axr.set_ylabel("RMS temperature (K)")
    axr.set_ylim(0, 450)
    axr.grid(True, linestyle=":")
    if i == 0:
        axr.legend()

fig5.tight_layout()
fig5.savefig("Fig5_temperature_profiles.png", dpi=300)

# ---------------------------------------------------------------------------
# FIGURE 6 — Comparison at 1.0D and 3.5D across OCs
# ---------------------------------------------------------------------------
compare_heights = [1.0, 3.5]
fig6, (ax6m, ax6r) = plt.subplots(1, 2, figsize=(12, 5))

# Mean comparison
for OC, h, col_rad, col_val in groups_mean:
    if h in compare_heights:
        radius = get_y(df_mean, col_rad)
        y = get_y(df_mean, col_val)
        ax6m.plot(radius[:len(y)], y, marker='o', label=f"{OC}% {h}D")

ax6m.set_title("(a) Mean temperature")
ax6m.set_xlabel("Distance from center (cm)")
ax6m.set_ylabel("Mean temperature (K)")
ax6m.grid(True, linestyle=":")
ax6m.legend()

# RMS comparison
for OC, h, col_rad, col_val in groups_rms:
    if h in compare_heights:
        radius = get_y(df_rms, col_rad)
        y = get_y(df_rms, col_val)
        ax6r.plot(radius[:len(y)], y, marker='o', label=f"{OC}% {h}D")

ax6r.set_title("(b) RMS temperature")
ax6r.set_xlabel("Distance from center (cm)")
ax6r.set_ylabel("RMS temperature (K)")
ax6r.grid(True, linestyle=":")
ax6r.legend()

fig6.tight_layout()
fig6.savefig("Fig6_comparison.png", dpi=300)

plt.show()

