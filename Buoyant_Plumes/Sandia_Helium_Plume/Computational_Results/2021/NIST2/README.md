### Contributor

Name: Randall McDermott (a), Marcos Vanella (a), Glenn Forney (a), Emanuele Gissi (b)

Institution, Country:

(a) National Institute of Standards and Technology (NIST), USA

(b) Corpo Nazionale dei Vigili del Fuoco (CNVVF), Italy

------------------

### Test case

Case 1: Sandia Helium Plume (Unstructured Geometry)

#### Link to Results Presentation

[NIST2 Case 1 Unstructured Results Presentation](https://github.com/MaCFP/macfp-db/releases/download/macfp-2.0/NIST2_Sandia_Helium_Plume.pdf)

------------------

### CFD package

Code: [Fire Dynamics Simulator (FDS)](https://github.com/firemodels/fds)
 
Version: FDS6.7.5-1204-g8eda6af9a

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: Full Sandia FLAME test facility built using [BlenderFDS](https://blenderfds.org/)

Cell size: [1.25, 2.5, 5, 10] cm

Cell type: cubic Cartesian + unstructured cut cell near surfaces

Total cells: See table in Computational Cost section

Comments: The outer mesh and chimney section were maintained at 10 cm resolution.  The resolution in plume region varied as shown in the table.  Note that mesh arrangement was not optimized for scaling.

#### Angular space discretization (radiation solver)

Number of solid angles: NA

Comments:

------------------

### Initial conditions

Comments: small, divergence free random velocity fluctuations

------------------

### Boundary conditions

Plume source: constant mass flux for helium mixture  

Air source: constant 0.3 m/s per Tieszen et al. 1998

OPEN outflow conditions  (outlet of chimney at zmax)

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

Wall clock time:

Simulation time:

Number of CPUs (MPI Processes):

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (hh:mm:ss) | CPU Cost |
| -------:| ----------: | :-------- | :----------- | -------------: | :------------ | :------- |
| 10      | 409600      | 100       | 30           | 677            | 00:11:17      | 0.00551  |
| 5       | 753664      | 100       | 30           | 4770           | 01:19:30      | 0.0211   |
| 2.5     | 3506176     | 184       | 30           | 11968          | 03:19:28      | 0.0209   |
| 1.25    | 25526272    | 184       | 30           | 160343         | 20:32:23      | 0.0385   |

------------------

### Averaging period

Last 20 s

------------------

### Special issues/problems

In the unstructured geometry cases the plume source was inset by 5 cm to mimic the honeycomb depth of the FLAME facility. However, no attempt was made to model the honeycomb as a porous medium.

------------------

### Relevant publications

1. [FDS Technical Reference Guide](https://github.com/firemodels/fds/releases)

2. [FDS Validation Guide](https://github.com/firemodels/fds/releases)

