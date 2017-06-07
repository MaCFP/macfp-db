
### Contributor
Name: John Hewson, Heeseok Koo

Institution: Sandia National Labs

Country: USA

------------------

### Test case

Sandia Flames (Methane tests 14, 24, 17)

------------------

### CFD package
Code: SIERRA/Fuego

Version: 4.44

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: full geometry, 5.8m in diameter, 14m in height

Cell size: 2.5 cm near the pool

Cell type: non-uniform. Hexahedron mostly with tetrahedron where geometry varies rapidly

Total cells: 1,700,000

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 

Comments:

------------------

### Initial conditions
Comments: slow uniform velocity, zero mixture fraction 

------------------

### Boundary conditions
Comments: 

Wall: no-slip, adiabatic

Top: open 

Fuel inlet: mixture fraction = 1, uniform velocity

Air inlet: mixture fraction = 0, uniform velocity

------------------

### Models (include parameters)
Turbulence model: one-equation (subgrid scale kinetic energy) LES 

Combustion model: steady flamelet 

No radiation 

No soot 

Comments:

------------------

### Discretization methods
Time: 

CFL: 0.7-1.0

Advection: central velocity and sub-grid scale kinetic energy. Slight first-order upwinding was added for mixture fraction

Diffusion: central

Pressure-velocity coupling: 

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 96 hours

Simulation time: 70 s

Number of CPUs (MPI Processes): 128 

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.37  (wall clock time in seconds?)

------------------

### Averaging period

30 s (40-70s)

------------------

### Special issues/problems


------------------

### Relevant publications

