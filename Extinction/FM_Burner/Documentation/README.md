## FM Burner Experimental Setup

The burner design and boundary conditions are described below. Figure 1 shows the burner geometry. The burner has an inner diameter of 13.7 cm (5.4 in.) and an outer diameter of 15.2 cm (6 in.). The burner wall has a thickness of 0.3 in. and is water cooled to be approximately 25 ºC. The upper edge is shaped to be 45º slanted. The burner surface is filled with steel beads, see Figure 2, that are cooled by a cooling water coils placed inside steel beads.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Extinction/FM_Burner/Documentation/FM_Burner_design.png" width="400">

Figure 1: Burner design drawing (units are inches).

<img src="https://github.com/MaCFP/macfp-db/blob/master/Extinction/FM_Burner/Documentation/FM_Burner_photo.png" width="400">

Figure 2: Burner photo.

Figure 3 shows the enclosure drawing. The enclosure has a cross section of 122 by 122 cm2 (4 by 4 ft2). The lower section is a plenum space and a sand bed for distributing the oxidant. The burner placed on a translation stage sits above the sand bed, with the bottom surface of burner approximately 11.4 cm (4.5 in.) away from the bed surface. The burner centerline is aligned with the exhaust hood at the start of a test, and could traverse laterally in an optical based experiment, e.g. laser induced incandescence measurements. The distance between the burner surface and hood lower edge is approximately 81 cm (32 in.). The hood has an outer diameter of 61 cm (24 in.). The exhaust flow rate is maintained at approximately 0.11 m^3/s. At this condition, the oxygen concentrations around the flame at various heights was verified to be the same as prescribed.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Extinction/FM_Burner/Documentation/FM_Burner_front.png" width="400">
<img src="https://github.com/MaCFP/macfp-db/blob/master/Extinction/FM_Burner/Documentation/FM_Burner_side.png" width="400">

Figure 3: Enclosure drawing, (a) front view; (b) top view (units are inches).

### Radiative Characteristics of Buoyant Diffusion Flames

The flame examined in this study has a theoretical heat release rate of 15 kW. Three oxygen concentrations are investigated, including normal air (20.9% oxygen by volume), 16.8% and 15.2% oxygen in nitrogen. The fuel flow rates and corresponding oxygen concentrations are listed in Table 1. The flow rate of oxidizer, i.e., air and nitrogen, under each OC condition is 3650±250 L/min. The corresponding nominal velocity normal to the sand bed is 0.041±0.003 m/s. The oxygen concentration in the co-flow is monitored using a gas analyzer, and verified at different locations around flame, i.e., 30 cm radial distance from the burner centerline, and -5 cm, 20 cm, 46 cm, and 71 cm height from the burner surface, respectively. The change of oxygen concentration does not exceed 0.1 vol%. 

Table 1: Fuel and Oxidizer Flow Rate

|Oxygen Concentration | Y_O2 Oxidizer   | Ethylene Flow Rate | Radiant Fraction|
|---------------------|-----------------|--------------------|-----------------|
|(Vol %)              |(Mass fraction)  |(g/s)               |      |
| 20.9                | 0.231           | 0.318              | 0.34 |
| 16.8                | 0.187           | 0.318              | 0.30 |
| 15.2                | 0.170           | 0.318              | 0.22 |

#### Notes

The temperature was measured using a two-thermocouple probe, and the reported data is corrected for radiation. This technique is mainly applied to correct the thermal inertia as the radiation correction for a small thermocouple junction is relatively small. The two thermocouples have nominal wire sizes of 25 and 50 microns.

The derivation of soot volume fraction from either radiation probe data or LII data assumes 9.5 as a dimensionless extinction coefficient based on Williams’ study [7, 8] and 7.6 as the dimensionless absorption coefficient assuming 20% scattering. In Williams’ study [7, 8], a soot density value of 1.74 g/cm3 is used to derive the 9.5 value for dimensionless extinction coefficient. Therefore, a soot density of 1.74 g/cm3 should be used when converting soot mass fraction to volume fraction.

#### Flame Images

<img src="https://github.com/MaCFP/macfp-db/blob/master/Extinction/FM_Burner/Documentation/FM_Burner_flame_images.png" width="600">

Figure 4: FM Burner flame images at various oxygen concentrations.

### Combustion Efficiency

The combustion efficiency and limiting oxygen index (LOI) for four (4) fuels (methane, propylene, propane, and ethylene) are reported in [9]. The theoretical heat release of all test conditions is maintained at 10 kW.  The flame was anchored by 36 pre-mixed ethylene/air pilot flames surrounding the burner. Each premixed flame was adjusted to be approximately 2.5 cm long. The total heat release rate of pilot flames is approximately 1 kW.

