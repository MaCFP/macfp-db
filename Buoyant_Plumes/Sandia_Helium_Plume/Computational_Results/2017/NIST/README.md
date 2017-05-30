### Contributor
Name: Randall McDermott

Institution: NIST

Country: USA

------------------

### Test case

Sandia Helium Plume

------------------

### CFD package
Code: FDS

Version: FDS6.5.3-1794-g24e4bad

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:  3 m x 3 m x 4 m

Cell size: DX=1.5 cm

Cell type: uniform cubic

Total cells: 9,437,184

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: N/A

Comments:

------------------

### Initial conditions
Comments: random purturbation

------------------

### Boundary conditions
Comments: OPEN external boundaries, prescribed mass flux

------------------

### Models (include parameters)
Turbulence model: modified Deardorff (C_DEARDORFF=0.1), SC_T=0.5, PR_T=0.5

Combustion model: N/A

Radiation model: N/A

Radiative fraction: N/A

Soot model: N/A

Comments:

------------------

### Discretization methods
Time: RK2

Advection: Superbee flux limiter

Diffusion: Central differencing

Pressure-velocity coupling: Exact projection

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: 12:20:32

Simulation time: 20 s

Number of cores: 16

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): 0.0038

------------------

### Averaging period

10 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. Pub 1

2. Pub 2
