## General Information and Simulation Setup 

### Contributor

Name: Johannes Sailer, Karthik Krishnamurthy, Fabian Brännström 

Institution: University of Wuppertal (UWuppertal)

Country: Germany

### Test case

Case 5 - FM Burner

------------------------------------------------------------------------

### CFD package

Code: fireFOAM

Version: Esi v2006

------------------------------------------------------------------------

### Resolution

1.  Computational domain discretization (flow solver)
    -   closed domain with part of hood
    -   Domain: 1.2 m x 1.2 m x 1.8 m (closed domain with simplified
        hood)
    -   Cell size: 2.5 cm (very-coarse), 1.25 cm (coarse), 0.625 cm (medium)
    -   Cell type: Non-uniform
    -   Total cells: 163k (very coarse), 185k (coarse), 287k (medium)
    -   Comments: 
        - cylindrical refinement regions are applied

3.  Angular space discretization (radiation solver)
    - Number of solid angles: 16, 64
    - Comments: Impact for upwind setup very low

    ------------------------------------------------------------------------

### Initial conditions

Comments:
- Temperature: 300 K
- Pressure: 101325 Pa

------------------------------------------------------------------------

### Boundary conditions

Comments:

-   Fuel temperature: 298 K
-   Mass flow rate: 0.318 g/s (15 kW)
-   Co-flow velocity: 0.041 m/s
-   Co-flow 02 mass fraction: 0.231

------------------------------------------------------------------------

### Models (include parameters) 

- Turbulence model: WALE
- Combustion model: Eddy Dissipation Model (C_EDC = 1 or 2.5)
- Radiation model: Finite Volume Discrete Ordinates Method (fvDOM)
- Radiative fraction: Prescribed (\chi_rad=0.34 for Y_O2=0.231)
- Soot model: -
- Comments: -

------------------------------------------------------------------------

### Discretization methods

- Time: implicit, 2nd order (backward and 1st order Euler)
- maximum CFL: 0.8
- Divergence schemes: 
  - Velocity - Central difference (linear) and other settings with blended schemes (filterLinear2 0.1 0.5), 
  - Scalars - TVD (Gauss limitedLinear01 1.0-0.5)
  - radiative intensity - 1st upwind (upwind)
- Diffusion: Conservative Gaussian integration (Gauss linear corrected)
- Pressure-velocity coupling: PIMPLE (8 outer loops)

------------------------------------------------------------------------

### Table of setups
The table provides a list of all cases and the corresponding names for the setups, which are used for the plots as shortcut:

**Very coarse setup**:

| **Name**   | **Cell size** | **Combustion**       | **Rad.-angles** | **Rad.Freq** | **ddt**   | **div U**     | **scalars**           |
| ---------- | ---------- | -----------------    | ------------ | ----------- | --------- | ------------- | --------------------- |
| v0a        | v-coarse   | C_EDC 1 | 16           | 10          | backward     | linear        | limitedLinear01 05, h1    |
| v0b        | v-coarse   | C_EDC 1 | 16           | 10          | backward     | linear        | limitedLinear01 05, h1    |
| v0f        | v-coarse   | C_EDC 1 | 16           | 10          | backward     | linear        | limitedLinear01 05, h1    |

**Coarse setup**:
| **Name** | **Cell size** | **Combustion**         | **Rad.-angles** | **Rad.Freq** | **ddt** | **div U**   | **scalars**         |
| ---      | ---           | ----                   | ---             | ---          | ---     | ---         | ---                 |
| v2a      | coarse        | C_EDC 1   | 16              | 10           | Euler   | filt.Linear | limitedLinear01 1, h1   |
| v2b      | coarse        | C_EDC 1   | 16              | 10           | backward   | filt.Linear | limitedLinear01 1, h1   |
| v2c      | coarse        | C_EDC 1   | 16              | 10           | backward   | linear      | limitedLinear01 05, h1  |
| v2d      | coarse        | C_EDC 3   | 16              | 10           | backward   | linear      | limitedLinear01 05, h1  |
| v2e      | coarse        | C_EDC 3   | 16              | 10           | backward   | linear      | limitedLinear01 05, h05 |
| v2f      | coarse        | C_EDC 2.5 | 16              | 10           | backward   | linear      | limitedLinear01 05, h05 |
| v2g      | coarse        | C_EDC 2.5 | 16              | 10           | backward   | linear      | limitedLinear01 05, h05 |
| v2h      | coarse        | C_EDC 2.5 | 16              | 10           | backward   | linear      | limitedLinear01 05, h05 |
| v2i      | coarse        | C_EDC 2.5 | 64              | 1            | backward   | linear      | limitedLinear01 05, h05 |

**Medium setup**:
| **Name**   | **Cell size** | **Combustion**    | **Rad.-angles** | **Rad.Freq** | **ddt**   | **div U**     | **scalars**           |
| ---------- | ---------- | -----------------      | ------------ | ----------- | --------- | ------------- | --------------------- |
| v3a        | medium     | C_EDC 1   | 16           | 10          | Euler     | filt.Linear   | limitedLinear01 1, h1     |
| v3b        | medium     | C_EDC 1   | 16           | 10          | backward     | filt.Linear   | limitedLinear01 1, h1     |
| v3ba       | medium     | C_EDC 1   | 16           | 10          | backward     | filt.Linear   | limitedLinear01 05, h1    |
| v3c        | medium     | C_EDC 1   | 16           | 10          | backward     | linear        | limitedLinear01 05, h1    |
| v3e        | medium     | C_EDC 3   | 16           | 10          | backward     | linear        | limitedLinear01 05, h05   |
| v3f        | medium     | C_EDC 2.5 | 16           | 10          | backward     | linear        | limitedLinear01 05, h05   |
| v3g        | medium     | C_EDC 2.5 | 64           | 10          | backward     | linear        | limitedLinear01 05, h05   |
| v3i        | medium     | C_EDC 2.5 | 64           | 1           | backward     | linear        | limitedLinear01 05, h05   |

### Computational Cost (hh:mm:ss) 


Simulation time: 20-40 sec

Number of CPUs (MPI Processes): 18 (very coarse) - 24 (coarse and medium)

Wall clock time: -

Wall clock time per time step: -

CPU cost (Number of CPUs \* Wall clock time / Simulation time / Total
cells): - 

------------------------------------------------------------------------

### Averaging period

Averaging period: min. 15 sec (after initial developing period)

------------------------------------------------------------------------

### Special issues/problems
- spatial distribution of plots too low
- simulation time not tracked in detail

    ------------------------------------------------------------------------

### Relevant publications

none

