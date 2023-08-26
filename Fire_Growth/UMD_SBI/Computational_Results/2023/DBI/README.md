### Contributor

Name: Guoxiang Zhao

Institution: DBI - The Danish Institute of Fire and Security

Country: Denmark

------------------

### Test case

UMD-SBI: Flame spread experiments in a 1.46 m corner wall configuration with MaCFP PMMA (based on the Single Burning Item (SBI) Test, EN13823)

------------------

### CFD package

Code: Fire Dynamics Simulator (FDS)

Version: 6.7.9-0

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 2 m by 2 m by 2.8 m (includes hood) for 1 cm and 2.5 cm grids. 0.5 cm shrunk the hood and domain to 1 m by 1 m x 1.4 m.

Cell size: 2.5 cm and 1 cm for UMD props, 2.5 cm for DBI props.

Cell type: Cubes

Total cells: 1.75E5 (1 mesh), 1.4E6 (16 mesh), 1.12E7 (64 mesh), 2.24E7 (128 mesh)

#### Angular space discretization (radiation solver)

Number of solid angles: 300

------------------

### Initial conditions

Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions

Comments: Between bottom edge of curtain and floor there was Open boundaries. The floor, hood cone, and hood curtains were solid. The top of the hood was a fixed volume flow exhuast of 0.56 m^3/s.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane (burner) and MMA (pyrolyzate)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction: Propane FDS default of 0.29, MMA FDS default of 0.35
Yields: Propane Soot=0.01, CO=0.005 (smoke detection work done by JH for the FPRF suggests Tewarson is high for non-bench scale fires). MMA Soot: 0.018, CO_Yield 0.007.

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model in PMMA solid when an absoprtion coeffiicent is specified

Material property set: Properties of black PMMA taken from the various json files at https://github.com/MaCFP/matl-db/tree/master/PMMA/Material_Properties.  Grid study, blowing, and cone flux cases used the UMD properties.

Comments:

HRR was 

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

Simulation time: 200 s 

Number of CPUs (MPI Processes): 2.5 cm (6), 1 cm (6); 

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 4 cm (0.0024 s); 2 cm (0.014 s); 1 cm (0.044 s); 0.5 cm (0.096 s)

------------------

### Averaging period

0.2 s

------------------

### Special issues/problems

Grid independence

------------------

### Relevant publications

1. FDS Technical Reference Guide


