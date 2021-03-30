
### Contributor
Name: O. Luwi Oluwole, Bifen Wu

Institution: FM Global

Country: USA

------------------

### Test case

Case 3a- Waterloo 30cm methanol pool fire

------------------

### CFD package
Code: FireFOAM

Version: v2012 (based on OpenFOAM v2012: https://www.openfoam.com/releases/openfoam-v2012/)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.5m-diameter x 1.81m-high cylinder

Cell size: 5mm horizontal resolution
(elevation, vertical cell size): (0-30cm, 10mm), (30-33cm, 2.5mm), (33-90cm, 5mm), (90-120cm, 10mm), (120-181cm, 20mm)


Cell type: Non-uniform

Total cells: 1.05 million

Comments:

#### Angular space discretization (radiation solver)
Number of solid angles: 128

Comments:

------------------

### Initial conditions
Comments:

Temperature: 293 K
Pressure: 101325 Pa

------------------

### Boundary conditions
Comments:

Inlet T: 338 K
Inlet mass flow rate: 1.0692 g/s
Burner walls: no-slip, adiabatic
Top, sides and bottom: open

------------------

### Models (include parameters)
Turbulence model: Dynamic k-equation model

Combustion model: Eddy Dissipation Model (Eddy dissipation and diffusion coefficients = 4)

Radiation model: fvDOM

Radiative fraction: (predicted or prescribed; if prescribed, what value)

prescribed: fixed radiant fraction = 0.22
predicted:  Box Model with Emission TRI (default constants,i.e. C_TRI=1.25, C_Tvar=2)
            Calculated global radiant fraction=0.20

Soot model: none

Comments: Heat of combustion=21,105 kJ/kg

------------------

### Discretization methods
Time: Backward (2nd-order)

CFL: 3.0

Advection: Velocity - 2nd-order, unbounded central difference (Gauss linear), Scalars - TVD (Gauss limitedLinear01 1.0)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (max 10 outer loops, with residual control (U:1e-5, p:5e-4); exits loop when specified tolerances are satisfied for velocity and pressure)

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 66:03:30

Simulation time: 60 s

Number of CPUs (MPI Processes): 128

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.485 wall-sec/sim-sec/cell (for the predicted radiation case, i.e. Box model)

------------------

### Averaging period

t=5-60 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. I. Sikic, O.O. Oluwole, J. Wen, S. Dembele, B. Wu, X. Zhao, K. V. Meredith, Y. Wang, "A wide band gas radiation model for fire CFD simulations", 11th U. S. National Combustion Meeting, Pasadena, CA, 2019.

2. I. Sikic, S. Dembele, J. Wen, "Non-grey radiative heat transfer modelling in LES-CFD simulated methanol pool fires", JQSRT, 234:78-89, 2019

3. Chatterjee, P., Wang, Y., Meredith, K.V., and Dorofeev, S.B., "Application of a subgrid soot-radiation model in the numerical simulation of a heptane pool fire.", Proc. Comb. Inst., 35:2573-2580, 2015

