
### Contributor
Name: Ning Ren

Institution: FM Global

Country: USA

------------------

### Test case

Case 3- Waterloo/NIST 30 cm methanol pool fire

------------------

### CFD package
Code: FireFOAM

Version: v1912 (based on OpenFOAM v1912: https://www.openfoam.com/releases/openfoam-v1912/)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 2.4m-long X 2.4m-wide x 2.0m-high cube

Cell size (gas-phase): fine mesh: (2.5mm X 2.5mm X 2.5mm); medium mesh: (5mm X 5mm X 5mm); coarse mesh: (10mm X 10mm X 10mm)  

Cell size (liquid-phase): 0.5 mm mesh in the in-depth direction

Cell type: structural grid with refinement zones in the burner region

Total cells: 3.29 million (fine mesh)

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 16

Comments:

------------------

### Initial conditions
Comments:

Temperature: 293 K  
Pressure: 101325 Pa

------------------

### Boundary conditions
Comments:

Pool T: predicted by the lqiuid phase model  
Fuel evaporation rate: driven by heat flux and coupled with liquid phase model  
Burner walls: no-slip, fixed temperature  
Top, sides and bottom: open

------------------

### Models (include parameters)
Turbulence model: Dynamic Smagorinsky model (Lagrangian average)  
                  Turbulent Pr = 1  
                  Turbulent Sc = 1  

Combustion model: Eddy Dissipation Model (Eddy dissipation and diffusion coefficients = 4)

Radiation model: fvDOM

Radiative fraction: prescribed

prescribed: fixed radiant fraction = 0.18  

Soot model: none

Comments: Heat of combustion=21,105 kJ/kg

------------------

### Discretization methods
Time: Backward (2nd-order)

CFL: 0.8

Advection: Velocity - 2nd-order, unbounded central difference (Gauss linear), Scalars - TVD (Gauss limitedLinear01 1.0)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (max 3 outer loops, with residual control (U:1e-5, p:5e-4))

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 140 hrs (fine mesh)

Simulation time: 90 s (fine mesh), 160 s (medium, coarse mesh)

Number of CPUs (MPI Processes): 192 (fine mesh), 128 (medium mesh), 64 (coarse mesh)


------------------

### Averaging period

t=60-90 s (fine mesh) or 120-160 s (medium,coarse mesh)

------------------

### Special issues/problems

------------------

### Relevant publications