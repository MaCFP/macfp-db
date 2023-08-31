### Contributor

Name: Georgios Maragkos, Bart Merci

Institution: Ghent university

Country: Belgium

------------------

### Test case

NIST Pool Fires

------------------

### CFD package

Code: FireFOAM

Version: 2.2.x

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 3 m x 3 m (cylindrical) for the 30-37 cm pool fires and 4 m x 4 m (cylindrical) for the 100 cm pool fires.

Cell size: 1 cm, 2 cm, 4 cm, 8 cm (for the 100 cm pool fires only)

Cell type: non-uniform

Total cells: 

30 m pool fires: 1 cm case: 613875; 2 cm case: 222750; 4 cm case: 29190
37 m pool fires: 1 cm case: 1486800; 2 cm case: 264600; 4 cm case: 33075
100 m pool fires: 1 cm case: 1904247; 2 cm case: 637947; 4 cm case: 173700 , 8 cm: 19200

Comments: A rim, one cell in thickness and height, surrounding the burner has been used for the 1 cm grid size cases only (and for the liquid fuels only).

#### Angular space discretization (radiation solver)

Number of solid angles: 96

Comments:

------------------

### Initial conditions

Comments: Ambient temperature and pressure set to 293 K and 101325 Pa, respectively. 
Surface burner temperatures set to 329 K (acetone), 351 K (ethanol) and 338 K (methanol), which are the evaporation temperatures of the liquid fuels. For the gaseous fuels, the surface temperatures are set to 343K (propane) and 343 K (methane) (based on Hamins 2023).

------------------

### Boundary conditions

Open boundary conditions allowing for air entrainment. The mass loss rate is prescribed at the burner in the case of liquid fuels (liquid evaporation is not modelled).

Comments:

------------------

### Models (include parameters)

Turbulence model: dynamic Smagorinsky, Pr_t = Sc_t (dynamically calculated).

Combustion model: EDM with a single step reaction (no model constants).

Radiation model: Finite-volume, Gray version of Weighted Sum of Gray Gases (WSGG) with the path length calculated as L=3.6V/A.

Radiative fraction: The radiative fraction is 'predicted' but a correction, based on the values below, is applied to the source emission term.

| Fuel              | Radiant Fraction | HEAT RELEASE RATE (kW)|
| :-----------------| :----------------| :---------------------|
| Acetone (30 cm)   | 0.31             | 37                    |
| Ethanol (30 cm)   | 0.26             | 31                    |
| Methanol (30 cm)  | 0.22             | 19                    |
| Methane (37 cm)   | 0.22             | 34                    |
| Propane (37 cm)   | 0.23             | 21                    |
| Propane (37 cm)   | 0.30             | 34                    |
| Methanol (100 cm) | 0.21             | 254                   |

Comments: The volume, V, and surface area, A, in the calculation of the path length are calculated dynamically by assuming a conical flame shape and tracking the HRRPUV. For radiation, a first-order accurate upwind scheme is used.

------------------

### Discretization methods

Time: Backward; second-order accurate

CFL: 0.9 (for 1-2 cm grid size), 0.5 (for 4-8 cm grid size)

Advection: Velocity - central difference (Gauss linear), scalars - TVD (Gauss limitedLinear 0.25)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (3 outer loops)

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 840213 s (1 cm grid size - 100 cm CH3OH)

Simulation time: 35 s

Number of CPUs (MPI Processes): 24

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.302

------------------

### Averaging period

total simulation time: 35 s

averaged statistics: last 30 s

------------------

### Special issues/problems

All reported temperatures are gas phase temperatures since equivalent experimental data exist.

------------------

### Relevant publications
1. G. Maragkos, A. Snegirev, J. At Thabari, B. Merci, Flame ignition and extinction modelling using infinitely fast chemistry in large eddy simulations of fire-related reacting flows, 14th International Symposium on Fire Safety Science (IAFSS2023), Tsukuba, Japan, 22-27 October 2023.

2. G. Maragkos, B. Merci, The use of a dynamic approach in CFD simulation of MaCFP 3 test cases, Poster presentation, 14th International Symposium on Fire Safety Science (IAFSS2023), Tsukuba, Japan, 22-27 October 2023.
