#!/usr/bin/env python3
"""Export pure gas burner y = 0 wall surface integrals (kW) for MaCFP line CSV.

Reads FDS ``*_devc.csv`` from ``Output/UMC_SBI_without_PMMA/``:
  - **GHF tot y0** — gauge heat flux (total), surface integral
  - **GHF rad y0** — radiometer, surface integral
  - **GHF con y0** — convective heat flux gauge (CHFG), surface integral

Writes ``Output/UMD_GHF_rad_CHGF.csv`` in MaCFP line format: units row, names row,
``.3E`` data; columns ordered tot/rad/con × (4 cm, 2 cm, 1 cm, 0.5 cm).
Time base is the 4 cm output grid.

Example::

  python3 UMD_SBI_pure_gasburner_export_GHF_rad_CHGF.py
  python3 UMD_SBI_pure_gasburner_export_GHF_rad_CHGF.py --plot Plots/UMD_GHF_rad_CHGF.png
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

COLUMNS = [
    ("GHF tot  y0", "Gauge heat flux (total) — y = 0 face, surface integral"),
    ("GHF rad  y0", "Radiometer — y = 0 face, surface integral"),
    ("GHF con  y0", "Convective heat flux gauge — y = 0 face, surface integral"),
]

CASES: list[tuple[str, str]] = [
    ("4 cm", "UMD_SBI_4_cm_pure_gasburner_devc.csv"),
    ("2 cm", "UMD_SBI_2_cm_pure_gasburner_devc.csv"),
    ("1 cm", "UMD_SBI_1_cm_pure_gasburner_devc.csv"),
    ("0.5 cm", "UMD_SBI_5_mm_pure_gasburner_devc.csv"),
]


def read_devc_columns(path: Path, cols: list[str]) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(newline="") as f:
        next(f)
        reader = csv.DictReader(f)
        fieldnames = [c.strip() for c in (reader.fieldnames or [])]
        key_map = {name.strip(): name for name in fieldnames}
        rows: list[list[float]] = []
        for row in reader:
            try:
                rows.append([float(row[key_map["Time"]])] + [float(row[key_map[c]]) for c in cols])
            except (KeyError, TypeError, ValueError):
                continue
        if not rows:
            raise ValueError(f"No numeric rows in {path}")
        arr = np.asarray(rows, dtype=float)
    t = arr[:, 0]
    data = {c: arr[:, i + 1] for i, c in enumerate(cols)}
    return t, data


def fmt_macfp(x: float) -> str:
    if not math.isfinite(x):
        return ""
    return f"{x: .3E}"


def interpolate_on_master(t_master: np.ndarray, t: np.ndarray, y: np.ndarray) -> np.ndarray:
    out = np.full(t_master.shape, np.nan, dtype=float)
    eps = 1e-9
    lo, hi = float(t[0]) - eps, float(t[-1]) + eps
    m = (t_master >= lo) & (t_master <= hi)
    if np.any(m):
        out[m] = np.interp(t_master[m], t, y)
    return out


def write_macfp_csv(out_path: Path, t_master: np.ndarray, col_series: list[np.ndarray]) -> None:
    qty_short = ["GHF_tot", "GHF_rad", "GHF_con"]
    n_mesh = 4
    n_qty = len(qty_short)
    if len(col_series) != n_mesh * n_qty:
        raise ValueError("column series count mismatch")
    units = ["s"] + ["kW"] * (n_mesh * n_qty)
    names = ["t"]
    for qty in qty_short:
        names.extend([f"{qty}_4cm", f"{qty}_2cm", f"{qty}_1cm", f"{qty}_0p5cm"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(units)
        w.writerow(names)
        for i in range(len(t_master)):
            row = [fmt_macfp(float(t_master[i]))]
            for series in col_series:
                row.append(fmt_macfp(float(series[i])))
            w.writerow(row)


def load_series(data_dir: Path) -> tuple[np.ndarray, list[tuple[str, np.ndarray, dict[str, np.ndarray]]]]:
    col_names = [c for c, _ in COLUMNS]
    loaded: list[tuple[str, np.ndarray, dict[str, np.ndarray]]] = []
    t_master: np.ndarray | None = None
    for label, fname in CASES:
        t, d = read_devc_columns(data_dir / fname, col_names)
        loaded.append((label, t, d))
        if label == "4 cm":
            t_master = t.copy()
    if t_master is None:
        raise RuntimeError("Could not set time master from 4 cm devc.csv")
    return t_master, loaded


def export_csv(data_dir: Path, csv_out: Path) -> None:
    col_names = [c for c, _ in COLUMNS]
    t_master, loaded = load_series(data_dir)
    col_series: list[np.ndarray] = []
    for col, _title in COLUMNS:
        for _label, t, d in loaded:
            col_series.append(interpolate_on_master(t_master, t, d[col]))
    write_macfp_csv(csv_out, t_master, col_series)
    print(f"Saved → {csv_out}  ({len(t_master)} times, t = {t_master[0]:g}–{t_master[-1]:g} s)")


def plot_from_devc(data_dir: Path, png_out: Path) -> None:
    col_names = [c for c, _ in COLUMNS]
    t_master, loaded = load_series(data_dir)
    fig, axes = plt.subplots(3, 1, figsize=(9.0, 8.5), sharex=True, constrained_layout=True)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for ax, (col, title) in zip(axes, COLUMNS):
        for i, (label, t, d) in enumerate(loaded):
            ax.plot(t, d[col], lw=1.6, label=label, color=colors[i % len(colors)])
        ax.set_ylabel("kW")
        ax.set_title(title)
        ax.grid(True, alpha=0.35)
        ax.legend(loc="best", fontsize=9, framealpha=0.9)
    axes[-1].set_xlim(float(t_master[0]), float(t_master[-1]))
    axes[-1].set_xlabel("Time (s)")
    fig.suptitle(
        "UMD_SBI pure gas burner — y = 0 face surface integrals (four meshes)",
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
    p.add_argument("--csv", type=Path, default=OUTPUT_DIR / "UMD_GHF_rad_CHGF.csv")
    p.add_argument("--plot", type=Path, default=None, help="Optional PNG path")
    p.add_argument("--no-csv", action="store_true")
    args = p.parse_args()
    data_dir = args.data_dir.resolve()
    if not args.no_csv:
        export_csv(data_dir, args.csv.resolve())
    if args.plot:
        plot_from_devc(data_dir, args.plot.resolve())


if __name__ == "__main__":
    main()
