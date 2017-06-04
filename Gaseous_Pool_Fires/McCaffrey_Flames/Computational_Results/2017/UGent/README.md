### Contributor
Name: Georgios Maragkos

Institution: Ghent University

Country: Belgium

------------------

### Test case
Gaseous_Pool_Fires - McCaffrey_Flames

------------------

### CFD package
Code: FireFOAM

Version: 2.4.x

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 3 m x 3 m x 3 m

Cell size: 1.25 cm (flame and intermittent region), 2.5 cm (plume region), 5-10 cm (top and sides of the domain)

Cell type: Non-uniform

Total cells: 0.54 million

Comments: Local mesh refinement employed when constructing the mesh having different mesh resolutions.

#### Angular space discretization (radiation solver)
Number of solid angles: 48

Comments: -

------------------

### Initial conditions
Comments: The initial conditions for temperature and pressure were set to 293 K and 101325 Pa, respectively.

------------------

### Boundary conditions
Comments: Inlet fuel temperature set to 293 K. Mass flow rate according to the experiments applied at the fuel inlet. Open boundary conditions allowing for entrainment but reverse flow was not allowed at the top of the domain to avoid any numerical instabilities.

------------------

### Models (include parameters)
Turbulence model: Dynamic Smagorinsky (Prt=0.7)

Combustion model: EDM (The version used in FDS 6)

Radiation model: fvDOM

Radiative fraction: Prescribed 20%.

Soot model: -

Comments: No absorption/emission considered in the radiation modelling.

------------------

### Discretization methods
Time: First order Euler (Euler)

Advection: Velocity - Second order, unbounded central difference (Gauss linear), Scalars - First/second order, bounded  TVD with a Sweby limiter (species: limitedLinear01 1.0)

Diffusion: Unbounded, second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PISO algorithm

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: Depending on the case approximately 8 h.

Simulation time: 50 sec

Number of cores: 24

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): 0.0256

------------------

### Averaging period
45 sec
------------------

### Special issues/problems
-
------------------

### Relevant publications
1. G. Maragkos, T. Beji, B. Merci, Implementation and Evaluation of the Dynamic Smagorinsky Model and an Eddy Dissipation Model with Multiple Reaction Time Scales in FireFOAM, To be presented at MCS 10, Naples Italy, 2017.
