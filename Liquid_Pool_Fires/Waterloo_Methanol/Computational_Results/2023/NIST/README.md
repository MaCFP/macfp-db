
### Contributor
Name: Randy McDermott<sup>a</sup>, Kevin McGrattan<sup>a</sup>, Jason Floyd<sup>b</sup>

Institutions:  
<sup>a</sup>National Institute of Standards and Technology (NIST), Gaithersburg, Maryland  
<sup>b</sup>Fire Safety Research Institute, UL Research Institutes, Columbia, Maryland

Country: USA

------------------

### Test case

Waterloo Methanol 30 cm

------------------

### CFD package
Code: [Fire Dynamics Simulator (FDS)](https://github.com/firemodels/fds)

Version:

FDS-6.8.0-564-g879930a-master

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.6 m x 0.6 m by 0.8 m

Cell size: 5 mm, 1 cm, 2 cm

Cell type: Cubes

Total cells: 5 mm case: 2304000; 1 cm case: 288000; 2 cm case: 36000

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments: Default FDS radiation solver

------------------

### Initial conditions
Comments: All flow variables are originally ambient and then ramped up in approximately 1 s

------------------

### Boundary conditions
* OPEN at all exterior boundaries  
* log law wall function for momentum  
* combined forced and natural convection correlations for h_conv and h_mass

#### Predicted MLR
* 15 cm thick SURF with 15 cells in depth
* ∆z = 0.294 mm in first liquid cell  (based on ∆z<sup>2</sup>/α<sup>2</sup> = 1 (unity time scale))
* stretched grid with stretch factor of 2  
* liquid properties for methanol; no effective turblent transport
* in-depth radiation absorption considered; κ=1500 m<sup>-1</sup>
* dynamic, energy-conserving remeshing scheme as liquid thickness recedes

Comments:

------------------

### Models (include parameters)
Turbulence model: Deardorff (algebraic k_sgs; C_DEARDORFF=0.1), Sc_t = Pr_t = 0.5

Near-wall turb model: WALE (C_WALE=0.6)

Combustion model: EDM wih two-step fast-fast serial reactions

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: Predicted based on RadCal tabulated absorption coefficients, gray gas, mean beam length = 10 cm

Soot model: CO is the product of the first reaction step, with 100% of the carbon in the fuel converted to CO. CO then oxidizes to carbon dioxide based on availability of O2 model.

Comments:

------------------

### Discretization methods
Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM flux limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------

### Computational Cost (hh:mm:ss)

#### Prescribed MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 36000       | 8         | 60           | 2604           | 00-00:43:24      | 0.0096   |
| 1       | 288000      | 8         | 60           | 50529          | 00-14:02:09      | 0.0234   |
| 0.5     | 2304000     | 64        | 60           | 641621         | 07-10:13:41      | 0.2970\* |

#### Predicted MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 36000       | 8         | 60           | 2814           | 00-00:46:54      | 0.0104   |
| 1       | 288000      | 8         | 60           | 46643          | 00-12:57:23      | 0.0216   |
| 0.5     | 2304000     | 64        | 60           | 669761         | 07-18:02:41      | 0.3100\* |

\* Ten-fold increase in cost appears to be attributable to the ULMAT pressure solver.  MAX_PRESSURE_ITERATIONS (100) were reached every time step.  Still investigating why this occurs with GEOM.


Wall clock time: see table above

Simulation time: see table above

Number of CPUs (MPI Processes): see table above

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): see table above

------------------

### Averaging period

total simulation time: 60 s  
averaged statistics: last 30 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. [FDS Technical Reference Guide](https://github.com/firemodels/fds/releases)

2. [FDS Validation Guide](https://github.com/firemodels/fds/releases)

