### Contributor

Name: Tristan Hehnen [a], Lukas Arnold [a, b]

Institution: [a] Chair of Computational Civil Engineering (CCE) at Bergische Universität Wuppertal (BUW) and [b] Institute for Advanced Simulation 7 (IAS-7) at Forschungszentrum Jülich (FZJ)

Country: Germany

------------------

### Test case

NIST Parallel Panels -- Two vertical panels lined with black cast PMMA, ignited by a propane burner

------------------

### CFD package

Code: Fire Dynamics Simulator (FDS)

Version: FDS6.7.9-0-gec52dee-HEAD

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain:
- Simulation with sample: 0.9 m by 1.2 m by 6.4 m
- Simulation with empty panels: 0.8 m by 1.2 m by 1.5 m

Total cells per size:
- Simulation with sample:
    - 2.0 cm:    864,000
    - 1.0 cm:  6,048,000
    - 0.5 cm: 48,384,000
- Simulation with empty panels:
    - 2.0 cm:    384,000
    - 1.0 cm:  1,440,000
    - 0.5 cm: 11,520,000

Cell type: Cubes

Comments: The cases use uniform cells throughout.

#### Angular space discretization (radiation solver)

Number of solid angles: 104

Comments: This is the default number of solid angles in FDS

------------------

### Initial conditions

Comments: Ambient temperature of 20 °C.

------------------

### Boundary conditions

Comments: Open (passive) pressure boundaries except at the floor.

------------------

### Models (include parameters)

FDS simulation mode set to LES:
Turbulence model (include Sc_t and Pr_t): Deardorff turbulence model with FDS defaults of 0.5 for both Schmidt and Prandtl numbers.

Combustion model: 1-step mixing-controlled reactions of propane (burner) and Methane (PMMA pyrolyzate)

Radiation model: Finite-volume, gray gas with specified radiative fraction

Radiative fraction:
- Propane: 0.30 (default)
- Methane (PMMA): 0.20 (default)

Soot model:
Fixed soot yield
- Propane: 0.024
- Methane (PMMA): 0.022

Comments:
- No CO-yields have been considered

------------------

### Pyrolysis Models (include parameters)

Solver: FDS

Radiation absorption model: 2-flux model, absorption coefficient is 3434.326925173834 1/m

Material property set: BUW_FZJ_C (MaCFP-3, 2023)

Comments:

------------------

### Discretization methods

Time: Second-order accurate Runge-Kutta

CFL: 1

Advection: Superbee flux limiter

Diffusion: Second-order central difference

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost (hh:mm:ss)
Data for simulations including PMMA sample.

Wall clock time:
- 2.0 cm (03-23:59:22)
- 1.0 cm (05-00:00:48)
- 0.5 cm (04-00:12:22)

Simulation time:
- 2.0 cm (487.83 s)
- 1.0 cm (55.12 s)
- 0.5 cm (10.36 s)

Number of CPUs (MPI Processes):
- 2.0 cm (64)
- 1.0 cm (112)
- 0.5 cm (112)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):
- 2.0 cm (0.03935220663543235 s)
- 1.0 cm (0.11612661129925281 s)
- 0.5 cm (0.46464834477334477 s)

------------------

### Averaging period

2 s

------------------

### Special issues/problems

Material parameter set is model-dependent, inverse modelling was performed with FDS6.7.9-0-gec52dee-HEAD.

------------------

### Relevant publications

1. BUW_FZJ_C contribution to MaCFP-3: https://zenodo.org/record/8005836

2. Article providing overview over parameter estimation procedure. Note, here (BUW_FZJ_C) the pyrolysis reactions release either CH4 or CO2 not the mixture discussed in the article: https://doi.org/10.1016/j.firesaf.2023.103926
