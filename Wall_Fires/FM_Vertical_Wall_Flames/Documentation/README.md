## FM Global vertical wall fire configuration

Summarized by Ning Ren

#### Introduction

The FM Global wall fire experimental study [1] targets characterizing turbulent, vertical wall flames produced by an array of vertically stacked porous wall burners supplied with gaseous fuels. The wall burners were water cooled with carefully adjusted fuel supply rates. This experimental configuration represents meter-scale, buoyancy-driven, diffusion flames as in typical upward fire spread scenarios. For fire growth and spread problems, flame heat transfer is of central importance. In this study, the flame-to-wall heat fluxes were characterized at different elevations, fuels and fuel flow rates. Other flame characterizations included soot depth, flame temperature profiles, and outward flame radiances. These data are useful for developing physics based heat transfer models as well as for CFD model validation [2]. 

#### Experimental design

An elevation view of the apparatus is illustrated in Fig. 1. The burner was assembled by an array of 132 mm high × 380 m wide, water cooled, porous, sintered bonze panels. Each of the sintered metal panels was individually supplied with gaseous fuel and individually measured for heat feedback from the flames by the temperature rise of the cooling water. The forward heat transfer zone was simulated by a 660 mm high solid metal, water cooled heat transfer plate, which was divided into five 132 mm thermal segments to measure the distribution of forward heat transfer. The height of the fuel-inlet zone can be adjusted by varying the number of individual panels supplied with gaseous fuel. 

![alt text](https://github.com/NingRen/macfp-db/blob/wallFire-FM/Wall_Fires/FM_Vertical_Wall_Flames/Documentation/Wall_Fire_Burner.png)

Figure 1: Elevation view of FM vertical gas burner apparatus [1], units in mm

In the fuel-inlet zone, gaseous fuel was supplied by an electronic mass flow controller with an accurate measure of the fuel flow rate. A horizontal flame anchor consisting of a 1 mm high × 5 mm deep × 380 mm wide strip of ceramic material, was placed normal to the surface at the leading edge of the lowest active panel. The flame anchor encouraged tripping of the boundary layer and was important for anchoring the flames at low mass flow rate.

Four fuels were used in the experiments: methane, ethane, ethylene and propylene. The minimum fuel mass flux rate is 4 g/m<sup>2</sup>/s, below which flame becomes non-luminous and blue.

The flame thickness, characterized by the soot depth, δ<sub>s</sub>, was measured by inserting arrays of 5 mm diameter glass rods into the flame perpendicular to the wall surface and rapidly withdrawing them after a two second exposure. The soot depth, δs, is then defined as the distance where the soot deposit is visually judged to have decreased to 50% of the maximum deposit on that rod. 

Temperature profiles across the flame boundary were measured by a thermocouple rake, which consisted of 15 ungrounded Chromel-Alumel thermocouples inside 1.6 mm Inconel sheaths spaced 12.6 mm on center and protruding 1.5 cm downwards into the rising flow. The rake was angled 56° from the normal to the burner surface in a horizontal plane. Temperature was measured at two locations: 365 and 771 mm downstream from the flame leading edge.

Thermocouples are often used to measure local gas temperatures both inside and near a flame. However, radiation heat loss from thermocouples can depress measured temperatures inside the flame, while radiation from the flame can increase the measured temperatures outside the flame. Correction of these effects was performed from detailed knowledge of the radiation field together with a simple heat transfer model, which is available in Ref. 1. 

A scanning radiometer was employed to measure the vertical distribution of outward radiance emitted from the flame. The outward radiance is defined as the radiant flux per unit solid angle in the outward normal direction. Scanning radiometer measurements were averaged at the mid-height of each 132-mm high burner segment.

#### Experimental data

Available [experimental data](https://github.com/NingRen/macfp-db/tree/wallFire-FM/Wall_Fires/FM_Vertical_Wall_Flames/Experimental_Data) include:

##### Soot depth for propylene wall fires
| Vertical measurement location (mm) | Mass flux range (g/m<sup>2</sup>/s) |
| ---------------------------------- | ------------------------ |
| 365 | 6.99 - 29.29 |
| 527 | 6.17 - 62.18 |
| 771 | 5.67 - 22.37 |
| 1022 | 4.41 - 17.13 |
| 1317 | 4.41 - 17.51 |


##### Uncorrected (raw) and corrected thermocouple temperature for propylene wall fires
| Vertical measurement location (mm) | Mass flux range (g/m<sup>2</sup>/s) |
| ---------------------------------- | ------------------------ |
| 771 | 8.75 - 22.49 |

##### Outward radiance for propylene wall fire wall fires
| Vertical measurement location (mm) | Mass flux range (g/m<sup>2</sup>/s) |
| ---------------------------------- | ------------------------ |
| 66 | 5.35 - 24.74 |
| 330 | 5.35 - 24.74 |
| 594 | 5.35 - 24.74 |
| 990 | 5.35 - 14.58 |

##### Total flame-to-wall heat flux for propylene wall fires (some reported measurements were interpolated to match the fuel flow rate condition used in temperature measurements)
| Mass flux (g/m<sup>2</sup>/s) |
| ------------------ |
| 12.68 |
| 17.05 |
| 22.27 |

##### Total flame-to-wall heat flux for other fuels: methane, ethane and ethylene (some reported measurements were interpolated to match the fuel flow rate condition used in temperature measurements)
| Fuels | Mass flux (g/m<sup>2</sup>/s) |
| ----- | ------------------ |
| Methane | 10.6 |
| Ethane | 10.2 |
| Ethylene | 11.5 |

#### Reference
[1] J.L. de Ris, G.H. Markstein, L. Orloff, and P.A. Beaulieu, “Similarity of Turbulent Wall Fires,” Fire Safety Science, Vol. 7, pp. 259-270.

[2] N. Ren, Y. Wang, S. Vilfayeau and A. Trouvé, “Large Eddy Simulation of Turbulent Vertical Wall Fires Supplied with Gaseous Fuel through Porous Burners,” Combustion and Flame, Article in Press.

