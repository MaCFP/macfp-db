### Contributor
Name:Lei Li, Arnaud Trouve  

Institution: University of Maryland, College Park  

Country: USA

------------------

### Test cases

A symmetric corner geometry with propane burner and PMMA panels on both corner faces (full SBI case with condensed fuel), similar to the single burning item test.

------------------

### CFD package
Code:Fire Dynamics Simulator (FDS)  

Version:6.10.1  

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.12 m by 1.12 m by 2.8 m (including hood). Burner surface was at 0 m. Region ranges: XMIN=-0.2 m:XMAX=0.92 m, YMIN=-0.2 m:YMAX=0.92 m, and ZMIN=0.2 m:ZMAX=2.6 m. The grid was uniform mesh with cubic cells having dimension of either 0.5 cm, 1 cm, 2 cm, or 4 cm.

Cell size: 4/2/1/0.5 cm  

Cell type: Cubes 

Total cells: 54,880 (3 meshes)/439,040 (24 meshes) /3,512,320 (128 meshes)/28,098,056 (128 meshes)

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 300

Comments:

------------------

### Initial conditions
Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions
Comments: The floor at z = −0.20 m is FLOOR with concrete; the x- and y-min/max side boundaries are OPEN from z = −0.20 m to 1.80 m. Hood geometry was cuboid and built by solid surfaces. A ceiling exhaust at z = 2.60 m connects to HVAC with a constant volume flow of 0.84 m³/s to an ambient outlet node. Gas-side gauge heat flux uses &PROP ID='HFG' with GAUGE_TEMPERATURE = 18 °C (~291 K); gauge emissivity is using default value (1). 

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane burner.

Radiation model: Finite-volume, gray gas with specified radiative fraction 
Radiative fraction: Propane value of 0.30

Soot model: Propane Soot=0.022, CO=0.005

Comments:

------------------

### Pyrolysis Models (include parameters)
Solver (e.g., GPyro, FDS, ThermaKin; include version):

Radiation absorption model: NA

Material property set: (developed by [institution]; calibration data; calibration method used [e.g., manual iteration, monte carlo sampling, optimization algorithm, PROPTI, Gpyro])


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
Wall clock time: 4/2/1 cm for simulation time 200 s 7/181/3283 core-hour; 0.5 cm for simulation time 44 s 12800 core-hour

Simulation time: 4/2/1 cm for simulation time 200 s; .5 cm for simulation time 44 s

Number of CPUs (MPI Processes): 3/24/128/128 for  4/2/1/0.5 

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):  0.010/0.033/0.076/0.037/ for 4/2/1/0.5

------------------

### Averaging period
Most heat-flux and flow-field outputs are saved as instantaneous time histories every 2 s.
------------------

### Special issues/problems
Grid independence on convective heat flux gauge
------------------

### Relevant publications
1. Pub 1

2. Pub 2

