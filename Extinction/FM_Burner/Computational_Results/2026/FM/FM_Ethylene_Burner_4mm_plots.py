#!/usr/bin/env python3
"""
One-off MaCFP-4 plotting script for the FM ethylene burner case.

Run with a Python environment that has numpy, scipy, pandas, and matplotlib.
In this workspace:
    /panfs/lux/miniconda3/envs/sciml-torch/bin/python3 FM_Ethylene_Burner_4mm_plots.py

The script reads the submitted MaCFP CSV files in this directory and creates
comparison plots in ./Plots.
"""

from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

SCRIPT_DIR = Path(__file__).resolve().parent
EXP_ROOT = (SCRIPT_DIR / ".." / ".." / ".." / "Experimental_Data").resolve()
TEMPERATURE_EXP_DIR = EXP_ROOT / "Temperature"
SOOT_EXP_DIR = EXP_ROOT / "LII"
UPDATED_EXP_DIR = EXP_ROOT / "FM_Burner_dataset_update_Oct2025"
PLOTS_DIR = SCRIPT_DIR / "Plots"
PLOTS_DIR.mkdir(exist_ok=True)

GRID_LABEL = "4mm"
NOMINAL_HRR_KW = 15.0
BURNER_DIAMETER_CM = 14.0
OXYGEN_CONDITION = "20.9"

BASE_NAME = f"FM_Ethylene_Burner_{GRID_LABEL}"
HRR_CSV = SCRIPT_DIR / f"{BASE_NAME}_hrr.csv"
TEMPERATURE_CSV = SCRIPT_DIR / f"{BASE_NAME}_temperature_profile.csv"
SOOT_CSV = SCRIPT_DIR / f"{BASE_NAME}_soot_profile.csv"
VELOCITY_CSV = SCRIPT_DIR / f"{BASE_NAME}_velocity_profile.csv"
SUBMITTED_CSVS = [HRR_CSV, TEMPERATURE_CSV, SOOT_CSV, VELOCITY_CSV]

MEAN_TEMPERATURE_EXP_CSV = TEMPERATURE_EXP_DIR / "Mean_temperature.csv"
RMS_TEMPERATURE_EXP_CSV = UPDATED_EXP_DIR / "temperature_rms.csv"
MEAN_SVF_EXP_CSV = SOOT_EXP_DIR / "fvmean.csv"
RMS_SVF_EXP_CSV = SOOT_EXP_DIR / "fvrms.csv"
VERTICAL_VELOCITY_EXP_CSV = UPDATED_EXP_DIR / "vertical_velocity_mean_20.9_OC.csv"
HORIZONTAL_VELOCITY_EXP_CSV = UPDATED_EXP_DIR / "horizontal_velocity_mean_20.9_OC.csv"

TEMPERATURE_HEIGHTS = ["1.0D", "1.5D", "2.0D", "2.5D", "3.0D", "3.5D"]
PLOT_PROFILE_HEIGHTS = ["0.5D", "1.0D", "1.5D", "2.5D", "3.5D"]

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "legend.fontsize": 8,
    "figure.dpi": 150,
})


def require(path):
    if not Path(path).exists():
        raise FileNotFoundError(f"Required path not found: {path}")
    return Path(path)


def height_value(height_label):
    return float(height_label.rstrip("D"))


def read_velocity_csv(path):
    data = pd.read_csv(path)
    data.columns = [
        "x_cm",
        *[float(re.search(r"[-+]?\d*\.?\d+", str(col)).group()) for col in data.columns[1:]],
    ]
    return data.apply(pd.to_numeric, errors="coerce").dropna(subset=["x_cm"])


def read_temperature_rms_csv(path):
    source = pd.read_csv(require(path))
    profiles = {}
    for height_label in TEMPERATURE_HEIGHTS:
        radius_col = f"r_{OXYGEN_CONDITION}_{height_label} (cm)"
        rms_col = f"T_RMS_{OXYGEN_CONDITION}_{height_label} (K)"
        profile = source[[radius_col, rms_col]].rename(columns={radius_col: "Radius (cm)", rms_col: height_label})
        profile = profile.apply(pd.to_numeric, errors="coerce").dropna(subset=["Radius (cm)"])
        profiles[height_label] = profile.set_index("Radius (cm)")[height_label]
    return pd.concat(profiles, axis=1).sort_index().reset_index()


