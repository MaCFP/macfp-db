## NIST Pool Fires

This directory contains experimental measurements of liquid and gaseous pool fires. Results using two circular, liquid pool burners are reported, 30 cm and 100 cm in diameter. Results using a 37 cm diameter, water-cooled, gaseous burner are also reported.  Experimental results are reported for steadily burning fires in a well-ventilated, quiescent environment. A warm-up period of 10 min was required for the mass burning rate of the liquid fuels to be steady.  

| Diameter (m) | Fuel     | Mass Flux g/(m<sup>2</sup> s) | References         |
|--------------|----------|--------------------|--------------------|
| 30           | Methanol | 13.2± 0.9          | 1,2,3,4,5,6,7,9,10 |
| 30           | Ethanol  | 14.8± 1.2          | 1,2,3,6            |
| 30           | Acetone  | 18.3± 0.6          | 1,2,3,6            |
| 37           | Methane  | 6.4± 0.1           | 3                  |
| 100          | Methanol | 16.3± 0.2          | 1,7,8              |

![Pool Fire Photograph](100cm_Methanol_Pool_Fire.jpg)

Photographs of the 100 cm methanol pool fire with a 1 cm lip height.

<p align="left">
  <img width="615" src="30cm_Methanol_Pool_Fire.jpg">
</p>

Photographs of the 30 cm methanol pool fire with a 1 cm lip height.



### Notes:

#### Burners
* Kim et al (2019) report that the NIST burner has an inner diameter of 30.1 cm, a wall thickness of 0.13 cm, and a depth of 15 cm. 

* The 30 cm burner is 15 cm deep. The burner is fitted with legs such that the burner rim is positioned 30 cm above the floor. The bottom of the burner is maintained at a constant temperature by flowing tap water (nominally 20 °C) through a 3 cm section on the bottom of the fuel pan.

* Weckman and Strong (1996) report using a 30.5 cm diameter burner. Weckman (2020) reports that the outer diameter of the burner is 30.5 cm, the wall thickness is 0.15 cm, and the depth is 6.0 cm. 

* The lip height reported by Weckman and Strong (1996) and Kim et al. (2019) is 10 mm. Hamins et al. (1994), Klassen et al. (1994), and Hamins and Lock (2016) report a lip height of 5 mm.

* The 37 cm gaseous burner is water-cooled and maintains a nearly ambient temperature at the surface.

* The 100 cm burner is 15 cm deep with a wall thickness of 1.6 mm. It is also water cooled at the bottom.

#### Thermophysical data

* The heat of combustion for methanol (lower heating value with water as a gaseous product) is 19940 kJ/kg (SFPE Handbook, 2016).

#### Fuel Mass Flux

* The measured mass flux for the 30 cm methanol pool fire, averaged over the various studies, is 13.2 ± 0.9 g/(m<sup>2</sup> s) (Kim et al., 2019; Buch et al. 1997; Klassen and Gore, 1994; Weckman and Strong, 1996; Hamins et al., 1994; Falkenstein-Smith et al., 2020a, 2020b).

* The mass flux for the 100 cm methanol pool is 16.3 ± 0.2 g/(m<sup>2</sup> s) (Sung et al., 2020). 

* The measured mass flux for the 30 cm acetone pool fire, averaged over the various studies, is 18.3 ± 0.6 g/(m<sup>2</sup> s). 

* The measured mass flux for the 30 cm ethanol pool fire, averaged over the various studies, is 14.8 ± 1.2 g/(m<sup>2</sup> s). 

* The measured mass flux for the 37 cm methane pool fire is 6.4 ± 0.1 g/(m<sup>2</sup> s). 

#### Radiative Fraction

* The measured radiative fraction for the 30 cm methanol pool fire, averaged over the various studies, is 0.22 ± 0.02 (Kim et al., 2019; Buch et al., 1997; see discussion of Klassen and Gore, 1994 results in Sung et al., 2020).

* The measured radiative fraction for the 100 cm methanol pool fire, averaged over the various studies, is 0.21 ± 0.01 (Klassen and Gore, 1994*; Sung et al., 2020).  *Note: The radiative fraction from Klassen and Gore was recalculated using the net heat of combustion of 19940 kJ/kg and to improve the estimate of radiative heat feedback to the pool surface (see Sung et al., 2020).

* The measured radiative fraction for the 30 cm acetone pool fire is 0.31 ± 0.06 (Kim et al., 2019).

* The measured radiative fraction for the 30 cm ethanol pool fire is 0.26 ± 0.07 (Kim et al., 2019).

* The measured radiative fraction for the 37 cm methane fire is 0.15 (Hamins et al., 1996).

#### Temperature

* Hamins and Lock (2016) made mean and rms centerline and radial thermocouple temperature measurements for a 30 cm methanol pool fire. The radial measurements were made at heights of 3.8, 30.8, 40.8, 50.8, and 60.8 cm above the pool surface (as opposed to the rim of the burner pan).

