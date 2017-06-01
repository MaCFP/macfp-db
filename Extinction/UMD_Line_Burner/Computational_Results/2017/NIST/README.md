
### Contributor
Name: Randall McDermott

Institution: NIST

Country: USA

------------------

### Test cases

1. methane, XO2 = 0.18 (O2 and TC profiles)
2. methane combustion efficiency (ramp XO2)
3. propane combustion efficiency (ramp XO2)

------------------

### CFD package
Code: FDS

Version: FDS6.5.3-1794-g24e4bad

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:

1. 0.85 m x 0.60 m x 1.2 m
2. 1.65 m x 2.00 m x 1.5 m
3. 1.65 m x 2.00 m x 1.5 m

Cell size:

1. 0.3125 cm (uniform)
2. 0.3125 cm (above coflow), 1.25 cm, 2.5 cm
2. 0.3125 cm (above coflow), 1.25 cm, 2.5 cm

Cell type: uniform, cubic

Total cells:

1. 20,054,016 (128 core)
2. 25,475,072 (184 core)
3. 25,475,072 (184 core)

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles:

1. 104 (default)
2. 700
3. 700

Comments:

RTE updated completely once every 0.2 s

------------------

### Initial conditions

small random velocity perturbation

Comments:

------------------

### Boundary conditions
OPEN outer boundaries, prescribed fuel mass flux, prescribed coflow mass flux

Comments:

For cases 2 and 3, the N2 mass flux is ramped to achieve linear variation in XO2 from 0.21 to 0.10.

------------------

### Models (include parameters)

Turbulence model: modified Deardorff (C_DEARDORFF = 0.1), SC_T = 0.5, PR_T = 0.5

Combustion model: EDC with thermal extinction model (CFT from SFPE Handbook), simple AIT threshold for reignition, 0.6 m x 0.15 m x 0.15 m pilot region (AIT = 0 K) above burner

Radiation model: DO-FVM

Radiative fraction: prescribed ramp to match experimental data linked to XO2 DEVC in simulated coflow

Soot model: N/A

Comments:

------------------

### Discretization methods
Time: RK2

Advection: CHARM limiter

Diffusion: central difference

Pressure-velocity coupling: staggered grid, exact projection

------------------

### Computational Cost (hh:mm:ss)
Wall clock time:
1. 33:20:20 (120020 s)
2. 53:39:48 (193188 s)
3. 66:57:25 (241045 s)

Simulation time:
1. 20 s
2. 60 s
3. 60 s

Number of CPUs (MPI Processes):
1. 128
2. 184
3. 184

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):
1. 0.03830
2. 0.02325
3. 0.02902

------------------

### Averaging period
1. 20 s
2. 1 s (eta, qr), 10 s (flame height)
3. 1 s (eta, qr), 10 s (flame height)

------------------

### Special issues/problems

Discovered problem with RTE_SOURCE_CORRECTION for high resolution cases, global CHI_R was overpredicted.  Reverted to using simple CHI_R*Q radiative source term.

Weak approximation of Lf.  Height at 99% HRRPUV was used from a vertical line of point devices in the center of the burner. HRRPUV was not spatially averaged (planar) because this is difficult to do in FDS across mesh boundaries.

------------------

### Relevant publications
1. Pub 1

2. Pub 2
