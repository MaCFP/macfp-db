### Contributor

Name: Georgios Maragkos, Bart Merci

Institution: Ghent university

Country: Belgium

------------------

### Test case

FM burner

------------------

### CFD package

Code: FireFOAM

Version: 2.2.x

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 1.2 m x 1.8 m (cylindrical)

Cell size: 5 mm, 1 cm, 2 cm

Cell type: non-uniform

Total cells: 1053360 (5 mm); 257040 (1 cm); 32130 (2 cm)

Comments:

#### Angular space discretization (radiation solver)

Number of solid angles: 96

Comments:

------------------

### Initial conditions

Comments: Ambient temperature and pressure set to 298 K and 101325 Pa, respectively.

------------------

### Boundary conditions

Open boundary conditions allowing for air entrainment on the sides of the domain. At the coflow (surrounding the burner), a fixed velocity (0.041 m/s) is applied.

Comments:

------------------

### Models (include parameters)

Turbulence model: dynamic Smagorinsky, Pr_t = Sc_t (dynamically calculated).

Combustion model: EDM with a single step reaction (no model constants).

Radiation model: Finite-volume, Gray version of Weighted Sum of Gray Gases (WSGG) with the path length calculated as L=3.6V/A.

Radiative fraction: The radiative fraction is 'predicted' but a correction, based on the experimentally reported chi_r value (0.34 for C2H4), is applied in the cases without extinction. In the extinction cases, the correction considers a decreasing chi_r with decreasing oxygen concentration in the co-flow, based on available experimental data (e.g., from the FM burner and UMD line burner cases).

Comments: The volume, V, and surface area, A, in the calculation of the path length are calculated dynamically by assuming a conical flame shape and tracking the HRRPUV. For radiation, a first-order accurate upwind scheme is used.

------------------

### Discretization methods

Time: Backward; second-order accurate

CFL: 0.9 (0.5 for the 2 cm cases)

Advection: Velocity - central difference (Gauss linear), scalars - TVD (Gauss limitedLinear 0.25)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (3 outer loops)

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 197416 s (5 mm grid size - no extinction)

Simulation time: 35 s

Number of CPUs (MPI Processes): 20

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.107

------------------

### Averaging period

total simulation time: 35 s
 
averaged statistics: last 30 s

Comments: The cases without extinction are run for 35 s with averaging over the last 30 s. The extinction cases are run for 90 s, with the oxygen mass fraction in the co-flow remaining constant (Y_O2=0.233) for the first 4 s and then reduced by 0.002/s (with an equivalent increase in the nitrogen mass fraction, Y_N2).

------------------

### Special issues/problems

------------------

### Relevant publications
1. G. Maragkos, A. Snegirev, J. At Thabari, B. Merci, Flame ignition and extinction modelling using infinitely fast chemistry in large eddy simulations of fire-related reacting flows, 14th International Symposium on Fire Safety Science (IAFSS2023), Tsukuba, Japan, 22-27 October 2023.

2. G. Maragkos, B. Merci, The use of a dynamic approach in CFD simulation of MaCFP 3 test cases, Poster presentation, 14th International Symposium on Fire Safety Science (IAFSS2023), Tsukuba, Japan, 22-27 October 2023.
