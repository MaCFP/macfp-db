##UMD Line Burner Experimental Data

Within this directory you will find a set of .csv files which have been extracted from the Matlab `Data.mat` workbook.  The script to process this data is in `../Processing_Scripts/extract_data.m`.

O2_Data contains the local O2 mole fraction data for the methane at 18 vol % O2 in coflow, non-anchored flame at 12.5 and 25.0 cm elevations.

TC_Data contains the local TC temperature data for the methaneat 18 vol % O2 in coflow, non-anchored flame at 12.5 and 25.0 cm elevations.

CH4_NA contains calorimetry, radiative emissions, and flame height data for the methane, non-anchored testing condition.

CH4_A contains the same for the methane, anchored condition.

C3H8_NA contains the same for the propane, non-anchored condition.

C3H8_A contains the same for the propane, anchored condition.

The variables contained within each structure include:

######O2_Data

| header | units | description |
| ----- | --- | ----------------------------------------------------------|
| x_125 | [m] | Position vector for XO2 measurements at 12.5 cm elevation |
| x_250 | [m] | Position vector for XO2 measurements at 25.0 cm elevation |
| XO2_125 | [mol frac] | Local time-mean oxygen mole fraction at 12.5 cm elevation |
| XO2_250 | [mol frac] | Local time-mean oxygen mole fraction at 25.0 cm elevation |
| S_x | [m] | Uncertainty for position data |
| S_XO2 | [mol frac] | Uncertainty for XO2 data |

######TC_Data

| header | units | description |
| ----- | --- | ----------------------------------------------------------|
| x_125 | [m] | Position vector for TC measurements at 12.5 cm elevation  |
| x_250 | [m] | Position vector for TC measurements at 25.0 cm elevation  |
| TC_125 | [C] | Local time-mean TC temperature at 12.5 cm elevation |
| TC_250 | [C] | Local time-mean TC temperature at 25.0 cm elevation |
| S_x  | [m] | Uncertainty for position data |
| S_TC | [C] | Uncertainty for TC temperature data |

######CH4_NA, CH4_A, C3H8_NA, and C3H8_A

| header   | units      | description |
| -------- | ---------- | ----------- |
| XO2      | [mol frac] | Oxidizer oxygen mole fraction |
| q_R      | [kW/m2]    | Radiative heat flux |
| Chi_R    | [-]        | Radiative loss fraction |
| Q_f      | [kW]       | Fuel flow based heat release rate (mdot_fuel * dH_comb,fuel) |
| Q_O2     | [kW]       | OC calorimetry based heat release rate |
| Q_CO2    | [kW]       | CDG calorimetry based heat release rate |
| eta      | [-]        | Combustion efficiency (Q_CO2 / Q_f) |
| XO2_Lf   | [mol frac] | Oxidizer oxygen mole fraction (for use with Lf data) |
| Lf       | [m]        | Flame height |
| S_'data' | [varies]   | Uncertainty for 'data' in same units as 'data' |
  
  
