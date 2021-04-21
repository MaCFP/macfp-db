### Contributor
Name: Georgios Maragkos

Institution: Ghent University (UGent)

Country: Belgium

------------------

### Test case

Case 3b - NIST 1 m methanol pool fire

------------------

### CFD package
Code: FireFOAM

Version: 2.2.x (https://github.com/fireFoam-dev/fireFoam-2.2.x)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 4 m x 4 m (cylinder)

Cell size: 20 cm, 10 cm, 4 cm, 2 cm, 1 cm

Cell type: Non-uniform

Total cells: 1.8k (20 cm), 10k (10 cm), 145k (4 cm), 605k (2 cm), 1.99mil (1 cm)

Comments: Refinement regions when local grid refinement (i.e., 2 cm, 1 cm) is used:

• 2 cm: 2.5 m x 2.5 m  
• 1 cm: 1.5 m x 1.5 m 
 
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
• Mass flow rate: Prescribed value corresponding to a HRR of 254 kW.

------------------

### Models (include parameters)
Turbulence model: Dynamic Smagorinsky with a variable Prandtl number

Combustion model: Eddy Dissipation Model (C_EDM=2)

Radiation model: Finite Volume Discrete Ordinates Method (fvDOM)

Radiative fraction: Prescribed (chi_rad=0.21)

Soot model: -

Comments: Some limited heat flux results with a WSGGM model (see Reference 3 for details of the model) have also been included to illustrate the impact of radiation modelling on the heat feedback on the fuel surface.

------------------

### Discretization methods
Time: Backward

CFL: 0.9

Advection: Velocity - Central difference (Gauss linear), Scalars - TVD (Gauss limitedLinear01 0.5)

Diffusion: Conservative Gaussian integration (Gauss linear corrected)

Pressure-velocity coupling: PIMPLE (3 outer loops)

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 1339120 s (for the 1 cm case)

Simulation time: 35

Number of CPUs (MPI Processes): 20

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.384 (for the 1 cm case)

------------------

### Averaging period

Averaging period: 30 sec (between 5 s – 35 s)

------------------

### Special issues/problems

------------------

### Relevant publications

1. G. Maragkos, T. Beji, B. Merci, Advances in modelling in CFD simulations of turbulent gaseous pool fires, Combust. Flame 181 (2017) 22-38. https://doi.org/10.1016/j.combustflame.2017.03.012

2. G. Maragkos, T. Beji, B. Merci, Towards predictive simulations of gaseous pool fires, Proc. Comb. Inst. 37 (2019) 3927-3934. https://doi.org/10.1016/j.proci.2018.05.162

3. G. Maragkos, B. Merci, On the use of dynamic turbulence modelling in fire applications, Combust. Flame 26 (2020) 9-23. https://doi.org/10.1016/j.combustflame.2020.02.012

4. G. Maragkos, B. Merci, Grid insensitive modelling of convective heat transfer fluxes in CFD simulations of medium-scale pool fires, Fire Saf J., 103104, 2020. https://doi.org/10.1016/j.firesaf.2020.103104.
