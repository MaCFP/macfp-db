## UMD Line Burner Experimental Data

Within this directory you will find a set of .csv files containing measurement data from the University of Maryland turbulent line burner [1-4].

O2_Data contains local O2 mole fraction data for the methane, non-anchored flame in 18 vol % O2 coflow, along widthwise flame profiles at 12.5 and 25.0 cm elevations.

TCz_Data contains the local TC mean and rms temperature data for the methane, non-anchored flame in air coflow, along the vertical flame centerline.

TCx_Data contains the local TC mean and rms temperature data for the methane, non-anchored flame in air coflow, along widthwise flame profiles at 0.25, 0.50, 0.75, and 1.00 m elevations.

CH4_A contains calorimetry, radiative emissions, and flame height data for the methane, anchored flame suppressed via nitrogen dilution of the oxidizer.

C3H8_A contains the same for the propane, anchored flame.

CH4_Mist contains calorimetry data for the methane, non-anchored flame suppressed via water mist.

The variables contained within each structure include:

##### O2_Data

| header  | units      | description |
| ------- | ---------- | ----------- |
| x_125   | [m]        | Position vector for XO2 measurements at 12.5 cm elevation |
| x_250   | [m]        | Position vector for XO2 measurements at 25.0 cm elevation |
| XO2_125 | [mol/mol]  | Local time-mean oxygen mole fraction at 12.5 cm elevation |
| XO2_250 | [mol/mol]  | Local time-mean oxygen mole fraction at 25.0 cm elevation |
| S_x     | [m]        | Uncertainty for position data |
| S_XO2   | [mol/mol]  | Uncertainty for XO2 data |

##### TCz_Data
| header   | units      | description |
| -------- | ---------- | ----------- |
| z        | [m]        | Position vector for TC measurements |
| TCz      | [K]        | Local time-mean TC temperature along vertical flame centerline |
| TCz_rms  | [K]        | Local time-rms TC temperature along vertical flame centerline |

##### TCx_Data
| header   | units      | description |
| -------- | ---------- | ----------- |
| x        | [m]        | Position vector for TC measurements |
| TCx_0.25 | [K]        | Local time-mean TC temperature at 0.25 m elevation |
| TCx_0.50 | [K]        | Local time-mean TC temperature at 0.50 m elevation |
| TCx_0.75 | [K]        | Local time-mean TC temperature at 0.75 m elevation |
| TCx_1.00 | [K]        | Local time-mean TC temperature at 1.00 m elevation |
| TCx_rms_0.25 | [K]    | Local time-rms TC temperature at 0.25 m elevation |
| TCx_rms_0.50 | [K]    | Local time-rms TC temperature at 0.50 m elevation |
| TCx_rms_0.75 | [K]    | Local time-rms TC temperature at 0.75 m elevation |
| TCx_rms_1.00 | [K]    | Local time-rms TC temperature at 1.00 m elevation |


##### CH4_A and C3H8_A

| header   | units      | description |
| -------- | ---------- | ----------- |
| XO2      | [mol/mol]  | Oxidizer oxygen mole fraction |
| q_R      | [kW/m2]    | Radiative heat flux |
| Chi_R    | [-]        | Radiative loss fraction |
| Q_f      | [kW]       | Fuel flow based heat release rate (mdot_fuel * dH_comb,fuel) |
| Q_CO2    | [kW]       | CDG calorimetry based heat release rate |
| eta      | [-]        | Combustion efficiency (Q_CO2 / Q_f) |
| XO2_Lf   | [mol/mol]  | Oxidizer oxygen mole fraction (for use with Lf data) |
| Lf       | [m]        | Flame height |
| S_'data' | [varies]   | Uncertainty for 'data' in same units as 'data' |

##### CH4_Mist

| header   | units      | description |
| -------- | ---------- | ----------- |
| Y_wm     | [kg/kg]    | Mass fraction of liquid-phase water mist in oxidizer |
| Q_f      | [kW]       | Fuel flow based heat release rate (mdot_fuel * dH_comb,fuel) |
| Q_CO2    | [kW]       | CDG calorimetry based heat release rate |
| eta      | [-]        | Combustion efficiency (Q_CO2 / Q_f) |
| S_'data' | [varies]   | Uncertainty for 'data' in same units as 'data' |


#### References

1. J.P. White, E.D. Link, A.C. Trouvé, P.B. Sunderland, A.W. Marshall, J.A. Sheffel, M.L. Corn, M.B. Colket, M. Chaos, and H.-Z. Yu. Radiative emissions measurements from a buoyant, turbulent line flame under oxdizer-dilution quenching conditions, _Fire Safety Journal_, 76:74-84, 2015.

2. J.P. White, Measurement and simulation of suppression effects in a buoyant turbulent line fire, Ph.D. thesis, University of Maryland, College Park, 2016.

3. J.P. White, S. Verma, E. Keller, A. Hao, A. Trouvé, A.W. Marshall, Water mist suppression of a turbulent line fire, _Fire Safety Journal_ 91:705-713, 2017.

4. J.P. White, E.D. Link, A. Trouvé, P.B. Sunderland, A.W. Marshall, A general calorimetry framework for measurement of combustion efficiency in a suppressed turbulent line fire, _Fire Safety Journal_ 92:164-176, 2017



