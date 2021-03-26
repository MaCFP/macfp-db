### Contributor

Name: Baopeng Xu, Jennifer Wen  

Institution: University of Warwick

Country: UK

------------------

### Test case

Case 3b - NIST 0.3 m & 1 m methanol pool fire

------------------

### CFD package
Code: FireFOAM

Version: 2.2.x (https://github.com/fireFoam-dev/fireFoam-2.2.x)

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
∆z: 0.1 cm - 5 cm (fine mesh); 0.12 cm - 5 cm (medium mesh); 0.15 cm - 5 cm (coarse mesh)  

Cell type: structured hexahedral  

Total cells:  
0.3 m pool fire:  
Coarse mesh:  97 k  
Medium mesh: 252 k  
Fine mesh: 904 k  
1.0 m pool fire:  
Coarse mesh:  204 k  
Medium mesh: 642 k  
Fine mesh: 2.344 mil  

Comments: -

#### Angular space discretization (radiation solver)

Number of solid angles: 80

Comments: -

------------------

### Initial conditions

Comments:  
Temperature: 295 K (0.3 m Pool Fire), 293 K (1.0 m Pool Fire)  
Pressure: 101325 Pa  

### Boundary conditions
Comments:  
Inlet conditions:  
Tempertaure: 295 K (0.3 m pool fire), 293 K (1.0 m pool fire)  
Mass flow rate: predicted mass flow rate  
Velocity: marangoni convection corrected velocity  
Open flow boundary conditions at sides and top air boundaries

------------------

### Models (include parameters)
SGS Models:  
Turbulence model: k-equation  
Combustion model: modified Eddy Dissipation Concept (EDC)  
Radiation model: fvDOM (0.3 m pool fire); fvDOM-WSGG (1.0 m pool fire)  
Radiative fraction: emission-only RTE with prescribed global radiant fraction (Xrad= 22%)  
Soot model: -

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


