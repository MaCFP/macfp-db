### Contributor
Name: Daniel Alvear Portilla, Mariano Lázaro Urrutia, Alain Alonso Ipiña

Institution: GIDAI group. University of Cantabria

Country: Spain

------------------

### Test case

Sandia Flames (Test 14,17,24)

------------------

### CFD package
Code: FDS

Version: FDS6.5.3-598-geb56ed1

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 
(6.2 x 6.2 x 6.6) Mesh 1
(4.45 x 4.45 x 4.45) Mesh 2
(2.5 x 2.5 x 0.45) Mesh 3

Cell size: 5 cm

Cell type: Uniform cartesian

Total cells: 2.267.289

Comments: Number of MPI Processes: 1
Number of OpenMP Threads: 4
Total Elapsed Wall Clock Time (s): 

#### Angular space discretization (radiation solver)
Number of solid angles: 100

Comments: 3 meshes. 1 for model FLAME facility, 2 for model the 
extractor hood.

------------------

### Initial conditions
Comments: small velocity perturbation. Initial conditions for temperature and pressure according to the experiments.

------------------

### Boundary conditions
Comments: Inlet air temperature and flow, ambient temperature and presure, and the temperature of the surfaces are according to initial values.
Top surface of the extractor hood is open.


------------------

### Models (include parameters)
Turbulence model:
Vreman Model (C_VREMAN): 0.07
Turbulent Prandtl Number: 0.50
Turbulent Schmidt Number: 0.50

Combustion model: EDC combustion Model

Radiation model: Radiative heat transport via radiation transport 
equation for a gray gas. Number of solid angles:100

Radiative fraction: (predicted or prescribed; if prescribed, what value)

Soot model: Y_SOOT=0.00 (for methane)

------------------

### Discretization methods
Time: Second-order Runge-Kutta (RK2)


------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: 
Case 14: 220:24:15
Case 17: 231:03:09
Case 24: 212:32:20


Simulation time: 50 seconds

Number of cores: 1

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells):
Case 14: 0,006
Case 17: 0,007
Case 24: 0,006

------------------

### Averaging period

10 seconds

------------------

### Special issues/problems

------------------

### Relevant publications
