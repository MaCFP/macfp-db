
### Contributor
Name: Randy McDermott<sup>a</sup>, Kevin McGrattan<sup>a</sup>, Jason Floyd<sup>b</sup>

Institutions:  
<sup>a</sup>National Institute of Standards and Technology (NIST), Gaithersburg, Maryland  
<sup>b</sup>Fire Safety Research Institute, UL Research Institutes, Columbia, Maryland

Country: USA

------------------

### Test case

NIST Pool Fires

------------------

### CFD package
Code: [Fire Dynamics Simulator (FDS)](https://github.com/firemodels/fds)

Version:

FDS-6.8.0-564-g879930a-master

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.28 m x 1.28 m by 1.92 m

Cell size: [4, 2, 1, 0.5] cm

Cell type: cubic

Total cells: [49,152; 393,216; 3,145,728; 25,165,824]

Comments:

#### Angular space discretization (radiation solver)

**37 cm methane and propane**

Number of solid angles: 16, `TIME_STEP_INCREMENT`=1, `ANGLE_INCREMENT`=1

**30 cm liquid fuels**

Number of solid angles: 600, `TIME_STEP_INCREMENT`=10, `ANGLE_INCREMENT`=10

**100 cm methanol**

Number of solid angles: 600, `TIME_STEP_INCREMENT`=1, `ANGLE_INCREMENT`=1

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
* 15 cm thick SURF with 15 cells in depth
* ∆z = 0.294 mm in first liquid cell based on ∆z<sup>2</sup>/α<sup>2</sup> = 1 (unity time scale))
* stretched grid with stretch factor of 2-3
* liquid properties for methanol; no effective turblent transport
* in-depth radiation absorption considered; κ=1500 m<sup>-1</sup>
* dynamic, energy-conserving remeshing scheme as liquid thickness recedes

Comments:

------------------

### Models (include parameters)
Turbulence model: Deardorff (algebraic k_sgs, C_DEARDORFF=0.1), Sc_t = Pr_t = 0.5

Near-wall turb model: WALE (C_WALE=0.6)

Combustion model: EDM wih two-step fast-fast serial reactions, see table below for fuel-specific parameters, no suppression

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: See table

| Fuel              | Radiant Fraction | FUEL_C_TO_CO_FRACTION | FUEL_H_TO_H2_FRACTION | SOOT_YIELD | CO_YIELD |
| :-----------------| :----------------| :---------------------| :---------------------|:-----------|:---------|
| Acetone           | 0.31             | 0.80                  | 0.50                  | 0.014      | 0.003    |
| Ethanol           | 0.26             | 0.95                  | 0.50                  | 0.008      | 0.001    |
| Methane           | 0.22             | 0.97                  | 0.50                  | 0          | 0        |
| Methanol (30 cm)  | 0.22             | 1.00                  | 0.50                  | 0          | 0        |
| Methanol (100 cm) | 0.21             | 1.00                  | 0.50                  | 0          | 0        |
| Propane (20 kW)   | 0.15             | 0.75                  | 0.50                  | 0.024      | 0.005    |
| Propane (34 kW)   | 0.22             | 0.75                  | 0.50                  | 0.024      | 0.005    |

Comments:  A two-step reaction mechanism is implemented. In the first reaction, fuel is converted to CO, soot, H2, and H2O. In the second reaction, the CO, soot, and H2 are converted to CO2 and H2O. Both reactions employ fast kinetics, but proceed in series, not in parallel. The relative amounts of CO, soot, and H2 produced in the first step (dictated by the parameters FUEL_C_TO_CO_FRACTION and FUEL_H_TO_H2_FRACTION) are still subjects of study, and for the moment have been estimated based on measured results. The fractions of carbon atoms converted to CO in the first step are as follows---0.85 for acetone; 0.95 for ethanol; 0.97 for methane; 1.0 for methanol; 0.85 for propane. For all fuels, one half of the hydrogen atoms are converted to H2 in the first step.


------------------

### Discretization methods
Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM flux limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: see table below

Simulation time: see table below

Number of CPUs (MPI Processes): see table below

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): see table below

#### Acetone prescribed MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 49152       | 1         | 60           | \*\*           | \*\*             | \*\*     |
| 2       | 393216      | 8         | 60           | 24551          | 00-06:49:11      | 0.008    |
| 1       | 3145728     | 96        | 60           | 48902          | 00-13:35:02      | 0.025    |

