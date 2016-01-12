##McCaffrey Centerline Plume Correlations

####Introduction

In [McCaffrey, 1979], a burner using natural gas (35 kJ/L [45 MJ/kg assuming 19 g/gmol]) at various controlled rates was constructed of a porous refractory material 0.3 m square.  Along the centerline of the burner, velocity and temperature were measuered using bi-directional probe and thermocouple, respectively.  The centerline data collapses when scaled by the Froude number as shown in the plots below.

Radiant fraction measurements for natural gas were made in [McCaffrey, 1981].  For convenience, we have extracted the data from that report for the heat release rates reported in [McCaffrey, 1979].

| Q (kW) | Q*    | D*    |HRRPUA (kW/m^2) |   X_r  |
|:------:|:-----:|:-----:|:--------------:|:------:|
| 14.4   | 0.270 | 0.178 | 160            | 0.17   |
| 21.7   | 0.407 | 0.209 | 241            | 0.21   |
| 33.0   | 0.618 | 0.248 | 367            | 0.25   |
| 44.9   | 0.841 | 0.280 | 499            | 0.27   |
| 57.5   | 1.07  | 0.309 | 639            | 0.27   |

Within the Processing_Scripts directory of this repository you can find the scripts used to create the plots below.  The data from [McCaffrey, 1979] is digitized and provides a rough estimate of the uncertainty in the correlation.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Gaseous_Pool_Fires/McCaffrey_Flames/Documentation/McCaffrey_Velocity_Correlation.png" width="600">

<img src="https://github.com/MaCFP/macfp-db/blob/master/Gaseous_Pool_Fires/McCaffrey_Flames/Documentation/McCaffrey_Temperature_Correlation.png" width="600">


####References

[McCaffrey, 1979] B. J. McCaffrey. Purely Buoyant Diffusion Flames: Some Experimental Results. National Bureau of Standards, NBSIR 79-1910, 1979.

[McCaffrey, 1981] B. J. McCaffrey. Some Measurements of the Radiative Power Output of Diffusion Flames. In Western-States Section of the Combustion Institute, Paper No. WSS/CT 81-15, 1981.
