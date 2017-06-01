### Contributor
Name: Kevin McGrattan

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test cases
The following FDS input files are available at the Github repository `firemodels/fds`. The propylene case spans mass fluxes from 0 to 65 g/m<sup>2</sup>/s in a 65 s simulation. The other cases run for 20 s at a fixed mass flux rate.

[propylene](https://github.com/firemodels/fds/tree/master/Validation/FM_Vertical_Wall_Flames/FDS_Input_Files/propylene.fds)

[ethane](https://github.com/firemodels/fds/tree/master/Validation/FM_Vertical_Wall_Flames/FDS_Input_Files/ethane.fds)

[ethylene](https://github.com/firemodels/fds/tree/master/Validation/FM_Vertical_Wall_Flames/FDS_Input_Files/ethylene.fds)

[methane](https://github.com/firemodels/fds/tree/master/Validation/FM_Vertical_Wall_Flames/FDS_Input_Files/methane.fds)

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS)

Version: 6.5.3

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.15 m by 0.38 m by 2.00 m

Cell size: 3 mm

Cell type: cube

Total cells: 4,096,000

Comments: The domain is divided into 2 x 4 x 20 = 160 meshes

#### Angular space discretization (radiation solver)
Number of solid angles: 104

Comments: Narrow band model, 6 bands, absorption coefficient calculated by RadCal

------------------

### Initial conditions
Comments: Quiescent, 20 C ambient temperature

------------------

### Boundary conditions
Comments: Passive open boundaries on top and bottom and front face. Solid walls on edge. Burner on back wall.

------------------

### Models (include parameters)
Turbulence model: Deardorff

Combustion model: Single step fast reaction; Eddy dissipation concept (EDC)

Radiation model: Finite-Volume Method (FVM)

Radiative fraction: Predicted

Soot model: Specified soot yield based on Tewarson's chapter of SFPE Handbook, 4th edition. Soot is tracked as a passive scalar.

Comments: The soot depth is defined as the distance from the burner surface beyond which the soot mass fraction drops below 0.0025.

------------------

### Discretization methods
Time: Explicit, second-order Runge-Kutta

Advection: Superbee flux limiter

Diffusion: Explicit, central difference

Pressure-velocity coupling: Low-Mach number formulation of Navier-Stokes equations. Solution of Poisson equation for pressure using Crayfishpak, a direct FFT-based elliptic solver.

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: 10:26:38

Simulation time: 20 s

Number of cores: 160

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): 0.073 seconds per cell per simulated second

------------------

### Averaging period
10 s averaging for ethane, ethylene and methane heat flux calculation. 2 s averaging for all else.

------------------

### Special issues/problems
The heat flux to the burner surface is over-predicted for all four fuels. We believe that this is caused by the effective absorption coefficient calculated by RadCal for the six chosen wavelength bands. 

------------------

### Relevant publications
1. McGrattan, et al., FDS Technical Reference Guide, NIST Special Publication 1018-1, sixth ed., January 2017.

2. de Ris et al., "Similarity of Turbulent Wall Fires," Fire Safety Science--Proceedings of the Seventh International Symposium, pp 259-270.

