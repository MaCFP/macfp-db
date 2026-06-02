### Contributor
Name: Kevin McGrattan

Institution: National Institute of Standards and Technology (NIST)

Country: USA

------------------

### Test case

JIS Facade

------------------

### CFD package
Code: Fire Dynamics Simulator (FDS) 

Version: 6.10.1

------------------

### Resolution


#### Computational domain discretization (flow solver)
Domain: 3.6 m × 3.6 m × 4.5 m

Cell size: 1.25 cm, 2.5 cm, 5 cm

Cell type: cubic

Total cells: 1.25 cm case, 1.5 M (90 mesh); 2.5 cm case, 0.59 M (34 mesh); 5 cm case, 0.47 M (27 mesh)

#### Angular space discretization (radiation solver)
Number of solid angles: 104, default radiation solver

Comments: Default FDS radiation solver with full update every 15 time steps

------------------

### Initial conditions
Comments: Quiescent. The fire is ramped up to the first HRR, held steady, then ramped to the next HRR, held steady, etc.

------------------

### Boundary conditions
Comments: Open, i.e. passive, external boundaries. The hood is not modeled. Convection modeled via empirical correlations. Momentum transfer is modeled via log-law wall model with WALE model used in the first grid cell off the wall.

------------------

### Models (include parameters)
Turbulence model: Deardorff (algebraic k-sgs); Sc = 0.5; Pr = 0.5

Combustion model: Two-step serial fast reactions for propane [2]. No extinction model or re-ignition model used.

Radiation model: Finite-volume method, first-order upwind

Radiative fraction: Predicted

Comments:  0.75 of carbon atoms in propane molecule are assumed to be converted to CO in the first step of a two-step serial (fast-fast) reaction scheme. 0.25 of the carbon atoms are converted to soot. Both CO and soot are allowed to oxidize, with a final specified post-flame soot yield of 0.019 and CO yield 0.005.


------------------

### Pyrolysis Models (include parameters)
Solver: 1-D heat conduction into wall

Radiation absorption model: Opaque wall surface; emissivity 0.9

Material property set: Wall properties specified in Ref. 1


------------------

### Discretization methods
Time: Second-order accurate Runge-Kutta predictor-corrector scheme

CFL: Time step bound with a CFL limits 0.8 to 1.0

Advection: Superbee flux limiter

Diffusion: Central-difference

Pressure-velocity coupling: Low Mach number assumption; Poisson equation solved for pressure

------------------

### Computational Cost (hh:mm:ss)
Wall clock time: 1.25 cm: 7.2 h; 2.5 cm: 2.4 h; 5 cm: 1.3 h

Simulation time: 1.25 cm: 648 CPU-h; 2.5 cm: 82 CPU-h; 5 cm: 35 CPU-h

Number of CPUs (MPI Processes): 1.25 cm: 90; 2.5 cm: 34; 5 cm: 27

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells): 1.25 cm: 0.0017; 2.5 cm: 0056; 5 cm: 0.003 CPU-s/cell/s

------------------

### Averaging period

All devices are time-averaged for 30 s.

------------------

### Special issues/problems

The modeled thermocouples are assumed to have a diameter of 1 mm. The modeled heat flux gauges are assumed to be at ambient temperature and use the same radiative and convective heat transfer models as the surrounding wall.

------------------

### Relevant publications
1. X. Sun, H. Yoshioka, T. Noguchi, Y. Nishio, Y. Ohmiya, T. Hayakawa, and B. Zhou. Large eddy
simulations fire modeling of JIS A 1310 facade calibration test with respect to sidewall. Fire and
Materials, 48:411–425, 2024.

2. K. McGrattan, R. McDermott, and J. Floyd. A simple two-step reaction scheme for soot and co.
Proceedings of the Tenth International Seminar on Fire and Explosion Hazards (ISFEH10), Oslo,
Norway, 2022-05-23 2022.

### Plotting scripts for NIST simulations of the JIS A 1310 experiments

The Python script in this directory creates plots that compare FDS and experimental results for the JIS Facade experiments. The plots are based on those found in Sun et al., Fire and Materials, 48:411–425, 2024. To create the plots, you should only need to run a single Python script:
```
python NIST_JIS_Facade_plots.py
```
The script creates a sub-directory called `Plots` containing:
   1. Experimental and simulated temperature contours in three vertical planes normal to the wall (Fig. 8 from Sun et al.)
   2. Experimental and simulated surface temperature profiles across and above the window (Fig. 9 from Sun et al.)
   3. Experimental and simulated heat flux profiles above the window (Fig. 10, Row C from Sun et al.)

