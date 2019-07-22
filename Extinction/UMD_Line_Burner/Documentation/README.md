## University of Maryland Line Burner Setup

by James P. White

#### Introduction

The University of Maryland, turbulent line burner (TLB) experimental facility provides for the study of a low-strain, buoyancy-driven, fully-turbulent diffusion flame in a canonical line-fire configuration. This facility provides well-controlled inlet and boundary conditions, while introducing the complicating effects of buoyancy and turbulence characteristic of large-scale fires. A variety of non-intrusive diagnostics are used to measure local and integral flame characteristics. The facility comprises a slot burner centrally located within a co-flowing oxidizer. Controlled suppression of the flame is achieved via the introduction of either nitrogen gas or a fine water mist into the oxidizer stream. A detailed description of this facility has been presented by White et al. [1-4].

#### Experimental Description

A plan-view illustration of the burner and oxidizer assembly is presented in Fig. 1. The burner features a ground-glass filled, stainless-steel fuel port, measuring 5 cm wide by 50 cm long, with 1.5 mm thick side walls. Methane gas (99.5% purity) or propane gas (99.5% purity) are the primary burner fuels. A methane flow rate of 1.00 +/- 0.02 g/s (nominal 6.0 cm/s) or a propane flow rate of 1.08 +/- 0.02 g/s (nominal 2.3 cm/s) is utilized, measured using a mass flow controller. Assuming complete combustion, the total heat-release rate is roughly 50 kW for either fuel. The burner is centrally located at the outlet of a surrounding oxidizer port, measuring 50 cm wide by 75 cm long, with 10 cm thick side walls. Flow conditioning elements ensure that the oxidizer is well-mixed and exits the oxidizer port with a uniform vertical velocity profile.

Sitting on top of the oxidizer port and surrounding the fuel port is a thin, 5 mm tall, 5 cm wide strip of ceramic fiberboard, positioned so the top of the board is 10 mm below the lip of the fuel port (and 5 mm above the oxidizer port). This board serves as a flow blockage to reduce the oxidizer velocity near the flame base, forcing the onset of buoyancy-generated turbulence upstream toward the fuel port and reducing the tendency to form laminar structures at the base of the flame. The oxidizer port sits 15 mm below the fuel port, while the perimeter around the oxidizer port sits at the same elevation as the fuel port.

For nitrogen-dilution suppression experiments, the flame is suppressed via the introduction of a variable flow of gaseous nitrogen into the oxidizer. The oxidizer is provided at a fixed total flow rate of 85 +/- 7 g/s (total, including variable nitrogen flow, nominal 25 cm/s), measured using a calibrated pitot-static probe. Suppression potential is characterized by the oxygen mole-fraction in the oxidizer, X_O2. Quantity X_O2 is measured using a paramagnetic oxygen analyzer via a probe located in the oxidizer port. The analyzer provides a measurement accuracy of +/- 1250 ppm O2 and a response time of 5 s.

For water-mist suppression experiments, the flame is suppressed via the introduction of a fine water mist into the oxidizer, generated using an array of piezoelectric atomizers. For water-mist suppression experiments, the oxidizer is provided at a fixed flow rate of 55 +/- 4 g/s (nominal 16 cm/s). The mist and oxidizer delivery systems support uniform entrainment of the mist into the oxidizer to provide a uniform distribution of mist-laden air at the outlet of the oxidizer port. The droplet size distribution of the entrained mist is characterized by a Sauter mean diameter (d_32) of 6.6 +/- 0.1 micron and a span of 1.9, measured using a Malvern Spraytec laser-diffraction system positioned at the outlet of the oxidizer port. Suppression potential is characterized by the mist mass-fraction in the oxidizer, Y_wm. Quantity Y_wm is measured using a mass balance based on steady-state operating conditions for which the rate of water delivery into the experimental facility is approximately equal to the net rate of mist produced by the piezoelectric atomizers [2].

