#!/usr/bin/env python3
"""Export hood ``HRR`` (kW) for UMD_SBI pure gas burner — four mesh resolutions.

Reads FDS ``*_devc.csv`` from ``Output/UMC_SBI_without_PMMA/`` and writes
``Output/UMD_HRR.csv`` in MaCFP line format (units row, names row, ``.3E`` data).
Time base is the 4 cm output grid; other meshes are linearly interpolated with
blank cells outside each run's time range.

Example::

  python3 UMD_SBI_pure_gasburner_export_HRR.py
  python3 UMD_SBI_pure_gasburner_export_HRR.py --tmax 200 --plot Plots/UMD_HRR.png
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = HERE / "Output" / "UMC_SBI_without_PMMA"
OUTPUT_DIR = HERE / "Output"

COL_HRR = "HRR"

CASES: list[tuple[str, str]] = [
    ("HRR_4cm", "UMD_SBI_4_cm_pure_gasburner_devc.csv"),
    ("HRR_2cm", "UMD_SBI_2_cm_pure_gasburner_devc.csv"),
    ("HRR_1cm", "UMD_SBI_1_cm_pure_gasburner_devc.csv"),
    ("HRR_0p5cm", "UMD_SBI_5_mm_pure_gasburner_devc.csv"),
]


def read_hrr(path: Path) -> tuple[np.ndarray, np.ndarray]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(newline="") as f:
        next(f)
        reader = csv.DictReader(f)
        if COL_HRR not in (reader.fieldnames or []):
            raise KeyError(f"{path}: missing {COL_HRR!r}")
        t_list: list[float] = []
        h_list: list[float] = []
        for row in reader:
            try:
                t_list.append(float(row["Time"]))
                h_list.append(float(row[COL_HRR]))
            except (KeyError, TypeError, ValueError):
                continue
        if not t_list:
            raise ValueError(f"No numeric rows in {path}")
    return np.asarray(t_list, dtype=float), np.asarray(h_list, dtype=float)


def fmt_macfp(x: float) -> str:
    if not math.isfinite(x):
        return ""
    return f"{x: .3E}"


def interpolate_on_master(t_master: np.ndarray, t: np.ndarray, y: np.ndarray) -> np.ndarray:
    out = np.full(t_master.shape, np.nan, dtype=float)
    if len(t) == 0:
        return out
    eps = 1e-9
    lo, hi = float(t[0]) - eps, float(t[-1]) + eps
    m = (t_master >= lo) & (t_master <= hi)
    if np.any(m):
        out[m] = np.interp(t_master[m], t, y)
    return out


def load_all(data_dir: Path, tmax: float | None) -> tuple[np.ndarray, list[tuple[str, str, np.ndarray, np.ndarray]]]:
    master_path = data_dir / CASES[0][1]
    t_master, _ = read_hrr(master_path)
    if tmax is not None:
        t_master = t_master[t_master <= float(tmax) + 1e-9]
    loaded: list[tuple[str, str, np.ndarray, np.ndarray]] = []
    for col, fname in CASES:
        t, h = read_hrr(data_dir / fname)
        loaded.append((col, fname, t, h))
    return t_master, loaded


def write_macfp_csv(out_path: Path, t_master: np.ndarray, series: list[np.ndarray], col_names: list[str]) -> None:
    units = ["s"] + ["kW"] * len(col_names)
    names = ["t"] + col_names
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(units)
        w.writerow(names)
        for i in range(len(t_master)):
            row = [fmt_macfp(float(t_master[i]))]
            for s in series:
                row.append(fmt_macfp(float(s[i])))
            w.writerow(row)


def plot_figure(data_dir: Path, png_out: Path, tmax: float | None) -> None:
    _, loaded = load_all(data_dir, tmax)
    labels = ["4 cm", "2 cm", "1 cm", "0.5 cm"]
    fig, ax = plt.subplots(figsize=(9.0, 5.0), constrained_layout=True)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for i, (_col, _fname, t, h) in enumerate(loaded):
        m = np.ones(len(t), dtype=bool)
        if tmax is not None:
            m &= t <= float(tmax)
        ax.plot(t[m], h[m], lw=1.75, label=labels[i], color=colors[i % len(colors)])
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("HRR (kW)")
    ax.set_title("Heat release rate (hood energy balance)")
    ax.grid(True, alpha=0.35)
    ax.legend(loc="best", fontsize=10, framealpha=0.9)
    if tmax is not None:
        ax.set_xlim(0.0, float(tmax))
    fig.suptitle(
        "UMD_SBI pure gas burner — HRR vs time (4 / 2 / 1 / 0.5 cm)",
        fontsize=12,
        fontweight="bold",
    )
    png_out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_out, dpi=160)
    plt.close(fig)
    print(f"Saved → {png_out}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    p.add_argument("--tmax", type=float, default=200.0, help="Upper time limit (s)")
    p.add_argument("--csv", type=Path, default=OUTPUT_DIR / "UMD_HRR.csv")
    p.add_argument("--plot", type=Path, default=None, help="Optional PNG path")
    p.add_argument("--no-csv", action="store_true")
    args = p.parse_args()
    data_dir = args.data_dir.resolve()
    tmax = args.tmax
    if not args.no_csv:
        t_master, loaded = load_all(data_dir, tmax)
        series = [interpolate_on_master(t_master, t, h) for _c, _f, t, h in loaded]
        col_names = [c for c, _f in CASES]
        write_macfp_csv(args.csv.resolve(), t_master, series, col_names)
        print(f"Saved → {args.csv.resolve()}  ({len(t_master)} times, t = {t_master[0]:g}–{t_master[-1]:g} s)")
    if args.plot:
        plot_figure(data_dir, args.plot.resolve(), tmax)


if __name__ == "__main__":
    main()
