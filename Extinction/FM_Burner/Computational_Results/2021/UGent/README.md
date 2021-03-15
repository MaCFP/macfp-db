### Contributor
Name: Georgios Maragkos

Institution: Ghent University (UGent)

Country: Belgium

------------------

### Test case

Case 5 - FM Burner
------------------

### CFD package
Code: FireFOAM

Version: 2.2.x (https://github.com/fireFoam-dev/fireFoam-2.2.x)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.2 m x 1.8 m (cylinder)

Cell size: 2 cm, 1 cm, 0.5 cm

Cell type: Non-uniform

Total cells: 43k (2 cm), 177k (1 cm), 782k (0.5 cm)

Comments: Refinement regions when local grid refinement (i.e., 1 cm, 0.5 cm) is used:

• 1 cm: 0.8 m x 1.2 m
• 0.5 cm: 0.6 m x 0.9 m 
 
#### Angular space discretization (radiation solver)
Number of solid angles: 48

Comments: -

------------------

### Initial conditions
Comments:

• Temperature: 293 K
• Pressure: 101325 Pa

------------------

### Boundary conditions
Comments: 

• Fuel temperature: 298 K
• Mass flow rate: 0.318 g/s (15 kW)
• Co-flow velocity: 0.041 m/s 
• Co-flow 02 mass fraction: 0.231 

------------------

### Models (include parameters)
Turbulence model: Dynamic Smagorinsky with a variable Prandtl number

Combustion model: Eddy Dissipation Model (C_EDM=2)

Radiation model: Finite Volume Discrete Ordinates Method (fvDOM)

Radiative fraction: Prescribed (chi_rad=0.34 for Y_O2_oxidizer=0.231)

Soot model: -

Comments: -

------------------

### Discretization methods
Time: Backward

CFL: 0.9

Advection: Velocity - Central difference (Gauss linear), Scalars - TVD (Gauss limitedLinear01 0.5)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (3 outer loops)

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 535430 s (for the 0.5 cm case)

Simulation time: 35

Number of CPUs (MPI Processes): 20

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.391 (for the 0.5 cm case)

------------------

### Averaging period

Averaging period: 30 sec (between 5 s – 35 s)
------------------

### Special issues/problems

------------------

### Relevant publications

