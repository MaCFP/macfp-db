### Contributor

Name: Dushyant M. Chaudhari

Institution: Fire Safety Research Institute

Country: USA

------------------

### Test case

A symmetric corner geometry with cast black PMMA ignited by propane sandbox burner, similar to the single burning item test.

------------------

### CFD package

Code: Fire Dynamics Simulator (FDS)

Version: 6.8.0

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 2.08 m by 2.08 m by 2.88 m (including hood). Burner surface was at 0.16 m. Region of XMIN=-0.12 m:XMAX=0.68 m,  YMIN=-0.12 m:YMAX=0.68 m, and ZMIN=0.08 m:ZMAX=1.68 m was finest grid. Finest grid was uniform mesh with cubic cells having dimension of either 0.5 cm, 1 cm, 2 cm, or 4 cm. The rest of the domain had cubic cells with dimension of 4 cm.

Cell size: 4 cm, 2 cm, 1 cm, or 0.5 cm for finest grid. 

Cell type: Cubes

Total cells: 1.804E5 (16 meshes: 4cm finest grid), 2.92E5 (30 meshes: 2cm finest grid), 1.19E6 (30 meshes: 1cm finest grid), 8.36E6 (126 meshes: 0.5 cm finest rid)

#### Angular space discretization (radiation solver)

Number of solid angles: 400
Path Length: 0.5 m

------------------

### Initial conditions

Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions

Comments: XMIN boundary was concrete floor. Open boundary between the floor and bottom edge of the fire curtain. Fire curtain was solid boundary. Hood geometry was conical and was modeled as solid obstructions. X:{0.28,0.56} m, Y:{0.08,0.36} m, Z:{2.88,2.88} m was the exhaust stipulated to extract constant volume of 0.56 m^3/s using 20 m long HVAC duct venting to the ambient. Gauge temperature and gauge emissivity was fixed at 291 K and 0.95 (experimental conditions) respectively for all devices measuring gauge heat flux.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane (burner) and PMMAG (PMMA pyrolyzate having formula C5O2H8, RADCAL ID for MMA, and specific heat capacity of 2 kJ/kg/K)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction: Propane value of 0.30, MMA of 0.35
Yields: Propane Soot=0.024, CO=0.005 (Tewarson's SFPE fire protection handbook chapter). PMMAG Soot= 0.015, CO=0.005 (Tewarson's SFPE fire protection handbook chapter).

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model in PMMA solid when an absoprtion coeffiicent is specified

Material property set: Properties of [cast black PMMA](https://doi.org/10.1016/j.firesaf.2020.103083) i.e. UMD properties (MaCFP_PMMA_UMD.json)

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

Wall clock time: 4 cm (11,966 s [3.3 hr]) 2 cm (27,915 s [7.8 hr]]); 1 cm (152,888 s [42.5 hr]) 0.5 cm (486,207 s [135.1 hr])

Simulation time: 200 s

Number of CPUs (MPI Processes): 4 cm (16); 2 cm (30), 1 cm (30); 0.5 cm (126)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 4 cm (0.0053 s); 2 cm (0.014 s); 1 cm (0.020 s); 0.5 cm (0.037 s)

------------------

### Averaging period

0.2 s

------------------

### Special issues/problems

Grid independence

------------------

### Relevant publications

1. FDS Technical Reference Guide
