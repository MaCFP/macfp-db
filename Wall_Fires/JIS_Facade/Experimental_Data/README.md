## JIS A 1310 façade calibration test experimental Data Files

#### Sun_FAM_2024_mean_temperature.csv
* The file contains the mean temperature measured at different HRR(600kW, 750kW, 900kW).
  X, Y and Z indicate the location of thermocouples.
  X is the distance from the facade surface (m).
  Y is the distance from the center of the opening parallel to the facade surface (m).
  Z is the distance from the upper edge of the opening in vertical direction (m).

#### Sun_FAM_2024_mean_heat_flux.csv
* The file contains the mean heat flux on the facade surface measured at different HRR (600kW, 750kW, 900kW).
  Heat flux meters were located on the center line of the facade.
  Z is the distance from the upper edge of the opening in vertical direction (m).

#### Notes

* The experiments were conducted three times by shifting the position of the thermocouples (Y=0, 0.2275, 0.405). In each experiment, the gas flow rate was increased every 5 minutes (0-5 minutes: 600 kW, 5-10 minutes: 750 kW, 10-15 minutes: 900 kW).  The temperature was measured using a k-type thermocouple net. The experimental data shows the mean value for the last 3 minutes of each 5 minute period at each gas flow rate. The heat flux value is the mean value of the three experiments.

* Some parts of the data presented here in the MaCFP repository have been revised from the published version [Sun, 2024].  Following are clarifications to avoid confusion when comparing with the paper. The experimental data at Y=0.2275 in the reference [Sun, 2024] was mistakenly averaged over the first 3 minutes of each 5-minute period at each gas flow rate. Therefore, in this data set, the experimental data at Y=0.2275 were revised to the average for the last 3 minutes of each 5-minute period at each gas flow rate. As a result, the following differences exist between this data set and the experimental data shown in Figure 8, 9 and 10 of the reference [Sun, 2024].

  * Figure 8: The data used for the contour plots of "Middle-right" in section (A) differ from this data set. The larger discrepancies occur at:
  600kW: X = 0 to 0.2, Z = -0.8 to 1, values are approximately 100°C to 200°C higher than the reference.
  750kW: X = 0, Z = 0.1 to 0.3, values are approximately 50°C higher than the reference.
  900kW: X = 0, Z = 0.1 to 1, values are approximately 50°C higher than the reference.

  * In addition, in all contour plots of Figure 8, the temperatures at the bottom of the opening (Z = -0.9, X = 0.4, 0.8) were assumed to be the same as those at Z = -0.9, X = 0. Since this assumption was made only for visualization purposes, these values are excluded from this data set.

  * Figure 9: The data used for the plots (600kW-exp, 750kW-exp, 900kW-exp) in section (B), middle-right, differ from this data set in the same manner as described for Figure 8.

  * Figure 10: The data used for the plots (600kW-exp, 750kW-exp, 900kW-exp) in section (C) differ from this data set by within 1kW/m2.

#### References
1. Sun, X., Yoshioka, H., Noguchi, T., Nishio, Y., Ohmiya, Y., Hayakawa, T., Zhou, B., Large eddy simulations fire modeling of JIS A 1310 façade calibration test with respect to sidewall, Fire & Materials  48 (2024) 411-425.
