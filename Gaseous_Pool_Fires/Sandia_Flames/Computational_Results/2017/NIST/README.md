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

Version: FDS6.5.3-229-g743ab74

------------------

### Mesh
Domain: 3 m x 3 m x 4 m

Cell size: 1.5 cm

Cell type: uniform Cartesian

Total cells: 9.4 million

Comments: 16 cores, 50 hrs wall clock time

------------------

### Initial conditions
Comments: small velocity perturbation

------------------

### Boundary conditions
Comments: uniform inlet velocity, OPEN outer boundaries, OPEN coflow area around plate

------------------

### Models (include parameters)
Turbulence model: modified Deardorff (C_DEARDORFF=0.1), SC_T=0.5, PR_T=0.5

Combustion model: EDC (const applied to time scale, C_U=0.4)

Radiation model: Grey gas, 104 solid angles, CHI_R=0.2 (methane)

Soot model: Y_SOOT=0.01 (for methane)

Comments:

------------------

### Discretization
Time: RK2, CFL=0.8-1.0

Advection: velocity: central difference; scalar: Superbee limiter

Diffusion: central

Pressure-velocity coupling: Low-Mach exact projection

------------------

### Averaging period

10 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. FDS Validation Guide
2. FDS Technical Reference Guide

