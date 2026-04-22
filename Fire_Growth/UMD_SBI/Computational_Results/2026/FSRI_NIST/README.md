### Contributor

Name: Jason Floyd

Institution: UL Research Institutes' Fire Safety Research Institute

Country: USA

------------------

### CFD package

Code: Fire Dynamics Simulator (FDS)

Version: pre-release 6.11.0, various git hashes post hash f049aeb

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 2.0 m by 2.0 m by 2.8 m (including hood). Origin was set to the inside of the corner at the top of the burner surface.

Cell size: 4 cm, 2 cm, 1 cm, or 0.5 cm for finest grid.

Cell type: Cubes

Total cells: 4 cm - 1.75E5 cells, 8 meshes; 2 cm - 1.40E6 cells, 16 meshes, 1 cm - 2.25E6 cells, 64 meshes 0.5 cm - 9.68E6 cells, 324 meshes

1 cm case only meshed 1 cm around the corner and was 2 cm elsewhere
0.5 cm case only meshed 1 cm around the corner and stepped to 1 cm and then 2 cm elsewhere

#### Angular space discretization (radiation solver)

Number of solid angles: 400
Path Length: 0.1 m

Comments: 100 and 200 angle simulations run for base case (UMD properties with blowing correction). Optically thin cases run for base case with varying heat transfer coefficient.

------------------

### Initial conditions

Ambient temperature of 20 째C.

------------------

### Boundary conditions

XMIN boundary was concrete floor. Open boundary between the floor and bottom edge of the fire curtain. Fire curtain was solid boundary. Hood geometry was pryamidal and was modeled as solid obstructions. A circular hole was punched through the hood to create and exhaust duct whose end was given a constant extract flow rate of 0.56 m^3/s. Gauge temperature and gauge emissivity was fixed at 291 K and 0.95 (experimental conditions) respectively for all devices measuring gauge heat flux. Blowing correction used for pyrolyzing surfaces.

Comments: Non-blowing simulations run for base case. Fixed heat transfer coeffiicients for PMMA surface of 5, 10, and 20 W/m/K run for base case.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane (burner) and MMA (MMA pyrolyzate having formula C5O2H8, RADCAL ID for MMA, and specific heat capacity of 1.476 kJ/kg/K @ 113.5 째C to 1.903 @ 299.6 째C)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction: Propane value of 0.30, MMA of 0.35
Yields: Propane Soot=0.01, CO=0.005. MMA Soot= 0.018, CO=0.007.

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model in PMMA solid when an absoprtion coeffiicent is specified

Material property set: Properties of [cast black PMMA](https://doi.org/10.1016/j.firesaf.2020.103083) i.e. UMD properties (MaCFP_PMMA_UMD.json)

Comments: Simulations at 1 cm run for BUW, UMETT, DBI, and NIST property sets.  Spyro model run for FSRI (1, 2 and 4 cm), NIST (1 cm), and DBI (1 cm) cone data with 308 째C ignition temperature. 1 cm FSRI case also run with +/- 10 째C ignition temperature and as fixed HRRPUA curves using either the 25, 50, or 75 kW/m� cone data.

------------------

### Discretization methods

Time: Second-order accurate Runge-Kutta

CFL: 1

Advection: CHARM flux limiter (simulation mode set to LES for all simulations)

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 4 cm - 6 hr, 2 cm - 39 hr, 1 cm - 44 hr, 0.5 cm - 111 hr

Simulation time: 200 s

Number of CPUs (MPI Processes): 4 cm (8); 2 cm (16), 1 cm (64); 0.5 cm (324)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 4 cm (0.0053 s); 2 cm (0.014 s); 1 cm (0.020 s); 0.5 cm (0.037 s)

Comment: 1,2 and 4 cm run on Intel Xeon Platimum 8358, 0.5 cm on Intel Xeon Platinum 8168

------------------

### Output

#### HRR

FDS control logic was used to replicate the calorimetry equation used in the experiments with gas concentrations take as the average at the exhaust duct surface with a 1 s exponetial smoothing.  The calorimetry equation used at the NFRL (NIST) was also implemented.

#### Averaging Time

FDS line device outputs used a 10 s window
FDS point device outputs written at 1 s intervals.  The corner radiative flux measurements used a 5 s exponential smoothing.

------------------

### Special issues/problems

Grid independence

------------------

### Relevant publications

1. FDS Technical Reference Guide
