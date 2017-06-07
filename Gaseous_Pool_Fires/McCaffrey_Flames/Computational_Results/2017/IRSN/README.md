### Contributor
Name: Germain Boyer

Institution: IRSN

Country: France

------------------

### Test case

Mc Caffrey Flames

------------------

### CFD package
Code: ISIS

Version: 4.8.0

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: box 0.7x0.7x2.2 m3, 0.3x0.3x0.15 m3 excavation for the pool 

Cell size: uniform 0.01 m cells in the pool, stretching to 0.02 m at the outer edges

Cell type: cuboïd

Total cells: 502328

Comments:

A test on larger domain extent has been performed, with limited influence on the first and second order temperature and velocity moments:
  3% on <T>, 6% on <T''^2>, 6% on <W>, 10% on <w''^2>

#### Angular space discretization (radiation solver)
Number of solid angles: 

Comments: The P1 radiation model has been used

------------------

### Initial conditions
Comments: thermodynamical pressure 101325.0 Pa
          null velocity
          temperature : T=T0=302 K (ambient temperature)
          species : Y_F = 0, Y_O2 = 0.232
          mixture fraction: Z=0

      

------------------

### Boundary conditions

Burner inlet:
  Velocity: Vinj+Vinj' with 
    Vinj = Q/rho_inj/S/Delta_Hc
    Q: total heat release (kW/m2)
    rho_inj: injection density, rho_inj = P_atm*W_CH4/T0/R
    S: burner surface
    Delta_Hc: heat of combustion of methane, Delta_Hc=49.6 MJ/kg
    Vinj': velocity disturbance provided by the Synthetic Eddy Method
    200 eddies
    equivalent average Reynolds stress tensor R = | 0 0 0        |, I = 0.01
                                                  | 0 0 0        |
                                                  | 0 0 I*Vinj^2 |
  Species :  Y_F = 1
  Mixture fraction: Z = 1
  Temperature : T=T0 

Outlet: inlet/outlet boundary condition with fixed pressure

Walls: 
  Velocity: Werner and Wengle wall law
  Species: Neumann condition
  Temperature: Neumann condition
  Radiative intensity: gray surface, emissivity 0.95

Comments: 

------------------

### Models (include parameters)
Turbulence model: LES, dynamic Smagorinsky model, Cs=0.12; turbulent Schmidt/Prandtl number for scalars: Sc_t = 0.5

Combustion model: 

  Total enthalpy formulation for the enthalpy conservation equation, with tabulated total enthalpies for all species

  Transport equation for the mixture fraction Z

  Transport equation for the fuel mass fraction, with combustion source term with EDC modelling:
  w_F = mu_SGS / (Sc_t * C_LES * Delta_LES^2 )  * min (Y_F, Y_O2/s) with
    D_LES = 
    mu_SGS : subgrid viscosity
    Sc :  Turbulent Schmidt number
    C_LES : EDC constant, C_LES = 0.1
    Delta_LES : characteristic mesh size
    Y_F, Y_O2: fuel, oxygen mass fractions
    s: fuel stoechiometric ratio

Radiation model: P1

Radiative fraction: predicted 

Soot model: none

Comments:

------------------

### Discretization methods
Time: 11s of physical time
      2nd  order Crank-Nicholson scheme for the Navier-Stokes equations
      1st order backward-Euler scheme for the fuel mass fraction, mixture fraction and total enthalpy

CFL: 0.1

Advection: Marker-And-Cell scheme; centered discretization for Navier-Stokes, MUSCL discretization for the mass fractions

Diffusion: 2nd order finite differences

Pressure-velocity coupling: pressure prediction-correction

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 31:41:34 h:m:s 

Simulation time: 11s

Number of CPUs (MPI Processes): 16

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.35037

------------------

### Averaging period

3 s of physical time

------------------

### Special issues/problems

------------------

### Relevant publications


