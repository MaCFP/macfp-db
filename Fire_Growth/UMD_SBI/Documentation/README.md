## UMD Corner Fire Spread

### Note

A brief description of the experimental setup and measurement procedures is provided here. A more complete description of the setup and data processing can be found in a recent publication [1].

### Test Configuration
The experimental setup, shown in Fig. 1, was based on the Single Burning Item (SBI) test [2], but with symmetric panels. A triangular propane sandbox burner, with a heat release rate (HRR) of 30 kW, was placed 4 cm away from both the panels and was used to ignite the panels. The burner flame was maintained for the duration of the experiment. Two 149 cm tall, 40 cm wide and 0.58 cm thick black cast poly (methyl methacrylate) (PMMA) panels were mounted on the Marinite I calcium silicate board. The properties of both materials can be found in Ref. [1]. Here, the positive y-direction was assigned from the top edge of the burner in vertical direction. The PMMA panels extended 142. 5 cm (y = 142. 5 cm) above the top edge of the burner. 

A set of 7 experiments was performed. All sensor data were collected at 10 Hz frequency using a LabVIEW enabled computer. The flame was allowed to spread until the HRR reached 300 kW. Once the HRR exceeded this threshold value, the propane burner was turned off and the flame was extinguished.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Documentation/UMDCornerFireSpreadSetup.jpg" width="800">

*Figure 1.* Schematic of the experimental setup.

### Measurements

#### Heat Release Rate (HRR)

The panel and burner setup were located under an exhaust hood, which was equipped to perform oxygen consumption calorimetry based on readings from a paramagnetic oxygen sensor, multi-point averaging Pitot tube, three K-type thermocouples, and atmospheric pressure, temperature, and humidity sensor [1]. The calorimetry data (HRR) are provided in the HRR folder. The HRR response time for this system was found to be 13 s. The uncertainties in the HRR were computed from the scatter of individual measurements as two standard deviations of the mean.

#### Heat Flux to the Wall

The second set of measurements that was performed in the same experiments is the heat flux to the PMMA panels. The heat flux readings were collected as a function of time using 9.5 mm diameter water-cooled Schmidt-Boelter heat flux gauges installed flush with the exposed surface of one of the PMMA panels at 28 distinct locations depicted in Fig. 1. In this figure, x represents the distance from the vertical corner. The heat flux measurements were performed twice at each location and were verified to be symmetric with respect to the plane bisecting the vertical corner. The acquired data at each location were binned into 10 s intervals and the average was calculated using the data from two datasets and set of 100 data points per bin (total 200 data points). The error reported here was calculated as two standard deviations of the mean from the 200 data points and a 3% systematic uncertainty corresponding to the gauge calibration [1] was added to it. The average resulting from the 10 s bin were assigned to a time stamp which correspond to the mean of the first and last time stamp of the respective 10 s bin. The flame heat flux data are provided in the HFG folder. 

#### Radiation Intensity at a Distance

The third set of measurements performed in the same experiments was carried out using a DSLR camera with extended spectral receptivity equipped with a 900 nm ± 10 nm narrowband filter. This camera was focused on one panel to record emissions from soot during the flame spread process. Soot is known to be the primary emitting species at this wavelength [3]. The video data was processed in the following way: First, the individual frames were converted into grayscale format by taking an equal weighted mean of the R, G, and B channels. Second, the grayscale images were binned in 10 s intervals and averaged to have one grayscale image for the bin which was assigned a time stamp corresponding to the mean of the start and the end time stamp of the respective bin. The data were normalized by absolute maximum grayscale intensity observed across all experiments and time. The data were then transformed into a uniform grid of 0.5 cm and, finally, the normalized intensity data were obtained by averaging the uniform grid data for each bin across seven experiments. The processed data from these images in the form of normalized radiation intensity plots are reported in the 900 nm normalized intensity folder.

#### Heat Flux at a Distance

