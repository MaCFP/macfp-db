### Contributor
Name: Georgios Maragkos

Institution: Ghent University

Country: Belgium

------------------

### Test case
Liquid_Pool_Fires - Waterloo_Methanol

------------------

### CFD package
Code: FireFOAM

Version: 2.2.x (custom)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.5 m x 1.8 m (cylindrical)

Cell size: Approximately 0.5 cm in main areas of interest (covering the whole fire plume area). Cell sizes increase going towards the sides and top of the domain.

Cell type: Non-uniform

Total cells: 0.985 million

Comments: The local mesh refinement region where the cells above the pool fire are 0.5 cm covers an area of 0.6 cm in diameter and 0.9 m in height.  

#### Angular space discretization (radiation solver)
Number of solid angles: 72

Comments: -

------------------

### Initial conditions
Comments: The initial conditions for temperature and pressure were set to 293 K and 101325 Pa, respectively. 

------------------

### Boundary conditions
Comments: Tempertaure at the pool fire surface is set to 338 K (boiling temperature of methanol). Mass flow rate based on the experimentally reported feeding rate of methanol applied at the fuel inlet (assuming a methanol liquid density of 792 kg/m3). Open boundary conditions allowing for entrainment but reverse flow was not allowed at the top of the domain to avoid any numerical instabilities.

------------------

### Models (include parameters)
Turbulence model: Dynamic Smagorinsky

Combustion model: Dynamic EDC (Variable Prt)

Radiation model: fvDOM

Radiative fraction: Predicted 16.4%.

Soot model: -

Comments: Absorption/emission modelled with the WSGGM model.

------------------

### Discretization methods
Time: Second order backward (backward)

Advection: Velocity - Second order (Gauss filteredLinear2V 0.2 0), Scalars - First/second order, bounded  TVD with a Sweby limiter (species: limitedLinear01 1.0)

Diffusion: Unbounded, second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PISO algorithm

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: 103 h.

Simulation time: 65 sec

Number of cores: 24

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells):

------------------

### Averaging period
60 sec
------------------

### Special issues/problems
The custom version of FireFOAM used had been described in publication 1.
------------------

### Relevant publications
1. G. Maragkos, T. Beji, B. Merci, Advances in modelling in CFD simulations of turbulent gaseous pool fires, Combust. Flame 181:22-38 (2017).
