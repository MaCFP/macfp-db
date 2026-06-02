# FM Computational Results - FM Ethylene Burner (MaCFP-4)

## Solver

| Item | Value |
|------|-------|
| Code | fireFoam (OpenFOAM dev) |
| Fuel | C2H4 (ethylene) |
| Case | Normal oxygen concentration condition, 20.9% O2 |
| Nominal HRR | 15 kW |
| Combustion | Eddy Dissipation Model (EDM), single-step C2H4 reaction |
| Turbulence | LES, dynamic Lagrangian sub-grid model |
| Radiation / soot | Laminar smoke point soot model, conditional source term estimation for turbulence interactions |
| Grid | 4 mm in primary flame regions; 2 mm thin layer near burner surface used to trigger stability |

## Case Configuration

| Item | Value |
|------|-------|
| Burner diameter | 0.14 m |
| Burner surface location | z = 0.25 m |
| Fuel | Ethylene, C2H4 |
| Oxygen condition | 20.9% |
| Nominal HRR | 15 kW |

<!-- Radial profile heights are reported as height above the burner surface normalized
by burner diameter, z/D. The corresponding physical z coordinate is
`z = 0.25 m + (z/D) * 0.14 m`. -->

## Data Files

All CSV files use the MaCFP two-row header format:

- Row 1: units
- Row 2: column names
- Rows 3+: data in scientific notation

| File | Contents |
|------|----------|
| `FM_Ethylene_Burner_4mm_hrr.csv` | Time series of total HRR and positive radiative loss, both in kW |
| `FM_Ethylene_Burner_4mm_temperature_profile.csv` | Thermocouple-derived mean and RMS gas temperature profiles by radius and height |
| `FM_Ethylene_Burner_4mm_soot_profile.csv` | Soot volume fraction mean and RMS radial profiles in ppm |
| `FM_Ethylene_Burner_4mm_velocity_profile.csv` | Mean horizontal and vertical velocity radial profiles |

`HRR_rad_loss` is exported as a positive radiative-loss magnitude. The raw
FireFOAM file stores `volIntegrate(Qdot_rad)` with negative sign for loss.

## Experimental Data

The plotting script uses the existing repository experimental data under
`../../../Experimental_Data` relative to this directory. These paths reproduce
the original flat experimental dataset from
`~/notebooks/MaCFP-4/FMburner/Experimental_Data`:

| Repository file | Original flat file / use |
|-----------------|--------------------------|
| `Temperature/Mean_temperature.csv` | `Mean_temperature.csv`, mean temperature profile comparison |
| `FM_Burner_dataset_update_Oct2025/temperature_rms.csv` | `RMS_temperature.csv`, extracted as the 20.9% O2 `T_RMS` profiles |
| `LII/fvmean.csv` | `Mean_SVF.csv`, read after the units row |
| `LII/fvrms.csv` | `RMS_SVF.csv`, read after the units row and restricted to 20.9% O2 columns |
| `FM_Burner_dataset_update_Oct2025/vertical_velocity_mean_20.9_OC.csv` | Mean vertical velocity comparison |
| `FM_Burner_dataset_update_Oct2025/horizontal_velocity_mean_20.9_OC.csv` | Mean horizontal velocity comparison |
| `Temperature/Output_temperature_PDF.csv` | `Output_temperature_PDF.csv`, source experimental data retained for completeness; not used by the plotting script |

## Plots

Run the plotting script from this directory using a Python environment with
numpy, scipy, pandas, and matplotlib. In this workspace, the verified command
is:

```bash
/panfs/lux/miniconda3/envs/sciml-torch/bin/python3 FM_Ethylene_Burner_4mm_plots.py
```

This reads the submitted CSV files listed above and creates these PNG plots in
`./Plots`:

| File | Contents |
|------|----------|
| `FM_Ethylene_Burner_4mm_HRR.png` | Total HRR and radiative-loss time series |
| `FM_Ethylene_Burner_4mm_temperature_profile.png` | Mean and RMS temperature comparisons |
| `FM_Ethylene_Burner_4mm_soot_profile.png` | Mean and RMS soot volume fraction comparisons |
| `FM_Ethylene_Burner_4mm_velocity_profile.png` | Mean vertical and horizontal velocity comparisons |

Requires: Python 3, numpy, scipy, pandas, matplotlib.

## Disclaimer

The soot and radiation models used for this submission are recently developed
and remain under active development. The soot production model is the laminar
smoke point model proposed by M. Delichatsios et al. Turbulence-radiation
interaction is described in the recent work by Lu et al., "A Conditional
Source-term Estimation Approach for Turbulence-Radiation Interaction in Eddy
Dissipation Concept-Based Fire Simulations," accepted to the 41st International
Symposium on Combustion (ISOC). The turbulence-soot interaction model follows
the same principle as the turbulence-radiation interaction treatment and is also
under active development.

These submitted computational results are work in progress and may be updated
or withdrawn later.

## Contact

FM Research
