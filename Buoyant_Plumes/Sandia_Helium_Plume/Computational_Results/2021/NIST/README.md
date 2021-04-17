### Contributor
Name: Randall McDermott, Kevin McGrattan

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test case

Case 1: Sandia Helium Plume (Cartesian Geometry)

#### Link to Results Presentation

[NIST Case 1 Cartesian Results Presentation](https://github.com/MaCFP/macfp-db/releases/download/macfp-2.0/NIST_Sandia_Helium_Plume.pdf)

------------------

### CFD package

Code: [Fire Dynamics Simulator (FDS)](https://github.com/firemodels/fds)

Version: FDS6.7.5-820-g2de95544d-master

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain:  6 m x 6 m x 4 m  

Cell size: [1.5, 3, 6, 10, 20] cm

Cell type: cubic

Total cells: see Computational Cost

Comments:

#### Angular space discretization (radiation solver)

Number of solid angles: NA

Comments:

------------------

### Initial conditions

Comments: small, divergence free random velocity fluctuations

------------------

### Boundary conditions

Plume source: constant mass flux for helium mixture  

OPEN inflow and outflow conditions  (zmin and outlet chimney at zmax)

Constant temperature and loglaw wall functions on sides and top of the domain

------------------

### Models (include parameters)

Turbulence model: Modified Deardorff (algebraic k_sgs), C_DEARDORFF=0.1, SC_TURB=0.5, PR_TURB=0.5

Combustion model: NA

Radiation model: NA

Radiative fraction: (predicted or prescribed; if prescribed, what value)

Soot model: NA

Comments: Diffusion coefficient for helium + acetone mixture in nitrogen computed from molecular theory (see [1])

------------------

### Discretization methods

Time: RK2 (fully explicit)

CFL: 0.8-1.0

Advection: CHARM flux limiter (2nd order)

Diffusion: Central (2nd order)

Pressure-velocity coupling: Projection method

------------------

### Computational Cost (hh:mm:ss)

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :------------ | :------- |
| 20      | 18000       | 1         | 20           | 63.5           | 00:01:04      | 0.000176 |
| 10      | 144000      | 64        | 20           | 60.4           | 00:01:01      | 0.00134  |
| 6       | 589824      | 64        | 20           | 316.0          | 00:05:16      | 0.00171  |
| 3       | 1622016     | 64        | 20           | 4136.          | 01:08:56      | 0.00816  |
| 1.5     | 9879552     | 64        | 20           | 67110          | 18:38:30      | 0.0217   |

Wall clock time: see table above

Simulation time: see table above

Number of CPUs (MPI Processes): see table above

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): see table above

Comments: Load imbalance increased as the resolution increased because the same mesh arrangement was kept the same while increasing resolution of the central core meshes around the plume.  This mesh arrangement is not useful for assessing scalability.

------------------

### Averaging period

Last 10 s

------------------

### Special issues/problems

------------------

### Relevant publications

1. [FDS Technical Reference Guide](https://github.com/firemodels/fds/releases)

2. [FDS Validation Guide](https://github.com/firemodels/fds/releases)