def read_lii_csv(path, columns=None):
    data = pd.read_csv(require(path), header=1)
    return data if columns is None else data[columns]


def nearest_height(heights, target):
    return heights[np.argmin(np.abs(heights - target))]


def save_fig(fig, name):
    path = PLOTS_DIR / name
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path.name}")


def plot_hrr():
    hrr = pd.read_csv(HRR_CSV, header=1)
    fig, ax = plt.subplots(figsize=(6, 4))
    window_length = 5
    hrr_kw = savgol_filter(hrr["HRR"], window_length=window_length, polyorder=3)
    hrr_rad_loss_kw = savgol_filter(hrr["HRR_rad_loss"], window_length=window_length, polyorder=3)
    ax.plot(hrr["Time"], hrr_kw, color="tab:red", label="HRR")
    ax.plot(hrr["Time"], hrr_rad_loss_kw, color="tab:red", linestyle="--", label="radiative loss")
    ax.hlines(0.35 * NOMINAL_HRR_KW, xmin=0, xmax=hrr["Time"].max(), colors="k", linestyles=":", label="35% of 15 kW")
    ax.set_xlim(0, None)
    ax.set_ylim(0, 20)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("HRR (kW)")
    ax.legend(frameon=False)
    ax.grid(True, linestyle=":", alpha=0.4)
    save_fig(fig, f"{BASE_NAME}_HRR.png")


