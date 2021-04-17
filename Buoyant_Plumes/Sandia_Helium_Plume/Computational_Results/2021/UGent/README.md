### Contributor

Name: Georgios Maragkos, Bart Merci

Institution: Ghent University (UGent)

Country: Belgium

------------------

### Test case

Case 1 - Sandia helium plume

#### Link to Results Presentation

[UGent Case 1 Results Presentation](https://github.com/MaCFP/macfp-db/releases/download/macfp-2.0/UGent_MaCFP-2_Case1_Presentation_V2.pdf)

------------------

### CFD package
Code: FireFOAM

Version: 2.2.x (https://github.com/fireFoam-dev/fireFoam-2.2.x)

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 4 m x 4 m (cylinder)

Cell size: 20 cm, 10 cm, 6 cm, 3 cm, 1.5 cm

Cell type: Non-uniform

Total cells: 2k (20 cm), 12k (10 cm), 53k (6 cm), 139k (3 cm), 525k (1.5 cm)

Comments: Refinement regions when local grid refinement (i.e., 3 cm, 1.5 cm) is used:

• 3 cm: 2 m x 2 m  
• 1.5 cm: 1.5 m x 1.5 m 
 
#### Angular space discretization (radiation solver)
Number of solid angles: -

Comments: -

------------------

### Initial conditions
Comments:

• Temperature: 284 K  
• Pressure: 80900 Pa

------------------

### Boundary conditions
Comments: 

• Inlet mixture: 96.4% He, 1.7% C3H6O, 1.9% 02 (W_mixture ≈ 5.45 g/mol)  
• Mass flow rate: 0.06045 kg/(m2·s) (calculated as 0.325 m/s * 0.186 kg/m3)

------------------

### Models (include parameters)
Turbulence model:

* Dynamic Smagorinsky with a variable Schmidt number  
* No slip wall stress

Combustion model: -

Radiation model: -

Radiative fraction: -

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
Wall clock time: 86770 s (for the 1.5 cm case)

Simulation time: 35

Number of CPUs (MPI Processes): 20

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.094 (for the 1.5 cm case)

------------------

### Averaging period

Averaging period: 30 sec (between 5 s – 35 s)

------------------

### Special issues/problems

• The 0.5 m wide wall surrounding the inlet has been included in the simulations.  
• The boundary outside the surrounding wall and the sides of the computational domain have been modelled as open surfaces. There is no imposed co-flow velocity.

------------------

### Relevant publications
1. G. Maragkos, P. Rauwoens, Y. Wang, B. Merci, Large Eddy Simulations of the Flow in the Near-Field Region of a Turbulent Buoyant Helium Plume, Flow Turbul. Combust. 90 (2013) 511–543. https://doi.org/10.1007/s10494-012-9437-5

2. G. Maragkos, P. Rauwoens, B. Merci, Application of FDS and FireFOAM in Large Eddy Simulations of a Turbulent Buoyant Helium Plume, Combust. Sci Technol. 184 (2012) 1108-1120. https://doi.org/10.1080/00102202.2012.664002 

3. G. Maragkos, B. Merci, On the use of dynamic turbulence modelling in fire applications, Combust. Flame 26 (2020) 9-23. https://doi.org/10.1016/j.combustflame.2020.02.012

