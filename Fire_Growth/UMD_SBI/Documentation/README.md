## UMD Corner Fire Spread

### Note

A brief description of the experimental setup and measurement procedures is provided here. A more complete description of the setup and data processing can be found in a recent publication [1].

Corresponding authors: stolia@umd.edu, dushyant.chaudhari@ul.org

### Test Configuration
The experimental setup, shown in Fig. 1, was based on the Single Burning Item (SBI) test [2], but with symmetric panels. 
Two 50 cm wide and 0.58 cm thick black cast poly (methyl methacrylate) (PMMA) panels having a total height of 146 cm were mounted onto Marinite I calcium silicate board (1.27 cm thick). The Marinite I calcium silicate boards were 60 cm wide and thus extended out 10 cm beyond the PMMA  panels on both sides. The properties of both materials can be found in Ref. [1]. 

Panel walls were ignited by a triangular propane sandbox burner (side length = 25 cm; height = 3.5 cm), that was placed 4 cm away from both panels. The burner flame was maintained on throughout the duration of the experiment, with a heat release rate (HRR) of 30 kW.  In this configuration, the bottom 3.5 cm of the PMMA panels was located below the top surface of the burner and did not contribute significantly to the HRR. The positive y-direction was therefore assigned as upwards (in vertical direction) from the top edge of the burner. Thus, y = 0 cm corresponds to the top surface of the burner and the PMMA panels extended to y = 142.5 cm (i.e., the top of the panel walls were 142.5 cm above the top edge of the burner). 
 
The burner was built exactly in accordance with EN 13823 [2]. The stainless steel plate used for fabricating the burner was approximately 0.2 cm thick. The burner was layered with fine sand (2 to 4 mm diameter sand) on the top such that it created a flat burner surface, without a lip. A welded U-channel, made of steel and width of 4 cm, separated the panel and the burner. The panel mounted on the Marinite I board rested on 0.635 cm thick Kaowool on an 80/20 Aluminum frame. 

The corner setup was placed inside an exhaust hood, whose bottom edge was 220 cm above the concrete floor. The exhaust hood extracted combustion products at a set volumetric flow rate of 0.56 $\mathrm{m}^3\cdot \mathrm{s}^{-1}$. Fire resistant curtains, extending towards the floor 160 cm below the bottom of the hood, to constrain the volume of the enclosure. The remainder 60 cm between the floor and the bottom of the fire curtains were covered with a fabric mesh on all sides to help homogenize the incoming air flow.

A set of 7 experiments was performed. All sensor data were collected at 10 Hz frequency using a LabVIEW enabled computer. The flame was allowed to spread until the HRR reached 300 kW. Once the HRR exceeded this threshold value, the propane burner was turned off and the flame was extinguished.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Documentation/UMDCornerFireSpreadSetup.jpg" width="1000">

*Figure 1.* Schematic of the experimental setup.

### Measurements

#### Heat Release Rate (HRR)

