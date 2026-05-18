#!/usr/bin/env python3
"""Export / plot UMD_SBI full-case hood ``HRR`` (kW) for MaCFP line CSV.

Same cases as ``UMD_SBI_mesh_sensitivity_study/UMD_SBI_full_case/plot_HRR_profile_mesh_compare.py``:
  - 4 cm (short local ``4cm/`` run)
  - 4 cm (1200 s deck, ``1200s/4cm/``)
  - 2 cm, 1 cm, 5 mm v1

Writes ``UMD_HRR_with_PMMA_case.csv`` (MaCFP line format like ``UMD_HRR.csv``):
units row, names row, ``.3E`` data. Time base is the **2 cm** output grid (interpolate other runs);
values outside each run's time range are blank.

Example::

  python3 UMD_SBI_full_case_export_HRR.py --tmax 200
  python3 UMD_SBI_full_case_export_HRR.py --tmax 200 --plot Output/UMD_HRR_with_PMMA_case.png
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_FULL_CASE = (
    HERE.parents[3]
    / "UMD_SBI_mesh_sensitivity_study"
    / "UMD_SBI_full_case"
)

COL_HRR = "HRR"

# (CSV suffix, label, path relative to full_case root)
CASES: list[tuple[str, str, str]] = [
    ("HRR_4cm", "4 cm", "4cm/UMD_SBI_4_cm_devc.csv"),
    ("HRR_4cm_1200s", "4 cm (1200 s)", "1200s/4cm/UMD_SBI_4_cm_devc.csv"),
    ("HRR_2cm", "2 cm", "2cm/UMD_SBI_full_case_2_cm_devc.csv"),
    ("HRR_1cm", "1 cm", "1cm/UMD_SBI_full_case_1_cm_devc.csv"),
    ("HRR_5mm_v1", "5 mm v1", "5mm_v1/UMD_SBI_full_case_5_mm_devc.csv"),
]

MASTER_MESH = "2cm/UMD_SBI_full_case_2_cm_devc.csv"


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


def load_all(full_case: Path, tmax: float | None) -> tuple[np.ndarray, list[tuple[str, str, np.ndarray, np.ndarray]]]:
    master_path = full_case / MASTER_MESH
    t_master, _ = read_hrr(master_path)
    if tmax is not None:
        t_master = t_master[t_master <= float(tmax) + 1e-9]
    loaded: list[tuple[str, str, np.ndarray, np.ndarray]] = []
    for col, label, rel in CASES:
        t, h = read_hrr(full_case / rel)
        loaded.append((col, label, t, h))
    return t_master, loaded


def export_csv(full_case: Path, csv_out: Path, tmax: float | None) -> None:
    t_master, loaded = load_all(full_case, tmax)
    series = [interpolate_on_master(t_master, t, h) for _col, _lab, t, h in loaded]
    col_names = [c for c, _l, _r in CASES]
    write_macfp_csv(csv_out, t_master, series, col_names)
    print(f"Saved → {csv_out}  ({len(t_master)} times, t = {t_master[0]:g}–{t_master[-1]:g} s)")


def plot_figure(full_case: Path, png_out: Path, tmax: float | None) -> None:
    _, loaded = load_all(full_case, tmax)
    fig, ax = plt.subplots(figsize=(9.0, 5.0), constrained_layout=True)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for i, (_col, label, t, h) in enumerate(loaded):
        m = np.ones(len(t), dtype=bool)
        if tmax is not None:
            m &= t <= float(tmax)
        ax.plot(t[m], h[m], lw=1.75, label=label, color=colors[i % len(colors)])
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("HRR (kW)")
    ax.set_title("Heat release rate (hood energy balance)")
    ax.grid(True, alpha=0.35)
    ax.legend(loc="best", fontsize=10, framealpha=0.9)
    if tmax is not None:
        ax.set_xlim(0.0, float(tmax))
    fig.suptitle(
        "UMD_SBI full case — HRR vs time (4 cm, 4 cm 1200 s, 2 / 1 / 5 mm v1)",
        fontsize=12,
        fontweight="bold",
    )
    png_out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_out, dpi=160)
    plt.close(fig)
    print(f"Saved → {png_out}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--full-case-root", type=Path, default=DEFAULT_FULL_CASE)
    p.add_argument("--tmax", type=float, default=200.0, help="Upper time limit (s); default 200 for figure")
    p.add_argument("--csv", type=Path, default=HERE / "UMD_HRR_with_PMMA_case.csv")
    p.add_argument("--plot", type=Path, default=None, help="Optional PNG path")
    p.add_argument("--no-csv", action="store_true")
    args = p.parse_args()
    full_case = args.full_case_root.resolve()
    tmax = args.tmax
    if not args.no_csv:
        export_csv(full_case, args.csv.resolve(), tmax)
    if args.plot:
        plot_figure(full_case, args.plot.resolve(), tmax)


if __name__ == "__main__":
    main()
