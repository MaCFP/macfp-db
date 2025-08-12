## JIS A 1310 façade calibration test experimental Data Files

The full-scale façade standard test is widely employed as a comprehensive method to assess the façade fire spread. Within this approach, the calibration test without combustible façade decouples the intricate interaction between gas-phase combustion and material pyrolysis, which simplifies diagnostics and provides an ideal scenario for model validation. This repository contains data for calibration tests in accordance with JIS A 1310. The calibration tests
were conducted to obtain the flame morphologies, gas-phase temperature, and heat flux of over-ventilated façade fires. The results of Sun et al. (Fire & Materials, 2024) highlight that the enhancement of sidewall in façade flame spread occurs under external heat release rate, and the 0.2 m sidewall distance for the designated JIS test is identified as a critical threshold increasing façade thermal load.

#### JIS A 1310 Geometry

<img src="JIS_A_1310_geometry.png" alt="Alt text" height="600"/> <img src="Sun_FAM_2024_TC_tree.png" alt="Alt text" height="600"/>

#### Experimental Data Files

Experimental data are tabulated in [JIS_Facade/Experimental_Data](https://github.com/MaCFP/macfp-db/tree/master/Wall_Fires/JIS_Facade/Experimental_Data)

#### Mean_temperature.csv
* The file contains the mean temperature measured at different HRR(600kW, 750kW, 900kW).
  X, Y and Z indicate the location of thermocouples.
  X is the distance from the facade surface (m).
  Y is the distance from the center of the opening parallel to the facade surface (m).
  Z is the distance from the upper edge of the opening in vertical direction (m).

#### Mean_heat_flux.csv
* The file contains the mean heat flux on the facade surface measured at different HRR (600kW, 750kW, 900kW).
  Heat flux meters were located on the center line of the facade.
  Z is the distance from the upper edge of the opening in vertical direction (m).

#### Notes
The experiments were conducted three times by shifting the position of the thermocouples (Y=0, 0.2275, 0.405). In each experiment, the gas flow rate was increased every 5 minutes (0-5 minutes: 600 kW, 5-10 minutes: 750 kW, 10-15 minutes: 900 kW).  The temperature was measured using a two-thermocouple probe, and the **reported data is corrected for radiation**. The experimental data shows the mean value for the last 3 minutes of each 5 minute period at each gas flow rate. The heat flux value is the mean value of the three experiments.

<img src="Sun_FAM_2024_flame_images.png" alt="Alt text" width="850"/>

#### References
1. Sun, X., Yoshioka, H., Noguchi, T., Nishio, Y., Ohmiya, Y., Hayakawa, T., Zhou, B., Large eddy simulations fire modeling of JIS A 1310 façade calibration test with respect to sidewall, Fire & Materials  48 (2024) 411-425.
