### Contributor

Name: Georgios Maragkos, Bart Merci

Institution: Ghent university

Country: Belgium

------------------

### Test case

UMD_SBI

------------------

### CFD package

Code: FireFOAM

Version: 2.2.x

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 0.7 m x 0.7 m x 2 m (L x W x H)

Cell size: 4 cm, 2 cm, 1 cm. Uniform grid size for the 2 cm and 4 cm cases while a local grid refinement for the 1 cm case (i.e., 1 cm grid size in the main areas of interest, including the burner and the panels, and 2 cm elsewhere).

Cell type: Cubes

Total cells: 16179 (4 cm), 122344 (2 cm), 631803 (1 cm)

#### Angular space discretization (radiation solver)

Number of solid angles: 96

------------------

### Initial conditions

Comments: Ambient temperature and pressure set to 293 K and 101325 Pa, respectively. 

------------------

### Boundary conditions

Comments: Open boundary conditions allowing for air entrainment on the opposite sides from the two panels. The top boundary is also set as open (no extraction is applied).

------------------

### Models (include parameters)

Turbulence model (include Sc_t and Pr_t): dynamic Smagorinsky, Pr_t = Sc_t (dynamically calculated).

Combustion model: EDM with a single step reaction (no model constants). The pyrolyzate gases retaken as C3H8 (i.e., same as the burner fuel).

Radiation model: Finite-volume, Gray version of Weighted Sum of Gray Gases (WSGG) with the path length calculated as L=3.6V/A.

Radiative fraction: The radiative fraction is 'predicted' but a correction, based on the global radiative fraction, is applied to the source emission term. The radiative fraction for the C3H8 burner is taken as 0.25 while for the PMMA panels is taken as 0.33. The global radiative fraction then varies linearly between these two values based on the mass loss rates of the burner and the panels.

Comments: The volume, V, and surface area, A, in the calculation of the path length are calculated dynamically by assuming a triangular pyramid flame shape and tracking the HRRPUV. For radiation, a first-order accurate upwind scheme is used.

------------------

### Pyrolysis Models (include parameters)

Solver: 1D single-step Arrhenius model 

Radiation absorption model: None

Material property set: The properties of black PMMA are taken from https://doi.org/10.1016/j.polymdegradstab.2020.109433. No temperature-dependency could be considered in the thermophysical properties (c_p and k). Specific heat, c_p, was taken as 1492 J/Kg/K while thermal conductivity, k, was taken as 0.16 W/m/K (corresponding to their average values in the 298 K - 394 K region).

Comments:

------------------

### Discretization methods

Time: Backward; second-order accurate

CFL: 0.9

Advection: Velocity - central difference (Gauss linear), Scalars-TVD (Gauss limitedLinear 0.25)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (3 outer loops)

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 7300 s (4 cm), 60747 s (2 cm), 725379 s (1 cm)

Simulation time: 200 s

Number of CPUs (MPI Processes): 20 (for all three grid sizes)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.045 (4 cm), 0.049 (2 cm), 0.115 (1 cm)

------------------

### Averaging period

A 1 second averaging period has been applied to the heat flux results to reduce the fluctuation of the data.
------------------

### Special issues/problems

------------------

### Relevant publications

1. G. Maragkos, B. Merci, The use of a dynamic approach in CFD simulation of MaCFP 3 test cases, Poster presentation, 14th International Symposium on Fire Safety Science (IAFSS2023), Tsukuba, Japan, 22-27 October 2023.
