
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
Domain: 2.9 m (radius) x 10 m (height)

Cell size: 4 cm

Cell type: hexahedron, non-uniform

Total cells: 230,000

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 

Comments:

------------------

### Initial conditions
Comments: slow uniform velocity, zero mixture fraction 

------------------

### Boundary conditions
Comments: 'drag source' was added near the top exit plane to avoid boundary instabilities

Wall: no-slip, adiabatic

Top: open 

Inlet: mixture fraction = 1, uniform velocity

Coflow: mixture fraction = 0, uniform velocity that reflects the area difference between coflow and air ring

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
Wall clock time: 6 hours

Simulation time: 40 s

Number of CPUs (MPI Processes): 64 

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.15  (wall clock time in seconds?)

------------------

### Averaging period

20 s (20-40s)

------------------

### Special issues/problems


------------------

### Relevant publications

