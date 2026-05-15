#!/usr/bin/env python3
# Lei Li
# May 2026
#
# Adapted for UMD_SBI MaCFP-4 line CSVs in this folder (May 2026).
# Original workflow used ``macfp.dataplot`` with ``NIST_Pool_Fires_cmp_config.csv``.
# This copy plots the MaCFP line-format CSVs from the ``Output/`` directory:
#   - ``Output/UMD_HRR.csv``
#   - ``Output/UMD_GHF_rad_CHGF.csv``
# Figures go to ``Plots/`` under this script's directory.

from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Optional: uncomment to use ``macfp.dataplot`` with a pool-fire config (paths must exist).
# sys.path.append(str(Path(__file__).resolve().parent.parent / "PMMA_source/macfp-db/Utilities/"))
# import macfp  # noqa: E402
# macfp.dataplot(config_filename="example/NIST_Pool_Fires_cmp_config.csv", ...)

HERE = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = HERE / "Output"
DEFAULT_PLOT_DIR = HERE / "Plots"

MESH_LABELS = ["4 cm", "2 cm", "1 cm", "0.5 cm"]


def read_macfp_line_csv(path: Path) -> tuple[list[str], np.ndarray]:
    """Load MaCFP-style CSV: row 0 = units, row 1 = names, row 2+ = numeric data (``.3E``); blanks → NaN."""
    with path.open(newline="") as f:
        rows = list(csv.reader(f))
    if len(rows) < 3:
        raise ValueError(f"{path}: expected units row, names row, and at least one data row")
    names = [c.strip() for c in rows[1]]
    ncols = len(names)
    data: list[list[float]] = []
    for parts in rows[2:]:
        row: list[float] = []
        for j in range(ncols):
            cell = parts[j].strip() if j < len(parts) else ""
            if cell == "":
                row.append(math.nan)
            else:
                row.append(float(cell))
        data.append(row)
    return names, np.asarray(data, dtype=float)


def plot_hrr(names: list[str], arr: np.ndarray, out_path: Path, title: str) -> None:
    t = arr[:, 0]
    fig, ax = plt.subplots(figsize=(9.0, 5.0), constrained_layout=True)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for j in range(1, min(arr.shape[1], 5)):
        y = arr[:, j]
        lab = names[j] if j < len(names) else f"col{j}"
        ax.plot(t, y, lw=1.75, label=MESH_LABELS[j - 1] if j - 1 < len(MESH_LABELS) else lab, color=colors[(j - 1) % len(colors)])
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("HRR (kW)")
    ax.set_title("Heat release rate (hood / energy balance device)")
    ax.grid(True, alpha=0.35)
    ax.legend(loc="best", fontsize=10, framealpha=0.9)
    fig.suptitle(title, fontsize=12, fontweight="bold")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)
    print(f"Saved → {out_path}")


def plot_surface_integrals(names: list[str], arr: np.ndarray, out_path: Path, title: str) -> None:
    t = arr[:, 0]
    n_mesh = 4
    titles = [
        "Gauge heat flux (surface integral)",
        "Radiometer (surface integral)",
        "Convective heat flux gauge (surface integral)",
    ]
    fig, axes = plt.subplots(3, 1, figsize=(9.0, 8.5), sharex=True, constrained_layout=True)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for panel in range(3):
        ax = axes[panel]
        i0 = 1 + panel * n_mesh
        for k in range(n_mesh):
            j = i0 + k
            if j >= arr.shape[1]:
                break
            y = arr[:, j]
            lab = names[j] if j < len(names) else f"col{j}"
            ax.plot(t, y, lw=1.6, label=MESH_LABELS[k], color=colors[k % len(colors)])
        ax.set_ylabel("kW")
        ax.set_title(titles[panel])
        ax.grid(True, alpha=0.35)
        ax.legend(loc="best", fontsize=9, framealpha=0.9)
    axes[-1].set_xlabel("Time (s)")
    fig.suptitle(title, fontsize=12, fontweight="bold")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)
    print(f"Saved → {out_path}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Directory containing UMD_HRR.csv and UMD_GHF_rad_CHGF.csv")
    p.add_argument("--plot-dir", type=Path, default=DEFAULT_PLOT_DIR, help="Where to write PNG figures")
    args = p.parse_args()
    data_dir = args.data_dir.resolve()
    plot_dir = args.plot_dir.resolve()

    hrr_csv = data_dir / "UMD_HRR.csv"
    ghf_csv = data_dir / "UMD_GHF_rad_CHGF.csv"

    missing = [str(path) for path in (hrr_csv, ghf_csv) if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            "Required CSV file(s) not found: "
            + ", ".join(missing)
            + "\nExpected layout: ./Output/UMD_HRR.csv and ./Output/UMD_GHF_rad_CHGF.csv"
        )

    names_h, arr_h = read_macfp_line_csv(hrr_csv)
    plot_hrr(
        names_h,
        arr_h,
        plot_dir / "UMD_HRR.png",
        "UMD_SBI pure gas burner — HRR vs time (4 / 2 / 1 / 0.5 cm)",
    )

    names_g, arr_g = read_macfp_line_csv(ghf_csv)
    plot_surface_integrals(
        names_g,
        arr_g,
        plot_dir / "UMD_GHF_rad_CHGF.png",
        "UMD_SBI pure gas burner — y = 0 PMMA face surface integrals (four meshes)",
    )


if __name__ == "__main__":
    main()