|Fuel               | LOI  (vol %)  | 
|-------------------|---------|
| methane (CH4)     | 12.1    |
| propylene (C3H6)  | 11.2    |
| propane (C3H8)    | 10.3    |
| ethylene (C2H4)   | 8.2     |

### Velocity Field and Temperature Update (Oct 2025)

In October of 2025, the FM Burner dataset was updated to include the following data at the plane across the flame centerline for three oxygen concentrations:

* Mean vertical and horizontal velocity (2D map)
* Mean and RMS temperature
* Temperature PDF at different locations

These data are located in [FM_Burner/Experimental_Data/FM_Burner_dataset_update_Oct2025/](https://github.com/MaCFP/macfp-db/blob/master/Extinction/FM_Burner/Experimental_Data/FM_Burner_dataset_update_Oct2025/).


#### References

References:

[1] D. Zeng, P. Chatterjee, Y. Wang, The effect of oxygen depletion on soot and thermal radiation in buoyant turbulent diffusion flames, Proc Combust Inst 37 (2019) 825-832. doi: https://doi.org/10.1016/j.proci.2018.05.139.

[2] N. Ren, D. Zeng, K.V. Meredith, Y. Wang, S.B. Dorofeev, Modeling of flame extinction/re-ignition in oxygen-reduced environments, Proc Combust Inst 37 (2019) 3951-3958. doi: https://doi.org/10.1016/j.proci.2018.06.076.

[3] X. Ren, D. Zeng, Y. Wang, G. Xiong, G. Agarwal, M. Gollner, Temperature measurement of a turbulent buoyant ethylene diffusion flame using a dual-thermocouple technique, Fire Saf. J. 120 (2021) 103061. doi: https://doi.org/10.1016/j.firesaf.2020.103061.

[4] G. Xiong, D. Zeng, P.P. Panda, Y. Wang, Laser induced incandescence measurement of soot in ethylene buoyant turbulent diffusion flames under normal and reduced oxygen concentrations, Combust. Flame 230 (2021) 111456. doi: https://doi.org/10.1016/j.combustflame.2021.111456.

[5] P. Chatterjee, D. Zeng, Y. Wang, Numerical modeling of soot radiation in optically-thin, buoyant diffusion flames at varying oxygen concentrations, Proc Combust Inst 38 (2021) 4987-4994. doi: https://doi.org/10.1016/j.proci.2020.08.028.

[6] G. Xiong, D. Zeng, Y. Wang, Effect of oxygen concentration on the velocity in buoyant turbulent diffusion flames, Fire Saf. J. 140 (2023) 103903. doi: https://doi.org/10.1016/j.firesaf.2023.103903.

[7] T.C. Williams, C.R. Shaddix, K.A. Jensen, J.M. Suo-Anttila, Measurement of the dimensionless extinction coefficient of soot within laminar diffusion flames, Int. J. Heat Mass Transfer 50 (2007) 1616-1630. doi: https://doi.org/10.1016/j.ijheatmasstransfer.2006.08.024.

[8] M.Y. Choi, G.W. Mulholland, A. Hamins, T. Kashiwagi, Comparisons of the soot volume fraction using gravimetric and light extinction techniques, Combust. Flame 102 (1995) 161-169. doi: https://doi.org/10.1016/0010-2180(94)00282-W.

[9] D. Zeng, Y. Wang, Dependence of limiting oxygen index of buoyant turbulent non-premixed flame on fuel. In. 26th Int. Colloquium on the Dynamics of Explosions and Reactive Systems, Boston; 2017.

[10] G. Xiong, X. Ren, D. Zeng, R. Barlow, Y. Wang, Temperature measurements in sooty buoyant turbulent non-premixed flames under different oxygen concentrations, Fire Saf. J. 158 (2025) 10.1016/j.firesaf.2025.104555.

[11] G. Xiong, R. Barlow, D. Zeng, Y. Wang, Extinction of buoyant turbulent non-premixed flames under reduced oxygen concentrations, Proc Combust Inst 40 (2024) 105307. doi: https://doi.org/10.1016/j.proci.2024.105307.

[12] G. Xiong, D. Zeng, Y. Wang, Thermal radiation and soot in buoyant turbulent diffusion flames under different oxygen concentrations: Measurements and implications to radiation modeling, Combust. Flame 267 (2024) 113587. doi: https://doi.org/10.1016/j.combustflame.2024.113587.