def plot_temperature_profiles():
    mean_temperature = pd.read_csv(require(MEAN_TEMPERATURE_EXP_CSV))
    rms_temperature = read_temperature_rms_csv(RMS_TEMPERATURE_EXP_CSV)
    sim = pd.read_csv(TEMPERATURE_CSV, header=1)

    fig, axs = plt.subplots(
        nrows=2,
        ncols=len(TEMPERATURE_HEIGHTS),
        sharex=True,
        sharey="row",
        gridspec_kw={"hspace": 0.12, "wspace": 0.0},
        figsize=(18, 7),
    )
    legend_items = {}
    x_tick_max_cm = 12
    radius_ticks_cm = np.arange(0.0, x_tick_max_cm + 0.1, 2.0)

    for i, height_label in enumerate(TEMPERATURE_HEIGHTS):
        height_over_d = height_value(height_label)
        mean_ax = axs[0, i]
        rms_ax = axs[1, i]
        mean_ax.set_title(f"z = {height_label}")

        if height_label in mean_temperature.columns:
            line = mean_ax.plot(
                mean_temperature["Radius (cm)"],
                mean_temperature[height_label],
                marker="o",
                color="k",
                linestyle="none",
                label="FM mean" if "FM mean" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FM mean", line)

        if height_label in rms_temperature.columns:
            rms_data = rms_temperature[["Radius (cm)", height_label]].apply(pd.to_numeric, errors="coerce").dropna()
            line = rms_ax.plot(
                rms_data["Radius (cm)"],
                rms_data[height_label],
                marker="o",
                color="k",
                linestyle="none",
                label="FM RMS" if "FM RMS" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FM RMS", line)

        sim_slice = sim[np.isclose(sim["height_over_D"], height_over_d)].sort_values("radius")
        if not sim_slice.empty:
            line = mean_ax.plot(
                sim_slice["radius"],
                sim_slice["T_mean"],
                color="tab:red",
                linewidth=2,
                label="FireFOAM mean" if "FireFOAM mean" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FireFOAM mean", line)

            line = rms_ax.plot(
                sim_slice["radius"],
                sim_slice["T_rms"],
                color="tab:red",
                linewidth=2,
                label="FireFOAM RMS" if "FireFOAM RMS" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FireFOAM RMS", line)

        mean_ax.set_xlim(0, x_tick_max_cm)
        rms_ax.set_xlim(0, x_tick_max_cm)
        mean_ax.set_xticks(radius_ticks_cm)
        rms_ax.set_xticks(radius_ticks_cm)
        mean_ax.set_ylim(bottom=300, top=1500)
        rms_ax.set_ylim(bottom=0, top=500)
        mean_ax.label_outer()
        rms_ax.label_outer()
        plt.setp(mean_ax.yaxis.get_majorticklabels(), fontsize=8)
        plt.setp(rms_ax.xaxis.get_majorticklabels(), rotation=45, fontsize=8)
        plt.setp(rms_ax.yaxis.get_majorticklabels(), fontsize=8)

    axs[0, 0].set_ylabel("Mean Temperature (K)")
    axs[1, 0].set_ylabel("Temperature RMS (K)")
    fig.text(0.5, 0.02, "Radius (cm)", ha="center")
    fig.legend(list(legend_items.values()), list(legend_items.keys()), frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(0.985, 0.965))
    fig.subplots_adjust(left=0.08, right=0.91, bottom=0.12, top=0.89, hspace=0.12, wspace=0.0)
    save_fig(fig, f"{BASE_NAME}_temperature_profile.png")


def plot_soot_profiles():
    mean_svf = read_lii_csv(MEAN_SVF_EXP_CSV)
    rms_columns = ["distance from center", *[f"{OXYGEN_CONDITION}_OI_{height_label}" for height_label in PLOT_PROFILE_HEIGHTS]]
    rms_svf = read_lii_csv(RMS_SVF_EXP_CSV, columns=rms_columns)
    sim = pd.read_csv(SOOT_CSV, header=1)

    fig, axs = plt.subplots(
        nrows=2,
        ncols=len(PLOT_PROFILE_HEIGHTS),
        sharex="row",
        sharey="row",
        gridspec_kw={"hspace": 0.12, "wspace": 0.0},
        figsize=(18, 7),
    )
    legend_items = {}
    x_tick_max_cm = 12
    radius_ticks_cm = np.arange(0.0, x_tick_max_cm + 0.1, 2.0)

    for i, height_label in enumerate(PLOT_PROFILE_HEIGHTS):
        height_over_d = height_value(height_label)
        mean_ax = axs[0, i]
        rms_ax = axs[1, i]
        mean_ax.set_title(f"z = {height_label}")
        exp_col = f"{OXYGEN_CONDITION}_OI_{height_label}"

        if "distance from center" in mean_svf.columns and exp_col in mean_svf.columns:
            data = mean_svf[["distance from center", exp_col]].apply(pd.to_numeric, errors="coerce").dropna()
            data = data[data["distance from center"] >= 0.0]
            line = mean_ax.plot(
                data["distance from center"],
                data[exp_col],
                marker="o",
                color="k",
                linestyle="none",
                label="FM mean" if "FM mean" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FM mean", line)

        if "distance from center" in rms_svf.columns and exp_col in rms_svf.columns:
            data = rms_svf[["distance from center", exp_col]].apply(pd.to_numeric, errors="coerce").dropna()
            data = data[data["distance from center"] >= 0.0]
            line = rms_ax.plot(
                data["distance from center"],
                data[exp_col],
                marker="o",
                color="k",
                linestyle="none",
                label="FM RMS" if "FM RMS" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FM RMS", line)

        sim_slice = sim[np.isclose(sim["height_over_D"], height_over_d)].sort_values("radius")
        if not sim_slice.empty:
            line = mean_ax.plot(
                sim_slice["radius"],
                sim_slice["sootVF_mean"],
                color="tab:red",
                linewidth=2,
                label="FireFOAM mean" if "FireFOAM mean" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FireFOAM mean", line)
            line = rms_ax.plot(
                sim_slice["radius"],
                sim_slice["sootVF_rms"],
                color="tab:red",
                linewidth=2,
                label="FireFOAM RMS" if "FireFOAM RMS" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FireFOAM RMS", line)

        mean_ax.set_xlim(0, x_tick_max_cm)
        rms_ax.set_xlim(0, x_tick_max_cm)
        mean_ax.set_xticks(radius_ticks_cm)
        rms_ax.set_xticks(radius_ticks_cm)
        mean_ax.set_ylim(bottom=0, top=2.5)
        rms_ax.set_ylim(bottom=0, top=2.5)
        mean_ax.label_outer()
        rms_ax.label_outer()
        plt.setp(mean_ax.yaxis.get_majorticklabels(), fontsize=8)
        plt.setp(rms_ax.xaxis.get_majorticklabels(), rotation=45, fontsize=8)
        plt.setp(rms_ax.yaxis.get_majorticklabels(), fontsize=8)

    axs[0, 0].set_ylabel("Mean soot volume fraction (ppm)")
    axs[1, 0].set_ylabel("Soot RMS (ppm)")
    fig.text(0.5, 0.02, "Radius (cm)", ha="center")
    fig.legend(list(legend_items.values()), list(legend_items.keys()), frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(0.985, 0.965))
    fig.subplots_adjust(left=0.08, right=0.91, bottom=0.12, top=0.89, hspace=0.12, wspace=0.0)
    save_fig(fig, f"{BASE_NAME}_soot_profile.png")


def plot_velocity_profiles():
    vertical_exp = read_velocity_csv(require(VERTICAL_VELOCITY_EXP_CSV))
    horizontal_exp = read_velocity_csv(require(HORIZONTAL_VELOCITY_EXP_CSV))
    vertical_heights = np.array(vertical_exp.columns[1:], dtype=float)
    horizontal_heights = np.array(horizontal_exp.columns[1:], dtype=float)
    sim = pd.read_csv(VELOCITY_CSV, header=1)

    fig, axs = plt.subplots(
        nrows=2,
        ncols=len(PLOT_PROFILE_HEIGHTS),
        sharex="row",
        sharey="row",
        gridspec_kw={"hspace": 0.12, "wspace": 0.0},
        figsize=(18, 7),
    )
    legend_items = {}
    x_tick_max_cm = 10
    x_ticks_cm = np.arange(-x_tick_max_cm, x_tick_max_cm + 0.1, 5.0)

    for i, height_label in enumerate(PLOT_PROFILE_HEIGHTS):
        height_over_d = height_value(height_label)
        height_cm = height_over_d * BURNER_DIAMETER_CM
        vertical_col = nearest_height(vertical_heights, height_cm)
        horizontal_col = nearest_height(horizontal_heights, height_cm)
        vertical_ax = axs[0, i]
        horizontal_ax = axs[1, i]
        vertical_ax.set_title(f"z = {height_label}")

        line = vertical_ax.plot(
            vertical_exp["x_cm"],
            vertical_exp[vertical_col],
            marker="o",
            color="k",
            linestyle="none",
            label="FM" if "FM" not in legend_items else "_nolegend_",
        )[0]
        legend_items.setdefault("FM", line)
        horizontal_ax.plot(
            horizontal_exp["x_cm"],
            horizontal_exp[horizontal_col],
            marker="o",
            color="k",
            linestyle="none",
        )

        sim_slice = sim[np.isclose(sim["height_over_D"], height_over_d)].sort_values("x")
        if not sim_slice.empty:
            line = vertical_ax.plot(
                sim_slice["x"],
                sim_slice["UMean_z"],
                color="tab:red",
                linewidth=2,
                label="FireFOAM" if "FireFOAM" not in legend_items else "_nolegend_",
            )[0]
            legend_items.setdefault("FireFOAM", line)
            horizontal_ax.plot(sim_slice["x"], sim_slice["UMean_x"], color="tab:red", linewidth=2)

        vertical_ax.set_xlim(-x_tick_max_cm, x_tick_max_cm)
        horizontal_ax.set_xlim(-x_tick_max_cm, x_tick_max_cm)
        vertical_ax.set_xticks(x_ticks_cm)
        horizontal_ax.set_xticks(x_ticks_cm)
        vertical_ax.label_outer()
        horizontal_ax.label_outer()
        plt.setp(vertical_ax.yaxis.get_majorticklabels(), fontsize=8)
        plt.setp(horizontal_ax.xaxis.get_majorticklabels(), rotation=45, fontsize=8)
        plt.setp(horizontal_ax.yaxis.get_majorticklabels(), fontsize=8)

    axs[0, 0].set_ylabel("Mean U_z (m/s)")
    axs[1, 0].set_ylabel("Mean U_x (m/s)")
    fig.text(0.5, 0.02, "x (cm)", ha="center")
    fig.legend(list(legend_items.values()), list(legend_items.keys()), frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(0.985, 0.965))
    fig.subplots_adjust(left=0.08, right=0.91, bottom=0.12, top=0.89, hspace=0.12, wspace=0.0)
    save_fig(fig, f"{BASE_NAME}_velocity_profile.png")


def main():
    for path in SUBMITTED_CSVS:
        require(path)

    print(f"Plotting {BASE_NAME} from submitted CSV files")
    print(f"Experimental data: {EXP_ROOT}")

    plot_hrr()
    plot_temperature_profiles()
    plot_soot_profiles()
    plot_velocity_profiles()
    print(f"Done. Outputs are in {SCRIPT_DIR}")


if __name__ == "__main__":
    main()
