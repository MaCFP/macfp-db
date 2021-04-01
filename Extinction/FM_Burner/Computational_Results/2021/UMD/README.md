### Contributor
Name: Mohamed Ahmed and Arnaud Trouve

Institution: University of Maryland

Country: USA

------------------

### Test case

Case 5: Ethylene Burner

------------------

### CFD package
Code: fireFoam

Version: 16.12.08  
https://github.com/fireFoam-dev/fireFoam-dev/commit/47c980c20b13c60c71a0e6d8d562d07c7efd3f58

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:  
1.22 m by 1.22 m by 1.8 m

Cell size:  
For r < 0.2 m and 0.127 m < z < 1.0 m: 3 mm < dx=dy < 5 mm and dz = 5 mm  
Otherwise: mesh is stretched

Cell type: Structured hexahedra

Total cells: 1,299,648 cells

Comments:  
- The burner diameter is 0.15 m, and the burner walls are modeled with zero thickness  
- The burner surface is elevated by 0.127 m above the bottom surface

 
#### Angular space discretization (radiation solver)
Number of solid angles: 72

Comments:

------------------

### Initial conditions
Comments:

- Temperature: 298 K  
- Pressure: 101325 Pa  
- Velocity: 0 m/s  
- SGS turbulence kinetic energy: 0.0001 m2/s2

------------------

### Boundary conditions

Comments:

- Burner surface: advective-diffusive flow of C2H4 at a fixed flow rate (given in the experiment) and a temperature of 353 K  
- Burner side walls: no-slip and a fixed temperature at 298 K  
- Bottom boundary: fixed velocity at 0.041 m/s and fixed mass fractions of O2 and N2  
- Sides: no-slip adiabatic walls  
- Top: open to atmosphere

------------------

### Models (include parameters)
Turbulence model:  
Dynamic k-equation model

Unity Lewis number for calculation of turbulent diffusivities  
Turbulent Schmidt number = 0.5  
Turbulent Prandtl number = 0.5  

Combustion model:  
Eddy Dissipation Model  
|Name|Value|Note|  
|---|---|---|  
|semiImplicit|no||  
|C_EDC|4.0|Eddy dissipation coefficient [-]|  
|C_Diff|6|Diffusion coefficient [-]|


Radiation model:  
Finite Volume Discrete Ordinates Method (fvDOM); 

Radiant fraction:  
Model 1: Weighted-Sum-of-Gray-Gases (WSGG)  
4 gray gases plus 1 transparent gas for H2O/CO2 mixture and 2 gray gases for soot (Total of 10 bands)  

Model 2: Prescribed Global Radiant Fraction (PGRF)  
The radiant fraction is taken from experimental data   

Soot model:  
Soot oxidation and formation rates are calculated based on smoke point height concept with presumed  
Beta-PDFs of mixture fraction and temperature to account for sub-grid scale fluctuations

Comments:  
- WSGG uses the model description provided in: F. Cassol et al. IJHMT 79 (2014) 796–806  
- Smoke point height concept is adopted from: C.W. Lautenberger et al. FSJ 40 (2005) 141–176

------------------

### Discretization methods
Time: Backward  

CFL: maximum 0.75  

Advection:  
- velocity: Gauss filteredLinear2V 0.1 0.05  
- scalars: Gauss limitedLinear 0.1

Diffusion: Gauss linear

Pressure-velocity coupling: PIMPLE (number of outer loops: until residual of U and P is < 1e-6 or a max. of 8 loops)


------------------

### Computational Cost (hh:mm:ss)

Wall clock time: WSGG 192 hours, PGRF 100 hours  

Simulation time: 25 sec.

Number of CPUs (MPI Processes): 80

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):  
WSGG 1.7 - PGRF 0.89


------------------

### Averaging period
15 sec. (from t=10 sec to t=25 sec.)

------------------

### Special issues/problems

------------------

### Relevant publications
