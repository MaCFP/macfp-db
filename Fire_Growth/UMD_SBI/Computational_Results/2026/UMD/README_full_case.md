### Contributor
Name:Lei Li, Arnaud Trouve  

Institution: University of Maryland, College Park  

Country: USA

------------------

### Test case
A symmetric corner geometry with a propane burner and PMMA panels on both corner faces (full SBI case with condensed fuel), similar to the single burning item test. Input decks: `UMD_SBI_mesh_sensitivity_study/UMD_SBI_full_case/{4cm,2cm,1cm,5mm_v1}/` (FDS 6.10.1, LES).
------------------

### CFD package
Code:Fire Dynamics Simulator (FDS)  

Version:6.10.1  

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.12 m by 1.12 m by 2.8 m (including hood). Burner surface was at 0 m. Region ranges: XMIN=-0.2 m:XMAX=0.92 m, YMIN=-0.2 m:YMAX=0.92 m, and ZMIN=0.2 m:ZMAX=2.6 m. The grid was uniform mesh with cubic cells having dimension of either 0.5 cm, 1 cm, 2 cm, or 4 cm (same domain topology as the pure gas burner mesh study).

Cell size: 4/2/1/0.5 cm  

Cell type: Cubes 

Total cells: 54,880 (3 meshes) / 439,040 (24 meshes) / 3,512,320 (128 meshes) / 28,098,560 (128 meshes, 56×56×70 cells per block at 5 mm)

Comments: 4 cm uses three fixed meshes (28×28×23/24). Finer cases use `&MULT` blocks (2 cm: 2×2×4 + hood; 1 cm and 5 mm: 4×4×8).

#### Angular space discretization (radiation solver)
Number of solid angles: 300

Comments:

------------------

### Initial conditions
Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions
Comments: The floor at z = −0.20 m is FLOOR with concrete; the x- and y-min/max side boundaries are OPEN from z = −0.20 m to 1.80 m. Hood geometry was cuboid and built by solid surfaces. A ceiling exhaust at z = 2.60 m connects to HVAC with a constant volume flow of 0.84 m³/s to an ambient outlet node. Corner PMMA faces use `SURF_ID='PMMA F'` with `BLOWING=T` (5.8 mm PMMA over 12.7 mm MARINITE). Gas-side gauge heat flux uses `&PROP ID='HFG'` with `GAUGE_TEMPERATURE = 18 °C` (~291 K); gauge emissivity uses the default value (1).

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: Two mixing-controlled reactions—propane burner (`&REAC ID='PROPANE'`, soot yield 0.01, CO yield 0.005, radiative fraction 0.30) and MMA from PMMA pyrolysis (`&REAC FUEL='MMA'`, soot yield 0.022, CO yield 0.01, radiative fraction 0.31, heat of combustion 24,410 kJ/kg).

Radiation model: Finite-volume, gray gas with specified radiative fraction per fuel.

Radiative fraction: 0.30 (propane), 0.31 (MMA)

Soot model: As listed above for each fuel.

Comments:

------------------

### Pyrolysis Models (include parameters)
Solver (e.g., GPyro, FDS, ThermaKin; include version): FDS 6.10.1 solid-phase pyrolysis (`&MATL`, `&SURF`), two-step PMMA model after Fiola et al. (2021):

- `PMMA_melt` → 0.98 `PMMA_int` + 0.02 MMA(g): A = 4.95×10¹⁶ s⁻¹, E = 164 kJ/mol, ΔH = 5 kJ/kg  
- `PMMA_int` → 0.002 `PMMA_char` + 0.998 MMA(g): A = 1.35×10¹¹ s⁻¹, E = 164 kJ/mol, ΔH = 817 kJ/kg  

Material properties: ρ = 1210 kg/m³; conductivity and specific heat ramps (`PMMA K`, `PMMA C`); absorption coefficient 2870 m⁻¹; emissivity 0.96. Panel assembly: 5.8 mm PMMA (`PMMA_melt`) + 12.7 mm MARINITE backing on `PMMA F` surfaces.

Radiation absorption model: Solid absorption coefficient 2870 m⁻¹ (PMMA species); gas MMA uses `RADCAL_ID='MMA'`.

Material property set: Fiola et al. (2021) two-step PMMA kinetics and temperature-dependent transport; MARINITE and hood solids as in the full-case FDS decks.

Comments: Pyrolysis gas (MMA, C₅H₈O₂) enters the gas phase and burns with the parameters above; burner propane provides the imposed gas-burner heat release.

------------------

### Discretization methods
Time: Second-order accurate Runge-Kutta

CFL: 1

Advection: Superbee flux limiter

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 4/2/1/0.5 cm for simulation time 200 s: 04:14:01 / 11:21:32 / 40:41:14 / 24:14:26 (Zaratan; 4 cm scaled from completed 1200 s archive run)

Simulation time: 200 s for all full-case mesh levels listed above (`T_END=200`)

Number of CPUs (MPI Processes): 3 / 24 / 128 / 128 for 4 / 2 / 1 / 0.5 cm

CPU cost (Number of CPUs × Wall clock time / Simulation time / Total cells): 0.004 / 0.011 / 0.267 / 0.020 for 4 / 2 / 1 / 0.5 cm

Core-hour (MPI × wall-clock hours): ~13 / ~273 / ~5,207 / ~3,100 for 4 / 2 / 1 / 0.5 cm at 200 s simulation time

Comments: Costs exceed the pure gas burner cases at the same resolution because of solid pyrolysis, blowing surfaces, and dual-fuel combustion. The 4 cm wall time is estimated as (200/1200) × the 1200 s `1200s/4cm` run; other meshes use completed 200 s `.out` logs in `UMD_SBI_full_case/{2cm,1cm,5mm_v1}/`.

------------------

### Averaging period
Most heat-flux and flow-field outputs are saved as instantaneous time histories every 2 s. Post-processed HRRPUV and flame-height comparisons use time averages with t ≥ 10 s through the last available slice per mesh (see `thirdrun_trouve/hrrpuv_plot_time.py`).
------------------

### Special issues/problems
Grid independence on convective heat flux gauge and PMMA-panel heat flux. The 5 mm case stops earlier in wall time than coarser meshes at the same `T_END`; some MaCFP exports use the extended `1200s/4cm` device file when the local 4 cm 200 s run is incomplete.
------------------

### Relevant publications
1. Fiola, B., et al. (2021)—PMMA pyrolysis model reference in FDS decks.

2. Pub 2