#### Acetone predicted MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 49152       | 1         | 60           | 7123           | 00-01:58:43      | 0.002    |
| 2       | 393216      | 8         | 60           | \*\*           | \*\*             | \*\*     |
| 1       | 3145728     | 96        | 60           | 48305          | 00-13:25:05      | 0.024    |

#### Ethanol prescribed MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 49152       | 1         | 60           | \*\*           | \*\*             | \*\*     |
| 2       | 393216      | 8         | 60           | 24368          | 00-06:46:08      | 0.008    |
| 1       | 3145728     | 96        | 60           | 44130          | 00-12:15:30      | 0.022    |

#### Ethanol predicted MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 49152       | 1         | 60           | 7164           | 00-01:59:24      | 0.002    |
| 2       | 393216      | 8         | 60           | \*\*           | \*\*             | \*\*     |
| 1       | 3145728     | 96        | 60           | 48941          | 00-13:35:41      | 0.025    |
| 0.5     | 25165824    | 96        | 6.96 \*\*\*  | 69697          | 00-19:21:37      | 0.038    |

#### Methane

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 393216      | 8         | 60           | 32051          | 00-08:54:11      | 0.011    |
| 1       | 3145728     | 96        | 60           | 55843          | 00-15:30:43      | 0.028    |

#### Propane 20 kW

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 393216      | 8         | 60           | 25754          | 00-07:09:14      | 0.009    |
| 1       | 3145728     | 96        | 60           | 50778          | 00-14:06:18      | 0.026    |

#### Propane 34 kW

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 393216      | 8         | 60           | 28488          | 00-07:54:48      | 0.0115   |
| 1       | 3145728     | 96        | 60           | 51851          | 00-14:24:11      | 0.0160   |
| 0.5     | 25165824    | 96        | 60           | 943060         | 10-21:57:40      | 0.0600   |

#### Methanol 30 cm prescribed MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 2       | 393216      | 8         | 60           | 22402          | 00-06:13:22      | 0.008    |
| 1       | 3145728     | 96        | 60           | 44366          | 00-12:19:26      | 0.023    |

#### Methanol 30 cm predicted MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 4       | 49152       | 1         | 60           | 6235           | 00-01:43:55      | 0.002    |
| 2       | 393216      | 8         | 60           | \*\*           | \*\*             | \*\*     |
| 1       | 3145728     | 96        | 60           | 43124          | 00-11:58:44      | 0.022    |
| 0.5     | 25165824    | 96        | 6.68 \*\*\*  | 79867          | 00-22:11:07      | 0.046    |

#### Methanol 100 cm prescribed MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 20      | 16000       | 2         | 60           | \*\*           | \*\*             | \*\*     |
| 10      | 128000      | 16        | 60           | 6518           | 00-01:48:38      | 0.014    |
| 5       | 1024000     | 128       | 60           | 17547          | 00-04:52:27      | 0.037    |
| 2.5     | 8192000     | 128       | 60           | \*\*           | \*\*             | \*\*     |
| 1       | 3604480     | 110       | 60           | \*\*           | \*\*             | \*\*     |

#### Methanol 100 cm predicted MLR

| ∆x (cm) | Total cells | CPU cores | Sim Time (s) | Wall Clock (s) | WC (dd-hh:mm:ss) | CPU Cost |
| :-------| :-----------| :-------- | :----------- | :------------- | :--------------- | :------- |
| 20      | 16000       | 2         | 60           | 3841           | 00-01:04:01      | 0.008    |
| 10      | 128000      | 16        | 60           | \*\*           | \*\*             | \*\*     |
| 5       | 1024000     | 128       | 60           | 16933          | 00-04:42:13      | 0.035    |
| 2.5     | 8192000     | 128       | 60           | 446851         | 05-04:07:31      | 0.116    |
| 1       | 3604480     | 110       | 60           | 602836         | 06-23:27:16      | 0.307 \*\*\*\*   |


\*\* File lost

\*\*\* Case rerunning and original file over-written

\*\*\*\*  Significant cost increase.  CPU cost log file shows radiation and communication as roughly equal and together consuming 90 \% of the total.

------------------

### Averaging period

total simulation time: 60 s  
averaged statistics: last 30 s

------------------

### Special issues/problems

High O2 levels near base of the pool, presumably due to issues with the extinction model.  Testing that theory now.

------------------

### Relevant publications
1. [FDS Technical Reference Guide](https://github.com/firemodels/fds/releases)

2. [FDS Validation Guide](https://github.com/firemodels/fds/releases)

