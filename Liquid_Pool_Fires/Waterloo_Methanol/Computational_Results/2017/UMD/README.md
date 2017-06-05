### Contributor
Name: A.Marchand, S. Verma and A.Trouve

Institution: University of Maryland

Country: United States of America

------------------

### Liquid Pool Fires/Waterloo_Methanol
------------------

### CFD package

Code: FireFOAM

Version: FireFOAM-dev (version of December 2016)

------------------

### Resolution

#### Computational domain discretization (flowsolver)

Domain: cylindrical domain

radius = 0.605 m
height = 1.8 m

inlet is at z = 0.3 m


Cell size:

30 cells across the inlet


|Zone|Cell Size|
|---|---|
|-0.3 m < z < 0 m | 0.005 m|
|0 m < z < 0.3 m | 0.0025 m |
| 0.3 m < z < 0.9 m| 0.005 m |
| 0.9 m < z < 1.8 m| 0.01 m |

Celltype: hexahedral

Totalcells: 560720 cells

Comments: the inlet is at 0.3 m to avoid numerical influence from the bottom boundary

#### Angular space discretization (radiation solver)

Number of solid angles: 16 solid angles

Comments:

------------------

### Initial conditions


|Name    |      Value |
|---|---|
|CH3OH_Metanol| uniform 0 |
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

|..|base|inlet|inletsides|sides|top|
|---|---|---|---|---|---|
|CH3OH_Metanol| inletOutlet  |               totalFlowRateAdvectiveDiffusive| zeroGradient |          inletOutlet           |      inletOutlet |
|IDefault |     greyDiffusiveRadiation  |    greyDiffusiveRadiation     |     greyDiffusiveRadiation| greyDiffusiveRadiation   |   greyDiffusiveRadiation|
|N2     |       inletOutlet      |           totalFlowRateAdvectiveDiffusive| zeroGradient          | inletOutlet           |      inletOutlet |
|O2        |    inletOutlet   |             totalFlowRateAdvectiveDiffusive| zeroGradient        |   inletOutlet       |          inletOutlet |
|T        |     inletOutlet           |fixedValue     |                 zeroGradient      |     inletOutlet     |            inletOutlet |
|U       |      pressureInletOutletVelocity| flowRateInletVelocity    |       noSlip      |           pressureInletOutletVelocity | inletOutlet |
|Ydefault   |   inletOutlet    |             fixedValue   |                   zeroGradient    |       inletOutlet         |        inletOutlet |
|alphat     |   zeroGradient    |            fixedValue     |                 zeroGradient   |        zeroGradient   |             zeroGradient|
|k           |  inletOutlet |               fixedValue   |                   zeroGradient     |      inletOutlet   |              inletOutlet |
|nut     |      zeroGradient   |             fixedValue      |                zeroGradient    |       zeroGradient     |           zeroGradient|
|p          |   calculated       |           calculated      |                calculated      |       calculated      |            calculated  |
|p_rgh    |     totalPressure              |fixedFluxPressure             |fixedFluxPressure    |  totalPressure       |        fixedFluxPressure|

Comments:

- base is the bottom boundary
- inlet is the fuel inlet Boundary
- inletsides is the edge of the pool
- sides is the edge of the domain
- top is the top boundary


------------------

### Models(include parameters)

Turbulence model:

dynamicKEqnCoeffs (OpenFOAM-dev turbulence library): Eddy viscosity SGS model using a modeled balance equation to simulate
the behaviour of k in which a dynamic procedure is applied to evaluate the
coefficients.

Combustion model: Eddy Dissipation Concept (FireFOAM  combustion library)

|Name|Value|Note|
|---|---|---|
|semiImplicit|no||
|C_EDC|4.0|Eddy dissipation coefficient [-]|
|C_Diff|6|Diffusion coefficient [-]|


Radiation model: Finite Volume Discrete Ordinates Method


|Name|Value|Note|
|---|---|---|
|nPhi|2|azimuthal angles in PI/2 on X-Y.(from Y to X)|
|nTheta|2|polar angles in PI (from Z to X-Y plane)|
|convergence|1e-3|convergence criteria for radiation iteration|
|maxIter|3|maximum number of iterations|
|solverFreq|20|Number off low iterations per radiation iteration|

Radiative fraction: prescribed radiative fraction of 0.18 [2]
Soot model: no soot model

Comments:

------------------

### Discretization methods

Time:

| Parameter |Discretization method |
| ---|---|
| default | backward |


Diffusion:

| Parameter |Discretization method |
| ---|---|
|snGradSchemes|limited 1.0|
| laplacianSchemes|Gauss linear limited 1.0|


Advection:

| Parameter |Discretization method |
| ---|---|
| gradSchemes|Gauss linear|
| div(phi,U)  |   Gauss linear|
| div(phi,k)   |   Gauss linear|
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


Pressure-velocity coupling:

|Parameter|Factor|
|---|---|
|momentumPredictor | yes|
|nOuterCorrectors |  3|
|nCorrectors    |   2|
|nNonOrthogonalCorrectors | 0|

------------------

### Computational Cost(hhh:mm:ss)

Wall clocktime :

|Clock Time | Number of cores | Simulation Time | CPU cost|
|---|---|---|---|
|89:58:05| 60 | 60 |0.58|

------------------

### Averaging period

The averaging is between t = 10 s and t = 60 s, with revolution average (for 36 angles).

The turbulence time scales are estimated only between r = 0 cm and 15 cm over one line.

------------------

### Special issues/problems

------------------

### Relevant publications

1.  E.J. Weckman and A.B. Strong (1996) "Experimental Investigation of the Turbulence Structure of Medium-Scale Methanol Pool Fires", Combustion and Flame, 105:245-266.
2. Klassen and Gore (1994) "Structure and Radiation Properties of Pool Fires", NIST report GCR-94-651.
