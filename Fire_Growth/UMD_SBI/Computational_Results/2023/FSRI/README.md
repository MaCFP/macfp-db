### Contributor

Name: Jason Floyd

Institution: Fire Safety Research Institute

Country: USA

------------------

### Test case

SBI -- Two vertical panels in a corner lined with black PMMA ignited by a propane burner

------------------

### CFD package

Code: Fire Dynamics Simulator (FDS)

Version: 6.8.0

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 2 m by 2 m by 2.8 m (includes hood) for 1,2, and 4 cm grids. 0.5 cm shrunk the hood and domain to 1 m by 1 m x 1.4 m.

Cell size: 4 cm, 2 cm, 1 cm, 0.5 cm for UMD props, 2 cm for UMB props with cone heat flux or blowing, 2 and 1 cm for selected other property sets

Cell type: Cubes

Total cells: 1.75E5 (1 mesh), 1.4E6 (16 mesh), 1.12E7 (64 mesh), 2.24E7 (128 mesh)

#### Angular space discretization (radiation solver)

Number of solid angles: 300

------------------

### Initial conditions

Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions

Comments: Between bottom edge of curtain andf floor there was Open (passive) pressure boundaries. The floor, hood cone, and hood curtains were solid. The top of the hood was a fixed volume flow exhuast of 0.56 m^3/s using FDS HVAC.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane (burner) and MMA (pyrolyzate)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction: Propane FDS default of 0.29, MMA FDS default of 0.35
Radiation pathlength: 10 cm
Yields: Propane Soot=0.01, CO=0.005 (smoke detection work done by JH for the FPRF suggests Tewarson is high for non-bench scale fires). MMA Soot: 0.018, CO_Yield 0.007 (from https://doi.org/10.3390/app11135942).

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model in PMMA solid when an absoprtion coeffiicent is specified

Material property set: Properties of black PMMA taken from the various json files at https://github.com/MaCFP/matl-db/tree/master/PMMA/Material_Properties.  Grid study, blowing, and cone flux cases used the UMD properties.

FDS STRETCH_FACTOR set to 1 for wall cells with PMMA. This results in unform 0.34 mm cells for PMMA (16 cells) and 0.385 mm cells for the MARINITE layer (34 cells).

Comments:

HRR was computed using gas concentrations in the hood exhaust duct and the formula in https://doi.org/10.1016/j.polymdegradstab.2020.109433

------------------

### Discretization methods

Time: Second-order accurate Runge-Kutta

CFL: 1

Advection: Superbee flux limiter

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 4 cm (84,728 s [23.54 hr]) 2 cm (245,260 s [68.12 hr]]); 1 cm (1,541,700 s [428.25 hr]) 0.5 cm (3347800 s [929.94 hr] reduced domain size)

Simulation time: 200 s (0.5 cm was terminated due to HPC maintenace at 198.57 s)

Number of CPUs (MPI Processes): 4 cm (1); 2 cm (16), 1 cm (64); 0.5 cm (128)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 4 cm (0.0024 s); 2 cm (0.014 s); 1 cm (0.044 s); 0.5 cm (0.096 s)

------------------

### Averaging period

2 s for profiles
HRR and point heat flux gauge output 0.2 s but Savgol filter applied for plotting.

------------------

### Special issues/problems

Grid independence

------------------

### Relevant publications

1. FDS Technical Reference Guide

2. Test Report, to be published.

