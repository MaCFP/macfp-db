
### Contributor
Name: Joshua A. Hubbard, John C. Hewson, Michael A. Hansen, Jared R. Kirsch

Institution: Sandia National Laboratories, Albuquerque, New Mexico

Country: United States of America

------------------

### Test case

------------------

### CFD package
Code: Sierra/Fuego

Version: 4.58.3

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: cylinder 2.25m tall and 2m diameter

Cell size: coarse (~1cm), fine (~0.25-0.5cm)

Cell type: hex

Total cells: The coarse mesh had a total of 2.36 x 106 nodes with 1282 nodes on the pool surface and an average pool surface nodal area of 5.6 x 10-5 m2.  The fine mesh had a total of 4.94 x 106 nodes with 11230 nodes on the pool surface and an average pool surface nodal area of 0.64 x 10-5 m2.  

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 128 ordinates using Thurgood algorithm with quadrature 4 (8n2 ordinates)

Comments:

------------------

### Initial conditions
Comments: The domain was initialized as a quiescent environment at 298K.  Under-relaxation factors and other numerical methods were used during simulation startup to maintain stability.  Those numerical methods were phased out over the first five seconds of simulation time and those five seconds of data were discarded.

------------------

### Boundary conditions
Comments: 

1.  The pool surface was modeled with a constant mass flux (1.07 x 10-3 kg/s / 0.0707 m2 = 0.0151 kg/m2-s).  The pool temperature was specified as 333 K, slightly below the boiling point of methanol.  The mixture fraction and scalar variance at the pool surface were set to 1.0 and 0.0, respectively.  The bottom of the domain was modeled as a constant temperature wall at 298K.  The remainder of the domain boundaries were specified as an outflow boundary: 0 gage pressure, 0 velocity, 0 mixture fraction, 298K temperature.

2.  A heat and mass transfer balance at the fuel surface was used to predict the fuel mass flux.  The pool temperature was specified as 333 K, slightly below the boiling point of methanol.  The mixture fraction and scalar variance at the pool surface were set to 1.0 and 0.0, respectively.  The bottom of the domain was modeled as a constant temperature wall at 298K.  The remainder of the domain boundaries were specified as an outflow boundary: 0 gage pressure, 0 velocity, 0 mixture fraction, 298K temperature.

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t): Sc = 0.9, Pr = 0.9, Large Eddy Simulation, KSGS

Combustion model: Nonadiabatic Strained Laminar Flamelet model with clipped Gaussian presumed-PDF closure, flamelets generated with Spitfire

Radiation model: Discrete ordinates method using Gray gas approximation. https://www.sandia.gov/TNF/radiation.html

Radiative fraction: predicted.  The gray gas approximation overestimates the radiative fraction, and the gas radiation emission coefficients and absorption coefficients were adjusted to match the radiative fraction for the prescribed mass flux simulations.  

Soot model: None

Comments: We do not employ a fixed radiant fraction, but we do modify the gray gas absorption and emission terms to get reasonable overall radiant fractions for the flame.  Reduced emission and absorption coefficients are designed to mimic local absorption effect in strongly emitting/absorbing gas bands. 

------------------

### Discretization methods

Time: BDF2, timesteps on the order of 0.2-0.5 milliseconds

CFL: 0.75

Advection: Hybrid scheme with MUSCL upwinding at high Peclet numbers and central differencing at low Peclet.  Cutoff Peclet is 5000 for velocity and 2 for scalars.

Diffusion: Second order central differencing.

Pressure-velocity coupling: Iterative segregated pressure projection with Rhie-Chow style smoothing.

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 6 days

Simulation time: 10 seconds

Number of CPUs (MPI Processes): 1296 (fine mesh)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

1296 * (6*24*3600) / (10 * 5E6) = 13.4

------------------

### Averaging period

10 seconds

------------------

### Special issues/problems

--Integrated mass fluxes, and integrated heat fluxes, approximately 10% high for coarse mesh due to the way fluxes were summed over nodal values.  The error went away for the fine mesh.
--Convective heat fluxes at the pool surface displayed a dependence on mass flux.  Higher mass fluxes gave convective heat fluxes of approximately zero due to dT/dz at the pool surface.
--Plume temperatures were closer to experimental measurements for lower mass fluxes (poolbc).

------------------

### Relevant publications

1.  Aro C, Black A, Brown A, Burns S, Cochran B, Domino S, Evans G, Glaze D, Gritzo L, Hewson H, Houf B, Martinez M, Moen C, Newren E, Nicolette V, Sutherland J, Tauber W, Templeton J, Tieszen S, Wagner G. Sierra Fuego Theory Manual – Version 4.50. In. Sierra Fuego Theory Manual – Version 4.50. Albuquerque, New Mexico, Sandia National Laboratories, 2018. 
2.  Domino S, Moen CD, Burns SP, Evans GH. SIERRA/Fuego: A Multi-Mechanics Fire Environment Simulation Tool. 41st Aerospace Sciences Meeting and Exhibit, Reno, Nevada.
