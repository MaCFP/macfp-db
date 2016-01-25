##FM vertical wall fire data

The experimental data are summarized in the following .csv files, which include soot depth at different elevation locations and fuel flow rates for propylene, uncorrected and corrected temperature profiles at Z = 771 mm with different fuel flow rates for propylene, flame outward radiance at different elevation locations and fuel flow rates for propylene, and total heat flux at different fuel flow rates for methane, ethane, ethylene and propylene. Those data have been published in Refs. 1 and 2. 

Detailed description of the .csv files are

#####C3H6_Soot_Depth
| header | units | description |
| ------ | ----- | ----------- |
| Flow_Rate | [g/m2/s] | Fuel flow rates |
| Z=365mm | [mm] | Soot depth measurement at elevation location, Z = 365 mm |
| Flow_Rate | [g/m2/s] | Fuel flow rates |
| Z=537mm | [mm] | Soot depth measurement at elevation location, Z = 537 mm |
| Flow_Rate | [g/m2/s] | Fuel flow rates |
| Z=771mm | [mm] | Soot depth measurement at elevation location, Z = 771 mm |
| Flow_Rate | [g/m2/s] | Fuel flow rates |
| Z=1022mm | [mm] | Soot depth measurement at elevation location, Z = 1022 mm |
| Flow_Rate | [g/m2/s] | Fuel flow rates |
| Z=1317mm | [mm] | Soot depth measurement at elevation location, Z = 1317 mm |

#####C3H6_T_Thermocouple_at_771mm
| header | units | description |
| ------ | ----- | ----------- |
| Y | [mm] | Distance to the wall |
| m=22.49 | [K] | Uncorrected thermocouple temperature profile at fuel flow rate of 22.49 g/m2/s |
| m=22.37 | [K] | Uncorrected thermocouple temperature profile at fuel flow rate of 22.37 g/m2/s |
| m=17.05 | [K] | Uncorrected thermocouple temperature profile at fuel flow rate of 17.05 g/m2/s |
| m=12.68 | [K] | Uncorrected thermocouple temperature profile at fuel flow rate of 12.68 g/m2/s |
| m=11.85 | [K] | Uncorrected thermocouple temperature profile at fuel flow rate of 11.85 g/m2/s |
| m=8.75 | [K] | Uncorrected thermocouple temperature profile at fuel flow rate of 8.75 g/m2/s |

#####C3H6_T_Gas_at_771mm
| header | units | description |
| ------ | ----- | ----------- |
| Y | [mm] | Distance to the wall |
| m=22.49 | [K] | Corrected thermocouple (Gas) temperature profile at fuel flow rate of 22.49 g/m2/s |
| m=22.37 | [K] | Corrected thermocouple (Gas) temperature profile at fuel flow rate of 22.37 g/m2/s |
| m=17.05 | [K] | Corrected thermocouple (Gas) temperature profile at fuel flow rate of 17.05 g/m2/s |
| m=12.68 | [K] | Corrected thermocouple (Gas) temperature profile at fuel flow rate of 12.68 g/m2/s |
| m=11.85 | [K] | Corrected thermocouple (Gas) temperature profile at fuel flow rate of 11.85 g/m2/s |
| m=8.75 | [K] | Corrected thermocouple (Gas) temperature profile at fuel flow rate of 8.75 g/m2/s |

#####C3H6_Flame_Radiance
| header | units | description |
| ------ | ----- | ----------- |
| Flow_Rate | [g/m2/s] | Fuel flow rates |
| Z=66mm | [kW/m2/sr] | Outward flame radiance at elevation location: Z = 66 mm |
| Z=330mm | [kW/m2/sr] | Outward flame radiance at elevation location: Z = 330 mm |
| Z=594mm | [kW/m2/sr] | Outward flame radiance at elevation location: Z = 594 mm |
| Z=990mm | [kW/m2/sr] | Outward flame radiance at elevation location: Z = 990 mm |

#####C3H6_Total_Heat_Flux
| header | units | description |
| ------ | ----- | ----------- |
| Z | [m] | Elevation (from flame leading edge) |
| m=12.68 | [kW/m2] | Total flame-to-wall heat flux at fuel flow rate of 12.68 g/m2/s |
| m=17.05 | [kW/m2] | Total flame-to-wall heat flux at fuel flow rate of 17.05 g/m2/s |
| m=22.37 | [kW/m2] | Total flame-to-wall heat flux at fuel flow rate of 22.37 g/m2/s |

#####Other_Fuel_Total_Heat_Flux
| header | units | description |
| ------ | ----- | ----------- |
| Z | [m] | Elevation (from flame leading edge) |
| CH4_m=10.6 | [kW/m2] | Total flame-to-wall heat flux for methane at fuel flow rate of 10.6 g/m2/s |
| C2H6_m=10.2 | [kW/m2] | Total flame-to-wall heat flux for ethane at fuel flow rate of 10.2 g/m2/s |
| C2H4_m=11.5 | [kW/m2] | Total flame-to-wall heat flux for ethylene at fuel flow rate of 11.5 g/m2/s |

####Reference
[1] J.L. de Ris, G.H. Markstein, L. Orloff, and P.A. Beaulieu, “Similarity of Turbulent Wall Fires,” Fire Safety Science, Vol. 7, pp. 259-270.

[2] N. Ren, Y. Wang, S. Vilfayeau and A. Trouvé, “Large Eddy Simulation of Turbulent Vertical Wall Fires Supplied with Gaseous Fuel through Porous Burners,” Combustion and Flame, Article in Press.

