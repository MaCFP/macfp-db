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


#### References

1. Zeng, D., Wang, Y., Effect of oxygen depletion on the radiative characteristics of buoyant turbulent diffusion flames, in: 15th Fire & Materials Conference, 2017.
2. Zeng, D., Chatterjee, P., Wang, Y., The effect of oxygen depletion on soot and thermal radiation in buoyant turbulent diffusion flames, Proc Combustion Institute 37 (1) (2019) 825-832.
3. Ren, N., Zeng, D., Meredith, K.V., Wang, Y., and Dorofeev, S.B., Modeling of flame extinction/re-ignition in oxygen-reduced environments. Proceedings of the Combustion Institute, 2019. 37(3): p. 3951-3958.
4. Ren, X., Zeng, D., Wang, Y., Xiong, G., Agarwal, G., and Gollner, M., Temperature measurement of a turbulent buoyant ethylene diffusion flame using a dual-thermocouple technique. Submitted to IAFSS, 2019.
5. Xiong, G., Zeng, D., Panda, P.P., and Wang, Y., Laser induced incandescence measurement of soot in ethylene buoyant turbulent diffusion flames under normal and reduced oxygen concentrations. Submitted to Proceedings of Combustion Institute, 2019.
6. Chatterjee, P., Zeng, D., and Wang, Y., Numerical Modeling of Soot-Radiation in Optically-Thin, Buoyant Diffusion Flames of Varying Oxygen Concentrations. Submitted to Proceedings of Combustion Institute, 2019.
7. T.C. Williams, C.R. Shaddix, K.A. Jensen, J.M. Suo-Anttil, Measurement of the dimensionless extinction coefficient of soot within laminar diffusion flames. International Journal of Heat and Mass Transfer 50:1616–1630, 2007.
8. M.Y. Choi, G.W. Mulholland, A. Hamins, T. Kashiwagi, Comparisons of the Soot Volume Fraction Using Gravimetric and Light Extinction Techniques. Combustion and Flame, 102:161-169, 1995.
9. Zeng, D., Wang, Y., Dependence of Limiting Oxygen Index of Buoyant Turbulent non-premixed Flame on Fuel, in: 26th ICDERS (International Colloquium
on the Dynamics of Explosions and Reactive Systems), Boston, 2017.
