## General Information and Simulation Setup 

### Contributor

Name: Shivam Mittal, Fabian Brännström

Institution: University of Wuppertal (UWuppertal)

Department: Fire Dynamics

Country: Germany

### Test case

Case 5 - FM Burner

------------------------------------------------------------------------

### CFD package

Code: FDS

Version: FDS6.7.8-88-g922085eba-nightly

------------------------------------------------------------------------

### Resolution


####  Computational domain discretization (flow solver)
    -   closed domain with part of hood
    -   Domain: 1.2 m x 1.2 m x 1.2 m (closed domain with no hood )
    -   Cell size: 0.5 cm (in fine flame region)
    -   Cell type: cubes
    -   Total cells: XXX


#### Angular space discretization (radiation solver)
    - Number of solid angles: 104, 512
    - Time steps between full solution of all angles: 1, 10, 50, 200, 1000
      - This corresponds roughly to: 5e-4s, 5e-3s, 2.5e-2s, 5e-1s, 1e-2s

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

Turbulence model: Deardoff (algebraic k_sgs); Sc_t=0.5; Pr_t=0.5

Combustion model: Two-step fast-fast serial reactions

Radiation model: Finite-volume, upwind, first-order accurate

Radiative fraction: Predicted based on RadCal tabulated absorption coefficients

- Comments: -

------------------------------------------------------------------------

### Discretization methods

Time: Predictor-Corrector; second-order accurate

CFL: 0.8 to 1.0

Advection: CHARM Flux Limiter

Diffusion: Second-order accurate central difference

Pressure-velocity coupling: Low Mach number approximation; solution of Poisson equation for pressure

------------------------------------------------------------------------

### Computational Cost (hh:mm:ss) 


Simulation time: 70-200 sec

Number of CPUs (MPI Processes): 64 cores

Wall clock time: -

Wall clock time per time step: -

CPU cost (Number of CPUs \* Wall clock time / Simulation time / Total
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

- The `Time Step` referes to the number of time steps when complete radiation solving is accomplished.
- Average time step size is about `5e-4` between each time step (though this depends especially during the initial development phase)

------------------------------------------------------------------------

### Averaging period
- Different averaging times is evaluated for radiative wall heat flux.
  - Averaging is started from the end of the time data and varied in different steps.

- If not otherwise stated the complete time span is used for averaging.


------------------------------------------------------------------------

### Special issues/problems
- 

------------------------------------------------------------------------

### Relevant publications

none

