### Contributor
Name: Michael Meehan

Institution: Sandia National Laboratories

Country: United States of America

------------------

### Test case

NIST Pool Fires:
- 30 cm methanol
- 100 cm methanol

------------------

### CFD package

Code: Sierra/Fuego

Version: 15.3.5

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:
- 30 cm: 18.6 cm diameter, 200 cm vertical
- 100 cm: 616.0 cm diameter, 800 cm vertical

Cell size:
- 30 cm: 2.0 cm, 1.0 cm, 0.5 cm
- 100 cm: 4.0 cm, 2.0 cm, 1.0 cm

Cell type: unstructured hexes

Total elements:
- 30 cm: 79752, 521560, 3115390
- 100 cm: 528024, 2797765, 8820831

Comments: The cell sizes provided here are roughly the cell sizes above the burner and approximately two diameters downstrean. The grid resolution gradually increases away from the near-field. We also refine the mesh in the vertical direction above to the pool surface.

#### Angular space discretization (radiation solver)
Number of solid angles: 128

------------------

### Initial conditions
Comments: The domain is initially filled with quiestent air at 298 K. 

------------------

### Boundary conditions
Comments: The pool surface is modeled as an inflow boundary condition with a prescribed mass flux of 0.0163 kg/m^2/s of methanol. The surfaces are modeled as isothermal walls at 298 K. The remaining boundary conditions are open to the atmosphere.

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t): Inagaki LES turbulent model with 0.9 for Sc_t and Pr_t.

Combustion model: Strained laminar flamelet model with non-adiabatic defect (radiative losses).

Radiation model: Gray gas model

Radiative fraction: Predicted

Soot model: None

Comments:

------------------

### Discretization methods
Time: Second-order backwards difference

CFL: 0.75

Advection: MUSCL (second order)

Diffusion: Second order central differencing

Pressure-velocity coupling: Low-Mach number approximation

------------------

### Computational Cost (hh:mm:ss)

Wall clock time (hours):
- 30 cm: 
- 100 cm:

Simulation time:
- 30 cm: 
- 100 cm:

Number of CPUs (MPI Processes):
- 30 cm: 
- 100 cm:

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):
- 30 cm: 
- 100 cm:

------------------

### Averaging period

- 30 cm: 
- 100 cm:

------------------

### Special issues/problems

- 30 cm: 
- 100 cm:

------------------

### Relevant publications

1. Hubbard, Joshua A., et al. "Medium-Scale Methanol Pool Fire Model Validation." Journal of Heat Transfer 144.6 (2022): 061303.

