### Contributor
Name: Lei Li, Arnaud Trouve  

Institution: University of Maryland, College Park  

Country: USA

------------------

### Test cases

A symmetric corner geometry with propane burner and PMMA panels on both corner faces (full SBI case with condensed fuel), similar to the single burning item test.

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS)  

Version: 6.10.1  

Simulation mode: LES (`&MISC SIMULATION_MODE='LES'`)

------------------

### Resolution

#### Computational domain (flow solver)

Uniform cubic cells over a 1.12 m × 1.12 m × 2.8 m domain (including hood). Burner surface at *z* = 0 m. Domain limits: *x*, *y* ∈ [−0.20, 0.92] m; *z* ∈ [−0.20, 2.60] m.

Cell type: cubes (aspect ratio 1.0 on all meshes).

#### Pure gas burner — mesh summary

Source decks: `Output/UMC_SBI_without_PMMA/UMD_SBI_*_pure_gasburner.fds`

| Cell size | Δ*x* = Δ*y* = Δ*z* (m) | MPI processes | FDS meshes | Total cells | *T*<sub>end</sub> (s) | Wall clock (h) | FDS input file |
|-----------|-------------------------|---------------|------------|-------------|----------------------|----------------|----------------|
| 4 cm | 0.040 | 3 | 3 | 54,880 | 200 | 2.5 | `UMD_SBI_4_cm_pure_gasburner.fds` |
| 2 cm | 0.020 | 24 | 24 | 439,040 | 200 | 7.6 | `UMD_SBI_2_cm_pure_gasburner.fds` |
| 1 cm | 0.010 | 128 | 128 | 3,512,320 | 184 | 25.7 | `UMD_SBI_1_cm_pure_gasburner.fds` |
| 0.5 cm | 0.005 | 128 | 128 | 28,098,560 | 108 | — (in progress) | `UMD_SBI_5_mm_pure_gasburner.fds` |

Notes:
- 4 cm mesh uses three explicit `&MESH` blocks (`IJK = 28 × 28 × 23/24`).
- 2 cm mesh uses 24 meshes (`MULT M`: 2×2×4 = 16; `MULT M1`: 2×2×2 = 8).
- 1 cm and 0.5 cm meshes use `MULT M` with 4×4×8 = 128 copies of a 0.28 m × 0.28 m × 0.35 m block (`IJK = 28 × 28 × 35` for 1 cm; `IJK = 56 × 56 × 70` for 0.5 cm).
- Surface-integrated gauge / radiometer / convective fluxes for the pure gas burner are taken on the **y = 0** PMMA face (`GHF tot/rad/con y0` in `*_devc.csv`).

#### Full case (PMMA pyrolysis) — mesh summary

Source decks: `Output/UMD_SBI_with_PMMA/UMD_SBI_full_case_*.fds`

| Cell size | Δ*x* = Δ*y* = Δ*z* (m) | MPI processes | FDS meshes | Total cells | *T*<sub>end</sub> (s) | Wall clock (h) | FDS input file |
|-----------|-------------------------|---------------|------------|-------------|----------------------|----------------|----------------|
| 4 cm | 0.040 | 3 | 3 | 54,880 | 1200 | 25.4 | `UMD_SBI_full_case_4_cm.fds` |
| 2 cm | 0.020 | 24 | 24 | 439,040 | 200 | 11.4 | `UMD_SBI_full_case_2_cm.fds` |
| 1 cm | 0.010 | 128 | 128 | 3,512,320 | 200 | 40.7 | `UMD_SBI_full_case_1_cm.fds` |
| 0.5 cm | 0.005 | 1280 | 1280 | 28,098,560 | 200 | 122.5 | `UMD_SBI_full_case_0p5_cm.fds` |

Notes:
- Mesh layout matches the pure gas burner cases at each resolution; the 0.5 cm full-case deck uses 1280 meshes (32×4×10) with a 7×56×56 `IJK` base block.
- Panel heat-flux integrals for the full case are taken on the **x = 0** PMMA face (`GHF tot/rad/conv x0` in `*_devc.csv`).
- MaCFP comparison plots for HRR and GHF use 0–200 s; the 4 cm full-case run extends to 1200 s in the archived `*_devc.csv`.

#### Angular space discretization (radiation solver)

Number of solid angles: 300

Comments: Solid-angle sensitivity study indicated 200 angles were sufficient for the pure gas burner; 300 angles are used in the archived full-case decks.

------------------

