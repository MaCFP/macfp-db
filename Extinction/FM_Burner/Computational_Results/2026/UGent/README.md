### Contributor

Name: Youk Moorthamers, Alexander Snegirev, Georgios Maragkos, Bart Merci

Institution: Ghent university

Country: Belgium

------------------

### Test case

FM burner

------------------

### CFD package

Code: Ansys Fluent

Version: 2024R2

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 1.22 m x 1.22 m 2.00 m (includes the 1.83 m high compartment and conical extraction hood)

Cell size: approx. 5 mm, 1 cm, 2 cm

Cell type: Hexahedral cells, structured mesh with refinement zones in the flame area 

Total cells: 1,429,026 (5 mm); 545,172 (1 cm); 207,080 (2 cm)

Comments: Refinement only for cells in the flame zone

#### Angular space discretization (radiation solver)

Number of solid angles: 72

Comments: For isotropic angular discretization in fluent, the number of solid angles equals 8*N², where N is the number of polar and azimuthal angles per octant, here N = 3. Solution method: Discrete Ordinates (DO) with first-order upwind scheme

------------------

### Initial conditions

Comments: Ambient temperature and pressure set to 298 K and 101325 Pa, respectively. Simulations are initialized with the specified oxygen fraction in the domain. Oxygen in the co-flow is always set constant.

------------------

### Boundary conditions

A fixed oxidizer co-flow velocity (0.041 m/s) and fuel mass flow-rate are applied. 
Compartment walls and ceiling are "wall" BCs. A constant extraction flow rate of 0.073 m³/s is specified in the extraction hood.
Since there is a gap between the extraction pipe and the ceiling, an ambient air pressure inlet is specified at the top.

A 1.5 cm high anchoring zone is applied above the burner to approximate the experimental anchor. 

Comments:

------------------

### Models (include parameters)

Turbulence model: Standard Smagorinsky-Lilly sgs model, C_s = 0.1 

Combustion model: Subgrid Combustion Model (SCM) with a single-step reaction using autoignition based temeprature-dependent kinetic parameters [1] 

Radiation model: Discrete Ordinates, Gray version of Weighted Sum of Gray Gases (WSGG) with the path length calculated as L=3.6V/A.

Radiative fraction: Predicted with TRI factor that includes two-zone temperature non-uniformity and unresolved temperature fluctuations [1]

Soot: Two-equation Moss-Brooks model with a piecewiese polynomial dependency of the precursor concentration on mixture fraction. The polynomial is calibrated with a single pre-cursor constant C_pre, see [2] :
    C_pre = 2.5 for C2H4 -> calibrated on the soot predictions of the FM burner flame at X_O2 = 0.21
    C_pre = 3.0 for C3H6
    C_pre = 2.0 for C3H8
    C_pre = 1.0 for CH4 (by definition)

Comments: C_pre required re-calibration at reduced oxygen

------------------

### Discretization methods

Time: Bounded Second Order Implicit

CFL: Time step chosen constant to keep CFL below 1 in the flame zone

Spatial Discretization:
    Gradients:  Least Squares Cell Based
    Pressure:   Second Order
    Momentum:   Bounded Central Differencing
    Species, soot, nuclei and energy: Second Order Upwind

Pressure-velocity coupling: COUPLED, with Rhie-Chow momentum-based flux formulation

------------------

### Computational Cost (hh:mm:ss)

Wall clock time: 136,596 s (5 mm grid size - no extinction)

Simulation time: 50 s

Number of CPUs (MPI Processes): 160 (of a 48 node 2x 96-core AMD EPYC 9654 (Genoa @ 2.4 GHz) cluster)

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 0.306

------------------

### Averaging period

total simulation time: 55 s
 
averaged statistics: last 50 s

Comments: .

------------------

### Special issues/problems
Temperature statistics: RMS and PDF, deviate significantly from the experiment. The reason is likely related to the thermocouple compensation. For one simulation (air, 5 mm) a thermocouple temperature T_tc has been calculated from which a reconstructed gas temperature T_g,rec is obtained . This exercise shows a strong sensitivity of the temperature statistics (mainly RMS and PDF) to the convective time scale. Good agreement between the temperature statistics (computed from T_exp and T_g,rec) can be obtained if the convective time scale is reduced by a factor of two in the estimation of the gas temperature from a thermocouple temperature. 

------------------

### Relevant publications
1. Y. Moorthamers, A. Snegirev, G. Maragkos, J. At Thabari, B. Merci, Large eddy simulations of weakly turbulent diffusion flames in an oxygen-reduced co-flow using a new subgrid combustion model, Fire Saf. J. 157 (2025)  104513, https://doi.org/10.1016/j.firesaf.2025.104513
2. A. Snegirev, E. Markus, E. Kuznetsov, J. Harris, T. Wu, On soot and radiation modeling in buoyant turbulent diffusion flames, Heat Mass Transf. 54 (2018) 2275-2293, https://doi.org/10.1007/s00231-017-2198-x. 