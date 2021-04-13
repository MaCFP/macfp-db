
### Contributor
Name: Xinyu Zhao, Bifen Wu, Joseph N. Squeo

Institution: Univeristy of Connecticut (UConn)

Country: USA

------------------

### Test case

Case 5: FM burner ethylene pool fire

------------------

### CFD package
Code: In-house OpenFOAM buoyancy flame solver based on reactingFOAM and fireFOAM

Version: OpenFOAM-5.x

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 1.22 m by 1.22 m by 1.8 m

Cell type: structured hexahedra

Cell size: 3.5 mm finest resolution (based on cubic root of cell volumes) near flame front, with increasing cell size up to 10-15 mm/cell downstream

Total cells: 2,196,880 

Comments: nonuniform grid; grid refinement concentrated near the plume region; finite burner wall thickness, the raised fuel inlet and a full-enclosure set-up is considered in the computational domain; 



------------------

### Initial conditions
Comments:  
• Temperature: 293 K  
• Pressure: 101325 Pa  
• Velocity: 0 m/s  
• SGS turbulence kinetic energy: 0 m2/s2


------------------

### Boundary conditions
Comments: Solid walls with no-slip; top is open to atmosphere; forced flow at floor; no-slip adiabatic walls at the sides

• Fuel temperature at fuel nozzle inlet: 353 K  
• Fuel mass flow rate: 0.318 g/s (15 kW)  
• Co-flow mass flow rate: 74.0 g/s (air)  

------------------

### Models (include parameters)
Turbulence model: : LES; one equation eddy-viscosity with Ck = 0.03 subgrid scale model and cubic root of local cell volume is used to resolve the subgrid


Combustion/Chemistry model: VODE w/ analytical Jacobian and AHI-S solver is used to solve the finite-rate chemistry


Radiation model: optically-thin with LBL-database (with MCRT-LBL capabilities)

Soot model: Leung's [1] two-equation semi-empirical model with modified oxidation to include O and OH radicals. Reaction rates are tuned following the work of Guo et al [2].

[1] K. M. Leung, R. P. Lindstedt, and W. P. Jones. A simplified reaction mechanism for
soot formation in nonpremixed flames. Combustion and Flame, 87:289–305, 1991.

[2] Hongsheng Guo, Fengshan Liu, and Gregory J. Smallwood. Soot and no formation
in counterflow ethylene/oxygen/nitrogen diffusion flames. Combustion Theory and
Modelling, 8(3):475–489, 2004.

Comments:

------------------

### Discretization methods
Time: Euler; first-order accurate

CFL: max 0.5

Advection: Gauss linear

Diffusion: Gauss linear

Pressure-velocity coupling: Low Mach number approximation; PIMPLE (number of outer loops: max. of 3 loops)

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 1 hour wall clock time is approximately t=0.0229 s computation time

* Estimated 8.40 s wall clock time per time-step dt, with dt = 1E-06 s  
* Chem Execution Time = 1.5 s per time step dt  
* Rad. Execution Time = 0.11 s per time step dt  

Simulation time: t=4.6255 s

Number of CPUs (MPI Processes): 144

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

(144 CPUs * 10.4653 hr / 1.2458e-06 hr / 2,196,880 cells) = 550.61

------------------

### Averaging period

0.1855 s (from t=4.44 s to t=4.6255 s)

------------------

### Special issues/problems

The runs are still on-going due to the computational cost; we are looking into runing the cases with AMR next.

------------------

### Relevant publications


