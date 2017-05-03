
### Contributor
Name: Georgios Maragkos

Institution: Ghent University

Country: Belgium                  

------------------

### Test case
Gaseous_Pool_Fires - Sandia_Flames (Methane tests 14, 17, 24)

------------------

### CFD package
Code: FireFOAM

Version: 2.2.x

------------------

### Mesh
Domain: 4 m x 6 m (cylindrical)

Cell size: ?1.5 cm (around centerline), ?3.0 cm (outside refinement), ?6.0 cm (sides)

Cell type: Non-uniform

Total cells: ?2.38 million

Comments: Mesh refinement around the centerline (half an inlet diameter outside the fire source and up to the outlet). Plate surrounding the fuel inlet included. Patches: Inlet (fuel inlet), Plate (wall surrounding fuel inlet), Coflow (area outside Plate), Sides (sides of domain), Outlet (top of domain)

------------------

### Initial conditions
Comments: Initial conditions for temperature and pressure according to the experiments

------------------

### Boundary conditions
Comments: Inlet fuel temperature and fuel mass flow rate according to experiments. The boundary condition specified below are given in OpenFOAM terminology.

Inlet: T (fixedValue), p_rgh (buoyantPressure), U(flowRateInletVelocity), Y(totalFlowRateAdvectiveDiffusive), alpha_sgs (zeroGradient), mu_sgs (zeroGradient), k_sgs (fixedValue)

Plate: T (zeroGradient), p_rgh (buoyantPressure), U(fixedValue (0,0,0)), Y(zeroGradient), alpha_sgs (zeroGradient), mu_sgs (zeroGradient), k_sgs (zeroGradient)

CoFlow: T (inletOutlet), p_rgh (totalPressure), U(pressureInletOutletVelocity), Y(inletOutlet), alpha_sgs (zeroGradient), mu_sgs (zeroGradient), k_sgs (inletOutlet)

Sides: T (inletOutlet), p_rgh (totalPressure), U(pressureInletOutletVelocity), Y(inletOutlet), alpha_sgs (zeroGradient), mu_sgs (zeroGradient), k_sgs (inletOutlet)

Outlet: T (inletOutlet), p_rgh (buoyantPressure), U(inletOutlet), Y(inletOutlet), alpha_sgs (zeroGradient), mu_sgs (zeroGradient), k_sgs (inletOutlet)

------------------

### Models (include parameters)
Turbulence model: constant Smagorinsky (cs=0.1, Prt=0.7)

Combustion model: Eddy Dissipation Model (EDM) (cEDM=4, cdiff=2)

Radiation model: fvDOM - grey gas model (48 solid angles)

Soot model: None

Comments: The code employs a unity Lewis number assumption. The time scale in the EDM combustion model considers laminar and turbulent mixing. The calculation of sub-grid scale kinetic energy is based on local equilibrium.

------------------

### Discretization
Time: First order Euler (Euler)

Advection: Velocity: Second order, unbounded central difference (Gauss linear), Scalars: First/second order, bounded  TVD with a Sweby limiter (species: limitedLinear01 1.0, enthalpy: limitedLinear 1.0)

Diffusion: Unbounded, second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PISO algorithm

------------------

### Averaging period
45 sec

------------------

### Special issues/problems
None

------------------

### Relevant publications
1. G. Maragkos, B. Merci, Large Eddy Simulations of CH4 Fire Plumes, Flow Turbul. Combust. (2017) - DOI: 10.1007/s10494-017-9803-4
 
