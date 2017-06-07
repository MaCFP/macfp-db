### Contributor
Name: A. Marchand, S. Verma and A. Trouve

Institution: University of Maryland

Country: United States of America

------------------

### Turbulent Line Burner

------------------

### CFD package

Code: FireFOAM

Version: FireFOAM-dev (version of December 2016 - commit 47c980c20b13c60c71a0e6d8d562d07c7efd3f58)

------------------

### Resolution

#### Computational domain discretization (flowsolver)

Domain: 2mx0.85mx2m

Cell size:

|Zone Size|Cell Size|Note|
|---|---|---|
|0.4 m × 0.6 m × 0.6 m | 4.2 mm × 4.2 mm × 4.2 mm | above the burner surface |
|0.6 m x 0.8 m x 0.8 m | 8.33 mm × 8.33 mm × 8.33 mm | continuous flame region |
|Far field | 16.7 mm x 16.7 mm x 16.7 mm | above the burner surface |


Cell type: hexahedral

Total cells: 1779200 cells

Comments:

#### Angular space discretization (radiation solver)

Number of solid angles: 16 solid angles

Comments:

------------------

### Initial conditions


|Name|Value|
|---|---|
|B|uniform (000000)|
|CH4|uniform 0|
|IDefault|uniform 0|
|N2|uniform 0.767|
|O2|uniform 0.233|
|T|uniform 294.75|
|U|uniform (000)|
|Ydefault|uniform 0|
|alphat|uniform 0|
|hth_ad|uniform -3431.28|
|hth_m|uniform -3431.28|
|k|uniform 0.0001|
|nut|uniform 0|
|p|uniform 101325|
|p_rgh|uniform 101325|

Comments :

hth_ad hth_m are respectively the adiabatic enthalpy and the mixing enthalpy. The parameters are needed for the extinction model developed by S. Vilfayeau [1].


------------------

### Boundary conditions


|..|anchored|blockage|frame|coflow|entrainment|inlet|outlet|
|---|---|---|---|---|---|---|---|
|B|fixedValue|zeroGradient|zeroGradient|fixedValue|inletOutlet|fixedValue|inletOutlet|
|CH4|totalFlowRateAdvectiveDiffusive|zeroGradient|zeroGradient|fixedValue|inletOutlet|totalFlowRateAdvectiveDiffusive|inletOutlet|
|IDefault|greyDiffusiveRadiation|greyDiffusiveRadiation|greyDiffusiveRadiation|greyDiffusiveRadiation|greyDiffusiveRadiation|greyDiffusiveRadiation|greyDiffusiveRadiation|
|N2|totalFlowRateAdvectiveDiffusive|zeroGradient|zeroGradient|uniformFixedValue|inletOutlet|totalFlowRateAdvectiveDiffusive|inletOutlet
|O2|totalFlowRateAdvectiveDiffusive|zeroGradient|zeroGradient|uniformFixedValue|inletOutlet|totalFlowRateAdvectiveDiffusive|inletOutlet|
|T|fixedValue|fixedValue|zeroGradient|fixedValue|inletOutlet|fixedValue|inletOutlet|
|U|flowRateInletVelocity|fixedValue|fixedValue|flowRateInletVelocity|pressureInletOutletVelocity|flowRateInletVelocity|inletOutlet|
|Ydefault|fixedValue|zeroGradient|zeroGradient|fixedValue|inletOutlet|fixedValue|inletOutlet|
|alphat|fixedValue|zeroGradient|zeroGradient|fixedValue|zeroGradient|zeroGradient|zeroGradient|
|hth_ad|enthalpy|zeroGradient|zeroGradient|enthalpy|enthalpy|enthalpy|enthalpy|
|hth_m|enthalpy|zeroGradient|zeroGradient|enthalpy|enthalpy|enthalpy|enthalpy|
|k|fixedValue|zeroGradient|zeroGradient|fixedValue|inletOutlet|fixedValue|inletOutlet|
|nut|fixedValue|zeroGradient|zeroGradient|fixedValue|zeroGradient|fixedValue|zeroGradient|
|p|calculated|calculated|calculated|calculated|calculated|calculated|calculated|
|p_rgh|fixedFluxPressure|fixedFluxPressure|fixedFluxPressure|fixedFluxPressure|totalPressure|fixedFluxPressure|fixedFluxPressure|


Comments: enthalpy boundary condition is a custom boundary condition developed for the turbulent line burner case.



------------------

### Models(include parameters)

Turbulence model:

One-equation eddy viscosity model. Eddy viscosity SGS model using a modeled balance equation to simulate the behaviour of k (kEqn library of OpenFOAM-dev)

|Parameter|Value|
|---|---|
|Ck|0.094|
|Ce|1.048|

Combustion model: Eddy Dissipation Concept + extinction model from [1]

