
### Contributor
Name: Shahrooz Motaghian and Tarek Beji

Institution: Ghent University

Country: Belgium

------------------

### Test case

FM-burner: ethylene flames

------------------

### CFD package
Code: OpenFOAM

Solver: FireFOAM

Version: v2006

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: Cylindrical with D=1.22m and height=1.8

The burner is located 36 cm above the bottom boundary (the oxidizer inlet boundary).

Mesh: Uniform sizing for r in [0-6.85cm] and z in [0-50cm] (covering the flaming region). 

The grid becomes coarser, moving toward side and top boundaries.

z=0 and r=0 correspond to the burner surface level and center of the burner, respectively.

Three grids are used in the simulations with the following uniform grid sizes in the flaming region:

The coarse grid: 0.7cm

The medium grid: 0.5cm

The fine grid: 0.25cm

Cell type: hexahedra

Comments:

#### Angular space discretization (radiation solver)

Number of solid angles: 160

Comments: 

------------------

### Initial conditions
Comments:

Temperature: 298 K

Pressure: 101325 Pa

Velocity: 0 m/s

------------------

### Boundary conditions
Comments:

Side boundaries: adiabatic wall 

Fuel inlet: fixed flow rate (diffusive and convective) with fuel temperature of 353K

Oxidizer inlet (bottom): Fixed velocity and mass fraction of oxygen and nitrogen

Top Boundary: Open 

------------------

### Models (include parameters)
Turbulence model: Density variable dynamic k-equation  model with dynamic calculation of Pr_t.

Sc_t=1.0

Combustion model: EDM - constant Delta^2/C_EDM between grids

delta: the average cell size in the flaming region

Radiation model:

RTE solver: Finite volume discrete ordinate method

Radiative properties model (gaseous species): RADCAL 

Soot model: a novel Two-Equation laminar smoke point-based model 

Turbulence-soot interaction (TSI) model: a novel Eddy dissipation concept-based model with correction for quasi laminar regime

Tabulation method for the TSI model: in situ adaptive tabulation (ISAT)

Comments:

The soot reactions are also considered in calculating gaseous species' total consumption/production.

------------------

### Discretization methods
Time: Backward

CFL: maximum 0.7

Advection: 

Momentum: Gauss linear

scalars: Gauss limitedLinear 0.1

Diffusion:  Gaussian scheme (Gauss linear corrected)

Pressure-velocity coupling

PIMPLE:

inner correction iterations: 2

non-orthogonal correction iterations: 1

outer iterations: 3

------------------

### Computational Cost (hh:mm:ss)

Wall clock time:

coarse:8 h

medium: 60 h

fine: 150 h



Simulation time:

For all grids: 0-30s

Number of CPUs (MPI Processes):

40 CPUs for all grids

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

coarse: 0.27

medium: 0.48

fine: 0.55

------------------

### Averaging period

5-30 s

------------------

### Special issues/problems

------------------

### Relevant publications

