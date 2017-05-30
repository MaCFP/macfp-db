### Contributor
Name: Oluwayemisi O. ("Luwi") Oluwole

Institution: FM Global

Country: USA

------------------

### Test case
Gaseous_Pool_Fires - McCaffrey_Flames

------------------

### CFD package
Code: FireFOAM

Version: dev

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 3 m x 3 m x 3 m

Cell size: 1.25 cm (from base to 1m height, 0.6m x 0.6m sides), 2.5 cm (up to 2m height above base, 1.2m x 1.2m sides), 5.0 cm (up to outlet, 1.3m x 1.3m sides), 10.0 cm (far sides: 3.0m x 3.0m sides)

Cell type: Non-uniform

Total cells: 0.39 million

Comments: Experiments showed negligible floor effects; for simplicity, a floor inlet configuration was used in these simulations. Finest mesh zone covered continuous and intermittent flame regions. This essentially reproduces the simulations in the 2011 publication cited below, using an updated version of FireFOAM. 

#### Angular space discretization (radiation solver)
Number of solid angles: -

Comments: - Radiation was not predicted; constant radiative fractions were prescribed as listed in the experimental data section. 

------------------

### Initial conditions
Comments: Temperature and pressure were initialized to 298.15 K and 101325 Pa, respectively.

------------------

### Boundary conditions
Comments: Ambient temperature set to 298.15 K. Inlet fuel mass flow rates according to fire size in experiments (Fuel heat of combustion = 5e4 kJ/kg). The boundary conditions specified below are given in OpenFOAM terminology.

Inlet: T (fixedEnthalpyFluxTemperature), p_rgh (fixedFluxPressure), U(flowRateInletVelocity), Y(totalFlowRateAdvectiveDiffusive), alpha_t (fixedValue 0), nu_t (fixedValue 0), k (fixedValue 1e-5)

Floor: T (zeroGradient), p_rgh (fixedFluxPressure), U(fixedValue (0,0,0)), Y(zeroGradient), alpha_t (fixedValue 0), nu_t (fixedValue 0), k (fixedValue 1e-5)

Sides: T (inletOutlet), p_rgh (prghTotalHydrostaticPressure), U(pressureInletOutletVelocity), Y(inletOutlet), alpha_t (zeroGradient), nu_t (zeroGradient), k (inletOutlet)

Outlet: T (inletOutlet), p_rgh (prghTotalHydrostaticPressure), U(pressureInletOutletVelocity), Y(inletOutlet), alpha_t (zeroGradient), nu_t (zeroGradient), k (inletOutlet)

------------------

### Models (include parameters)
Turbulence model: kEqn (Ck=0.03, Prt=1.0)

Combustion model: Eddy Dissipation Model (C_EDC=4, C_Diff=0)

Radiation model: fvDOM

Radiative fraction: Prescribed constant radiative fractions as listed in the experimental data section (~17-27%).

Soot model: -

Comments: No absorption/emission considered in radiation modeling.

------------------

### Discretization methods
Time: First order Euler (Euler)

Advection: Velocity - Second order, unbounded central difference (Gauss linear), Scalars - First/second order, bounded  TVD with a Sweby limiter (species: limitedLinear01 1.0, enthalpy: limitedLinear 1.0)

Diffusion: Unbounded, second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PIMPLE algorithm

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: ~20-32 h (within this range, time increased with fire size).

Simulation time: 100 sec

Number of cores: 96

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): -

------------------

### Averaging period
80 sec
------------------

### Special issues/problems
Running in PIMPLE mode (nOuterCorrectors > 1) is recommended, to ensure enthalpy conservation.

------------------

### Relevant publications
1. Y. Wang, P. Chatterjee, J. L. de Ris, Large Eddy Simulation of Fire Plumes, Proc. Combust. Inst. (2011) - DOI: 10.1016/j.proci.2010.07.031

