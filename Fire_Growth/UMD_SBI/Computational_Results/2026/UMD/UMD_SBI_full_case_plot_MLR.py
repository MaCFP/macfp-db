#!/usr/bin/env python3
"""Plot PMMA mass loss rate (MLR) from UMD_SBI full-case ``*_devc.csv``.

Reads surface-integrated burning rate from ``Output/UMD_SBI_with_PMMA/``:
  - **MLR PMMA y0** — y = 0 panel (kg/s)
  - **MLR PMMA x0** — x = 0 panel (kg/s)
  - **MLR PMMA tot** — sum of both panels (kg/s)

Mesh resolutions: 4 cm, 2 cm, 1 cm, 0.5 cm.

Writes:
  - ``Plots/UMD_MLR_full_case.png`` — three-panel mesh comparison (y0 / x0 / total)
  - ``Plots/UMD_MLR_full_case_tot.png`` — total MLR only
  - ``Output/UMD_MLR_full_case.csv`` — MaCFP line CSV (optional via default)

Example::

  python3 UMD_SBI_full_case_plot_MLR.py
  python3 UMD_SBI_full_case_plot_MLR.py --tmax 200 --no-csv
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = HERE / "Output" / "UMD_SBI_with_PMMA"
OUTPUT_DIR = HERE / "Output"
PLOTS_DIR = HERE / "Plots"

COL_Y0 = "MLR PMMA y0"
COL_X0 = "MLR PMMA x0"

CASES: list[tuple[str, str, str]] = [
    ("MLR_4cm", "4 cm", "UMD_SBI_full_case_4_cm_devc.csv"),
    ("MLR_2cm", "2 cm", "UMD_SBI_full_case_2_cm_devc.csv"),
    ("MLR_1cm", "1 cm", "UMD_SBI_full_case_1_cm_devc.csv"),
    ("MLR_0p5cm", "0.5 cm", "UMD_SBI_full_case_0p5_cm_devc.csv"),
]

MASTER_MESH = "UMD_SBI_full_case_2_cm_devc.csv"


def read_mlr(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(newline="") as f:
        next(f)
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        for col in (COL_Y0, COL_X0):
            if col not in fieldnames:
                raise KeyError(f"{path}: missing {col!r}")
        t_list: list[float] = []
        y0_list: list[float] = []
        x0_list: list[float] = []
        for row in reader:
            try:
                y0 = float(row[COL_Y0])
                x0 = float(row[COL_X0])
                t_list.append(float(row["Time"]))
                y0_list.append(y0)
                x0_list.append(x0)
            except (KeyError, TypeError, ValueError):
                continue
        if not t_list:
            raise ValueError(f"No numeric rows in {path}")
    t = np.asarray(t_list, dtype=float)
    y0 = np.asarray(y0_list, dtype=float)
    x0 = np.asarray(x0_list, dtype=float)
    return t, y0, x0, y0 + x0


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


def load_all(data_dir: Path, tmax: float | None) -> tuple[np.ndarray, list[tuple[str, str, np.ndarray, np.ndarray, np.ndarray, np.ndarray]]]:
    t_master, _, _, _ = read_mlr(data_dir / MASTER_MESH)
    if tmax is not None:
        t_master = t_master[t_master <= float(tmax) + 1e-9]
    loaded: list[tuple[str, str, np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = []
    for col, label, fname in CASES:
        t, y0, x0, tot = read_mlr(data_dir / fname)
        loaded.append((col, label, t, y0, x0, tot))
    return t_master, loaded


def write_csv(out_path: Path, t_master: np.ndarray, loaded: list[tuple[str, str, np.ndarray, np.ndarray, np.ndarray, np.ndarray]]) -> None:
    qty = ["MLR_y0", "MLR_x0", "MLR_tot"]
    col_series: list[np.ndarray] = []
    for q_idx in range(3):
        for _col, _label, t, y0, x0, tot in loaded:
            series = [y0, x0, tot][q_idx]
            col_series.append(interpolate_on_master(t_master, t, series))
    units = ["s"] + ["kg/s"] * len(col_series)
    names = ["t"]
    for q in qty:
        names.extend([f"{q}_4cm", f"{q}_2cm", f"{q}_1cm", f"{q}_0p5cm"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(units)
        w.writerow(names)
        for i in range(len(t_master)):
            row = [fmt_macfp(float(t_master[i]))]
            for s in col_series:
                row.append(fmt_macfp(float(s[i])))
            w.writerow(row)
    print(f"Saved → {out_path}  ({len(t_master)} times, t = {t_master[0]:g}–{t_master[-1]:g} s)")


def plot_mlr(data_dir: Path, png_out: Path, png_tot_out: Path, tmax: float | None) -> None:
    t_master, loaded = load_all(data_dir, tmax)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    titles = [
        ("y = 0 panel", lambda _t, y0, _x0, _tot: y0),
        ("x = 0 panel", lambda _t, _y0, x0, _tot: x0),
        ("Both panels (total)", lambda _t, _y0, _x0, tot: tot),
    ]

    fig, axes = plt.subplots(3, 1, figsize=(9.0, 8.5), sharex=True, constrained_layout=True)
    for ax, (title, getter) in zip(axes, titles):
        for i, (_col, label, t, y0, x0, tot) in enumerate(loaded):
            y = getter(t, y0, x0, tot)
            m = np.ones(len(t), dtype=bool)
            if tmax is not None:
                m &= t <= float(tmax)
            ax.plot(t[m], y[m] * 1000.0, lw=1.6, label=label, color=colors[i % len(colors)])
        ax.set_ylabel("MLR (g/s)")
        ax.set_title(f"PMMA mass loss rate — {title}")
        ax.grid(True, alpha=0.35)
        ax.legend(loc="best", fontsize=9, framealpha=0.9)
    axes[-1].set_xlim(float(t_master[0]), float(t_master[-1]))
    axes[-1].set_xlabel("Time (s)")
    fig.suptitle(
        "UMD_SBI full case — PMMA MLR vs time (4 / 2 / 1 / 0.5 cm)",
        fontsize=12,
        fontweight="bold",
    )
    png_out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_out, dpi=160)
    plt.close(fig)
    print(f"Saved → {png_out}")

    fig, ax = plt.subplots(figsize=(9.0, 5.0), constrained_layout=True)
    for i, (_col, label, t, _y0, _x0, tot) in enumerate(loaded):
        m = np.ones(len(t), dtype=bool)
        if tmax is not None:
            m &= t <= float(tmax)
        ax.plot(t[m], tot[m] * 1000.0, lw=1.75, label=label, color=colors[i % len(colors)])
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("MLR (g/s)")
    ax.set_title("PMMA mass loss rate — both panels")
    ax.grid(True, alpha=0.35)
    ax.legend(loc="best", fontsize=10, framealpha=0.9)
    if tmax is not None:
        ax.set_xlim(0.0, float(tmax))
    fig.suptitle(
        "UMD_SBI full case — total PMMA MLR vs time (4 / 2 / 1 / 0.5 cm)",
        fontsize=12,
        fontweight="bold",
    )
    fig.savefig(png_tot_out, dpi=160)
    plt.close(fig)
    print(f"Saved → {png_tot_out}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    p.add_argument("--tmax", type=float, default=200.0, help="Upper time limit (s)")
    p.add_argument("--csv", type=Path, default=OUTPUT_DIR / "UMD_MLR_full_case.csv")
    p.add_argument("--plot", type=Path, default=PLOTS_DIR / "UMD_MLR_full_case.png")
    p.add_argument("--plot-tot", type=Path, default=PLOTS_DIR / "UMD_MLR_full_case_tot.png")
    p.add_argument("--no-csv", action="store_true")
    p.add_argument("--no-plot", action="store_true")
    args = p.parse_args()

    data_dir = args.data_dir.resolve()
    t_master, loaded = load_all(data_dir, args.tmax)

    if not args.no_csv:
        write_csv(args.csv.resolve(), t_master, loaded)

    if not args.no_plot:
        plot_mlr(data_dir, args.plot.resolve(), args.plot_tot.resolve(), args.tmax)


if __name__ == "__main__":
    main()
