
### Contributor
Name: Jianhong Lin, Hua Zhou, Evatt Hawkes

Institution: UNSW

Country: Australia

------------------

### Test case

Case 3a - Waterloo 30cm methanol pool fire

------------------

### CFD package
Code: fireFPVFoam developed based on OpenFOAM

Version: OpenFOAM-7

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:   
3 m (diameter) x 3.3 m (height) cylinder  
inner diameter of the fuel pan = 30.1 cm  
liquid pool surface is located at z = 0.3 m  
pan lip thickness is 1 cm  
pan lip height is 1 cm  

Cell size:  
|elevation|mesh scheme g1|mesh scheme g2|mesh scheme g3|
|:---:|:---:|:---:|:---:|
|-30 to 0 cm |stretch|stretch|stretch|
|0 to 10 cm|1 cm|0.667 cm|0.5 cm|
|10 to 20 cm|strech (1 - 2 cm)|stretch (0.667 - 1.33 cm)|stretch (0.5 - 1 cm)|
|20 to 60 cm|2 cm|1.33 cm|1 cm|
|60 to 300 cm|stretch|stretch|stretch|


Cell type: Non-uniform

Total cells:   
mesh scheme g1: 0.17 million  
mesh scheme g2: 0.58 million  
mesh scheme g3: 1.34 million  

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 64

Comments:

------------------

### Initial conditions
Comments:

Temperature: 300 K    
Pressure: 101325 Pa  

------------------

### Boundary conditions

Inlet: inflow with prescribed mass flow rate of 1.07 g/s and temperature of 338 K  
Burner walls: no-slip, adiabatic    
Top, sides and bottom: open  


Comments:


------------------

### Models (include parameters)
Turbulence model: Dynamic k-equation model  
Unity Lewis number assumption applied  
Sct = 0.7  

Combustion model: Unsteady Radiative Flamelet Model  

Radiation model: fvDOM  

Radiative fraction: prescribed: fixed radiant fraction = 0.22   

Soot model: none  

Comments:  
Radiation is updated once every 20 flow time steps

------------------

### Discretization methods
Time: Euler

CFL: 0.6

Advection: Velocity - Gauss linear, Scalars - TVD (Gauss SuperBee)

Diffusion: Gauss linear corrected

Pressure-velocity coupling: PIMPLE

------------------

### Computational Cost (hh:mm:ss)
Wall clock time:  
g1: 02:00:00  
g2: 08:00:00  
g3: 14:00:00  

Simulation time: 35 s

Number of CPUs (MPI Processes):  
g1: 48 cores  
g2: 48 cores  
g3: 96 cores  

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):   
g1: 0.058 wall-sec/sim-sec/cell  
g2: 0.068 wall-sec/sim-sec/cell  
g3: 0.103 wall-sec/sim-sec/cell  

------------------

### Averaging period

t=10-35 s

------------------

### Special issues/problems

------------------

### Relevant publications

