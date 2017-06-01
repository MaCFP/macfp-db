
### Contributor
Name: Randall McDermott

Institution: NIST

Country: USA

------------------

### Test case

Sandia Flames (Test 14, 24, 17, 35)

------------------

### CFD package
Code: FDS

Version: FDS6.5.3-1794-g24e4bad

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 3 m x 3 m x 4 m

Cell size: 1.5 cm

Cell type: uniform cubic

Total cells: 9,437,184

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments:

------------------

### Initial conditions
Comments: small random velocity perturbation

------------------

### Boundary conditions
Comments: OPEN external boundaries, prescribed mass flux at burner, specified temperature of plate per experimental documentation

------------------

### Models (include parameters)
modified Deardorff (C_DEARDORFF=0.1), SC_T=0.5, PR_T=0.5

Combustion model: EDC (const applied to time scale, C_U=0.4)

Radiation model: DO-FVM

Radiative fraction: specified 0.2 for methane, 0.1 for hyrogen

Soot model: SOOT_YIELD=0.01 for methane, 0 for hydrogen

Comments:

------------------

### Discretization methods
Time: RK2

CFL: 0.8 - 1.0

Advection: central velocity, Superbee scalars

Diffusion: central

Pressure-velocity coupling: staggered grid, exact projection

------------------

### Computational Cost (hh:mm:ss)
Wall clock time:
Test 14: 159073 s (44:11:13)
Test 24: 165981 s (46:06:21)
Test 17: 174046 s (48:20:46)
Test 35: 106834 s (29:40:34) (current case had numerical instability at 10.06 s)

Simulation time: 20 s

Number of CPUs (MPI Processes): 16

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):
Test 14: 0.0135
Test 24: 0.0141
Test 17: 0.0148
Test 35: 0.0180

------------------

### Averaging period

------------------

### Special issues/problems

Recent code changes seem to have created an instability in the H2 case.  No time to rerun this before the meeting.

------------------

### Relevant publications
1. Pub 1

2. Pub 2