### Fire Phenomena
This page provides an overview of key fire dynamics phenomena of interest to the MaCFP Working Group as well as a list of Benchmark Experiments (i.e., fire modeling target cases) currently in the MaCFP repository that address these phenomena. 

Target phenomena are grouped into Condensed-Phase, Gas-Phase, or Couple Condensed- & Gas-Phase categories; for each phenomena of interest, direct links are provided to relevant Benchmark Experiments in the MaCFP Repo.

##### Condensed Phase Phenomena
# 
| **Priority** | **Condensed Phase Phenomena** | **Benchmark Experiment** |
| --- | --- | --- |
| Primary | Thermal decomposition of solid fuels | 6, 7 |
| | Ignition | 6 |
| | Gasification of condensed phase fuels | 7 (on matl-db repo..)|
|  ||  |
| Secondary | In-depth radiative absorption |
| | Charring |
| | Condensed phase heat transfer in complex materials |
| | Liquid phase transport effects |
||||
##### Gas Phase Phenomena
#
| **Priority** | **Gas Phase Phenomena** | **Benchmark Experiment** |
| --- | --- | --- |
| Primary | Buoyant plumes | 1 |
| | Convective heat transfer | 3b, 6a,b |
| | Radiative heat transfer | 3b, 6a,b |
| | Turbulent flow | 3a |
| | Turbulent mixing | 3a |
| | Species transport and composition | 3b |
||||
| Secondary | Soot formation and oxidation (aerosol species) | 3b |
| | Toxicity (yields of particles and toxic gases) | 3b |
| | Scale effects | 3b |
| | Compartment fire effects including ventilation |
| | Visibility |
| | Local extinction and re-ignition | 5 |
| | Suppression | 5 |
| | Fire growth | 6a,b |
| | Instabilities (large-scale puffing/small-scale phenomena) | 3a,3b |

##### Coupled Condensed- and Gas-Phase Phenomena
#
| Priority |  Condensed- and Gas-Phase Phenomena | Benchmark Experiment |
| --- | --- | --- |
| Primary | Fire spread | 6a, 6b |
| | Fire growth |
| Secondary | Wall-flame interactions |
||||

#### Benchmark Experiments
1. [Turbulent buoyant plumes](https://github.com/MaCFP/macfp-db/tree/master/Buoyant_Plumes)
   a. [Sandia Helium Plume](https://github.com/MaCFP/macfp-db/tree/master/Buoyant_Plumes/Sandia_Helium_Plume)
   b. [UMD Salt Water Plume](https://github.com/MaCFP/macfp-db/tree/master/Buoyant_Plumes/UMD_Salt_Water_Plume)

2. [Turbulent Gaseous Pool Fires with Prescribed Fuel Flow](https://github.com/MaCFP/macfp-db/tree/master/Gaseous_Pool_Fires)
   a. [NIST McCaffrey Natural Gas Flames](https://github.com/MaCFP/macfp-db/tree/master/Gaseous_Pool_Fires/McCaffrey_Flames)
   b. [Sandia Methane and Hydrogen flames](https://github.com/MaCFP/macfp-db/tree/master/Gaseous_Pool_Fires/Sandia_Flames)

3. [Turbulent Pool Fires with Liquid Fuel with Thermal Feedback Driven Fuel Flow](https://github.com/MaCFP/macfp-db/tree/master/Liquid_Pool_Fires)
   a. [Waterloo Methanol Pool Fire (30 cm)](https://github.com/MaCFP/macfp-db/tree/master/Liquid_Pool_Fires/Waterloo_Methanol)
   b. [NIST Methanol (30 and 100 cm), Ethanol (30 cm), Acetone (30 cm) Pool Fires](https://github.com/MaCFP/macfp-db/tree/master/Liquid_Pool_Fires/NIST_Pool_Fires)
4. [Turbulent  Gaseous Wall Fires](https://github.com/MaCFP/macfp-db/tree/master/Wall_Fires)
   a. [FM Global Vertical Wall Flames (Methane and Propane)](https://github.com/MaCFP/macfp-db/tree/master/Wall_Fires/FM_Vertical_Wall_Flames)

5. [Flame Extinction](https://github.com/MaCFP/macfp-db/tree/master/Extinction)
   a. [FM Burner](https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner)
   b. [UMD Methane and Propane Line Flames](https://github.com/MaCFP/macfp-db/tree/master/Extinction/UMD_Line_Burner)

6. [Fire Growth over Combustible Solids](https://github.com/MaCFP/macfp-db/tree/master/Fire_Growth)
   a. [NIST Parallel Panel (PMMA and other fuels)](https://github.com/MaCFP/macfp-db/tree/master/Fire_Growth/NIST_Parallel_Panel)
   b. [UMD Corner Wall (PMMA)](https://github.com/MaCFP/macfp-db/tree/master/Fire_Growth/UMD_SBI)