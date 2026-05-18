#!/usr/bin/env python3
"""Plot and export hood ``HRR`` (kW) for UMD_SBI full case — 1 cm, 2 cm, 4 cm meshes.

Reads ``HRR`` from ``*_devc.csv`` under ``UMD_SBI_mesh_sensitivity_study/UMD_SBI_full_case``:
  - 1 cm: ``1cm/UMD_SBI_full_case_1_cm_devc.csv``
  - 2 cm: ``2cm/UMD_SBI_full_case_2_cm_devc.csv`` (time base for CSV)
  - 4 cm: ``1200s/4cm/UMD_SBI_4_cm_devc.csv`` by default (``4cm/`` local run is ~6 s only)

Writes MaCFP line CSV (same layout as ``Output/UMD_HRR.csv``):
  ``Output/UMD_HRR_full_case_1_2_4cm.csv``

Figure: ``Plots/UMD_HRR_full_case_1_2_4cm.png``

Example::

  python3 UMD_SBI_full_case_HRR_1_2_4cm.py
  python3 UMD_SBI_full_case_HRR_1_2_4cm.py --tmax 200
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "Output"
PLOTS_DIR = HERE / "Plots"
DEFAULT_FULL_CASE = (
    HERE.parents[6]
    / "UMD_SBI_mesh_sensitivity_study"
    / "UMD_SBI_full_case"
)

COL_HRR = "HRR"

CASES: list[tuple[str, str, str]] = [
    ("HRR_4cm", "4 cm", "1200s/4cm/UMD_SBI_4_cm_devc.csv"),
    ("HRR_2cm", "2 cm", "2cm/UMD_SBI_full_case_2_cm_devc.csv"),
    ("HRR_1cm", "1 cm", "1cm/UMD_SBI_full_case_1_cm_devc.csv"),
]

MASTER_REL = "2cm/UMD_SBI_full_case_2_cm_devc.csv"


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


def load_series(
    full_case: Path, tmax: float | None, devc_4cm: Path | None
) -> tuple[np.ndarray, list[tuple[str, str, np.ndarray, np.ndarray]]]:
    t_master, _ = read_hrr(full_case / MASTER_REL)
    if tmax is not None:
        t_master = t_master[t_master <= float(tmax) + 1e-9]

    loaded: list[tuple[str, str, np.ndarray, np.ndarray]] = []
    for col, label, rel in CASES:
        path = devc_4cm if col == "HRR_4cm" and devc_4cm is not None else full_case / rel
        t, h = read_hrr(path)
        loaded.append((col, label, t, h))
    return t_master, loaded


def write_csv(out_path: Path, t_master: np.ndarray, series: list[np.ndarray], col_names: list[str]) -> None:
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


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--full-case-root", type=Path, default=DEFAULT_FULL_CASE)
    p.add_argument(
        "--devc-4cm",
        type=Path,
        default=None,
        help="Override 4 cm devc (default: 1200s/4cm; use 4cm/ for short local run)",
    )
    p.add_argument("--tmax", type=float, default=200.0, help="Upper time limit (s)")
    p.add_argument("--csv", type=Path, default=OUTPUT_DIR / "UMD_HRR_full_case_1_2_4cm.csv")
    p.add_argument("--plot", type=Path, default=PLOTS_DIR / "UMD_HRR_full_case_1_2_4cm.png")
    p.add_argument("--no-csv", action="store_true")
    p.add_argument("--no-plot", action="store_true")
    args = p.parse_args()

    full_case = args.full_case_root.resolve()
    devc_4cm = args.devc_4cm.resolve() if args.devc_4cm else None
    t_master, loaded = load_series(full_case, args.tmax, devc_4cm)
    col_names = [c for c, _, _ in CASES]
    series = [interpolate_on_master(t_master, t, h) for _c, _l, t, h in loaded]

    if not args.no_csv:
        write_csv(args.csv.resolve(), t_master, series, col_names)
        print(f"Saved → {args.csv.resolve()}  ({len(t_master)} rows, t = {t_master[0]:g}–{t_master[-1]:g} s)")

    if not args.no_plot:
        fig, ax = plt.subplots(figsize=(9.0, 5.0), constrained_layout=True)
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
        order = [("4 cm", 0), ("2 cm", 1), ("1 cm", 2)]
        for i, (lab, idx) in enumerate(order):
            _c, label, t, h = loaded[idx]
            m = np.ones(len(t), dtype=bool)
            if args.tmax is not None:
                m &= t <= float(args.tmax)
            ax.plot(t[m], h[m], lw=1.75, label=lab, color=colors[i % len(colors)])
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("HRR (kW)")
        ax.set_title("Heat release rate (hood energy balance)")
        ax.grid(True, alpha=0.35)
        ax.legend(loc="best", fontsize=10, framealpha=0.9)
        if args.tmax is not None:
            ax.set_xlim(0.0, float(args.tmax))
        fig.suptitle(
            "UMD_SBI full case (PMMA) — HRR vs time (1 / 2 / 4 cm)",
            fontsize=12,
            fontweight="bold",
        )
        args.plot.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.plot.resolve(), dpi=160)
        plt.close(fig)
        print(f"Saved → {args.plot.resolve()}")


if __name__ == "__main__":
    main()
