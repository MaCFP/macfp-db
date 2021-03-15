### Contributor
Name: Georgios Maragkos

Institution: Ghent University (UGent)

Country: Belgium

------------------

### Test case

Case 3a - Waterloo 30 cm methanol pool fire
------------------

### CFD package
Code: FireFOAM

Version: 2.2.x (https://github.com/fireFoam-dev/fireFoam-2.2.x)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.5 m x 1.8 m (cylinder)

Cell size: 6 cm, 3 cm, 2 cm, 1 cm, 0.5 cm

Cell type: Non-uniform

Total cells: 3.5k (6 cm), 16k (3 cm), 47k (2 cm), 158k (1 cm), 597k (0.5 cm)

Comments: Refinement regions when local grid refinement (i.e., 1 cm, 0.5 cm) is used:

• 1 cm: 0.9 m x 0.9 m
• 0.5 cm: 0.6 m x 0.6 m 
 
#### Angular space discretization (radiation solver)
Number of solid angles: 48

Comments: -

------------------

### Initial conditions
Comments:

• Temperature: 293 K
• Pressure: 101325 Pa

------------------

### Boundary conditions
Comments: 

• Fuel temperature: 338 K (boiling temperature of methanol).
• Mass flow rate: Prescribed value corresponding to a HRR of 21.3 kW.

------------------

### Models (include parameters)
Turbulence model: Dynamic Smagorinsky with a variable Prandtl number

Combustion model: Eddy Dissipation Model (C_EDM=2)

Radiation model: Finite Volume Discrete Ordinates Method (fvDOM)

Radiative fraction: Prescribed (chi_rad=0.22)

Soot model: -

Comments: -

------------------

### Discretization methods
Time: Backward

CFL: 0.9

Advection: Velocity - Central difference (Gauss linear), Scalars - TVD (Gauss limitedLinear01 0.5)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (3 outer loops)

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 319890 s (for the 0.5 cm case)

Simulation time: 35

Number of CPUs (MPI Processes): 20

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.306 (for the 0.5 cm case)

------------------

### Averaging period

Averaging period: 30 sec (between 5 s – 35 s)
------------------

### Special issues/problems

A rim, one cell in thickness and 1 cm in height, surrounding the inlet has been included. For the 2 cm and 3 cm cases, the rim has the same height as the grid size.

------------------

### Relevant publications
1. G. Maragkos, T. Beji, B. Merci, Advances in modelling in CFD simulations of turbulent gaseous pool fires, Combust. Flame 181 (2017) 22-38. https://doi.org/10.1016/j.combustflame.2017.03.012

2. G. Maragkos, T. Beji, B. Merci, Towards predictive simulations of gaseous pool fires, Proc. Comb. Inst. 37 (2019) 3927-3934. https://doi.org/10.1016/j.proci.2018.05.162

3. G. Maragkos, B. Merci, On the use of dynamic turbulence modelling in fire applications, Combust. Flame 26 (2020) 9-23. https://doi.org/10.1016/j.combustflame.2020.02.012

4. G. Maragkos, B. Merci, Grid insensitive modelling of convective heat transfer fluxes in CFD simulations of medium-scale pool fires, Fire Saf J., 103104, 2020. https://doi.org/10.1016/j.firesaf.2020.103104.
