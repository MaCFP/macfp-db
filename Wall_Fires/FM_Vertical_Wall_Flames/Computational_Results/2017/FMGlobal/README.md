
### Contributor
Name: Ning Ren

Institution: FM Global

Country: USA

------------------

### Test case
FM Global Vertical Wall Burner.
CH4
C2H4
C2H6
C3H6

------------------

### CFD package
Code:FireFOAM

Version: FireFOAM-dev

------------------

### Resolution

#### Computational domain discretization (flow solver)
Domain: 0.38 m (spanwise) by 0.9 m (wall-normal) by 1.5 m (vertical)

Cell size: For the 3-mm grid: Near-wall region is 3 mm (wall-normal) x 7.5 mm (spanwise) x 7.5 mm (vertical); Far-field (wall distance > 0.24 m) is 6 mm x 15 mm x 15 mm

Cell type: Non-uniform cube

Total cells: 984,960 (3-mm grid), 6,152,472 (1.5-mm grid)

Comments: Except the grid convergence study of C3H6 at 17.05 g/m2/s, other cases used the 3-mm grid.

#### Angular space discretization (radiation solver)
Number of solid angles: 16

Comments: 

------------------

### Initial conditions
Comments: Quiescent

------------------

### Boundary conditions
Comments: Open boundaries are used on top and inlet (bottom and opposite to the wall). The two sides in the spanwise direction used cyclic boundary condition. In the wall burner region, fluctuations (15%) is added to the fuel flow rate to promote the laminar to turbulent transition. 

------------------

### Models (include parameters)
Turbulence model: WALE model (Cw = 0.55)

Combustion model: Eddy Dissipation Model with reaction rate from laminar diffusion (C_EDC = 4, C_diff = 4). 

Radiation model: fvDOM

Radiative fraction: Considering radiation absorption from fuel & cold soot in the near wall region (blocking effect), effective values (75% of the measured radiant fraction of wall-fire configuration) are used for all fuels, which are 12% for CH4, 13% for C2H6, 18% for C2H4 and 25% for C3H6.

Soot model: No soot model

Comments: The soot depths describes the thickness of the flame. In the simulation, the flame thickness is obtained from the mean gas temperature profiles using T=900 K.

------------------

### Discretization methods
Time: First order Euler (Euler)

Advection: Velocity - Second order, unbounded central difference (Gauss linear)

Diffusion: Second order, conservative Gaussian integration (Gauss linear corrected;)

Pressure-velocity coupling: PIMPLE algorithm

------------------

### Computational Cost (hhh:mm:ss)
Wall clock time: ; 7:22:15 (3-mm grid); 64:55:50 (1.5-mm grid)

Simulation time: 16 s

Number of cores: 48 (3-mm grid); 144 (1.5-mm grid)

CPU cost (Number of cores * Wall clock time / Simulation time / Total cells): 21.34 hr/s/Million-Cells (3-mm grid); 95.12 hr/s/Million-Cells (1.5-mm grid)

------------------

### Averaging period
12 s

------------------

### Special issues/problems

------------------

### Relevant publications
1. J.L. de Ris, G.H. Markstein, L. Orloff, and P.A. Beaulieu, “Similarity of Turbulent Wall Fires,” Fire Safety Science, Vol. 7, pp. 259-270.

2. N. Ren, Y. Wang, S. Vilfayeau and A. Trouvé, “Large Eddy Simulation of Turbulent Vertical Wall Fires Supplied with Gaseous Fuel through Porous Burners,” Combustion and Flame, Vol. 169, (2016), pp. 194-208.


