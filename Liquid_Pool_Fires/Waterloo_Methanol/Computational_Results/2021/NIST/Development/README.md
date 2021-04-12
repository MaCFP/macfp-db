
### Contributor
Name: Randy McDermott<sup>a</sup>, Kevin McGrattan<sup>a</sup>, Jason Floyd<sup>b</sup>

Institutions:  
<sup>a</sup>National Institute of Standards and Technology (NIST), Gaithersburg, Maryland  
<sup>b</sup>Jensen Hughes, Rockville, Maryland

Country: USA

------------------

### Test case

Case 3a: Waterloo Methanol 30 cm (development)

------------------

### CFD package
Code: [Fire Dynamics Simulator (FDS)](https://github.com/firemodels/fds)

Version:

FDS6.7.5-1373-g26b258878-master

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
* new LES wall functions for heat and mass transfer based on modified Rayleigh number scaling with blowing (in development)

### Predicted MLR model with 3D Heat Transfer
* 6 cm thick liquid pool with 3D heat transfer  
* ∆z of liquid phase matches gas phase  
* surface heat flux internal wall model [Ref 1]  
* including internal radiation based on "optically thick" diffusivity model [Ref 1]  
* liquid properties for methanol with effective turblent thermal diffusivity, k_eff/k = 10 [See Ref 3]  
* initial liquid temperature set to 45 C (approx. average of T_boil and ambient)  
* 3D heat transfer model with explicit time integration; substepping in time for stability

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

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 36000       | 8         | 60           | 1479           | 00-00:24:39      | 0.0054   |
| 1       | 288000      | 16        | 60           | 16493          | 00-04:34:53      | 0.0152   |
| 0.5     | 2304000     | 128       | 60           | 81458          | 00-22:37:38      | 0.0754   |


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

3. T. Sikanen, S. Hostikka. Modeling and simulation of liquid pool fires with in-depth radiation absorption and heat transfer. Fire Safety Journal, 80:95-109, 2016. [doi](https://doi.org/10.1016/j.firesaf.2016.01.002)

