#!/usr/bin/env python3
"""Export / plot PMMA full-case x = 0 wall surface integrals (kW) for MaCFP line CSV.

Reads FDS ``*_devc.csv`` from ``UMD_SBI_mesh_sensitivity_study/UMD_SBI_full_case``:
  - **GHF tot x0** — gauge heat flux (total), surface integral
  - **GHF rad x0** — radiometer, surface integral
  - **GHF conv x0** — convective heat flux gauge, surface integral

Writes ``UMD_GHF_rad_CHGF_full_case.csv`` in MaCFP line format (same layout as
``Computational_Results/2026/UMD/Output/UMD_GHF_rad_CHGF.csv``): units row, names row,
``.3E`` data; columns ordered tot/rad/con × (4 cm, 2 cm, 1 cm, 0.5 cm). The 0.5 cm
column is left blank (full-case figure uses 1 / 2 / 4 cm only).

Default 4 cm path is ``1200s/4cm`` (complete to 1200 s); override with ``--devc-4cm``.
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

COLUMNS = [
    ("GHF tot  x0", "Gauge heat flux (total) — PMMA face x=0, surface integral"),
    ("GHF rad  x0", "Radiometer — PMMA face x=0, surface integral"),
    ("GHF conv x0", "Convective heat flux gauge — PMMA face x=0, surface integral"),
]

CASES: list[tuple[str, str]] = [
    ("4 cm", "1200s/4cm/UMD_SBI_4_cm_devc.csv"),
    ("2 cm", "2cm/UMD_SBI_full_case_2_cm_devc.csv"),
    ("1 cm", "1cm/UMD_SBI_full_case_1_cm_devc.csv"),
    ("0.5 cm", ""),  # not in full-case x0 comparison figure
]


def read_devc_columns(path: Path, cols: list[str]) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(newline="") as f:
        next(f)  # units row
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


def write_macfp_csv(
    out_path: Path,
    t_master: np.ndarray,
    col_series: list[np.ndarray],
) -> None:
    """Wide CSV: t + GHF_tot/rad/con for 4 / 2 / 1 / 0.5 cm."""
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


def resolve_cases(full_case: Path, devc_4cm: Path | None) -> list[tuple[str, Path | None]]:
    out: list[tuple[str, Path | None]] = []
    for label, rel in CASES:
        if not rel:
            out.append((label, None))
            continue
        if label == "4 cm" and devc_4cm is not None:
            out.append((label, devc_4cm))
        else:
            out.append((label, full_case / rel))
    return out


def load_series(full_case: Path, devc_4cm: Path | None) -> tuple[np.ndarray, list[tuple[str, np.ndarray, dict[str, np.ndarray]]]]:
    col_names = [c for c, _ in COLUMNS]
    cases = resolve_cases(full_case, devc_4cm)
    loaded: list[tuple[str, np.ndarray, dict[str, np.ndarray]]] = []
    t_master: np.ndarray | None = None
    for label, path in cases:
        if path is None:
            loaded.append((label, np.array([]), {}))
            continue
        t, d = read_devc_columns(path, col_names)
        loaded.append((label, t, d))
        if label == "2 cm":
            t_master = t.copy()
    if t_master is None:
        raise RuntimeError("Could not set time master from 2 cm devc.csv")
    return t_master, loaded


def export_csv(full_case: Path, csv_out: Path, devc_4cm: Path | None) -> None:
    col_names = [c for c, _ in COLUMNS]
    qty_short = ["GHF_tot", "GHF_rad", "GHF_con"]
    t_master, loaded = load_series(full_case, devc_4cm)
    col_series: list[np.ndarray] = []
    for col, _title in COLUMNS:
        for label, t, d in loaded:
            if not len(t):
                col_series.append(np.full_like(t_master, np.nan, dtype=float))
            else:
                col_series.append(interpolate_on_master(t_master, t, d[col]))
    write_macfp_csv(csv_out, t_master, col_series)
    print(f"Saved → {csv_out}  ({len(t_master)} times, t = {t_master[0]:g}–{t_master[-1]:g} s)")


def plot_from_devc(full_case: Path, png_out: Path, devc_4cm: Path | None) -> None:
    col_names = [c for c, _ in COLUMNS]
    t_master, loaded = load_series(full_case, devc_4cm)
    fig, axes = plt.subplots(3, 1, figsize=(9.0, 8.5), sharex=True, constrained_layout=True)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    plot_meshes = [("1 cm", 2), ("2 cm", 1), ("4 cm", 0)]
    for ax, (col, title) in zip(axes, COLUMNS):
        for i, (lab, idx) in enumerate(plot_meshes):
            label, t, d = loaded[idx]
            if not len(t):
                continue
            ax.plot(t, d[col], lw=1.6, label=lab, color=colors[i % len(colors)])
        ax.set_ylabel("kW")
        ax.set_title(title)
        ax.grid(True, alpha=0.35)
        ax.legend(loc="best", fontsize=9, framealpha=0.9)
    axes[-1].set_xlim(float(t_master[0]), float(t_master[-1]))
    axes[-1].set_xlabel("Time (s)")
    fig.suptitle(
        "Full case (PMMA pyrolysis): mesh sensitivity (x=0 wall)",
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
    p.add_argument(
        "--devc-4cm",
        type=Path,
        default=None,
        help="Override 4 cm devc.csv (default: FULL_CASE_ROOT/1200s/4cm/UMD_SBI_4_cm_devc.csv)",
    )
    p.add_argument(
        "--csv",
        type=Path,
        default=HERE / "UMD_GHF_rad_CHGF_full_case.csv",
    )
    p.add_argument("--plot", type=Path, default=None, help="Optional PNG path (from devc, not CSV)")
    p.add_argument("--no-csv", action="store_true")
    args = p.parse_args()
    full_case = args.full_case_root.resolve()
    devc_4cm = args.devc_4cm.resolve() if args.devc_4cm else None
    if not args.no_csv:
        export_csv(full_case, args.csv.resolve(), devc_4cm)
    if args.plot:
        plot_from_devc(full_case, args.plot.resolve(), devc_4cm)


if __name__ == "__main__":
    main()
