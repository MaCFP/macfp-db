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

Domain: 2.12 m by 2.12 m by 2.86 m (includes hood)

Cell size: 2.5 cm and 1 cm for UMD props, 2.5 cm for DBI props.

Cell type: Cubes

Total cells: 2.39E6 (1 cm for the fire domain and 2cm for the rest), 1.4E6 (2_5 cm for the entire domain)

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

Radiative fraction: 0.35
Yields: Soot: 0.018, CO_Yield 0.007.

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model in PMMA solid when an absoprtion coeffiicent is specified

Material property set: Properties of black PMMA taken from the various json files at https://github.com/MaCFP/matl-db/tree/master/PMMA/Material_Properties.  

Comments:


------------------

### Discretization methods

Time: Second-order accurate Runge-Kutta

CFL: 1

Advection: Superbee flux limiter

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost (hh:mm:ss)

Wall clock time:  1 cm (667,229.941 s ) 

Simulation time: 200 s 

Number of CPUs (MPI Processes): 2.5 cm (6), 1 cm (6); 

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 1 cm (0.044 s); 

------------------

### Averaging period

0.2 s

------------------

### Special issues/problems

The simulation results including HRR are grid independent based on the two mesh sizes considered.

------------------

### Relevant publications

1. FDS Technical Reference Guide