|Parameter|Value|Note|
|---|---|---|
|semiImplicit|no||
|C_EDC|4.0|Eddy dissipation coefficient [-]|
|C_Diff|6|Diffusion coefficient [-]|
|C_FEF|1.9616e10|model coefficient for Methane [-]|
|Ta	|3.6856e4|activation temperature for Methane [K]|
|Tst_ad|2240-1270|	adiabatic flame temperature for Heptane [K]|
|Tst_adDil|1270|	adiabatic flame temperaturefor Heptane [K]|
|Tfuel|294.75	|Temperature at which fuel is injected [K]|
|Tair	|294.75	|initial air temperature [K]|
|Tign	|	1100|re-ignitiontemperature [K]|
|Dac|1|Critical Damkohler number [-]|



Radiation model: Finite Volume Discrete Ordinates Method


|Name|Value|Note|
|---|---|---|
|nPhi|2|azimuthal angles in PI/2 on X-Y.(from Y to X)|
|nTheta|2|polar angles in PI (from Z to X-Y plane)|
|convergence|1e-3|convergence criteria for radiation iteration|
|maxIter|3|maximum number of iterations|
|solverFreq|20|Number off low iterations per radiation iteration|

Radiativefraction: prescribed radiative fraction based on the experimental data of J. White [2].

Sootmodel: no soot model

Comments:

------------------

### Discretization methods

Time:

| Parameter |Discretization method | CFL |
| ---|---|---|
| default | secon-order backward | 0.5 |


Diffusion:

| Parameter |Discretization method |
| ---|---|
|snGradSchemes|uncorrected|
|laplacianSchemes|Gauss linear uncorrected|


Advection:

| Parameter |Discretization method |
| ---|---|
|gradSchemes|Gauss linear|
| div(phi,U)  |    Gauss filteredLinear2V 0.2 0.05|
| div(phi,k)   |   Gauss linear|
| div(phi,K)|   Gauss limitedLinear 1|
| flux(phi,O2) |   Gauss limitedLinear01 1|
| flux(phi,CH4)  |  Gauss limitedLinear01 1|
| flux(phi,H2O)  |  Gauss limitedLinear01 1|
| flux(phi,unburntFuel) |   Gauss limitedLinear01 1|
| flux(phi,CO2)  |  Gauss limitedLinear01 1|
| flux(phi,h)  |  Gauss limitedLinear 1|
| div(phi,hth_ad)  |  Gauss limitedLinear 1|
| div(phi,hth_m)  |  Gauss limitedLinear 1|
| div(phi,h)  |  Gauss limitedLinear 1|
| div(((rho  nuEff) dev2(T(grad(U)))))| Gauss linear|
| div(phiU,p)   |  Gauss linear|
| div(Ji,Ii_h) |   Gauss upwind|
| div(phi,Yi_h) Gauss multivariateSelection|
| -- O2        |      limitedLinear01 1|
| -- N2        |      limitedLinear01 1|
| -- CH4        |      limitedLinear01 1|
| -- unburntFuel      |        limitedLinear01 1|
| -- H2O        |      limitedLinear01 1|
| -- CO2        |      limitedLinear01 1|
| -- hth_ad     |         limitedLinear 1|
| -- hth_m      |        limitedLinear 1|
| -- h         |     limitedLinear 1|


Pressure-velocity coupling:

|Parameter|Factor|
|---|---|
|momentumPredictor | yes|
|nOuterCorrectors |  3|
|nCorrectors    |   2|
|nNonOrthogonalCorrectors | 0|



Relaxation:

|Name|Factor|
|---|---|
|U|0.9|
|k|0.9|
|Specie|0.9|

------------------

### Computational Cost(hhh:mm:ss)

Wall clocktime :

|Oxygen strength| Clock Time | Number of cores | Simulation Time | CPU cost|
|---|---|---|---|---|
|21 % | 70:05:27 | 80 | 20 | 0.57|
|18 % | 86:45:01 | 80 | 25 | 0.56|
|16 % | 61:05:57 | 80 | 20 | 0.49|
|15 % | 62:30:45 | 80 | 20 | 0.51|
|14 % | 62:05:49 | 80 | 20 | 0.50|
|13 % | 57:05:46 | 80 | 20 | 0.46|
|12 % | 30:22:48 | 80 | 20 | 0.25|
|11 % | 29:38:02 | 80 | 20 | 0.24|


------------------

### Averaging period

The mean of the heat release rate is calculate over 10 seconds (between t = 10 s and t =20 s)

The mean temperature and mean oxygen strength is calculated between t = 10 s and t = 25 s for XO2 = 0.18 and spanwise averaging between X=-0.1 m and X=0.1 m.

------------------

### Special issues/problems

The data for the length of flame came from a previous study [1]. Lengths of flame were not recorded in the simulations.

------------------

### Relevant publications

1. Vilfayeau, S., J. P. White, P. B. Sunderland, A. W. Marshall, and A. Trouvé. "Large eddy simulation of flame extinction in a turbulent line fire exposed to air-nitrogen co-flow." Fire Safety Journal 86 (2016): 16-31.

2. White, J.P., Link, E.D., Trouvé, A.C., Sunderland, P.B., Marshall, A.W., Sheffel, J.A., Corn, M.L., Colket, M.B., Chaos, M. and Yu, B. “Radiative emissions measurements from a buoyant, turbulent line flame under oxidizer-dilution quenching conditions,” Fire Safety Journal 76 (2015):74-84.
