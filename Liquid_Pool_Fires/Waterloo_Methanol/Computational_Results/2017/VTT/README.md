### Contributor
Name: Topi Sikanen

Institution: VTT Technical research centre of FInland

Country: Finland

------------------

### Test case
Waterloo Methanol
------------------

### CFD package
Code: FDS

Version: FDS6.5.3-1780-g6a5fd29

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.64 x 0.64 x 1.28 m

Cell size: 2.5 mm

Cell type: uniform cartesian

Total cells: 33,554,432

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments:

------------------

### Initial conditions
Comments: Small velocity perturbation, temperature of ambient air and liquid 20 C

------------------

### Boundary conditions

Comments:  Pool modeled as a solid with 1-dimensional heat transfer & predicted evaporation from surface [3].  Pool lip is not included in the model, OPEN outer boundaries, OPEN coflow area around pool.

------------------

### Models (include parameters)
Turbulence model: modified Deardorff (C_DEARDORFF=0.1), SC_T=0.5, PR_T=0.5

Combustion model: EDC (const applied to time scale, C_U=0.4)

Radiation model: Grey gas

Radiative fraction: prescribed CHI_R=0.17 (Methanol [4])

Soot model: Y_SOOT=0.001

Comments:

Evaporation model: Mass transfer calculation based on vapor pressure. 1-dimensional heat conduction and radiation transport. Parameters:

      HEAT_OF_REACTION       = 1099
      CONDUCTIVITY           = 0.20
      SPECIFIC_HEAT          = 2.48
      DENSITY                = 796
      ABSORPTION_COEFFICIENT = 1140
      BOILING_TEMPERATURE    = 64.8



------------------

### Discretization methods
Time: RK2

CFL: 0.8 < CFL < 1

Advection: velocity: central difference; scalar: Superbee limiter

Diffusion: central

Pressure-velocity coupling: Low-Mach projection


------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 129:47:21

Simulation time: 15 s

Number of CPUs (MPI Processes): 32

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.0297

------------------

### Averaging period

10 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. FDS Validation Guide

2. FDS Technical Reference Guide

3. Sikanen, Topi, and Simo Hostikka. "Modeling and simulation of liquid pool fires with in-depth radiation absorption and heat transfer." Fire Safety Journal 80 (2016): 95-109.

4. Klassen, M., and J. P. Gore. Structure and radiation properties of pool fires. US Department of Commerce, National Institute of Standards and Technology, 1994.

