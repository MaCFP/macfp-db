
### Contributor
Name: Ning Ren

Institution: FM Global

Country: USA

------------------

### Test case

Waterloo 30 cm methanol pool fire

------------------

### CFD package
Code: FireFOAM

Version: v2012 (based on OpenFOAM v2012: https://www.openfoam.com/releases/openfoam-v2012/)
Latest public version (v1912): https://github.com/fireFoam-dev/fireFoam-v1912

------------------

### Resolution

#### Computational domain discretization (flow solver)
For the 30-cm methanol pool:
- Domain: 1.8m X 1.8m-wide x 1.4m
- Cell size (gas-phase, pool region): fine mesh: (0.5cm X 0.5cm X 0.5cm); medium mesh: (1cm X 1cm X 1cm); coarse mesh: (2cm X 2cm X 2cm)  
- Cell size (liquid-phase): 0.5 mm mesh in the in-depth direction
- Cell type: structural grid with refinement zones in the burner region
- Total cells: 0.975 million (fine mesh)

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 64 (baseline) and 128

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
Turbulence model: Dynamic Smagorinsky model (Lagrangain average)  
                  Turbulent Pr = 1  
                  Turbulent Sc = 1  

Combustion model: Eddy Dissipation Model (Eddy dissipation and diffusion coefficients = 4)

Radiation model: fvDOM

Radiative fraction: prescribed

prescribed: fixed radiant fraction 0.22 (30-cm pool)  

Soot model: none

Comments: Heat of combustion=21,105 kJ/kg

------------------

### Discretization methods
Time: Backward (2nd-order)

CFL: 0.9

Advection: Velocity - 2nd-order, unbounded central difference (Gauss linear), Scalars - TVD (Gauss limitedLinear01 1.0)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (max 3 outer loops, with residual control (U:1e-5, p:5e-4))

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 183 hrs (30-cm pool, fine mesh)

Simulation time: 240 s 

Number of CPUs (MPI Processes): 64 (30-cm pool, fine mesh)

------------------

### Averaging period

t = 180-240 s 

------------------

### Special issues/problems

------------------

### Relevant publications
