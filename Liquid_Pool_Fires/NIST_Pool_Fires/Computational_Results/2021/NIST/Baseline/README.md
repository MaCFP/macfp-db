
### Contributor
Name: Randy McDermott<sup>a</sup>, Kevin McGrattan<sup>a</sup>, Jason Floyd<sup>b</sup>

Institutions:  
<sup>a</sup>National Institute of Standards and Technology (NIST), Gaithersburg, Maryland  
<sup>b</sup>Jensen Hughes, Rockville, Maryland

Country: USA

------------------

### Test case

Case 3a: Waterloo Methanol 30 cm

------------------

### CFD package
Code: [Fire Dynamics Simulator (FDS)](https://github.com/firemodels/fds)

Version:

FDS6.7.5-1092-g94ad5b6a4-master

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.6 m x 0.6 m by 1.2 m

Cell size: 5 mm, 1 cm, 2 cm

Cell type: cubic

Total cells: 5 mm case: 2304000; 1 cm case: 288000; 2 cm case: 36000

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 104 (species predictions), 600 (30 cm), 500 (100 cm) (heat flux predictions)

Comments: Default FDS radiation solver

------------------

### Initial conditions
Comments: All flow variables are originally ambient and then ramped up in approximately 1 s

------------------

### Boundary conditions
* OPEN at all exterior boundaries  
* log law wall function for momentum  
* combined forced and natural convection correlations for h_conv and h_mass

#### Predicted MLR (methanol)
* 10 cm thick SURF with 15 cells in depth  
* ∆z = 0.2618 mm in first liquid cell based on ∆z<sup>2</sup>/α<sup>2</sup> = 1 (unity time scale))
* stretched grid with stretch factor of 2  
* liquid properties for methanol; no effective turblent transport
* in-depth radiation absorption considered; κ=1140 m<sup>-1</sup>
* dynamic, energy-conserving remeshing scheme as liquid thickness recedes

Comments:

------------------

### Models (include parameters)
Turbulence model: Deardoff (algebraic k_sgs, C_DEARDORR=0.1), Sc_t = Pr_t = 0.5

Near-wall turb model: WALE (C_WALE=0.6)

Combustion model: EDM wih two-step fast-fast serial reactions, see table below for fuel-specific parameters, no suppression

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: See table

| Fuel              | Radiant Fraction | FUEL_C_TO_CO_FRACTION | FUEL_H_TO_H2_FRACTION |
| :-----------------| :----------------| :---------------------| :---------------------|
| Acetone           | 0.31             | 0.85                  | 0.50                  |
| Ethanol           | 0.26             | 0.95                  | 0.50                  |
| Methane           | 0.15             | 0.97                  | 0.50                  |
| Methanol (30 cm)  | 0.22             | 0.97                  | 0.50                  |
| Methanol (100 cm) | 0.21             | 0.97                  | 0.50                  |
| Propane (20 kW)   | 0.15             | 0.85                  | 0.50                  |
| Propane (34 kW)   | 0.22             | 0.85                  | 0.50                  |

Comments: CO is the product of the first reaction step, with FUEL_C_TO_CO_FRACTION of the carbon in the fuel converted to CO with the remaining fraction going to C (Soot). CO and C then oxidize to carbon dioxide based on availability of O2 model, but leaving any specified post-flame SOOT_YIELD or CO_YIELD.  Similarly, for H2, FUEL_H_TO_H2_FRACTION of the H in the fuel is converted to H2, which is then oxidized to H2O in the second step.

Comments:  The parameters FUEL_C_TO_CO_FRACTION and FUEL_H_TO_H2_FRACTION are tuned to get in-flame species concentrations in reasonable agreement with the experimental data.

------------------

### Discretization methods
Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM flux limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------

### Computational Cost (hh:mm:ss)

#### Acetone

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 54000       | 12        | 60           | 2927           | 00-00:48:47      | 0.0108   |
| 1       | 432000      | 12        | 60           | 35481          | 00-09:51:21      | 0.0164   |
| 0.5     | 3456000     | 24        | 60           | 231898         | 02-16:24:58      | 0.0268   |

#### Ethanol

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 54000       | 12        | 60           | 2895           | 00-00:48:47      | 0.0107   |
| 1       | 432000      | 12        | 60           | 31254          | 00-09:51:21      | 0.0144   |
| 0.5     | 3456000     | 24        | 60           | 223101         | 02-16:24:58      | 0.0258   |

#### Methane

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 54000       | 24        | 60           | 1858           | 00-00:30:58      | 0.0137   |
| 1       | 432000      | 24        | 60           | 20214          | 00-05:36:54      | 0.0187   |
| 0.5     | 3456000     | 24        | 60           | 219842         | 02-13:04:02      | 0.0254   |

#### Methanol 30 cm prescribed MLR

600 radiation angles for predicting heat flux

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 72000       | 16        | 60           | 2587           | 00-00:43:07      | 0.0095   |
| 1       | 576000      | 16        | 60           | 31881          | 00-08:51:21      | 0.0147   |
| 0.5     | 4608000     | 32        | 60           | 229951         | 02-15:52:31      | 0.0266   |

#### Methanol 100 cm prescribed MLR

500 radiation angles for predicting heat flux

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 270000      | 10        | 60           | 7925           | 00-02:12:05      | 0.0048   |
| 2       | 648000      | 24        | 60           | 22562          | 00-06:16:02      | 0.0139   |
| 1       | 3744000     | 108       | 60           | 64430          | 00-17:53:50      | 0.0309   |

#### Methanol 100 cm predicted MLR

500 radiation angles for predicting heat flux

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 270000      | 10        | 60           | 7218           | 00-02:00:18      | 0.0044   |
| 2       | 648000      | 24        | 60           | 30640          | 00-08:30:40      | 0.0189   |
| 1       | 3744000     | 108       | 60           | 67548          | 00-18:45:48      | 0.0324   |

#### Propane 20 kW

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 54000       | 24        | 60           | 1558           | 00-00:25:58      | 0.0115   |
| 1       | 432000      | 24        | 60           | 18227          | 00-05:03:47      | 0.0168   |
| 0.5     | 3456000     | 24        | 60           | 163774         | 01-21:29:34      | 0.0189   |

#### Propane 34 kW

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 54000       | 24        | 60           | 1555           | 00-00:25:55      | 0.0115   |
| 1       | 432000      | 24        | 60           | 17320          | 00-04:48:40      | 0.0160   |
| 0.5     | 3456000     | 24        | 60           | 190057         | 02-04:47:37      | 0.0220   |

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

