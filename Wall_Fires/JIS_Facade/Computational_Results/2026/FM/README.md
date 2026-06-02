# FM Computational Results — JIS A 1310 Façade Fire (MaCFP-4)

## Solver

| Item | Value |
|------|-------|
| Code | fireFoam (OpenFOAM dev) |
| Fuel | C3H8 (propane) |
| Combustion | Eddy Dissipation Model (EDM), single-step C3H8 reaction |
| Turbulence | LES, dynamic Lagrangian sub-grid model |
| Radiation | fvDOM, 64 solid angles (nPhi=4, nTheta=4) |
| Radiation model | Mixed zone model (see below) |
| Grid | Successively refined to 0.5 in (12.7 mm) near flame surfaces and mixing regions |

## Radiation Model

A zone-dependent mixed absorption/emission model is used to account for the
different radiative character of the two flame regions:

- **Inside the compartment (burner region):** the net radiative source term is
  prescribed via a constant radiant loss fraction, χ_r = 0.33, applied to the
  local heat release rate. This avoids over-prediction of in-compartment
  temperatures caused by a purely optically-thin treatment.
- **Spill-over / façade plume region:** an optically-thin grey-gas model is
  applied using a soot absorption coefficient derived from a prescribed soot
  factor of 0.10 (fraction of fuel mass converted to radiatively active soot).
  The soot mass fraction field is not transported; it is reconstructed
  algebraically from the local fuel consumption rate.

This zonal approach avoids the well-known limitation of a single global radiant
fraction when the flame transitions from a confined compartment fire to a
external spill plume where soot radiation is the dominant heat-transfer
mechanism.

## Cases

Three independent LES runs, one per fire HRR:

| Case | Nominal HRR | Fuel mass flow (kg/s) |
|------|-------------|----------------------|
| 600 kW | 600 kW | ~0.01293 |
| 750 kW | 750 kW | ~0.01617 |
| 900 kW | 900 kW | 0.01940 |

Physical simulation time: 300 s per case.
Time-averaging window for spatial profiles: 150–300 s (quasi-steady period).

## Gauge Positions

Five heat-flux gauges and thermocouples on the façade (y = 0, centreline).
Heat-flux gauges are modelled as water-cooled (fixed wall temperature, 25 °C),
consistent with the experimental Gardon/Schmidt–Boelter gauges.

| Gauge | z from floor (m) | Height above window top (m) |
|-------|-----------------|-----------------------------|
| HF1 / TC1 | 1.865 | 0.505 |
| HF2 / TC2 | 2.265 | 0.905 |
| HF3 / TC3 | 2.865 | 1.505 |
| HF4 / TC4 | 3.365 | 2.005 |
| HF5 / TC5 | 3.865 | 2.505 |

Window top is at z = 1.36 m from the floor.

## File Descriptions

| File | Contents |
|------|----------|
| `FM_JIS_Facade_0p5in_{N}kW_devc.csv` | Compartment (inside) HRR time series — fire power N kW |
| `FM_JIS_Facade_0p5in_{N}kW_hrr.csv`  | Total + outside HRR time series — fire power N kW |
| `FM_JIS_Facade_0p5in_line.csv`        | Time-averaged heat flux (total/conv/rad) and gas temperature at 5 gauge heights for all three fire powers |

All CSV files use the MaCFP two-row header format (row 1 = units, row 2 = column names).
Temperature values in `_line.csv` are absolute gas temperature in °C.

## Plots

The script `FM_JIS_Facade_plots.py` generates comparison plots between the
simulation results and experimental data (Sun et al., 2024). To run:

```
python3 FM_JIS_Facade_plots.py
```

This creates four PNG files in `./Plots/`:

| File | Contents |
|------|----------|
| `FM_JIS_Facade_0p5in_HF_profile.png`    | Total heat flux vs height (sim + exp) |
| `FM_JIS_Facade_0p5in_CHF_profile.png`   | Convective heat flux vs height (sim only) |
| `FM_JIS_Facade_0p5in_RHF_profile.png`   | Radiative heat flux vs height (sim only) |
| `FM_JIS_Facade_0p5in_T_Y0_profile.png`  | Gas temperature (thermocouple-type) at X=0, Y=0 vs height — FM gas-phase probes at the façade surface vs experimental thermocouple measurements (Sun 2024) |

An additional file in `./Plots/` was generated directly from the simulation
post-processing and is submitted alongside the CSV data:

| File | Contents |
|------|----------|
| `FM_JIS_Facade_0p5in_flame_shape.png` | Instantaneous temperature field at t = 300 s on the vertical centreplane (Y = 0) for 600/750/900 kW, shown as a scatter plot coloured by T (300–1800 K) with isotherms at 800 K, 1000 K, and 1200 K |

**Coordinate note:** gauge heights in `_line.csv` are in simulation coordinates
(z from floor). The window top is at z = 1.36 m; the script converts to
experimental coordinates (z from window top) automatically.

Requires: Python 3, numpy, pandas, matplotlib.

## Contact

FM Global Research
