## NIST Pool Fires

This directory contains experimental measurements of liquid and gaseous pool fires. Two circular liquid pool diameters are reported, 30 cm and 100 cm. One 37 cm diameter gaseous burner is reported.

The 30 cm burner is 15 cm deep and has a wall thickness of 1.6 mm. The burner is fitted with legs such that the burner rim is positioned 30 cm above the floor. The bottom of the burner is maintained at a constant temperature by flowing tap water (nominally 20 °C) through a 3 cm section on the bottom of the fuel pan.

The 100 cm burner is 15 cm deep with a wall thickness of 1.6 mm. It is also water cooled at the bottom.

The 37 cm burner is water-cooled and maintains a nearly ambient temperature at the surface.

#### Notes:

* Weckman and Strong (1996) report a burner diameter of 30.5 cm. The burner used at NIST has a diameter of 30.1 cm.

* The lip height reported by Weckman and Strong (1996) and Kim et al. (2019) is 10 mm. Hamins et al. (1994), Klassen et al. (1994), and Hamins and Lock (2016) report a lip height of 5 mm.

* The heat of combustion for methanol (lower heating value) is 19940 kJ/kg (SFPE Handbook, 2016).

* The measured mass flux for the 30 cm methanol pool fire, averaged over the various studies, is 13.2 ± 0.9 g/(m<sup>2</sup> s) (Kim et al., 2019; Buch et al. 1997; Klassen and Gore, 1994; Weckman and Strong, 1996; Hamins et al., 1994; Falkenstein-Smith et al., 2019).

* The mass flux for the 100 cm methanol pool is 16.3 ± 0.2 g/(m<sup>2</sup> s) (Sung et al., 2019). 

* The measured mass flux for the 30 cm acetone pool fire, averaged over the various studies, is 18.3 ± 0.6 g/(m<sup>2</sup> s). 

* The measured mass flux for the 30 cm ethanol pool fire, averaged over the various studies, is 14.8 ± 1.2 g/(m<sup>2</sup> s). 

* The measured mass flux for the 37 cm methane burner is 6.4 ± 0.1 g/(m<sup>2</sup> s). 

* The measured radiative fraction for the 30 cm methanol pool fire, averaged over the various studies, is 0.22 ± 0.02 (Kim et al., 2019; Buch et al., 1997; Klassen and Gore, 1994).

* The measured radiative fraction for the 100 cm methanol pool fire, averaged over the various studies, is 0.21 ± 0.01 (Klassen and Gore, 1994*; Sung et al., 2019).  *Note: The radiative fraction from Klassen and Gore was recalculated using the net heat of combustion, 19940 kJ/kg (SFPE Handbook, 2016).

* The measured radiative fraction for the 30 cm acetone pool fire is 0.31 ± 0.06 (Kim et al., 2019).

* The measured radiative fraction for the 30 cm ethanol pool fire is 0.26 ± 0.07 (Kim et al., 2019).

* For methanol, the amount of CO in the exhaust stream is below detection limits; thus, the combustion efficiency for methanol is assumed to be 1. The efficiency for the other fuels is not reported.

![Pool Fire Photograph](100cm_Methanol_Pool_Fire.jpg)

Photographs of the 100 cm methanol fire.


### Temperature

Hamins and Lock (2016) made mean and rms centerline and radial gas temperature measurements for a 30 cm methanol pool fire. The radial measurements were made at heights of 3, 30, 40, 50, and 60 cm.

Sung et al. (2019) made mean and rms centerline and radial gas temperature measurements for a 100 cm methanol pool fire. The radial measurements were made at heights of 20, 60, 100, 140, and 180 cm.

### Gas Species Concentrations

Falkenstein-Smith et al. (2019) measured the time-averaged centerline species concentrations within the flaming region of three 30 cm liquid fuel fires: acetone, ethanol, and methanol. The measurements were made using a gas chromatograph/mass spectrometer system (GC/MSD). The volume fraction of each species was calculated via the number of moles identified by the GC/MSD at each centerline point. Soot mass fractions were measured during the gas sampling process. The data is in the files `Acetone_30_cm.csv`, `Ethanol_30_cm.csv`, and `Methanol_30_cm.csv`.


### Heat Flux

Radiative and total heat flux measurements were made at various locations for the 30~cm methanol pool fire. 

`Methanol_30_cm_HF_radial_Kim_2019.csv` Radial profile of total heat flux from the pool center out to 1.5 m.

`Methanol_30_cm_HF_radial_Hamins_1994.csv` Radial profile of radiative heat flux from the pool center to outer rim.

`Methanol_30_cm_HF_radial_Klassen_1994.csv` Radial profile of total heat flux from outer rim to 60 cm.

`Methanol_30_cm_HF_vertical_Kim_2019.csv` Vertical profile of total heat flux 60 cm from the pool center.

`Methanol_100_cm_HF_radial.csv` Radial profile of total heat flux from outer rim to 2 m (Sung et al. (2019)).

`Methanol_100_cm_HF_vertical.csv` Vertical profiles of total heat flux at various heights and distances from the pool center (Sung et al. (2019)).

### References

Buch, R., Hamins, A., Konishi, K., Mattingly, D., and Kashiwagi, T., Radiative Emission Fraction of Pool Fires Burning Silicone Fluids, Combust. Flame, 108, 118-126 (1997).

Falkenstein-Smith, R., K. Sung, J. Chen, and A. Hamins (2019) The Chemical Structure of Medium-Scale Pool Fires, Interflam Conference Proceedings, p. 2059, London, England, July 1-3, 2019.

Falkesntein-Smith, R., K. Sung, A. Hamins (2019) Mapping the Chemical Structure of Centerline Profiles in Medium-Scale Pool Fires, National Institute of Standards and Technology, Gaithersburg, MD, NIST Technical Note, in preparation.

Hamins, A., M. Klassen, J. Gore, S. Fischer, T. Kashiwagi (1994) Heat feedback to the fuel surface in pool fires, Combustion Science and Technology, 97:37-62.

Hamins, A. and A. Lock (2016) The Structure of a Moderate-Scale Methanol Pool Fire, National Institute of Standards and Technology, Gaithersburg, MD, NIST Technical Note 1928, October.

Kim, S.C., K.Y. Lee, and A. Hamins (2019) Energy Balance in Medium-Scale Methanol, Ethanol, and Acetone Pool Fires, Fire Safety Journal, 107:44-53, https://doi.org/10.1016/j.firesaf.2019.01.004

Klassen, M. and J.P. Gore (1994) Structure and Radiation Properties of Pool Fires, NIST GCR 94-651, National Institute of Standards and Technology, Gaithersburg, MD, June.

Sung, K., J. Chen, M. Bundy, M. Fernandez, and A. Hamins (2019) The Characteristics of a 1 m Methanol Pool Fire, National Institute of Standards and Technology, Gaithersburg, MD, NIST Technical Note, in preparation.

Weckman, E.J. and A.B. Strong (1996) Experimental investigation of the turbulence structure of medium-scale methanol pool fires, Combustion and Flame, 105:245-66.

SFPE Handbook of Fire Protection Engineering (5th ed.), Appendix 3, Fuel Properties and Combustion Data, (Ed.: M. Hurley) 2016.


