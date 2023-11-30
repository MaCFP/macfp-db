## General Information and Simulation Setup 

### Contributor

Name: Shivam Mittal, Fabian Brännström

Institution: University of Wuppertal (UWuppertal)

Department: Fire Dynamics

Country: Germany

### Test case

Case 5 - FM Burner

------------------------------------------------------------------------

### General Comments
Settings were mainly used by the setup from NIST which was applied for
MaCFP-2. This is one of the test cases for MaCFP-Radiation subgroup
and therefore further investigated.

Here the focus is on some radiation settings and the impact of
averaging (see some further information below).

------------------------------------------------------------------------

### CFD package

Code: FDS

Version: FDS6.7.8-88-g922085eba-nightly

------------------------------------------------------------------------

### Resolution


Computational domain discretization (flow solver)
-   closed domain with part of hood
-   Domain: 1.2 m x 1.2 m x 1.2 m (closed domain with no hood )
-   Cell size: 0.5 cm (in fine flame region)
-   Cell type: cubes
-   Total cells: XXX


Angular space discretization (radiation solver)
- Number of solid angles: 104 (default), 512
- Time steps between full solution of all angles: 1, 10, 50, 200, 1000, 2000, 4000
  - This corresponds roughly to a time between full radiation simulation of : 5e-4s, 5e-3s, 2.5e-2s, 1e-1s, 5e-1s, 1s, 2s

Comments: Otherwise default FDS radiation solver

### Initial conditions

Comments:
- Temperature: 300 K
- Pressure: 101325 Pa

------------------------------------------------------------------------

### Boundary conditions

Comments:

-   Fuel temperature: 298 K
-   Mass flow rate: 0.318 g/s (15 kW) - slightly larger inlet velocity than in experiment
-   Co-flow velocity: 0.041 m/s
-   Co-flow 02 mass fraction: 0.231

------------------------------------------------------------------------

### Models (include parameters) 

- Turbulence model: Deardoff (algebraic k_sgs); Sc_t=0.5; Pr_t=0.5

- Combustion model: Two-step fast-fast serial reactions

- Radiation model: Finite-volume, upwind, first-order accurate

- Radiative fraction: Predicted based on RadCal tabulated absorption coefficients

- Comments: -

------------------------------------------------------------------------

### Discretization methods

- Time: Predictor-Corrector; second-order accurate

- CFL: 0.8 to 1.0

- Advection: CHARM Flux Limiter

- Diffusion: Second-order accurate central difference

- Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------------------------------------------------------------

### Computational Cost (hh:mm:ss) 


- Simulation time: 70-200 sec

- Number of CPUs (MPI Processes): 64 cores

- Wall clock time: -

- Wall clock time per time step: -

- CPU cost (Number of CPUs \* Wall clock time / Simulation time / Total
cells): - 

------------------------------------------------------------------------

### Radiation Setups

 | Name | Time Step | Radiation Angles |
 |------|-----------|------------------|
 | V1   | 10        | 104              |
 | V2   | 10        | 512              |
 | V3   | 1         | 104              |
 | V4   | 1         | 512              |
 | V5   | 50        | 104              |
 | V6   | 50        | 512              |
 | V7   | 1000      | 104              |
 | V8   | 1000      | 512              |
 | V9   | 200       | 104              |
 | V10  | 200       | 512              |
 | V11  | 2000      | 104              |
 | V12  | 2000      | 512              |
 | V13  | 4000      | 104              |
 | V14  | 4000      | 512              |

- The `Time Step` referes to the number of time steps when complete radiation solving is accomplished.
- Average time step size is about `5e-4` between each time step (though this depends especially during the initial development phase)
- Based on this average step size of about `5e-4` sec we have a full radiation calculation of about each `2.0` sec for the variants `V13` and `V14`.

- Though the radiative fraction is post-processed, but is expected that these changes will have minor impact on the results.
- The main impact of these setups will be on the averaging and the heat flux to the wall which is slightly outside the scope of MaCFP3.


------------------------------------------------------------------------

### Averaging period
- Different averaging times is evaluated for radiative wall heat flux.
  - Averaging is started from the end of the time data and varied in different steps.

- If not otherwise stated the complete time span is used for averaging.



------------------------------------------------------------------------

### Post-Processing
The main Post-processing is done for the following monitors:
- Development of total radiative fraction over time
- Vertical radiation emission over height (symmetry line above burner)

Config file: FM_Burner_cmp_config.csv
- General plots for radiation

Config file: FM_Burner_cmp_config_WallRadiation.csv
- Additional plots with focus on wall heat flux 

Config file: FM_Burner_cmp_config_Transient.csv
- Focus on (backward) averaging and initial transient based [1]
- `dNM` is a time estimation for the initial transient before averaging should be started (see section 2.1 in [1]) 
- Backward averaging means that based on the available data; different time spans are used for averaging always starting at `200s` and going back to `0s`.

Monitor positions for plots
- General
  - MEAN_Radiative_Wall_Flux: x=0.6m, y=0m, z=0.106-0.8128m
  - STD_Radiative_Wall_Flux: x=0.6m, y=0m, z=0.106-0.8128m
- Initial Transient
  - `radfl_FM_rad_distribution_x06_y0_19_dNM`: x=0.6m, y=0m, z=Xm
  - `radfl_FM_rad_distribution_x06_y0_19_gi`: x=0.6m, y=0m, z=0.8128m
- Backward Averaging
  - `radfl_middle_x0_y_zn37_9`: x=0m, y=-0.15, z=-0.37m

------------------------------------------------------------------------

### Infos about plot scripts

Three different scripts are used for the plots:
- FM_Burner_plot_cmp.py
- FM_Burner_plot_cmp_Transient.py
- FM_Burner_plot_cmp_WallRadiation.py

The first one is producing plots for the total radiative heat flux and radiative power over the height.

The other plots are a bit outside the initial scope and were put into a different folder.



------------------------------------------------------------------------

### Special issues/problems
- 
------------------------------------------------------------------------

### Relevant publications

[1] Bergmann, Michael, Christian Morsbach, Graham Ashcroft, and Edmund Kügeler. ‘Statistical Error Estimation Methods for Engineering-Relevant Quantities From Scale-Resolving Simulations’. Journal of Turbomachinery 144, no. 3 (1 March 2022): 031005. https://doi.org/10.1115/1.4052402.

