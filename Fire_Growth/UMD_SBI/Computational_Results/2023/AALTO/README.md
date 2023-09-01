### Contributor
Name: Soroush Rashidzadeh, Aleksi Rinta-Paavola, Farid Alinejad, Simo Hostikka

Institution: Aalto University

Country: Finland

------------------

### Test case

------------------

### CFD package
Code: FDS

Version: 6.8.0

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.72*0.72*1.60 (m)

Cell size: 1 cm 

Cell type: cubic

Total cells: 829440

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 100

Comments: Angle_increment=20

------------------

### Initial conditions
Comments: Initial Temperature at 20 C 

------------------

### Boundary conditions
Comments: PMMA Corner wall and Conceret floor + Open Boundary conditions for the rest

------------------

### Models (include parameters)
Turbulence model (include Sc_t and Pr_t):

Combustion model: Default LES model in FDS 

Radiation model: Gray calculation with RADCAL

Radiative fraction: (predicted or prescribed; if prescribed, what value) not defined

Soot model: MMA Soot yield of 0.02

Comments:

------------------

### Pyrolysis Models (include parameters)
Solver (e.g., GPyro, FDS, ThermaKin; include version): FDS

Radiation absorption model:

Material property set: (developed by [institution]; calibration data; calibration method used [e.g., manual iteration, monte carlo sampling, optimization algorithm, PROPTI, Gpyro])

Properties of PMMA are from AALTO_I and AALTO_II

Comments:

------------------

### Discretization methods
Time:

CFL: 

Advection:

Diffusion:

Pressure-velocity coupling: Low Mach number approximation

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 56,120 seconds

Simulation time: 200sec

Number of CPUs (MPI Processes): 36

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):
0.0122
------------------

### Averaging period

------------------

### Special issues/problems

------------------

### Relevant publications
1. FDS Technical Reference Guide

2. Alinejad, F., Bordbar, H., & Hostikka, S. On the importance and modeling of in-depth spectral radiation absorption in the pyrolysis of black PMMA. Fire Safety Journal, 135, 2023, 103706. https://doi.org/10.1016/j.firesaf.2022.103706  

