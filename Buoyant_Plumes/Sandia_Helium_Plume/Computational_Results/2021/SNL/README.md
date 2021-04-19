### Contributor

Name: Alexander L. Brown, John C. Hewson

Institution: Sandia National Laboratories (SNL)

Country: USA

------------------

### Test case

Case 1: Sandia Helium Plume

#### Link to Results Presentation

[SNL Case 1 Results Presentation](https://github.com/MaCFP/macfp-db/releases/download/macfp-2.0/SNL_HePlumeResults_V3.pdf)

------------------

### CFD package

Code: SIERRA/Fuego

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 9 m (height) x 5.82 m (diameter)

Cell size:

The table below lists the fine grid resolutions discussed on slide 5. "z-fine" refers to the finest vertical resolution at the base of the plume and "y-fine" refers to the finest horizontal resolution.

|    | z-fine (m) | y-fine (m) | (fine cell vol)<sup>(1/3)</sup> | N cells |
|----|------------|------------|---------------------------------|---------|
|R4  | 0.008333   | 0.03906    | 0.0233                          | 250k    |
|R5  | 0.004167   | 0.01953    | 0.0117                          | 2.5M    |
|R6  | 0.002778   | 0.01302    | 0.0078                          | 8M      |
|R7  | 0.002083   | 0.00977    | 0.0058                          | 19M     |
|R8  | 0.001667   | 0.00781    | 0.0047                          | 66M     |

Cell type: unstructured

Total cells: see table (N cells column)

Comments:

#### Angular space discretization (radiation solver)

Number of solid angles: NA

Comments:

------------------

### Initial conditions

Comments:

------------------

### Boundary conditions

Plume source: constant inlet velocity  

OPEN side and top boundaries (rmax, zmax)  

Prescribed coflow air flow bc level with diffuser plane, function of radial position

------------------

### Models (include parameters)

Turbulence model:

* one-equation KSGS LES
* wall-resolved LES (log-law wall model with y+ < 5)

Combustion model: NA

Radiation model: NA

Radiative fraction: (predicted or prescribed; if prescribed, what value)

Soot model: NA

Comments: Schmidt number for helium + acetone mixture set to 0.9; unity Lewis number

------------------

### Discretization methods

Time: 2nd-order backward differencing (implicit), segregated

CFL: 0.7

Advection: hybrid centered with (MUSCL upwind); generally centered for velocity; monotonicity-preserving for scalars

Diffusion: centered

Pressure-velocity coupling: iterative segregated pressure projection with Rhie-Chow smoothing

------------------

### Computational Cost (hh:mm:ss)

Wall clock time:

Simulation time:

Number of CPUs (MPI Processes):

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

Comments:

------------------

### Averaging period

Simulation time: 23 s  
Avaraging period: last 15 s

------------------

### Special issues/problems

------------------

### Relevant publications

1. O'hern, T.J., Weckman, E.J., Gerhart, A.L., Tieszen, S.R. and Schefer, R.W., 2005. Experimental study of a turbulent buoyant helium plume. Journal of Fluid Mechanics, 544, p. 143