Two additional experiments were performed to measure radiative heat flux away from the flame, at locations shown in Fig. 2. Six water-cooled heat flux gauges and two radiometers were used in these measurements. They were oriented so that their wide angle sensors (150 degree viewing angle) were facing the vertical corner. The total heat flux gauge measurements were found to provide the same readings as the radiometers, when placed at the same location. This means that both measured the radiative heat flux from the flame and hot solid surfaces without any significant addition by convection. These data were processed in exactly the same way as were the total flame heat flux data. The error for these data were also calculated in the same way (two standard deviation of the mean from binned data and additional 3% systematic uncertainty corresponding to gauge calibration). These data are provided in the file: 
[Rad\_flux\_away\_from\_the\_flame\_binned.csv](https://github.com/MaCFP/macfp-db/blob/master/ExtinctionFire_Growth/UMD_SBI/Experimental_Data/). 

<img src="https://github.com/MaCFP/macfp-db/blob/master/Fire_Growth/UMD_SBI/Documentation/RadFluxAwayFromFireSetup.jpg" width="800">

*Figure 2.* Locations of the heat flux gauges and radiometers for measuring radiative heat flux away from the flame. Locations marked with red circles indicate locations where a radiometer was placed next to the total heat flux gauge to ensure that the total heat flux gauge read radiative heat flux only.

### Data file information

#### HRR

The heat release rate (HRR) was calculated using oxygen consumption calorimetry, as per equations briefly discussed in ref [1]. All the relevant data were acquired at 10 Hz frequency and the data are presented here at 1 Hz frequency (1 s interval) obtained by performing a moving average of the raw data. These data were averaged from seven experiments, and the errors reported here are two standard deviations of the mean. 

#### Total heat flux to the wall

Comma-delimited (.csv) files beginning with "Total\_HF\_binned\_", in the HFG directory, contains the total heat flux to the wall data for each height above the burner surface. These locations are from y = 10 cm to y = 130 cm, at 20 cm intervals (seven files). In each csv file, total heat flux data, processed as discussed earlier (see processing steps in 'Heat Flux to the Wall' Section), contains time in the first column. The next four columns are labeled as HFG\_x\_y where x denotes direction away from the corner (for x = 5 cm, x = 10 cm, x = 15 cm, and x = 22 cm) and y denotes height above the burner surface in cm. The last four columns present error data for the four distances away from the corner, with headers as Error\_x\_y for respective HFG\_x\_y value. The height above the burner surface is also indicated in the respective filename.

#### Heat flux away from the wall

The csv file named "Rad\_flux\_away\_from\_the\_flame\_binned.csv" contains radiative heat flux data at a distance. The first column in the csv file contains time in seconds. The next six columns contain heat fluxes at y = 10 cm to y = 135 cm at 25 cm interval with header as HFG\_y for respective height. The error for the respective height is presented in the last six columns, with headers as Error_y. 

#### Radiation intensity at a distance

Each csv file in the 900 nm normalized intensity directory contains the time at which the processed data was allocated (mean of the edges of the 10 s bin). The top row contains interval away from the corner at 0.5 cm interval, spanning  from x = 0 cm to x = 32 cm. The first column contains distance above the burner surface in cm. Data corresponding to six representative time-stamps are provided here with the time, t, also indicated in the filename. 

Please see Ref. [1] for more information about how the radiation intensities can be obtained from CFD models, provided spectrally resolved radiation intensity can be extracted. 

### References

1. D.M. Chaudhari, G.J. Fiola, S.I. Stoliarov, Experimental analysis and modeling of Buoyancy-driven flame spread on cast poly(methyl methacrylate) in corner configuration, Polym. Degrad. Stab. 183 (2021) 109433. doi:10.1016/j.polymdegradstab.2020.109433.

2. EN-13823, Reaction to Fire Tests for Building Products - Building Products Excluding Floorings Exposed to the Thermal Attack by a Single Burning Item,(2004).

3. R. Siegel, J.R. Howell, in: Thermal Radiation Heat Transfer, 4th ed., Taylor & Francis, 2002, p. 533.