The panel and burner setup were located under an exhaust hood, which was equipped to perform oxygen consumption calorimetry based on readings from a paramagnetic oxygen sensor, multi-point averaging Pitot tube, three K-type thermocouples, and atmospheric pressure, temperature, and humidity sensor [1]. The calorimetry data (HRR) are provided in the HRR folder. The HRR response time for this system was found to be 13 s. The uncertainties in the HRR were computed from the scatter of individual measurements as two standard deviations of the mean. [Data file info for HRR](#hrr)

#### Heat Flux to the Wall

The second set of measurements that was performed in the same experiments is the heat flux to the PMMA panels. The heat flux readings were collected as a function of time using 9.5 mm diameter water-cooled Schmidt-Boelter heat flux gauges installed flush with the exposed surface of one of the PMMA panels at 28 distinct locations depicted in Fig. 1. In this figure, x represents the distance from the vertical corner. The heat flux measurements were performed twice at each location and were verified to be symmetric with respect to the plane bisecting the vertical corner. The acquired data at each location were binned into 10 s intervals and the average was calculated using the data from two datasets and set of 100 data points per bin (total 200 data points). The error reported here was calculated as two standard deviations of the mean from the 200 data points and a 3% systematic uncertainty corresponding to the gauge calibration [1] was added to it. The average resulting from the 10 s bin were assigned to a time stamp which correspond to the mean of the first and last time stamp of the respective 10 s bin. The flame heat flux data are provided in the HFG folder. [Data file info for Heat Flux](#total-heat-flux-to-the-wall)

#### Radiation Intensity at a Distance

The third set of measurements performed in the same experiments was carried out using a DSLR camera with extended spectral receptivity equipped with a 900 nm ± 10 nm narrowband filter. This camera was focused on one panel to record emissions from soot during the flame spread process. Soot is known to be the primary emitting species at this wavelength [3]. The video data was processed in the following way: First, the individual frames were converted into grayscale format by taking an equal weighted mean of the R, G, and B channels. Second, the grayscale images were binned in 10 s intervals and averaged to have one grayscale image for the bin which was assigned a time stamp corresponding to the mean of the start and the end time stamp of the respective bin. The data were normalized by absolute maximum grayscale intensity observed across all experiments and time. The data were then transformed into a uniform grid of 0.5 cm and, finally, the normalized intensity data were obtained by averaging the uniform grid data for each bin across seven experiments. The processed data from these images in the form of normalized radiation intensity plots can be requested via email.

#### Flame Probabilities

The DSLR camera video acquired at 900 ± 10 nm narrowband filter (setup described in the preceding paragraph) were also processed to obtain flame probability maps during the fire-growth. First, individual frames from the video were converted to grayscale by equal weighted mean of the R, G, and B channels. Second, the grayscale images were binarized using a threshold of 39 s<sup>-1</sup> (50/(255$/times$ 0.005 s)). This threshold was normalized by the camera exposure time of 5 ms. The binarized frames were then binned in 10 s intervals and averaged for the respective bin intervals. The resulting data were then transformed into a uniform 0.5 cm grid by averaging pixel data around the physical 0.5 cm diameter circles (or semi-circle for boundary data) around the new grid points. For this, pixel to physical scale ratio for each experiment, calibrated before each test, were used. Finally, the data from the uniform 0.5 cm grid from seven experiments were averaged to obtain the reported flame probabilities. A way to interpret these data is given by an example: a probability of 0.2 mean that 20\% of images during a given 10 s interval had local intensity greater than the threshold, i.e. the flame was present at this location for 20\% of the time. [Data file info for Flame Probabilities](#flame-probabilities)

#### Heat Flux at a Distance

Two additional experiments were performed to measure radiative heat flux away from the flame, at locations shown in Fig. 2. Six water-cooled heat flux gauges and two radiometers were used in these measurements. They were oriented so that their wide angle sensors (150 degree viewing angle) were facing the vertical corner. The total heat flux gauge measurements were found to provide the same readings as the radiometers, when placed at the same location. This means that both measured the radiative heat flux from the flame and hot solid surfaces without any significant addition by convection. These data were processed in exactly the same way as were the total flame heat flux data. The error for these data were also calculated in the same way (two standard deviation of the mean from binned data and additional 3% systematic uncertainty corresponding to gauge calibration). [Data file info for Heat Fluxes at a Distance](#heat-flux-away-from-the-wall)

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Documentation/RadFluxAwayFromFireSetup.jpg" width="800">

*Figure 2.* Locations of the heat flux gauges and radiometers for measuring radiative heat flux away from the flame. Locations marked with red circles indicate locations where a radiometer was placed next to the total heat flux gauge to ensure that the total heat flux gauge read radiative heat flux only.

### Data file information

#### HRR

The heat release rate (HRR) was calculated using oxygen consumption calorimetry, as per equations briefly discussed in ref [1]. All the relevant data were acquired at 10 Hz frequency and the data are presented here at 1 Hz frequency (1 s interval) obtained by performing a moving average of the raw data. These data were averaged from seven experiments, and the errors reported here are two standard deviations of the mean. Data provided in the file: [HRR\_1Hz\_7TestAverage.csv](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Experimental_Data/HRR_1Hz_7TestAverage.csv). 

#### Total heat flux to the wall

Comma-delimited (.csv) files beginning with "Total\_HF\_binned\_", in the HFG directory, contains the total heat flux to the wall data for each height above the burner surface. These locations are from y = 10 cm to y = 130 cm, at 20 cm intervals (seven files). In each csv file, total heat flux data, processed as discussed earlier (see processing steps in 'Heat Flux to the Wall' Section), contains time in the first column. The next four columns are labeled as HFG\_x\_y where x denotes direction away from the corner (for x = 5 cm, x = 10 cm, x = 15 cm, and x = 22 cm) and y denotes height above the burner surface in cm. The last four columns present error data for the four distances away from the corner, with headers as Error\_x\_y for respective HFG\_x\_y value. The height above the burner surface is also indicated in the respective filename.

#### Heat flux away from the wall

The csv file named "Rad\_flux\_away\_from\_the\_flame\_binned.csv" contains radiative heat flux data at a distance. The first column in the csv file contains time in seconds. The next six columns contain heat fluxes at y = 10 cm to y = 135 cm at 25 cm interval with header as HFG\_y for respective height. The error for the respective height is presented in the last six columns, with headers as Error_y. Data provided in the file: 
[Rad\_flux\_away\_from\_the\_flame\_binned.csv](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Experimental_Data/Rad_flux_away_from_the_flame_binned.csv). 

#### Radiation intensity at a distance

Note: These data can be provided upon request via email.

Each csv file in the 900 nm normalized intensity directory contains the time at which the processed data was allocated (mean of the edges of the 10 s bin). The top row contains interval away from the corner at 0.5 cm interval, spanning  from x = 0 cm to x = 32 cm. The first column contains distance above the burner surface in cm. Data corresponding to six representative time-stamps are provided here with the time, t, also indicated in the filename. 

Please see Ref. [1] for more information about how the radiation intensities can be obtained from CFD models, provided spectrally resolved radiation intensity can be extracted. 

### Flame Probabilities

Csv files (beginning with `FlameProbabilities`) containing flame probability data for 35, 105, 145, and 185 s are provided here. The top row of each csv provides locations away from the corner in cm, and the first column provide location above the burner surface in cm. The first value in each csv file contains information of the time corresponding to the data. These times are average of the bin interval (For example, 105s means average of data between 100 and 110 s). Additional data can be provided upon request via email. Data provided in the directory: [FlameProbabilitites](https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Experimental_Data/FlameProbabilities) 

### References

1. D.M. Chaudhari, G.J. Fiola, S.I. Stoliarov, Experimental analysis and modeling of Buoyancy-driven flame spread on cast poly(methyl methacrylate) in corner configuration, Polym. Degrad. Stab. 183 (2021) 109433. doi:10.1016/j.polymdegradstab.2020.109433.

2. EN-13823, Reaction to Fire Tests for Building Products - Building Products Excluding Floorings Exposed to the Thermal Attack by a Single Burning Item,(2004).

3. R. Siegel, J.R. Howell, in: Thermal Radiation Heat Transfer, 4th ed., Taylor & Francis, 2002, p. 533.