Visible flame height is measured using a video camera, defined based on the 50% intermittent flame height [1]. These image-based measurements rely on visible flame emissions, including the incandescence of soot particles, and do not strictly locate the stoichiometric flame sheet. The uncertainty in each flame height measurement is roughly +/- 1.5 cm.

Radiative flame emissions are measured using a water-cooled Schmidt-Boelter heat-flux transducer. The sensor is positioned 100 cm radially outward from the burner centroid, 18 cm above the fuel port, facing perpendicular to the long axis of the burner. This device has a hemispherical absorptance of 0.94 for a spectral range between 0.6-15.0 micron, a maximum viewing angle of 90 degrees, and a response time of 0.25 s. Measurement uncertainty is +/- 3%. The convective portion of the measured heat flux is neglected and sans-flame measurements are applied to correct for background irradiation.

Heat flux data are converted to radiative loss fraction using a weighted multipoint radiation source model, whereby the measured heat flux is assumed to be received from an array of isotropic point sources uniformly distributed over a two-dimensional plane oriented across the visible flame surface [1]. The uncertainty in each radiative loss fraction measurement is roughly +/- 4.5%.

Mean and root-mean-square (rms) temperature statistics are recorded using an array of S-Type thermocouple probes positioned at selected locations along the vertical (axial) centerline of the flame and along radial (widthwise) flame profiles at selected elevations. Probe tips are constructed using 12.7-micron diameter wires with exposed, fusion-welded junctions (response time of approximately 1 ms). Temperature data are reported as uncompensated thermocouple measurements.

Combustion products are collected in a fire products collector, wherein a gas sampling system provides measurement of the molar concentrations of oxygen (+/- 1250 ppm O2), carbon dioxide (+/- 1000 ppm CO2), carbon monoxide (+/- 100 ppm CO), water vapor (+/- 1% RH), and total hydrocarbons (+/- 10 ppm THC) in the exhaust stream. From these measurements, integral heat release rate and combustion efficiency measurements are derived using species-based calorimetry techniques [2]. The uncertainty in the reported heat release rate measurements is roughly +/- 1.5 kW.

![alt text](https://github.com/MaCFP/macfp-db/blob/master/Extinction/UMD_Line_Burner/Documentation/umd_line_burner_plan_view.png)

Figure 1: Plan view of UMD Line Burner

#### Simulation Targets

Available [experimental data](https://github.com/MaCFP/macfp-db/tree/master/Extinction/UMD_Line_Burner/Experimental_Data) include:

* X_O2 at extinction, tabulated
  - methane
  - propane
* Flame height vs. X_O2
  - methane
  - propane
* Heat flux vs. X_O2
  - methane
  - propane
* HRR / combustion efficiency vs. Y_wm (water mist)
  - methane
* Mean local X_O2 profiles (x-direction)
  - methane, X_O2 = 0.18, z = 0.125
  - methane, X_O2 = 0.18, z = 0.250
* Mean thermocouple temperature profiles (x and z-directions)
  - methane, X_O2 = 0.21
* RMS thermocouple temperature profiles (x and z-directions)
  - methane, X_O2 = 0.21


#### References

1. J.P. White, E.D. Link, A.C. Trouvé, P.B. Sunderland, A.W. Marshall, J.A. Sheffel, M.L. Corn, M.B. Colket, M. Chaos, and H.-Z. Yu. Radiative emissions measurements from a buoyant, turbulent line flame under oxdizer-dilution quenching conditions, _Fire Safety Journal_, 76:74-84, 2015.

2. J.P. White, Measurement and simulation of suppression effects in a buoyant turbulent line fire, Ph.D. thesis, University of Maryland, College Park, 2016.

3. J.P. White, S. Verma, E. Keller, A. Hao, A. Trouvé, A.W. Marshall, Water mist suppression of a turbulent line fire, _Fire Safety Journal_ 91:705-713, 2017.

4. J.P. White, E.D. Link, A. Trouvé, P.B. Sunderland, A.W. Marshall, A general calorimetry framework for measurement of combustion efficiency in a suppressed turbulent line fire, _Fire Safety Journal_ 92:164-176, 2017


