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

Comments: Open (passive) pressure boundaries except at the floor. To simulate the random air movement in the lab, a sinusoidally-varying pressure of 0.05 Pa is applied at the lateral boundaries of the open domain. The period of the fluctuations is 10 s. No measurements were made to confirm these estimates. These fluctuations tend to widen the heat flux profile to the panels, but even with this fluctuation, the heat flux profile is still narrower than that which was measured.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step EDC mixing-controlled reactions of propane (burner) and MMA (pyrolyzate)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction: Prescribed, 0.29 for propane; 0.31 for PMMA (SFPE Handbook, 4th ed., Table 3-4.16)

Soot model: Fixed soot yield, 0.024 for propane; 0.022 for PMMA (SFPE Handbook, 4th ed., Table 3-4.16)

Comments: The radiative fractions and species yields are taken from Tewarson's chapter of the 4th SFPE Handbook

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model, absorption coefficient is 2870 1/m

Material property set: Properties of black PMMA were measured at the U. of Maryland

Comments:

------------------

### Discretization methods

Time: Second-order accurate Runge-Kutta

CFL: 1.0

Advection: Superbee flux limiter

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost

Wall clock time: 2 cm 11.25 h; 1 cm 146 h; 5 mm 236 h (Intel Xeon CPU E5-2630 v2 @ 2.60 GHz)

Simulation time: 600 s

Number of CPUs (MPI Processes): 96 for 2 cm and 1 cm cases; 320 for 5 mm case

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 2 cm (0.011 s); 1 cm (0.018 s); 5 mm (0.049 s)

------------------

### Averaging period

2 s

------------------

### Special issues/problems

1. Grid independence -- heat flux to surface over-predicted by fine grids.

2. Burner cannot be turned off as it was in the experiment. In the simulation, the propane burner's HRR is reduced by half whereas in the experiment the burner is turned off.


------------------

### Relevant publications

1. FDS Technical Reference Guide

2. Test Report, to be published.

