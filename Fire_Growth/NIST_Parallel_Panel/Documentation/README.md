## NIST Parallel Panel

### Disclaimers

The test description and measurement data presented here should be considered as preliminary results, for the purposes of initial fire model setup for the MaCFP Working Group; however, this summary has been analyzed by subject matter experts within the research team and is believed to be scientifically sound and consistent with the integrity expected of NIST research. A NIST Technical Note [1], currently in preparation, will be published shortly along with final experimental results and analysis.

Note: The identification of any commercial product or trade name does not imply endorsement or recommendation by NIST (or any other contributing institution).

### Test Overview

A set of 6 experiments was performed on poly(methyl methacrylate), PMMA. In each test, samples (i.e., 2.44 m tall, 0.61 m wide, and 5.8 mm thick slabs of PMMA mounted in a parallel panel configuration) were exposed to a propane burner (nominal heat release rate, HRR = 60 kW), which was turned off after sustained flaming was observed across the panel walls. Flames were allowed to spread upward across the panels and continue burning until self-extinction following complete sample burnout.

During experiments, measurements were acquired and recorded using National Instruments (NI) data acquisition (DAQ) modules and using a custom program called MIDAS (Modular In-situ Data Acquisition System), which was developed in LabVIEW. Mean values from each channel were recorded at 1 Hz. Ultimately, the uncertainties from the DAQ system were orders of magnitude lower than those of the measurement devices and/or systems used in these experiments. 

Measurement data obtained in this test series includes:
1. Time-resolved measurements of fire size (kW), soot generation, and gaseous species (CO and CO2) production;
2. Spatially resolved measurements of flame to wall heat transfer [kW/m2];
3. Radiative heat flux at a distance [kW/m2]; 
4. Initial and final sample mass; 
5. Photographs and video of material ignition and fire growth behavior

### Test Configuration

#### Parallel Panel Apparatus

Figure 1 provides a schematic of the Parallel Panel test apparatus used in these experiments. This experimental setup was based on an assembly originally developed at FM Global for experiments that measured flame spread rate over combustible wall lining materials [2]; this test method has been standardized as FM 4910 [7]. As seen here, PMMA slabs, each 2.44 m tall by 0.61 m wide (nominally 8 ft. tall by 2 ft. wide) and  5.8 mm thick are mounted onto two inert parallel walls and ignited at their base using a rectangular propane burner (description below). The panel walls were each constructed by a 25 mm thick layer Marinite Board (Thermophysical properties [3] available in Table 3) attached to a 13 mm thick layer of plywood, both of which are attached to a vertical metal frame. The metal support frame for the Parallel Panel Apparatus was constructed in two parts, each positioned on a sliding track. The panels were positioned such that the front surface of each sample aligned with the outer edge of the propane burner below (i.e., 30 cm apart); the bottom edge of each sample aligned with the top edge of the burner and was sealed by aluminum tape. The origin of the coordinate system is located at the center of the top of the propane burner; with the positive _z_-direction identifying height above the top surface of the burner in the vertical direction (see Fig. 1).

Samples were attached to the parallel panel walls by a series of bolts (twelve per panel), which were evenly distributed at six heights, _z_, across the height of each sample. Each bolt was drilled approximately 10 cm away from the centerline of the panels (i.e., at _y_ = -10 cm or _y_ = 10 cm; see Fig. 1 for relevant coordinate system). A steel washer, approximately 2.5 cm in diameter, was used to distribute the load held by the bolt at each attachment point at the sample's front surface. Additionally, a series of  steel brackets were used to secure the top, bottom, and outer edges of each sample to the panel walls. 

In each test, measurements of total flame to surface heat flux were obtained by a series of up to 14 water-cooled Schmidt-Boelter heat flux gauges (0.64 cm < diameter < 1.59 cm) positioned flush with the front surface of the PMMA slabs. Additionally, a Schmidt-Boelter heat flux gauge (2.54 cm diameter) was positioned approximately 3 m to 4.25 m away from the parallel panel assembly, approximately 45 degrees away from the gap between the two panels (i.e., at approximately _x_ = -1 m or -3 m, _y_ = -3 m, and _z_ = 0.9 m). This gauge was used to identify the timing of fire events at the test floor and to provide a measurement of radiation heat transfer at a distance from the fire for model validation. Required gauge locations are more carefully defined in Table 2 below and in the [Experimental Data Files](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/).

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Documentation/Panel_Assembly.png" width="400">

