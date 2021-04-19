
### Contributor
Name: Kevin McGrattan, Randy McDermott, Jason Floyd

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test case

Case 5: Ethylene Burner

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS)

Version: FDS6.7.5-1198-g0f426abb6-master

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.22 m by 1.22 m by 1.2 m

Cell size: 5 mm, 1 cm, 2 cm

Cell type: Cubes

Total cells: 5 mm case: 2211840; 1 cm case: 276480; 2 cm case: 34560

Comments: 64 meshes span the domain, with fine cells concentrated over the plume region

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments: Default FDS radiation solver

------------------

### Initial conditions
Comments: All flow variables are originally ambient and then ramped up in approximately 1 s

------------------

### Boundary conditions
Comments: Solid walls; open top; forced flow at floor

------------------

### Models (include parameters)
Turbulence model: Deardoff (algebraic k_sgs); Sc_t=0.5; Pr_t=0.5

Combustion model: Two-step fast-fast serial reactions

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: Predicted based on RadCal tabulated absorption coefficients

Soot model: Soot and CO are the products of the first reaction step, with 60% of the carbon in the fuel converted to CO, 40% to soot. CO and Soot then oxidize to carbon dioxide based on availability of O2 model.

Comments:

------------------

### Discretization methods
Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM Flux Limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: Fine case: 10.9 h

Simulation time: 20 s

Number of CPUs (MPI Processes): 64

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.057

------------------

### Averaging period

------------------

### Special issues/problems

------------------

### Relevant publications
1. FDS Technical Reference Guide

2. Pub 2

