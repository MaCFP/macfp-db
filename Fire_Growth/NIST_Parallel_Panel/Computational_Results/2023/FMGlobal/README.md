### Contributor

Name: Danyal Mohaddes, Ning Ren, Yi Wang

Institution: Factory Mutual Global Research (abbr. 'FMGlobal')

Country: USA

------------------

### Test case

NIST Parallel Panels -- Two vertical panels lined with black PMMA ignited by a propane burner

------------------

### CFD package

Code: FireFOAM

Version: v2012, FM's internal fork

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 6m by 6m by 5.1m

Minimum cell size: 2.54cm, 1.27cm, 0.64cm

Cell type: hexahedrons

Total cells: 105K, 346K, 2.29M

Comments: The base mesh has a resolution of 20.3cm, with two layers of refinement applied progressively in the vicinity of the panels, and a third layer of refinement applied between the panels. The meshes with 1.27cm and 0.64cm minimum cell sizes have additional fourth and fifth layers of refinement applied between the panels, respectively. The mesh between the panels is homogeneous and isotropic. The mesh with 0.64cm minimum cell size was used only for the purpose of a mesh convergence study in the inert wall case, and thus the fifth layer of refinement was applied only from the burner surface to halfway up the panels.

#### Angular space discretization (radiation solver)

Number of solid angles: 64

Comments: 16, 32 and 64 solid angles were considered in the inert case to assess sensitivity. Heat release rate and wall heat flux results were found to be insensitive to this choice. 64 solid angles were used in the presented results.

------------------

### Initial conditions

Comments: Quiescent ambient conditions of 101325Pa and 300K. 

------------------

### Boundary conditions

Comments: Open (passive) pressure boundaries on sides and top. Floor and back-sides of panels are no-slip isothermal at 300K. Propane burner surface has time-varying prescribed mass flow rate from [experiment](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/Burner_HF_Centerline_multi-layer.csv) and is assumed isothermal at 900K. Inner panel surfaces are no-slip with 1D conjugate heat transfer, assuming an adiabatic back boundary.

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): Dynamic Lagrangian turbulence model with 1.0 for both turbulent Schmidt and Prandtl numbers.

Combustion model: 1-step propane-air reaction. PMMA pyrolysate converted to propane gas at point of generation based on ratio of heats of combustion. TCI modeled using eddy dissipation model; EDC constant of 4.0.

Radiation model: Finite-volume, optically-thin with specified radiative fraction.

Radiative fraction: Propane: 0.35, PMMA pyrolysate: 0.32. Global radiative fraction scaled using relative instantaneous mass flow rates of propane and PMMA pyrolysate into the domain.

Soot model: None

------------------

### Pyrolysis Models (include parameters)

Solver: FireFOAM

Radiation properties: constant
- absorptivity = 0.9
- emissivity = 0.85

Material properties:
- density = 998kg/m3
- heat of combustion = 24.2e+6J/kg 

Effective material properties:
- thermal conductivity = 0.223W/m/K
- cp = 3147J/kg/K
- pre-exponential = 1.59e+14 1/s
- activation energy = 1.84e+5J/mol
- heat of pyrolysis = -7.72e+5J/kg
- reaction order = 1.0

Comments: Effective properties optimized from [FM's experimental data](https://github.com/MaCFP/matl-db/tree/master/PMMA/Calibration_Data/FM)

------------------

### Discretization methods

Time: First-order implicit

CFL: 3

Advection: Blended first-order upwind and second-order central difference; blending coefficient of 0.1

Diffusion: Second-order central difference

------------------

### Computational Cost

Wall clock time: 2.54cm (11:53:00), 1.27cm (35:16:00)

Simulation time: 325s

Number of CPUs (MPI Processes): 64

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 2.54cm (0.08), 1.27cm (0.07)

Comments: Above discussion is for PMMA runs.

------------------

### Relevant publications

1. FM's public-facing [fork of FireFOAM](https://github.com/fireFoam-dev/fireFoam-v1912)

