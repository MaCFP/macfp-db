
### Contributor
Name: Ning Ren

Institution: FM Global

Country: USA

------------------

### Test case
UMD Turbulent Line Burner
CH4
C3H8

------------------

### CFD package
Code:FireFOAM

Version: FireFOAM-dev

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.6 m by 1.4 m by 2.0 m

Cell size: 5 mm (flame and co-flow region), 2 cm grid in the far-field

Cell type: Non-uniform cube

Total cells: 1,355,200

Comments: The current model does not have flame blow off mechanism. Oxygen anchor is not necessary in the simulation. For simplicity, the small oxygen anchor was not used in the simulation.

#### Angular space discretization (radiation solver)
Number of solid angles: 16

Comments: Radiative heat flux is not a targated quantity for comparision. Therefore, a small number of angle is used.

------------------

### Initial conditions
Comments: Quiescent

------------------

### Boundary conditions
Comments: Open boundaries are used on top and side. The co-flow region has a flow rate of 120 g/s. Oxygen mass fraction in the co-flow region varies from 21% to 11%. Fuel flow rate is 1 g/s for CH4, and 1.08 g/s for C3H8.

------------------

### Models (include parameters)
Turbulence model: k-equation model (Ck = 0.03)

Combustion model: Eddy Dissipation Model (C_EDC = 4)

Radiation model: fvDOM

Radiative fraction: Prescribed based on the measurement (e.g. Xr = 7.5% for XO2 = 13% of CH4 fuel)

Soot model: No soot model

Comments: Flame extinction model is Reactive Volume Fraction model developed by Dorofeev, Sergey B. "Thermal quenching of mixed eddies in non-premixed flames." Proceedings of the Combustion Institute (2016).

------------------

### Discretization methods
Time: First order Euler (Euler)

Advection: Velocity - Second order, unbounded central difference (Gauss linear)

Diffusion: Second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PIMPLE algorithm

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: 18 hrs

Simulation time: 20 s

Number of cores: 32

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): 0.07650

------------------

### Averaging period
16 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. White, J. P., et al. "Radiative emissions measurements from a buoyant, turbulent line flame under oxidizer-dilution quenching conditions." Fire Safety Journal 76 (2015): 74-84.

2. Dorofeev, Sergey B. "Thermal quenching of mixed eddies in non-premixed flames." Proceedings of the Combustion Institute (2016).


