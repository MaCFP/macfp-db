
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
Domain: 3.6 m x 3.6 m by 3.6 m main section around the plume, plus an additional 3.6 m section to encompass heat flux measurements

Cell size: 1 cm, 2 cm, 4 cm (inner mesh); 4 cm outer mesh

Cell type: cubic

Total cells: 1 cm case: 2818048; 2 cm case: 1458000; 4 cm case: 891000

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 500

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
Turbulence model: Deardoff (algebraic k_sgs, C_DEARDORFF=0.1), Sc_t = Pr_t = 0.5

Near-wall turb model: WALE (C_WALE=0.6)

Combustion model: EDM wih two-step fast-fast serial reactions, see table below for fuel-specific parameters, no suppression

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: 0.21

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
| 4       | 891000      | 33        | 60           | 7903           | 00-02:11:43      | 0.0048   |
| 2       | 1458000     | 54        | 60           | 25609          | 00-07:06:49      | 0.0158   |
| 1       | 2818048     | 110       | 60           | 113324         | 01-07:28:44      | 0.0737   |

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

