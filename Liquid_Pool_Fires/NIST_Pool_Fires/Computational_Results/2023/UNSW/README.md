
### Contributor
Name: Jianhong Lin<sup>a</sup>, Hua Zhou<sup>b</sup>, Evatt R. Hawkes<sup>a</sup>, Man-Ching Ma<sup>a</sup>

Institutions:  
<sup>a</sup>University of New South Wales, NSW 2052, Australia
<sup>b</sup>Tsinghua University, Beijing 100084, China

Country: Australia

------------------

### Test case

NIST Pool Fires (Methane)

------------------

### CFD package
Code: fireFPVFoam developed byased on OpenFOAM-7
Version: OpenFOAM-7


------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 3 m x 3 m by (cylindrical)

Cell size: 1 cm, 2 cm, 4 cm

Cell type: non-uniform

Total cells: 1 cm case: 438600; 2 cm case: 55525; 4 cm case: 10377

Comments: The cells at the height between 0 - 70 cm are uniform with the size specified above. Further downstream, the grid resolution gradually increases. 

#### Angular space discretization (radiation solver)
Number of solid angles: 64 

Comments: 

------------------

### Initial conditions
Comments: The domain is initially filled with air at 300 K. At the near-field, the initial progress variable is set as 0.26 to trigger the combustion. Note that the progress variable here is defined as the sum of mass fractions of CO2, H2O, CO and H2.

------------------

### Boundary conditions
* Open boundary conditions for top, sides and bottom, allowing air entrainment 
* Fuel inlet with fixed axial velocity according to the mass flux documented by the experiment 

Comments:

------------------

### Models (include parameters)
Turbulence model: dynamic k-Eqn, Sc_t = Pr_t = 0.9

Combustion model: radiative flamelet/progress variable (RFPV) model

Radiation model: fvDOM, WSGG considering CO2 and H2O as participating media 

Comments:  

------------------

### Discretization methods
Time: Euler 

CFL: 0.6

Advection: Velocity - Gauss linear; Scalars - TVD (Gauss SuperBee)

Diffusion: Gauss linear corrected

Pressure-velocity coupling: PIMPLE

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 08:20:00 (1 cm)

Simulation time: 30 s

Number of CPUs (MPI Processes): 96

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.22

------------------

### Averaging period

total simulation time: 30 s  
averaged statistics: last 20 s

------------------

### Special issues/problems

------------------

### Relevant publications

