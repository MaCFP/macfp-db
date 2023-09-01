
### Contributor
Name: Randy McDermott, Kevin McGrattan, Jason Floyd

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test case

Case 5: FM Burner

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS)

Version: FDS-6.8.0-553-gcaacf88-master

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.2 m by 1.2 m by 1.8 m

Cell size: 5 mm, 1 cm, 2 cm

Cell type: Cubes

Total cells: 5 mm case: 5,616,000 (208 mesh); 1 cm case: 2,592,000 (96 mesh); 2 cm case: 324,000 (12 mesh)

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments: Default FDS radiation solver

------------------

### Initial conditions
Comments: All flow variables are originally ambient and then ramped up in approximately 1 s

------------------

### Boundary conditions
Comments: Solid walls; open top; forced flow at floor

------------------

### Models (include parameters)
Turbulence model: Deardoff (algebraic k_sgs); Sc_t=0.5; Pr_t=0.5

Combustion model: Two-step fast-fast serial reactions

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: Predicted based on RadCal tabulated absorption coefficients

Soot model: Soot and CO are the products of the first reaction step, then oxidize to carbon dioxide based on availability of O2 model, with prescribed post flame yields of soot and CO.  The table below provides the model parameters used for the different fuel scenarios.

| Fuel  | FUEL_C_TO_CO_FRACTION | CO_YIELD* | SOOT_YIELD* | AIT** (°C)|
|-------|-----------------------|-----------|-------------|-----------|
| CH4   | 1                     | 0         | 0           | 600       |
| C2H4  | 0.60                  | 0.013     | 0.045       | 450       |
| C3H6  | 0.60                  | 0.020     | 0.103       | 457       |
| C3H8  | 0.85                  | 0.006     | 0.026       | 450       |

Comments:

The key parameter in this model, FUEL_C_TO_CO_FRACTION, may be interpreted as an in-flame soot yield.  If FUEL_C_TO_CO_FRACTION=1, then no in-flame soot is generated.  If FUEL_C_TO_CO_FRACTION=0, then all the fuel's carbon is first converted to soot before being oxidized to the prescribed post-flame yield.  The values used in this work are taken from a study with the NIST pool fires centerline species data for propane [4].  The values used for ethylene and propylene are qualitative estimates (these are known to be sootier fuels).

\*  From Tewarson’s measurements reported in the SFPE Handbook [2]

** From Beyler SFPE Handbook [3]

------------------

### Discretization methods
Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM Flux Limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------

### Computational Cost (hh:mm:ss)

The timings below are based on the combustion efficiency runs for ethylene.

| resolution  | sim time [s] | wall clock [s] (hh:mm:ss) | CPUs (MPI procs) | Cells      |CPU cost* |
|-------------|--------------|---------------------------|------------------|------------|----------|
| 2 cm        | 65           | 12380  (03:26:20)         | 12               | 324000     | 0.007    |
| 1 cm        | 65           | 50419  (14:00:19)         | 96               | 2592000    | 0.029    |
| 5 mm        | 65           | 133773 (37:09:33)         | 208              | 5616000    | 0.076    |

\* CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells)

------------------

### Averaging period

For combustion efficiency cases, the total simulation time was 65 s and the nitrogen dilution was ramped linearly from 5 s to 65 s from 21 \% to 8 \% O2 by volume.

For the stationary cases at target O2 levels (21, 19, 17, 15), the simulation was run for 20 s and the statistics were averaged over the last 10 s.

------------------

### Special issues/problems

In the combustion efficiency cases, a special pilot fuel model was employed.  Ethylene was injected using 36 particles arranged in a uniform ring around the burner (mimicking the experiment).  The total mass flow of ethylene from the particles was set to give 1 kW from the pilot ring.  Notably, the "pilot fuel" ethylene was not subject to an ignition threshold before reacting, mimicking a controlled pilot flame.

------------------

### Relevant publications
1. FDS Technical Reference Guide

2. M.M. Khan, A. Tewarson, and M. Chaos. SFPE Handbook of Fire Protection Engineering, chapter Combustion Characteristics of Materials and Generation of Fire Products. Springer, New York, 5th edition, 2016.

3. C. Beyler. SFPE Handbook of Fire Protection Engineering, chapter Flammability Limits of Premixed and Diffusion Flames. Springer, New York, 5th edition, 2016.

4. McGrattan, K. , McDermott, R. and Floyd, J. (2022), A Simple Two-Step Reaction Scheme for Soot and CO, Proceedings of the Tenth International Seminar on Fire and Explosion Hazards (ISFEH10), Oslo, Norway.