### Initial conditions
Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions
Comments: The floor at *z* = −0.20 m is FLOOR with concrete; the *x*- and *y*-min/max side boundaries are OPEN from *z* = −0.20 m to 1.80 m. Hood geometry was cuboid and built by solid surfaces. A ceiling exhaust at *z* = 2.60 m connects to HVAC with a constant volume flow of 0.84 m³/s to an ambient outlet node. Gas-side gauge heat flux uses `&PROP ID='HFG'` with `GAUGE_TEMPERATURE = 18` °C (~291 K); gauge emissivity uses the default value (1).

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reaction for propane burner.

Radiation model: Finite-volume, gray gas with specified radiative fraction  
Radiative fraction: Propane value of 0.30

Soot model: Propane Soot = 0.022, CO = 0.005

Comments:

------------------

### Pyrolysis Models (include parameters)
Solver: FDS two-step PMMA pyrolysis (full case only; Fiola et al. 2021 property set)

Radiation absorption model: NA

Material property set: UMD / Fiola et al. calibration (full case); inert PMMA thermal properties only (pure gas burner)

Comments: Pure gas burner cases disable MMA combustion and pyrolysis; PMMA panels are inert solids.

------------------

### Discretization methods
Time: Second-order accurate Runge-Kutta

CFL: 1

Advection: Superbee flux limiter

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost

Values below are taken from the archived FDS `.out` and `*_devc.csv` files in `Output/`.

**CPU cost** (dimensionless):

\[
\text{CPU cost} = \frac{N_{\mathrm{CPUs}} \times t_{\mathrm{wall}}}{t_{\mathrm{sim}} \times N_{\mathrm{cells}}}
\]

where \(t_{\mathrm{wall}}\) is total elapsed wall-clock time (s) from the `.out` file, \(t_{\mathrm{sim}}\) is the simulated time reached (s), and \(N_{\mathrm{cells}}\) is the total number of grid cells.

#### Pure gas burner

| Cell size | MPI processes | Wall clock (s) | Wall clock (h) | Simulation time (s) | Total cells | Core-hours | CPU cost |
|-----------|---------------|----------------|----------------|---------------------|-------------|------------|----------|
| 4 cm | 3 | 9,142 | 2.54 | 200 | 54,880 | 7.6 | **0.0025** |
| 2 cm | 24 | 27,244 | 7.57 | 200 | 439,040 | 181 | **0.0074** |
| 1 cm | 128 | 92,348 | 25.7 | 184 | 3,512,320 | 3,283 | **0.0183** |
| 0.5 cm | 128 | — | — | 108 | 28,098,560 | — | — |

The 0.5 cm pure gas burner run in `Output/UMC_SBI_without_PMMA/` had not finished when archived (no `Total Elapsed Wall Clock Time` in the `.out` file; simulation stopped at *t* ≈ 108 s after a restart).

#### Full case (PMMA pyrolysis)

| Cell size | MPI processes | Wall clock (s) | Wall clock (h) | Simulation time (s) | Total cells | Core-hours | CPU cost |
|-----------|---------------|----------------|----------------|---------------------|-------------|------------|----------|
| 4 cm | 3 | 91,447 | 25.4 | 1,200 | 54,880 | 76 | **0.0042** |
| 2 cm | 24 | 40,892 | 11.4 | 200 | 439,040 | 273 | **0.0112** |
| 1 cm | 128 | 146,474 | 40.7 | 200 | 3,512,320 | 5,206 | **0.0267** |
| 0.5 cm | 1,280 | 440,875 | 122.5 | 200 | 28,098,560 | 156,800 | **0.1004** |

#### CPU cost summary (all 8 meshes)

| | 4 cm | 2 cm | 1 cm | 0.5 cm |
|---|:---:|:---:|:---:|:---:|
| **Pure gas burner** | 0.0025 | 0.0074 | 0.0183 | — |
| **Full case** | 0.0042 | 0.0112 | 0.0267 | 0.1004 |

CPU cost increases with mesh refinement for both cases. The full case is more expensive than the pure gas burner at the same resolution (e.g. 0.0042 vs 0.0025 at 4 cm), reflecting PMMA pyrolysis, additional chemistry, and longer 4 cm simulation time (1,200 s vs 200 s).

------------------

### Averaging period
Most heat-flux and flow-field outputs are saved as instantaneous time histories every 2 s.

------------------

### Special issues/problems
Grid independence on convective heat flux gauge.

------------------

### Relevant publications
1. Pub 1

2. Pub 2
