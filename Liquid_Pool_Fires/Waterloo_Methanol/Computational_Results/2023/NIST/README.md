
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
* 10 cm thick SURF with 15 cells in depth  
* ∆z = 0.2618 mm in first liquid cell  (based on ∆z<sup>2</sup>/α<sup>2</sup> = 1 (unity time scale))
* stretched grid with stretch factor of 2  
* liquid properties for methanol; no effective turblent transport
* in-depth radiation absorption considered; κ=1140 m<sup>-1</sup>
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
| :-------| :-----------| :-------- | :----------- | :------------- | :------------ | :------- |
| 2       | 36000       | 8         | 60           | 1941           | 00-00:32:21   | 0.0072   |
| 1       | 288000      | 8         | 60           | 29184          | 00-08:06:24   | 0.0135   |
| 0.5     | 2304000     | 64        | 60           | 87294          | 01-00:14:54   | 0.0404   |

#### Predicted MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 36000       | 8         | 60           | 1516           | 00-00:25:16      | 0.0056   |
| 1       | 288000      | 8         | 60           | 30989          | 00-08:36:29      | 0.0143   |
| 0.5     | 2304000     | 64        | 60           | 108643         | 01-06:10:43      | 0.0503   |


Wall clock time: see table above

Simulation time: see table above

Number of CPUs (MPI Processes): see table above

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): see table above

------------------

### Averaging period

total simulation time: 60 s  
averaged statistics: last 50 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. [FDS Technical Reference Guide](https://github.com/firemodels/fds/releases)

2. [FDS Validation Guide](https://github.com/firemodels/fds/releases)

