### Contributor

Name: Baopeng Xu, Jennifer Wen  

Institution: University of Warwick

Country: UK

------------------

### Test case

Case 3b - NIST 0.3 m & 1 m methanol pool fire

------------------

### CFD package

Code: Warwick-version FireFOAM (a coupled solver for both fire region and fuel region based on conjugate heat transfer and a film evaporation model)

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain:  
0.3 m pool fire: 165 cm diameter and 250 cm height  
1.0 m pool fire: 250 cm diameter and 400 cm height  

Cell size:  
0.3 m pool fire:  
∆x & ∆y: 0.5 cm, 1 cm, 2 cm (bulk flame region)  
∆z: 0.1 cm - 4 cm (fine mesh); 0.12 cm - 4 cm (medium mesh); 0.15 cm - 4 cm (coarse mesh)  
1.0  m pool fire:  
∆x & ∆y: 1 cm, 2 cm, 4 cm (bulk flame region)  
∆z: 0.1 cm - 5 cm (fine mesh); 0.12 cm - 5 cm (medium mesh); 0.12 cm - 5 cm (coarse mesh)  

Cell type: structured hexahedral

Total cells:  
0.3 m pool fire:  

Coarse mesh: 16 k (fuel region); 81 k (fire region)  
Medium mesh: 58 k (fuel region); 194 k (fire region)  
Fine mesh: 237 k (fuel region); 667 k (fire region)  
1.0 m pool fire:  
Coarse mesh:  41 k (fuel region); 163 k (fire region)  
Medium mesh: 163 k (fuel region); 477 k (fire region)  
Fine mesh: 600 k (fuel region); 1744 k (fire region)

Comments: -

#### Angular space discretization (radiation solver)

Number of solid angles: 80

Comments: -

------------------

### Initial conditions
Comments:  
Temperature (fire region & fuel region): 295 K (0.3 m Pool Fire), 293 K (1.0 m Pool Fire)  
Pressure: 101325 Pa

### Boundary conditions
Comments:  
Top and lateral boundaries: open flow boundary conditions  
Fuel pool surface: interface couplings of mass (evaporation model), momentum (thermo-capillary stress) and energy (conjugate heat transfer)  
Others: solid walls

------------------

### Models (include parameters)  
Turbulence: k-equation SGS model, constant turbulent Schmidt and Prandtl, SC_T=0.5, PR_T=0.5  
Combustion: extended eddy dissipation concept (EEDC)  
Radiation: FVM model (only gas phase radiation considered) -solid angles: 80  
Soot model: none

Comments:

------------------

### Discretization methods
Time: Euler  

CFL: 1.0  

Advection:  
div(phi,U)     Gauss linear 1;  
div(phi,K)     Gauss linear 1;  
div(phi,k)     Gauss limitedLinear 1;  
div(phi,Yi_hs) Gauss multivariateSelection  
{  
    CH3OH      limitedLinear01 1;  
    O2         limitedLinear01 1;  
    H2         limitedLinear01 1;  
    N2         limitedLinear01 1;  
    H2O        limitedLinear01 1;  
    CO2        limitedLinear01 1;  
    h          limitedLinear 1;  
    Ydefault   limitedLinear 1;  
    YfsDefault limitedLinear 1;  
    YfsCH3OH   limitedLinear01 1;  
    Yfn        limitedLinear 1;  
    Yfsi       limitedLinear 1;  
};  
div((muEff*dev2(T(grad(U))))) Gauss linear;  
div(phiU,p)    Gauss linear;  
div(Ji,Ii_h)   Gauss linearUpwind grad(Ii_h);  

Diffusion:  
gradSchemes          Gauss linear;  
laplacianSchemes     Gauss linear corrected;  

Pressure-velocity coupling:  
momentumPredictor yes;  
nOuterCorrectors  3;  
nCorrectors       1;  
nNonOrthogonalCorrectors 1;  

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 85:00:00 (0.3 m fine mesh)  

Simulation time: 50 s  

Number of CPUs (MPI Processes): 48  

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.325 (0.3 m fine mesh)  

------------------

### Averaging period

30 s (20 s- 50 s)

------------------

### Special issues/problems

------------------

### Relevant publications

B. Xu, J. Wen. The effect of convective motion within liquid fuel on the mass burning rates of pool fires – A numerical study. _Proc. Combustion Institute_, 2020, 1-8.

