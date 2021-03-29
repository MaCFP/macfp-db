Contributor  
Name: Li MA, Fatiha NMIRA, Jean-Louis CONSALVI

Institution: Direction R&D EDF and Aix-Marseille Université  

Country: France

Test case: Case 3-a 30 cm Liquid Methanol Pool Fire Waterloo configuration  
CFD package: Code_Saturne  
Code: https://www.code-saturne.org/cms/  

Version: 5.0.9  

Resolution  
Computational domain discretization (flow solver)  
Domain: (x; y; z) of 3*3*3 m^3  

Mesh:  
The mesh is uniformly refined in the region of 0.40.40.1 m3 centered  
around the burner, with a minimal grid spacing equal to 2.5 mm.  
Outside this region, Dx and Dy are stretched progressively towards  
the sides of the computational domain.  
In the vertical direction, Dz is stretched from z = 0.1 m to z = 0.2 m to reach 5 mm.  
An uniform Dz = 5 mm is then applied up to z = 0.6 m.  
Above z = 0.6 m, Dz is stretched progressively.  

Cell type: Non-uniform  

Total cells:  

Comments:  
Check CNF paper for more details about the mesh.  

Angular space discretization: FVM  
Number of solid angles: Polar angles = 48, Azimuthal angles = 96.  

Models (include parameters)  
Turbulence model: LES with Dynamic Smagorinsky model (SGS momentum stress) and Dynamic Diffusivity model (SGS scalar flux)  

Combustion model: Steady Laminar Flamelet with a transport equation for the second moment of the mixture fraction to obtain the SGS variance

Radiation model: RCFSK

Radiative fraction: -

Soot model: -

Comments:  
Check CNF paper for more details

Discretization methods  
Time: second-order Crank-Nicolson scheme

CFL: the time step is set to 5 * 10^(-4) s which corresponds  
to an averaged maximum CFL of 0.6.

Advection: A second order central scheme with TVD scheme

Diffusion: A second-order central difference scheme

Simulation Time: 25 s  
Averaging period: 19 s (The first 6s of simulation were used to establish a statistically stationary flow)

Relevant publications  
L. Ma, F. Nmira, J.L. Consalvi. Large Eddy Simulation of medium-scale methanol pool fires - effects of pool boundary conditions, Combustion and Flame, 2020, 336-354, 2020.

