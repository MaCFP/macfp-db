
### Contributor
Name: Jianhong Lin<sup>a</sup>, Hua Zhou<sup>b</sup>, Evatt R. Hawkes<sup>a</sup>, Man-Ching Ma<sup>a</sup>

Institutions:  
<sup>a</sup>University of New South Wales, NSW 2052, Australia
<sup>b</sup>Tsinghua University, Beijing 100084, China

Country: Australia

------------------

### Test case

FM Burner

------------------

### CFD package
Code: fireFPVFoam developed byased on OpenFOAM-7
Version: OpenFOAM-7


------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.22 m x 2 m by (cylindrical)

Cell size: 1 cm

Cell type: non-uniform

Total cells: 1 cm case: 617800; 

Comments: The cells at the height between 0 - 60 cm are uniform with the size specified above. Further downstream, the grid resolution gradually increases. 

#### Angular space discretization (radiation solver)
Number of solid angles: 64 

Comments: 

------------------

### Initial conditions
Comments: The domain is initially filled with air at 300 K. At the near-field, the initial progress variable is set as 0.26 to trigger the combustion. Note that the progress variable here is defined as the sum of mass fractions of CO2, H2O, CO and H2.

------------------

### Boundary conditions
* The sides are set as open boundaries allowing for air entrainment.
* The coflowing air enters the domain with a fixed velocity (0.041 m/s). 
* Fuel inlet with fixed axial velocity according to the mass flux documented by the experiment. 

Comments:

------------------

### Models (include parameters)
Turbulence model: dynamic k-Eqn, Sc_t = Pr_t = 0.9

Combustion model: radiative flamelet/progress variable (RFPV) model

Radiation model: fvDOM, WSGG considering CO2, H2O and soot as participating media 

Soot Model: two equation models for the soot mass fraction and soot number density. 
 
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

Wall clock time: - 

Simulation time: - 

Number of CPUs (MPI Processes): 96

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

------------------

### Averaging period

total simulation time: 30 s  
averaged statistics: last 20 s

------------------

### Special issues/problems

------------------

### Relevant publications

