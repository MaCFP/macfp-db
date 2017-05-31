### Contributor
Name: Randall McDermott

Institution: NIST

Country: USA

------------------

### Test case

McCaffrey Flames: 14 kW, 22 kW, 33 kW, 45 kW, 57 kW
Centerline temperature and vertical velocity

------------------

### CFD package
Code: FDS

Version: FDS6.5.3-1800-gdf9c12f

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:  1.5 m x 1.5 m x 2.1 m

Cell size: DX=1.4 cm

Cell type: uniform cubic

Total cells: 1,620,675

Comments:

DS/DX = [12.4   14.6   17.3   19.6   21.6]

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments:

------------------

### Initial conditions
Comments: random purturbation

------------------

### Boundary conditions
Comments: OPEN external boundaries, prescribed FUEL mass flux for 0.3 m x 0.3 m square pan burner

------------------

### Models (include parameters)
Turbulence model: modified Deardorff (C_DEARDORFF=0.1), SC_T=0.5, PR_T=0.5

Combustion model: EDC (const applied to time scale, C_U=0.4)

Radiation model: Grey gas, discrete ordinates, finite-volume method

Radiative fraction: prescribed, per MaCFP documentation CHI_R=[0.17 0.21 0.25 0.27 0.27]

Soot model: SOOT_YIELD=0

Comments:

------------------

### Discretization methods
Time: RK2

Advection: Superbee flux limiter

Diffusion: Central differencing

Pressure-velocity coupling: Exact projection

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: [4:28:17  5:57:39  5:11:2  6:16:51  7:03:51]

Simulation time: 30 s

Number of cores: 27

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): [0.0089    0.0119    0.0104    0.0126    0.0141]

------------------

### Averaging period

20 s

------------------

### Special issues/problems

I did not have time to explore affect of domain size on plume velocity decay.

------------------

### Relevant publications
1. Pub 1

2. Pub 2
