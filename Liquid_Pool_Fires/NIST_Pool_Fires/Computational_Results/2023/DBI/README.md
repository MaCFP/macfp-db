### Contributor
Name: Thushadh Wijesekere, Karlis Livkiss, Bjarne Husted

Institution: The Danish Institute of Fire and Security Technology (DBI)

Country: Denmark

------------------

### Test case

NIST pool fires - 30cm diameter 

------------------

### CFD package
Code: Fire Dynamic Simulator (FDS)

Version: FDS-6.8.0-0-g886e009-HEAD

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 2.4 m x 0.6 m x 1.6 m

Cell size: 5 mm, 10 mm, 20 mm

Cell type: cubic

Total cells: 5 mm case: 18 432 000, 10 mm case: 2 304 000, 20 mm case: 288 000

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 800

Comments: ` TIME_STEP_INCREMENT = 15`, Default radiation solver in FDS

------------------

### Initial conditions
Comments: quiescent atomsphere at 293 K and 101325 Pa

------------------

### Boundary conditions
Comments: `OPEN` at all exterior boundaries except at `ZMIN`

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t): Deardorff model (`C_DEARDORFF = 0.1`), Sc_t = 0.5, Pr_t = 0.5

Combustion model: Two-step simple chemistry model in FDS (`FUEL_C_TO_CO_FRACTION = 1, RADIATIVE_FRACTION = 0.22`)

Radiation model: Finite Volume Method, first-order accurate

Radiative fraction: (predicted or prescribed; if prescribed, what value) Prescribed: 0.22

Comments: Near-wall turbulence model: WALE model (`C_WALE = 0.6`)

------------------

### Discretization methods
Time: Predictor-corrector

CFL: `CFL_MIN = 0.8, CFL_MAX = 1`

Advection: CHARM

Diffusion: FDS default

Pressure-velocity coupling: FDS default (low mach number assumption, Poisson equation for pressure)

------------------

### Computational Cost (hh:mm:ss) 
**Prescribed HRR**
| cell size | CPU cores | Simulated Time (s) | wall clock time (s) | CPU cost |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 20 mm  | 40  | 60 | 1414.003 | 0.0033 |
| 10 mm  | 40  | 60 | 20705.122 | 0.0060 |
| 5 mm  | 40  | 160 | 449507.181 | 0.0061 |

**Predicted HRR**
| cell size | CPU cores | Simulated Time (s) | wall clock time (s) | CPU cost |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 20 mm  | 24  | 2800 | 58782.931 | 0.0017 |
| 10 mm  | 40  | 2800 | 1042347.411 | 0.0064 |
| 5 mm  | 24  | 200 | 1281066.002 | 0.0083 |

------------------

### Averaging period
**Prescribed HRR**
| cell size | Simulated Time (s) | Averaged time (s) |
| ------------- | ------------- | ------------- |
| 20 mm  | 60  | 40 - 60 |
| 10 mm  | 60  | 40- 60 |
| 5 mm  | 60  | 40 - 60 |

**Predicted HRR**
| cell size | Simulated Time (s) | Averaged time (s) |
| ------------- | ------------- | ------------- |
| 20 mm  | 2800  | 2500 - 2800 |
| 10 mm  | 60  | 2500 - 2800 |
| 5 mm  | 60  | 175 - 200 |


------------------

### Special issues/problems

Initial attempts for predicted HRR using an `EXTERNAL_HEAT_FLUX` could not reach the target HRR similar to the prescribed case. The predicted HRR (fuel burning rate) was much lower. Therefore, a heated solid block (20 cm x 20cm x 10cm) was placed in the center of the pool to heat up and eventually ignite the pool.
This allowed for predicted HRRs closer to the experimental value. However, this required that the simulations are run for much longer than the prescribed cases.

The heated block was placed in the pool for 1800s for the 20 mm and 1500s for the 10 mm cases while the desired HRR was achieved in the 5 mm case with 170s of heating.

------------------

### Relevant publications
