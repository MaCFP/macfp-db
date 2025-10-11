## JIS A 1310 façade calibration test

The full-scale façade standard test is widely employed as a comprehensive method to assess the façade fire spread. Within this approach, the calibration test without combustible façade decouples the intricate interaction between gas-phase combustion and material pyrolysis, which simplifies diagnostics and provides an ideal scenario for model validation. This repository contains data for calibration tests in accordance with JIS A 1310. The calibration tests
were conducted to obtain the flame morphologies, gas-phase temperature, and heat flux of over-ventilated façade fires. The results of Sun et al. (Fire & Materials, 2024) highlight that the enhancement of sidewall in façade flame spread occurs under external heat release rate, and the 0.2 m sidewall distance for the designated JIS test is identified as a critical threshold increasing façade thermal load.

<img src="JIS_A_1310_geometry.png" alt="Alt text" height="500"/> <img src="Sun_FAM_2024_TC_tree.png" alt="Alt text" height="500"/>

<img src="Sun_FAM_2024_flame_images.png" alt="Alt text" width="850"/>

#### Wall materials

Chamber walls: a 50-mm-thick exposed layer of alumina fiber blanket (material properties close to those of the ceramic fiber blanket in Table 2 of the 2023 FAM paper) and a 150-mm-thick back layer of ceramic fiber block (material properties close to those of the ceramic fiber blanket in Table 2 of the 2023 FAM paper).

Façade wall: a 25-mm-thick exposed layer of ceramic fiber blanket (material properties in Table 2 of the 2023 FAM paper) and a 24-mm-thick back layer of calcium silicate board (material properties in Table 2 of the 2023 FAM paper)

#### Thermocouple Measurements

The thermocouples used for the measurements are illustrated in the figure. Two types of thermocouples were employed: sheathed-type thermocouples were used in the region around the opening which is directly exposed to ejected flame, while exposed-junction thermocouples were used in other regions. The specifications of the two types are as follows:
 - K-type stainless-steel sheathed thermocouple, 3.2 mm bead diameter (approx. 0.6 mm wire).
 - K-type thermocouple, 2 mm bead diameter (0.65 mm wire, glass-fiber insulated, exposed junction).

The thermocouple modeling used in the reference [Sun, 2024] is as follows:
 - rho (Density): 8908 kg/m3
 - Cp (Heat capacity): 440 J/(kg K)
 - d (Diameter): 0.002 m
 - epsilon (Emissivity): 1

<img src="Information_about_thermocouples.png" alt="Alt text" width="850"/>

#### Experimental Data Files

Experimental data are tabulated in [JIS_Facade/Experimental_Data](https://github.com/MaCFP/macfp-db/tree/master/Wall_Fires/JIS_Facade/Experimental_Data)

#### References
1. Sun, X., Yoshioka, H., Noguchi, T., Nishio, Y., Ohmiya, Y., Hayakawa, T., Zhou, B., Large eddy simulations fire modeling of JIS A 1310 façade calibration test with respect to sidewall, Fire & Materials  48 (2024) 411-425.
