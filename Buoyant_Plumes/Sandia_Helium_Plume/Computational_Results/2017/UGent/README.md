### Contributor
Name: Georgios Maragkos

Institution: Ghent University

Country: Belgium

------------------

### Test case
Buoyant_Plumes - Sandia_Helium_Plume

------------------

### CFD package
Code: FireFOAM

Version: 1.6

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 4 m x 4 m (cylindrical)

Cell size: 1.23 cm (around centerline), 5.39 cm (sides and top boundaries)

Cell type: Non-uniform

Total cells: 1.26 million

Comments: The number of cells across the fuel inlet is 60. There is a plate surrounding the fuel inlet according to the experiments. Patches: Inlet (fuel inlet), Plate (wall surrounding fuel inlet), Coflow (area outside Plate), Sides (sides of domain), Outlet (top of domain)

#### Angular space discretization (radiation solver)
Number of solid angles: -

Comments: -

------------------

### Initial conditions
Comments: The initial conditions for temperature and pressure were set to 285 K and 80900 Pa, respectively.

------------------

### Boundary conditions
Comments: Inlet fuel temperature and velocity according to experiments Coflow velocity set to 0.01 m/s. The boundary condition specified below are given in OpenFOAM terminology.

Inlet: T (fixedValue 285), pd (zeroGradient), U(fixedValue 0.325), Y(fixedValue)

Plate: T (fixedValue 285), pd (zeroGradient), U(fixedValue (0,0,0)), Y(fixedValue 0.0)

CoFlow: T (fixedValue 285), pd (zeroGradient), U(fixedValue (0 0.01 0)), Y(inletOutlet)

Sides: T (inletOutlet), pd (totalPressure), U(zeroGradient), Y(inletOutlet)

Outlet: T (inletOutlet), pd (zeroGradient), U(inletOutlet), Y(inletOutlet)

------------------

### Models (include parameters)
Turbulence model: constant Smagorinsky (cs=0.1, Sct=0.5)

Combustion model: -

Radiation model: -

Radiative fraction: (predicted or prescribed; if prescribed, what value)

Soot model: -

Comments:

------------------

### Discretization methods
Time: Second order backward (Backward), CFL = 0.2

Advection: Velocity - Second order, unbounded central difference (Gauss linear), Scalars - First/second order, bounded  TVD with a Sweby limiter (species: limitedLinear01 1.0)

Diffusion: Unbounded, second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PISO algorithm

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: 195 h

Simulation time: 30 sec

Number of cores: 12

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): 0.2229

------------------

### Averaging period

10 sec

------------------

### Special issues/problems

------------------

### Relevant publications

1. G. Maragkos, P. Rauwoens, Y. Wang, B. Merci, Large Eddy simulations of the flow in the near-field region of a turbulent buoyant helium plume, Flow Turbul. Combust. 90:511-543 (2013) - DOI: 10.1007/s10494-012-9437-5
