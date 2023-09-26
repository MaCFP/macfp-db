
### Contributor
Name: Ahmed Abdalhamid<sup>a</sup>, Cecile Devaud<sup>a</sup>, Elizabeth Weckman<sup>a</sup>

Institutions:  
<sup>a</sup>University of Waterloo  


Country: Canada

------------------

### Test case

Waterloo Methanol 30 cm

------------------

### CFD package
Code: FireFOAM solver based on OpenFOAM-7.

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.5 m diameter by 1.75 m height

Cell size: 0.5 cm, 0.25 cm

Cell type: Cubes

Total cells: 0.5 cm case: 677336; 0.25 cm case: 1610752;

Comments:

#### Angular space discretization (radiation solver)
No radiation solver - Optically thin approximation

------------------

### Initial conditions
Ambient conditions

------------------

### Boundary conditions
* Prescribed mass flow rate at the inlet.  
* Fuel temperature set as the boiling temperature of methanol.


------------------

### Models (include parameters)
Turbulence model: Standard Smagorinsky model with C_k=0.02.

Combustion model: Conditional source-term estimation (CSE) model with trajectory-generated low-dimensional manifold (TGLDM) method for chemistry tabualtion. 

Radiation model: Optically thin approximation with weighted sum of grey gasses (WSGG). Turbulence-radiation interactions (TRI) are accounted for.

Radiative fraction: Predicted from the radiation model.

Soot model: none

Comments: GRI-Mech 3.0 chemistry mechanism with 53 species and 325 reactions is used for chemistry tabualtion. 

------------------

### Discretization methods
Time: Euler

CFL: 0.8

Advection: Total variation diminishing (TVD) scheme

Diffusion: Central differnece scheme

Pressure-velocity coupling: PIMPLE 
------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 2182500 s (0.5 cm grid size)

Simulation time: 25 s

Number of CPUs (MPI Processes): 1

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.129 (0.5 cm grid size)

------------------

### Averaging period

Averaging period: 20 s

------------------

### Special issues/problems

The fuel surface is lifted 30 cm from the ground. The case features a rim of 1 cm in height and thickness. 

------------------

### Relevant publications


