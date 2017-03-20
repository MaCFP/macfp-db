## Sandia Flames Setup

#### Introduction


In the early 2000's Sandia undertook a series of measurements of gaseous plumes and fires.  The nonreacting plumes used helium and are described in another [section of this site](http://github.com/MaCFP/macfp-db/tree/master/Buoyant_Plumes/Sandia_Helium_Plume/Documentation/README.md).  In addition to the nonreacting case, a series of methane "pool fires" of varying heat release rates were measured along with a single hydrogen "pool fire."  All of these plumes were from 1 m diameter sources in the FLAME facility at Sandia National Laboratory in Albuquerque, New Mexico, as described below and in the cited references.   

<img src="https://github.com/MaCFP/macfp-db/blob/master/Gaseous_Pool_Fires/Sandia_Flames/Documentation/Sandia_FLAME_overview.png" width="400">

Figure 1: Schematic of PIV setup in FLAME facility.

#### FLAME facility and experimental configuration

The Fire Laboratory for Accreditation of Models by Experimentation (FLAME) facility [Blanchat, 2001;Tieszen et al., 2002] is a nominally cubic central chamber with sides 6.2 m within which a 1 m plume source is centered 2.45 m above the floor level.  The ceiling tapers upward 32 degrees into a 2.3 m square chimney; this tapered ceiling section starts 3.55 m above the plume source.  Around the plume source is a 0.51 m ground plane giving an overall diameter at the plume source level of 2.02 m.  Coflowing air is supplied by an annular source with an inner radium of 2.30 m and an outer radius of 2.91 m that is located 1.74 m below the ground plane and 0.71 m above the facility floor.  The air flow velocity through the annular ducts was approximately 0.3 m/s (see below for test-specific measurements).  To provide additional cylidrical symmetry, an approximately cylidrical shield was created with sixteen steel plates hung from 2.15 m below the ground plane and extending to 0.9 m above the ground plane; these appear in Figure 1 surrounding the coflow.  Much greater detail regarding the facility is provided in the references [Blanchat, 2001;Tieszen et al., 2002].  An  [IGES format file](http://github.com/MaCFP/macfp-db/blob/master/Gaseous_Pool_Fires/Sandia_Flames/Documentation/Flame_first.igs) is provided to assist with the generation of the geometry; unfortunately, this rendering of the geometry does not have the cylindrical shield wall described above.  In addition to the above Figure 1, we provide elevation and plan views of the facility with some dimensions in Figures 2 and 3.   

**NOTE** that the pressure in the facility is 81.1 ±  0.4 kPa, approximately 20% below one standard atmosphere, because of the altitude of the facility.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Gaseous_Pool_Fires/Sandia_Flames/Documentation/Sandia_FLAME_elevation.png" width="451">

Figure 2: Elevation view of FLAME facility.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Gaseous_Pool_Fires/Sandia_Flames/Documentation/Sandia_FLAME_plan.png" width="408">

Figure 3: Horizontal plan view of FLAME facility.


#### Test Matrix

In the 2002 publication Tieszen et al., [2002] the authors describe measurements and uncertainty analysis for a single methane flow rate (0.52 kg/s).  This is followed in Tieszen et al., [2004] with measurements for two other methane flow rates, a near duplicate of the original flow rate and one hydrogen flow rate.  The conditions for all of these measurements are given in Table 1; see also Table 1 of [Tieszen et al., 2004].   


Table 1: Boundary conditions [Tieszen et al., 2004].  All reported uncertainties are twice the standard deviation, or approximately 95% confidence bounds, unless otherwise noted.   

|Test No.                                      | 14  | 24  | 17  | 35  |
| -------------------------------------------- | --- | --- | --- | --- |
|Fuel (a)                                      | CH4 | CH4 | CH4 | H2  |
|Fuel inlet velocity (m/s) (b)                 | 0.074 ± 4% | 0.097 ± 3% | 0.117 ± 3% | 0.336 ± 2% |
|Fuel mass flux (kg/m2 s)                      | 0.040 ± 4% | 0.053 ± 3% | 0.066 ± 3% | 0.022 ± 1% |
|Heat release rate (MW)                        | 1.59 ± 9% | 2.07 ± 8% | 2.61 ± 8% | 2.12 ± 6% |
|Inlet fuel temperature (K)                    | 284 ± 3 | 286 ± 3 | 274 ± 3 | 297 ± 3 |
|Ambient pressure (kPa)                        | 80.6 ± 0.2 | 81.0 ± 0.2 | 81.1 ± 0.2 | 82.2 ± 0.2 |
|Inlet air velocity (m/s) (c)                  | 0.323 ± 8% | 0.327 ± 9% | 0.299 ± 9% | 0.343 ± 4% |
|Inlet air temperature (K)                     | 285 ± 3 | 290 ± 3 | 278 ± 3 | 299 ± 3 |
|Inlet air humidity (%)                        | 22 ± 3 | 10 ± 3 | 29 ± 3 | 8 ± 3 |
|Burner ground plane temperature (K)           | 315 ± 4 | 310 ± 4 | 318 ± 8 | 354 ± 9 |
|Cylindrical shield wall temperature (K) (d)   | 308 ± 15 | 309 ± 11 | 320 ± 25 | 338 ± 25 |
|Facility wall temperature (K) (e)             | 301 ±4 | 302 ±4 | 306 ± 12 | 323 ± 8 |
|Facility ceiling temperature (K) (f)          | 318 ±5 | 322 ±5 | 349 ± 15 | 358 ± 9 |

(a) Commercial grade, 95% purity.

(b) Fuel inlet spatial uniformity is ±6% of inlet velocity in all cases [Blanchat, 2001].

(c) Quadrant to quadrant spatial variability ±10% or less, small features ±37% [Blanchat, 2001]; puffing-induced temporal fluctuation 4% or less for all cases.

(d) Spatially varying, cooler at the base, hotter at the top; see [Tieszen et al., 2002] for geometry.

(e) Spatially varying, cooler just above the shield wall, hotter near the ceiling; see [Tieszen et al., 2002] for geometry.

(f) Spatially varying, cooler near the facility wall, hotter near the chimney entrance; see [Tieszen et al., 2002] for geometry.

#### Available Measurements

Particle image velocimetry was used to obtain vertical and radial velocities at a plane across the plume approximately 1 m wide by 0.9 m high; the laser sheet thickness was approximately 8 mm.  The [Experimental_Data] (https://github.com/MaCFP/macfp-db/tree/master/Gaseous_Pool_Fires/Sandia_Flames/Experimental_Data) files contain average vertical and radial velocity for the four cases listed in Table 1.  For Tests 24 and 35 the turbulent kinetic energy has also been postprocessed and is included; in processing the turbulent kinetic energy, the plane-normal velocity fluctuations have been assumed to be equal to the horizontal fluctuations.  This data is provided as radial profiles with the approximate height above the ground plane indicated by the file name:  p3 indicates z = 0.301 m, p5 indicates z = 0.502 m, and p9 indicates z = 0.903 m above the source.  The 



#### Uncertainty

The authors have conducted an extensive analysis of potential uncertainties in [Tieszen et al., 2002; Tieszen et al., 2004].  The primary uncertainties indicated in Table 2 are derived by comparing right-to-left side results with the assumption that these should be the same.  These uncertainties are presented in the magnitude of the difference normalized by the mean values.  


Table 2: PIV data uncertainty summary, taken from integral estimates in Table 2 of [Tieszen et al., 2004].

|Test No.       | 14  | 24  | 17  | 35  |
| --------------| --- | --- | --- | --- |
|W mean (a) (%) | 7.0 | 17  | 21  | 8.0 |
|U mean (a) (%) | 13  | 17  | 23  | 16  |
|u'u' (a) (%)   | 10  | 16  | 28  | 16  |

(a) Right-to-left (symmetry test) +/-|Difference|/Mean

In [Tieszen et al., 2004] the test-to-test uncertainties were also analyzed after averaging left and right results.  These were used to demonstrate (c.f. Fig. 1 of [Tieszen et al., 2004]) that the uncertainties are relatively small along the centerline and become large near the outer edge of the plume; relative uncertainties could be greater than indicated in Table 2 for radial locations greater than 0.3 m and could be smaller than indicated for radial locations less than 0.2 m.  

Other items of note:

+ It is possible that the vertical velocity near the base is biased toward low velocities by up to 15%, with bias decreasing with increasing elevation to zero by the velocity peak; this is potentially due to the finite particle response times to strong acceleration.   

+  There has been some evidence to suggest some involvement of the flow below the ground plane suggesting that it is important to model this region and not just provide a large ground plane.  

+ Small spatial variations of the coflow air and plume sources were measured and documented in [Blanchat, 2001]; these variations have a standard deviation of 3% but are significantly larger _at their maximum deviations from the mean_ occuring near fabrication imperfections.  Details are provded in [Blanchat, 2001]. Given the significance of the induced radial flow at the flame base, these deviations are probably less important than their magnitude suggests, but this would be an interesting uncertainty quanitification study.  

##### Past simulations

In progress. 

#### References

[Blanchat, 2001] [T. K. Blanchat. Characterization of the air source and plume source at FLAME. Technical Report SAND01-2227, Sandia National Laboratory, Albuquerque, New Mexico, 2001.](http://github.com/MaCFP/macfp-db/tree/master/Gaseous_Pool_Fires/Sandia_Flames/Documentation/Blanchat_SAND2001-2227.pdf)

[Tieszen et al., 2002] S. R. Tieszen, T. J. O’Hern, R. W. Schefer, E. J. Weckman, and T. K. Blanchat. Experimental study of the flow field in and around a one meter diameter methane fire. _Combustion and Flame_, 129:378–391, 2002.

[Tieszen et al., 2004] S. R. Tieszen, T.J. O’Hern, E. J. Weckman, and R. W. Schefer. Experimental study of the effect of fuel mass flux on a 1-m-diameter methane fire and comparison with a hydrogen fire. _Combustion and Flame_, 139:126–141, 2004.