* Sung et al. (2020) made mean and rms centerline and radial thermocouple temperature measurements for a 100 cm methanol pool fire. The radial measurements were made at heights of 21, 61, 101, 141, and 181 cm above the pool surface (as opposed to the rim of the burner pan).

#### Gas Species and Soot Concentrations

* Falkenstein-Smith et al. (2020a and 2020b) measured the time-averaged centerline species concentrations within the flaming region of three 30 cm liquid fuel fires: acetone, ethanol, and methanol. Falkenstein-Smith et al. (2020b) measured the time-averaged centerline species concentrations and temperatures in a 37 cm, 34.5 kW methane fire and 37 cm, 20 kW and 34 kW propane fires. The measurements were made using a gas chromatograph/mass spectrometer system (GC/MSD). The volume fraction of each species was calculated via the number of moles identified by the GC/MSD at each centerline point. Soot mass fractions were measured during the gas sampling process. The data for the liquid fuels is in the files `Acetone_30_cm.csv`, `Ethanol_30_cm.csv`, and `Methanol_30_cm.csv`. The data for the gaseous fuels is in `Methane_37_cm.csv`, `Propane_37_cm_20_kW.csv`, and `Propane_37_cm_34_kW.csv`. 

* For the methanol, ethanol and acetone pool fires, the amount of CO in the exhaust stream is below detection limits; thus, the combustion efficiency is assumed to be equal to 1.0. 

#### Heat Flux

* Radiative and total heat flux measurements were made at various locations for the 30 cm methanol pool fire.  The positions of the heat flux gauges were 1 cm abover the liquid pool surface.

`Methanol_30_cm_HF_radial_Kim_2019.csv` Radial profile of total heat flux from the pool center out to 1.5 m.

`Methanol_30_cm_HF_radial_Hamins_1994.csv` Radial profile of radiative heat flux from the pool center to the outer rim.

`Methanol_30_cm_HF_radial_Klassen_1994.csv` Radial profile of total heat flux from outer rim to 60 cm.

`Methanol_30_cm_HF_vertical_Kim_2019.csv` Vertical profile of total heat flux 60 cm from the pool center.

`Methanol_100_cm_HF_radial.csv` Radial profile of total heat flux from outer rim to 2 m (Sung et al. (2019)).

`Methanol_100_cm_HF_vertical.csv` Vertical profiles of total heat flux at various heights and distances from the pool center (Sung et al. (2019)).

#### References

1. Buch, R., Hamins, A., Konishi, K., Mattingly, D., and Kashiwagi, T., Radiative Emission Fraction of Pool Fires Burning Silicone Fluids, Combust. Flame, 108, 118-126 (1997).

2. Falkenstein-Smith, R., K. Sung, J. Chen, and A. Hamins, Chemical Structure of Medium-Scale Liquid Pool Fires, Fire Safety Journal, available on-line 14 May 2020a, https://doi.org/10.1016/j.firesaf.2020.103099

3. Falkesntein-Smith, R., K. Sung, Chen, J., Harris, K., A. Hamins, The Structure of Medium-Scale Pool Fires, NIST Technical Note 2082, National Institute of Standards and Technology, Gaithersburg, MD, February 2020b. https://doi.org/10.6028/NIST.TN.2082

4. Hamins, A., M. Klassen, J. Gore, S. Fischer, T. Kashiwagi, Heat feedback to the fuel surface in pool fires, Combustion Science and Technology, 97:37-62 (1994).

5. Hamins, A. and A. Lock, The Structure of a Moderate-Scale Methanol Pool Fire, NIST Technical Note 1928, National Institute of Standards and Technology, Gaithersburg, MD, November 2016. https://doi.org/10.6028/NIST.TN.1928

6. Kim, S.C., K.Y. Lee, and A. Hamins, Energy Balance in Medium-Scale Methanol, Ethanol, and Acetone Pool Fires, Fire Safety Journal, 107:44-53 (2019). https://doi.org/10.1016/j.firesaf.2019.01.004

7. Klassen, M. and J.P. Gore, Structure and Radiation Properties of Pool Fires, NIST GCR 94-651, National Institute of Standards and Technology, Gaithersburg, MD, June 1994.

8. Sung, K., J. Chen, M. Bundy, M. Fernandez, and A. Hamins, The Thermal Character of a 1 m Methanol Pool Fire,  NIST Technical Note 2083, National Institute of Standards and Technology, Gaithersburg, MD, January 2020. https://doi.org/10.6028/NIST.TN.2083 

9. Weckman, E.J.; Personal Communication, Email to A. Hamins, 28 August 2020.  

10. Weckman, E.J. and A.B. Strong, Experimental investigation of the turbulence structure of medium-scale methanol pool fires, Combustion and Flame, 105:245-66 (1996).

11. SFPE Handbook of Fire Protection Engineering (5th ed.), Appendix 3, Fuel Properties and Combustion Data, (Ed.: M. Hurley) 2016.

12. Hamins, A., Konishi, K., Borthwick, P, Kashiwagi, T., Global Properties of Gaseous Pool Fires, Proceedings Combustion Institute, 26:1429-1436 (1996).
