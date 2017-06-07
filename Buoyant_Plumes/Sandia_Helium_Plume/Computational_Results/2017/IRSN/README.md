### Contributor
Name: Germain Boyer

Institution: IRSN

Country: France

------------------

### Test case

Sandia Helium Plume

------------------

### CFD package
Code: ISIS

Version: 4.8.0

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:

Cell size: 0.025 m

Cell type: cuboïd

Total cells: 20810880

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 

Comments: None

------------------

### Initial conditions
Comments: thermodynamical pressure 101325.0 Pa
          null velocity
          species : Y_air = 1, Y_He = 0 

------------------

### Boundary conditions
Helium inlet:
  Velocity: Vinj = 0.325 m/s with Random Fourier Modes:
    200 modes
    equivalent average Reynolds stress tensor R = | 0 0 0        |, I = 0.01
                                                  | 0 0 0        |
                                                  | 0 0 I*Vinj^2 |
  Species :  Y_air = 0, Y_He = 1

Air inlet: 
  Velocity: Vinj = 0.47 m/s
  Species : Y_air = 1, Y_He = 0

Outlet: inlet/outlet boundary condition with fixed pressure

Walls: 
  Velocity: Werner and Wengle wall law
  Species: Neumann condition

Comments: 

------------------

### Models (include parameters)
Turbulence model: LES, dynamic Smagorinsky model, Cs=0.12; turbulent Schmidt number for scalars: Sc_t = 0.5

Combustion model: none

Radiation model: none

Radiative fraction: (predicted or prescribed; if prescribed, what value): none

Soot model: none

Comments:

------------------

### Discretization methods
Time: 20s of physical time
      2nd  order Crank-Nicholson scheme for the Navier-Stokes equations
      1st order backward-Euler scheme for the mass fractions

CFL: 0.1

Advection: Marker-And-Cell scheme; centered discretization for Navier-Stokes, MUSCL discretization for the mass fractions

Diffusion: 2nd order finite differences

Pressure-velocity coupling: pressure prediction-correction

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 48:12:13 h:m:s 

Simulation time: 10s

Number of CPUs (MPI Processes): 200

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.16677

------------------

### Averaging period

3 s of physical time

------------------

### Special issues/problems

In spite of a refined mesh, the top velocity, resolved turbulent kinetic energy, Helium mass fraction and its variance are overestimated.
Conjointly, the puffing frequency is not clearly resolved, even if puffing structures can be observed on the helium mass fraction field and
temporal one-point recordings.


------------------

### Relevant publications

