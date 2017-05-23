INSTRUCTIONS:
1. Fill out the form below.
2. Delete this block of instructions
3. Save the file to README.md
4. Include the README.md file in the .zip file you email to the team leaders.

---- delete from here up ----

### Contributor
Name: Kevin McGrattan

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test case

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS)

Version: 6.5.3

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.15 m by 0.38 m by 2.00 m

Cell size: 3 mm

Cell type: cube

Total cells: 4,096,000

Comments: The domain is divided into 2 x 4 x 20 = 160 meshes

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments: Narrow band model, 6 bands, absorption coefficient calculated by RadCal

------------------

### Initial conditions
Comments: Quiescent

------------------

### Boundary conditions
Comments: Passive open boundaries on top and bottom and front face. Solid walls on edge. Burner on back wall.

------------------

### Models (include parameters)
Turbulence model: Deardorff

Combustion model: Single step fast reaction; Eddy dissipation concept (EDC)

Radiation model: Finite-Volume Method (FVM)

Radiative fraction: (predicted or prescribed; if prescribed, what value)

Soot model: Specified soot yield based on Tewarson's chapter of SFPE Handbook, 4th edition

Comments:

------------------

### Discretization methods
Time: Explicit, second-order Runge-Kutta

Advection: 

Diffusion:

Pressure-velocity coupling:

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time:

Simulation time:

Number of cores:

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells):

------------------

### Averaging period

------------------

### Special issues/problems

------------------

### Relevant publications
1. Pub 1

2. Pub 2

