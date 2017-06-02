### Contributor
Name: Topi Sikanen

Institution: VTT

Country: Finland

------------------

### Test case

Waterloo Methanol

------------------

### CFD package
Code: FDS

Version: FDS6.5.3-1780-g6a5fd29

------------------

### Mesh
Domain: 0.64 m x 0.64 m x 1.28 m

Cell size: 2.5 mm

Cell type: uniform Cartesian

Total cells: 33.5 million

Comments: 32 cores, 130 hrs wall clock time

------------------

### Initial conditions
Comments: small velocity perturbation

------------------

### Boundary conditions
Comments:  Pool modeled as a solid with 1-dimensional heat transfer & predicted evaporation from surface [3].  Pool lip is not included in the model, OPEN outer boundaries, OPEN coflow area around pool. 

------------------

### Models (include parameters)
Turbulence model: modified Deardorff (C_DEARDORFF=0.1), SC_T=0.5, PR_T=0.5

Combustion model: EDC (const applied to time scale, C_U=0.4)

Radiation model: Grey gas, 104 solid angles, CHI_R=0.17 (Methanol [4])

Soot model: Y_SOOT=0.001 

Evaporation model: Mass transfer calculation based on vapor pressure. 1-dimensional heat conduction and radiation transport. Parameters:

      HEAT_OF_REACTION       = 1099
      CONDUCTIVITY           = 0.20
      SPECIFIC_HEAT          = 2.48
      DENSITY                = 796
      ABSORPTION_COEFFICIENT = 1140
      BOILING_TEMPERATURE    = 64.8 

Comments: 

------------------

### Discretization
Time: RK2

Advection: velocity: central difference; scalar: Superbee limiter

Diffusion: central

Pressure-velocity coupling: Low-Mach projection

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
