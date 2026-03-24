### Contributor

Name: Youk Moorthamers

Institution: Ghent university

Country: Belgium

------------------

### Test case

FM burner

------------------

### CFD package

Code: Ansys Fluent

Version: 2024R2

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 1.22 m x 1.22 m 2.00 m (includes the 1.83 m high compartment and conical extraction hood)

Cell size: approx. 5 mm, 1 cm, 2 cm

Cell type: 

Total cells: 1,429,026 (5 mm); 545,172 (1 cm); 207,080 (2 cm)

Comments:

#### Angular space discretization (radiation solver)

Number of solid angles: 72

Comments:

------------------

### Initial conditions

Comments: Ambient temperature and pressure set to 298 K and 101325 Pa, respectively. Simulations are initialized with the specified oxygen fraction in the domain.

------------------

### Boundary conditions

A fixed oxidizer co-flow velocity (0.041 m/s) and fuel mass flow-rate are applied. 
Compartment walls and ceiling are "wall" BCs. A constant extraction flow rate of 0.073 m³/s is specified in the extraction hood.
Since there is a gap between the extraction pipe and the ceiling, an ambient air pressure inlet is specified at the top.

A 1.5 cm high anchoring zone is applied above the burner to approximate the experimental anchor in case of the SCM.

Comments:

------------------

### Models (include parameters)

Turbulence model:

Combustion model: Subgrid Combustion Model (SCM) with a single-step reaction, vanilla EDM of Fluent.

Radiation model: Discrete Ordinates, Gray version of Weighted Sum of Gray Gases (WSGG) with the path length calculated as L=3.6V/A.

Radiative fraction: Predicted with TRI factor that includes two-zone temperature non-uniformity and unresolved temperature fluctuations

Soot: 


Comments: 

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
1. 