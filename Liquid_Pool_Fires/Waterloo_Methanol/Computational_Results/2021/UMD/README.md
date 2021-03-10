### Contributor
Name: Mohamed Ahmed and Arnaud Trouve

Institution: University of Maryland

Country: USA

------------------

### Test case

Case 3-a 30 cm Liquid Methanol Pool Fire Waterloo configuration

------------------

### CFD package
Code: fireFoam

Version:16.12.08
https://github.com/fireFoam-dev/fireFoam-dev/commit/47c980c20b13c60c71a0e6d8d562d07c7efd3f58

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain:
cylindrical domain

diameter = 150 cm height = 173 m
inner diameter of the fuel pan = 30.5 cm
liquid pool surface is located at z = 0.3 m
pan lip thickness = 1 cm
pan lip height = 1 cm


Cell size: 	
multi-level mesh (vertical resolution, horizontal resolution):
Coarse mesh: (5 mm, 10 mm) near pool surface & (10 mm, 10 mm) in bulk flame region
Medium mesh: (2 mm, 5 mm) near pool surface & (5 mm, 5 mm) in bulk flame region
Fine mesh: (1 mm, 2.5 mm) near pool surface & (2.5 mm, 2.5 mm) in bulk flame region

Details of vertical cell sizes
|level|elevation (cm)|Coarse mesh (mm)|Medium mesh (mm)|Fine mesh (mm)|
|---|---|---|---|---|
|1|0-30|60|30|30|
|2|30-33|5|2|1|
|3|33-73|10|5|2.5|
|4|73-113|20|10|10|
|5|113-173|60|30|30|

Cell type: Structured hexahedra

Total cells:
	Coarse mesh: 0.185 million
	Medium mesh: 1.5 million
	Fine mesh: 7.7 million

Comments:
	Check CNF paper for more details about the mesh.

#### Angular space discretization (radiation solver)
Number of solid angles:
	64 solid angles

Comments:

------------------

### Initial conditions
|Name    |      Value |
|---|---|
|CH3OH_Methanol| uniform 0 |
|IDefault  |    uniform 0 |
|N2          |  uniform 0.767082 |
|O2          |  uniform 0.232918 |
|T           |  uniform 294.75 |
|U           |  uniform (0 0 0) |
|Ydefault    |  uniform 0 |
|alphat      |  uniform 0 |
|k           |  uniform 0.0001 |
|nut        |   uniform 0 |
|p          |   uniform 101325 |
|p_rgh      |   uniform 101325 |

------------------

### Boundary conditions

Pool surface: inflow with prescribed flow rate of 1.067 g/s and temperature of 337.8 K
Burner sides: no-slip adiabatic walls
Top, sides and bottom: open boundaries

Comments:
- The simulated heat release rate is 22.6 kW

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
Finite Volume Discrete Ordinates Method

|Name|Value|Note|
|---|---|---|
|nPhi|4|azimuthal angles in PI/2 on X-Y.(from Y to X)|
|nTheta|4|polar angles in PI (from Z to X-Y plane)|
|convergence|1e-3|convergence criteria for radiation iteration|
|maxIter|3|maximum number of iterations|
|solverFreq|20|Number off low iterations per radiation iteration|

Radiant fraction:  

model 1: Prescribed global radiant fraction (PGRF)  
The input value of the radiant fraction is 0.22.  

model 2: Weighted-Sum-of-Gray-Gases (WSGG)  
The calculated radiant fraction is 0.21.

Soot model:
none

Comments:
WSGG uses the model description provided in
M.H. Bordbar , G. Wecel and T. Hyppänen (2014) A line by line based weighted sum of gray gases model for inhomogeneous CO2-H2O mixture in oxy-fired combustion, Combust. Flame, 161:2435–2445 .

------------------

### Discretization methods
Time:
| Parameter |Discretization method |
| ---|---|
| default | backward |

CFL:
0.75

Advection:
| Parameter |Discretization method |
| ---|---|
| div(phi,U)  |   Gauss filteredLinear2V 0.1 0.05|
| div(phi,k)   |   Gauss limitedLinear 0.1|
| div(phi,K)|   Gauss limitedLinear 0.1|
| flux(phi,O2) |   Gauss limitedLinear01 0.1|
| flux(phi,CH3OH_Metanol)  |  Gauss limitedLinear01 0.1|
| flux(phi,H2O)  |  Gauss limitedLinear01 0.1|
| flux(phi,CO2)  |  Gauss limitedLinear01 1|
| flux(phi,h)  |  Gauss limitedLinear 0.1|
| div(phi,h)  |  Gauss limitedLinear 0.1|
| div(((rho  nuEff) dev2(T(grad(U)))))| Gauss linear|
| div(phiU,p)   |  Gauss linear|
| div(Ji,Ii_h) |   Gauss upwind|
| div(phi,Yi_h) Gauss multivariateSelection|
| -- O2        |      limitedLinear01 0.1|
| -- N2        |      limitedLinear01 0.1|
| -- CH3OH      |        limitedLinear01 0.1|
| -- C3H8      |        limitedLinear01 0.1|
| -- C8H8      |        limitedLinear01 0.1|
| -- C3H6       |       limitedLinear01 0.1|
| -- CH4        |      limitedLinear01 0.1|
| -- unburntFuel      |        limitedLinear01 1|
| -- H2O        |      limitedLinear01 0.1|
| -- CO2        |      limitedLinear01 0.1|
| -- hth_ad     |         limitedLinear 0.1|
| -- hth_m      |        limitedLinear 0.1|
| -- h         |     limitedLinear 0.1|

Diffusion:
| Parameter |Discretization method |
| ---|---|
| gradSchemes|Gauss linear|
| laplacianSchemes|Gauss linear uncorrected|

Pressure-velocity coupling:

|Parameter|Factor|
|---|---|
|momentumPredictor | yes|
|nOuterCorrectors |  8|
|nCorrectors    |   2|
|nNonOrthogonalCorrectors | 0|

------------------

### Computational Cost (hh:mm:ss)
Wall clock time:
Coarse mesh: 36:00:00
Medium mesh: 192:00:00
Fine mesh: 840:00:00

Simulation time:
Coarse and medium meshes: 70 sec.
Fine mesh: 35 sec. 

Number of CPUs (MPI Processes):
Coarse mesh: 96 cores
Medium mesh: 120 cores
Fine mesh: 288 cores

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):
Coarse mesh: 0.000267
Medium mesh: 0.000219
Fine mesh: 0.000898

------------------

### Averaging period
Coarse and medium meshes: 60 sec.
Fine mesh: 20 sec.

------------------

### Special issues/problems

------------------

### Relevant publications
1.  M.M. Ahmed and A. Trouve (2021) "Large eddy simulation of the unstable flame structure and gas-to-liquid thermal feedback in a medium-scale methanol pool fire", Combust. Flame, 225:237-254. https://doi.org/10.1016/j.combustflame.2020.10.055
