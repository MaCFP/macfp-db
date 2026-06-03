
### Contributor
Name: Randy McDermott, Chandan Paul, Marcos Vanella

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test case

FM Burner

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS)

Version: FDS-6.11.0-37-g81faf6d-master

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.2 m by 1.2 m by 1.8 m

Cell size: 2.5 mm (see "Output_Files_scaled"), 5 mm, 1 cm, 2 cm

Cell type: Cubes

Total cells: 2.5 mm case: 38,880,000 (1440 mesh), 5 mm case: 4,860,000 (180 mesh); 1 cm case: 2,592,000 (96 mesh); 2 cm case: 324,000 (96 mesh)

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments: Default solver parameters

------------------

### Initial conditions
Comments: All flow variables are originally ambient and then ramped up in approximately 1 s

------------------

### Boundary conditions
Comments: The FM burner test chamber was modeled, including the hood.  A volume flow rate of 0.08 m^3/s is prescribed out of the hood (this is lower than the 0.11 m^3/s reported which was after makeup air).  There is also a small OPEN vent around the hood exhaust that allows the simulation to maintain ambient pressure in the chamber.

------------------

### Models (include parameters)
Turbulence model: Deardoff (algebraic k_sgs); Sc_t=0.5; Pr_t=0.5

Combustion model: Two-step fast-fast serial reactions

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: Baseline case is RADCAL with 10 cm path length and *specified* radiant fraction (listed as `Chi_r` on plot).  We also explored RADCAL with 10 cm path length and *predicted* radiant fraction (`L10cm`), wideband (WB) with Planck mean (PM) absorption coefficient, and WB PM with different adjustment factors (1.5, 2.0) multiplying the absorption coefficient.

Soot model: Soot and CO are the products of the first reaction step, then oxidize to carbon dioxide based on availability of O2 model, with prescribed post flame yields of soot and CO.  The table below provides the model parameters used for the different fuel scenarios.

| Fuel  | FUEL_C_TO_CO_FRACTION | CO_YIELD* | SOOT_YIELD   | AIT** (°C)|
|-------|-----------------------|-----------|--------------|-----------|
| C2H4  | 0.90, 0.60            | 0.013     | 0.022, 0.043 | 450       |

Comments:

The key parameter in this model, FUEL_C_TO_CO_FRACTION, may be interpreted as an in-flame soot yield.  If FUEL_C_TO_CO_FRACTION=1, then no in-flame soot is generated.  If FUEL_C_TO_CO_FRACTION=0, then all the fuel's carbon is first converted to soot before being oxidized to the prescribed post-flame yield.

Another key issue with this case is the coefficient used in evaluating the soot absorption coefficient.  This year we compared against the reported soot volume fractions (baseline) and also against "scaled" f_v by a factor of 7.6/4.2=1.8 to account for the difference in the C0 value between the FM measurement method and the RADCAL soot properties used in FDS.

For the baseline case, a value of FUEL_C_TO_CO_FRACTION=0.9 was used to match the reported mean soot profile at 1D for the 21% O2 case.  The post-flame SOOT_YIELD was then tuned to match the soot profile at 3.5D for the 21% O2 case.

For the scaled case, a value of FUEL_C_TO_CO_FRACTION=0.6 was used (similar to previous MaCFP submissions) and the soot yields were left at the handbook values, 0.043 for the 21% O2 case.

\*  From Tewarson’s measurements reported in the SFPE Handbook [2]

** From Beyler SFPE Handbook [3]; only used on extinction cases

------------------

### Discretization methods
Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM Flux Limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------

### Computational Cost (hh:mm:ss)

The timings below are based on the 20.9 % O2 runs for ethylene.

| resolution  | sim time [s] | wall clock [s] (hh:mm:ss) | CPUs (MPI procs) | Cells      |CPU cost* |
|-------------|--------------|---------------------------|------------------|------------|----------|
| 2 cm        | 40           | 4421  (01:13:41)          | 96               | 324000     | 0.033    |
| 1 cm        | 40           | 43649 (12:07:29)          | 96               | 2592000    | 0.040    |
| 5 mm        | 40           | 86042 (23:54:02)          | 180              | 4860000    | 0.080    |
| 2.5 mm **   | 40           | 84637 (23:30:37)          | 1440             | 38880000   | 0.078 ** |

\* CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells)
\* On Vista at Texas Advanced Computing Center (TACC)

------------------

### Averaging period

For combustion efficiency cases, the total simulation time was 65 s and the nitrogen dilution was ramped linearly from 5 s to 65 s from 21 \% to 8 \% O2 by volume.

For the stationary cases at target O2 levels (21, 17, 15), the simulation was run for 40 s and the statistics were averaged over the last 20 s.

------------------

### Special issues/problems

In the combustion efficiency cases, a special pilot fuel model was employed.  Ethylene was injected using 36 particles arranged in a uniform ring around the burner (mimicking the experiment).  The total mass flow of ethylene from the particles was set to give 1 kW from the pilot ring.  Notably, the "pilot fuel" ethylene was not subject to an ignition threshold before reacting, mimicking a controlled pilot flame.

------------------

### Relevant publications
1. FDS Technical Reference Guide

2. M.M. Khan, A. Tewarson, and M. Chaos. SFPE Handbook of Fire Protection Engineering, chapter Combustion Characteristics of Materials and Generation of Fire Products. Springer, New York, 5th edition, 2016.

3. C. Beyler. SFPE Handbook of Fire Protection Engineering, chapter Flammability Limits of Premixed and Diffusion Flames. Springer, New York, 5th edition, 2016.

4. McGrattan, K. , McDermott, R. and Floyd, J. (2022), A Simple Two-Step Reaction Scheme for Soot and CO, Proceedings of the Tenth International Seminar on Fire and Explosion Hazards (ISFEH10), Oslo, Norway.

