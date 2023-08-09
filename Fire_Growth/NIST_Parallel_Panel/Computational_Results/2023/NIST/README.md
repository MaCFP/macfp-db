### Contributor

Name: Kevin McGrattan

Institution: National Institute of Standards and Technology

Country: USA

------------------

### Test case

NIST Parallel Panels -- Two vertical panels lined with black PMMA ignited by a propane burner

------------------

### CFD package

Code: Fire Dynamics Simulator (FDS)

Version: 6.8.0

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 1.2 m by 0.8 m by 4.8 m

Cell size: 2 cm, 1 cm, 0.5 cm

Cell type: Cubes

Total cells: 576000, 4608000, 9312000

Comments: The 2 cm and 1 cm cases used uniform cells throughout. The 0.5 cm case used fine cells between the panels and 1 cm cells outside.

#### Angular space discretization (radiation solver)

Number of solid angles: 104

Comments: This is the default number of solid angles in FDS

------------------

### Initial conditions

Comments: Ambient temperature of 20 °C. 

------------------

### Boundary conditions

Comments: Open (passive) pressure boundaries except at the floor. To simulate the random air movement in the lab, a sinusoidally-varying pressure of 0.02 Pa is applied at the lateral boundaries of the open domain. The period of the fluctuations is 10 s. No measurements were made to confirm these estimates. They are based on comparisons of heat flux measurements from the propane burner to the marinite wall panels. These fluctuations tend to widen the heat flux profile to the panels.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane (burner) and MMA (pyrolyzate)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction: Prescribed, 0.35

Soot model: Fixed soot yield, 0.024

Comments: The soot yield is for propane and based on Tewarson's chapter of the SFPE Handbook

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model, absorption coefficient is 2870 1/m

Material property set: Properties of black PMMA were measured at the U. of Maryland

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

Wall clock time: 2 cm (13:20:00); 1 cm (173:51:00)

Simulation time: 900 s

Number of CPUs (MPI Processes): 96

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 2 cm (0.009 s); 1 cm (0.014 s)

------------------

### Averaging period

2 s

------------------

### Special issues/problems

Grid independence

------------------

### Relevant publications

1. FDS Technical Reference Guide

2. Test Report, to be published.