Figure 1. Schematic of the Parallel Panel Apparatus (original apparatus design based on FM 4910 [7]; tests conducted at NIST)

#### Propane Burner 

As seen in Fig. 1, a rectangular propane burner was placed at the base of the parallel panel assembly to ignite samples. A mass flow controller was used to feed propane (CP grade, 99% purity) to the burner at a rate that would support, nominally, a 60 kW fire. For PMMA Test R6 (from which time-resolved HRR and q"rad data was selected for detailed analysis at MaCFP-3) this burner was filled with a 0.15 m deep layer of pea gravel, topped by 0.075 m layer of sand, and a 0.025 m thick sheet of porous, flexible insulation (Kaowool Blanket); each of these layers rested on top of a steel mesh that maintained a 0.05 m plenum at the base of the burner (see Fig. 2a). This multi-layered-fill design supported fairly uniform flaming across the burner's surface.

Measured burner heat release rate (HRR) quickly increases to 50 kW +/- 6.9 kW by t = 40 s after burner ignition; a steady state HRR of 63 kW +/- 7.0kW is achieved by t = 80 s. Reported uncertainties in burner HRR represent an expanded uncertainty (95% confidence interval, coverage factor = 2) in measured HRR at each time step of interest (20, 40, 60, 80 s...). This expanded uncertainty is calculated by quadrature (i.e., 'root-sum-of-squares'), considering both: (1) the standard deviation of the mean in recorded HRR [+/- 3s interval, repeated measurements at that time] and (2) the combined uncertainty corresponding to the calorimetry measurements themselves [5].

In a series of repeated experiments, burner flame heat flux (to inert Marinite walls) was measured at multiple locations across the base of the panel walls. Time-resolved measurements of flame heat flux show similar behavior to HRR - that is, a quick rise within the first 40 s of burner ignition, followed by a more gradual increase to quasi-steady values by t = 80 s. During experiments with PMMA panels, the burner is turned on from time t = 0 until t = 120 s.

Figure 2b plots average measured total burner flame heat flux (to a water-cooled Schmidt-Boelter gauge) as a function of height, z, along the centerline of panels. Here, average heat flux (at a given time, HRR, and height, z) is calculated as the mean value of all measurements recorded during a +/- 3 s interval at a specific height in repeated experiments (in either the same test on opposite panel walls or repeated tests; at each location, repeated measurements were recorded between 3 and 12 times).

Error bars indicate an expanded uncertainty (u_exp(q"burner); 95% confidence interval, coverage factor = 2) based on the combined standard uncertainty of average measurement results, u_c(q"burner). The combined standard uncertainty, u_c(q"burner), is calculated by quadrature (i.e., 'root-sum-of-squares'), considering both: (1) the standard deviation of the mean in recorded heat fluxes [+/- 3s interval, repeated measurements at that point] and (2) the relative combined standard uncertainty corresponding to gauge calibration (2.08%) [1].

As seen here, burner flame heat flux, q"burner, decreases with sample height, z. Measurements of centerline burner flame heat flux are comparable to those reported in previous studies when heat flux from this propane burner was measured in repeated tests under nominally the same conditions (repeated years apart) [2,4].


|<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Documentation/Burner_Fill.png" width="400">|  <img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Documentation/Burner_heatflux.png" width="400">| 
|-----|-----|
|(a)|(b)|

*Figure 2.* Propane Burner Fill and Heat Flux

Burner flame heat flux measurements shown in Fig. 2b are provided on the [**Experimental Data**](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/) page. Also included in this folder are width-resolved (across the width of panel walls) measurements of burner flame heat flux (multi-layer configuration) obtained during steady flaming (i.e., 20 s average of measurements obtained after steady flaming was observed). Figure 3 plots this dataset, which is provided as [Burner\_steadyHF\_Width\_multi-layer.csv](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/). As seen here, measured flame heat flux decreases toward either edge of the panels but is otherwise fairly symmetric across the width of the panels. 
A summary of the data contained in each of these files is provided in Table 1. 

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Documentation/Burner_heatflux_colormap.png" width="400">

*Figure 3.* Spatially resolved measurements (across the width of panel walls) of total flame heat flux, q"burner [kW/m2] at steady state (multilayer configuration)

*Table 1*: Description of [Propane Burner  Data](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/)  (.csv files)

|Experimental Data File Name |  Description |
|---------------------|-----------------|
|Burner\_HF\_Centerline\_sand\_multi-layer.csv      | Time-resolved measurements of total heat flux from the propane burner to the centerline of inert panel walls when the burner is in its multi-layered configuration (i.e., filled with a 0.15 m deep layer of pea gravel, topped by 0.075 m layer of sand, and a 0.025 m thick sheet of porous, flexible insulation; Fig. 2). This burner configuration was used for PMMA test R6 |
|Burner\_steadyHF\_Width\_multi-layer.csv           | Width-resolved measurements of total heat flux (at quasi-steady state) from the propane burner to inert panel walls when the burner was in its multi-layered configuration (i.e., filled with a 0.15 m deep layer of pea gravel, topped by 0.075 m layer of sand, and a 0.025 m thick sheet of porous, flexible insulation). This burner configuration was used for PMMA test R6 |


### Measurements

#### Heat Release Rate (HRR) and Heat Flux at a Distance

The entire parallel panel test assembly was positioned beneath the 6.1 m by 6.1 m exhaust hood at the National Fire Research Laboratory (NFRL) at NIST, which is instrumented and capable of performing heat release rate measurements by oxygen consumption calorimetry for fires up to 3 MW [5], with a relative expanded uncertainty (95% confidence interval, coverage factor = 2) for generic combustible fuels of 6.8 % (for fire sizes between 500 kW and 3 MW). Note: burner heat release (approx. 60 kW)is considerably lower than the standard operating range of the 3 MW calorimeter [5]; thus the expanded uncertainty of this calorimetry measurment is defined as 10% (type B uncertainty).

In Test PMMA R6, radiative heat flux at a distance, q"rad, was measured using a Schmidt-Boelter heat flux gauge positioned approximately 3 m away from the parallel panel assembly (location details in Table 2). The expanded uncertainty corresponding to gauge calibration (u_exp(q"rad); 95% confidence interval, coverage factor = 2)is defined as 4.17% based on a recent calibration exercise [1]. The uncertainty of the _x_ and _y_ location of this heat flux gauge is estimated as +/- 15 cm (Type B uncertainty, representing a 95% confidence interval of true gauge location).

Time-resolved measurements of total HRR (including energy release from the propane burner) and q"rad are provided (as .csv files) in the [Experimental  Data Section](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/); Table 2 provides key information about each of these tests.  Figure 4 plots time-resolved measurements of total HRR and q"rad. As seen here strong agreement is observed between the rise, fall, and time to peak of HRR and q"rad measurements. Note: In this test, the propane burner was turned on between 0 < t < 120 s; reported HRR measurements are not corrected for the energy release from the propane burner flames.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Documentation/PMMA_HRR_q-rad-only.png" width="400">

*Figure 4.* Time-resolved measurements of HRR and radiation heat flux at a distance, q"rad, from Test R6

*Table 2*: Description of [Burner Setup and q"rad & Species Yield Data](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/)

|Experimental Data File Name | Burner Configuration    | Location of heat flux gauge at a distance |Soot yield [g/g]|CO2 Yield [g/g]|CO Yield [g/g]|
|---------------------|-----------------|-----------------|----------|----------|----------|
|PMMA\_HRR\_qrad\_R6.csv        |   multi-layer fill | _x_ = -1 m, _y_ = -3 m, _z_ = 0.9 m |0.00526 +/- 0.00079|2.238 +/- 0.082|0.0036 +/- 0.0011|

#### Wall Flame Heat Flux

Flame to surface heat flux across the height of the panel characterizes flaming conditions and controls the rate of flame spread. In each test (6 repetitions total on PMMA), total flame to surface heat flux, q", measurements were obtained by a series of up to 14 water-cooled heat flux gauges, each positioned flush with the front surface of the PMMA slabs. Time-resolved measurements of heat flux and HRR obtained in each test replicate are analyzed to determine spatially resolved heat flux profiles at different fire sizes and to determine related statistics from repeated measurements. First, clean heat flux measurements recorded at the same heights, _z_, (but, potentially, at different times and on opposite walls, i.e., different _x_ locations) in different tests are averaged together by analyzing them as a function of fire size (i.e., HRR).  Average values of total heat flux, are calculated at each HRR of interest as the mean of interpolated values recorded at a specific height, _z_, across +/- 3 intervals (measurements) of HRR. A standard deviation of the mean is then calculated at each HRR based on separate measurements obtained by unique heat flux gauges at the same height, _z_, in either (a) the same test on opposite panel walls or (b) repeated tests, on either panel wall. This process is repeated at all measurement locations and spatially-resolved heat feedback profiles are determined based on these average curves. 

PMMA flame heat flux data is provided in the file [PMMA_heatflux.csv](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Experimental_Data/PMMA_heatflux.csv). Measured height-resolved total (flame to wall) heat flux profiles are plotted alongside representative images of flame structure at seven heat release rates in Fig. 5. Here, error bars indicate an expanded uncertainty (u\_exp(q"); 95% confidence interval, coverage factor = 2) based on the combined standard uncertainty of average measurement results, u\_c(q"). The combined standard uncertainty, u\_c(q"), is calculated by quadrature (i.e., 'root-sum-of-squares'), considering both: (1) the random error in recorded heat fluxes (which is calculated as the standard deviation of the mean of repeated measurements) and (2) the relative combined standard uncertainty corresponding to gauge calibration (2.08%) [1]. 

More details about these measurement devices and techniques as well as their respective capabilities and uncertainties will be provided in an upcoming publication [1].

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/NIST_Parallel_Panel/Documentation/PMMA_flame_spread_heatflux.png" width="1000">

*Figure 5.*  Representative images of flame structure and height-resolved measurements of total flame to wall heat flux (as measured by an array of water-cooled, Schmidt-Boelter heat flux gauges) during upward flame spread over cast poly(methyl methacrylate), PMMA


### Notes

In each test, initial sample mass (combined mass of both panels) was approximately 20.75 kg +/- 0.1 kg. A negligible amount of PMMA was observed after sample burnout, thus it is assumed that the entire initial sample mass burned to completion throughout the duration of the experiment.

*Table 3*: Thermophysical Properties of Marinite Structural insulation board [3]

|Temperature (C)|  Density (kg/m3) | Thermal Conductivity (W/m-K) | Specific Heat (J/g-K)| 
|---------------------|-----------------|-----------------|-----------------|
|24     |   737 |   0.127    |      -   |
|93     |   -   |   -        |  1.172   |
|149    |   -   |   0.118    |      -   |
|205    |   -   |   0.117    |  1.256   |
|316    |   -   |   0.114    |  1.340   |
|425    |   -   |   0.117    |  1.423   |
|538    |   -   |   0.124    |      -   |


### Acknowledgments

This work was supported by the Office of Nuclear Regulatory Research (RES) of the US Nuclear Regulatory Commission (US NRC).

### References

1. Leventon, I.T., Heck, M.V., McGrattan, K. B., Bundy, M.F., Davis, R.D., The Impact of Material Composition on Ignitability and Fire Growth. Volume 1: Full-Scale Burning Behavior of Combustible Solids Commonly Found in Nuclear Power Plants, NIST Technical Note 22xx, National Institute of Standards and Technology, Gaithersburg, MD, _(In Preparation)_. 
2. P.A. Beaulieu. Parallel Panel Experiments of FRP Composites. Technical Report 0003024286, FM Global, Norwood, Massachusetts, December 2007.
3. BNZ Materials, Inc., 'Marinite I Refractory Products - Fire-Resistant Thermal, Structural Insulation' https://www.bnzmaterials.com/wp-content/uploads/2013/03/Mar-I.pdf (accessed September 14, 2022)
4.  Wu. P., Parallel Wall Fire Tests with PMMA and FRPPMMA, Technical Memorandum 0003024286, FM Global, December 1997.
5.  Bryant, R.A., Bundy, M.F., The NIST 20 MW Calorimetry measurement system for large-fire research. NIST Technical Note 2077, National Institute of Standards and Technology, Gaithersburg, Maryland, 2019
6.  Pitts, W.M., Murthy, A.V., De Ris, J.L. Filtz, J.-R., Nygard, K., Smith, D., and Wetterlund, I. Round robin study of total heat flux gauge calibration at fire laboratories. Fire Safety Journal, 41(6):459-475, 2006.
7.  FM Global, FM 4910