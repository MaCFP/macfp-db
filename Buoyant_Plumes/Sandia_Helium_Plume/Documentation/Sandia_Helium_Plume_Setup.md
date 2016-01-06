##Sandia Helium Plume Setup

####Introduction

The Fire Laboratory for Accreditation of Models by Experimentation (FLAME) facility [Blanchat, 2001; O'Hern et al., 2005] at Sandia National Laboratory in Albuquerque, New Mexico, is designed specifically for validating models of buoyant fire plumes. The plume source is 1 m in diameter surrounded by a 0.5 m steel "ground plane". Particle Image Velocimetry (PIV) and Planar Laser-Induced Fluorescence (PLIF) techniques were used to obtain instantaneous joint scalar and velocity fields.

<img src="https://github.com/MaCFP/macfp-db/blob/master/Buoyant_Plumes/Sandia_Helium_Plume/Documentation/Sandia_FLAME_facility.png" width="800">

####Run Conditions

Table 1: Run conditions and results summary for each of the 10 repeat tests and theiraverages. Uncertainties listed are ± one standard deviation [O'Hern et al., 2005].

| Run no. | Helium inlet velocity | Test type | Re | Ri | Meas. puffing freq. | Corr. puffing freq. (a) |
| ------- |:-------:| ------- |:------:|:------:|:-------:|:-------:|
|         | (m/s) ± 1.3% |           |± 0.6% |± 6.5% | (Hz)  | (Hz)  |    
| 20      | 0.314        | PIV       | 3344  | 80.57 | 1.20  | 1.33  |
| 22      | 0.319        | PIV       | 3300  | 78.06 | 1.41  | 1.34  |
| 23      | 0.303        | PIV       | 3198  | 86.72 | 1.36  | 1.32  |
| 25      | 0.340        | PIV/PLIF  | 3306  | 68.75 | 1.53  | 1.36  |
| 26      | 0.315        | PIV       | 3253  | 80.20 | 1.39  | 1.33  |
| 27      | 0.305        | PIV       | 3242  | 85.32 | 1.37  | 1.32  |
| 29      | 0.352        | PIV/PLIF  | 3256  | 64.32 | 1.42  | 1.37  |
| 30      | 0.337        | PIV       | 3176  | 70.20 | 1.19  | 1.36  |
| 32      | 0.349        | PIV/PLIF  | 3275  | 65.32 | 1.42  | 1.37  |
| 36      | 0.316        | PIV/PLIF  | 2933  | 79.74 | 1.41  | 1.33  |
| 10 test ave | 0.325    |           | 3228  | 75.74 | 1.37  | 1.34  |
| 4 Favre ave | 0.339    |           | 3194  | 69.53 | 1.45  | 1.36  |

(a) given by f = V0 (0.8 Ri^(0.38))/D [Cetegen & Kasper, 1996]

####References

[Blanchat, 2001] T.K. Blanchat. Characterization of the air source and plume source at FLAME.  Technical Report SAND01-2227, Sandia National Laboratory, Albuquerque, New Mexico, 2001.

[O'Hern et al., 2005] T.J. O'Hern, E.J. Weckman, A.L. Gerhart, S.R. Tieszen, and R.W. Schefer.  Experimental study of a turbulent buoyant helium plume. _J. Fluid Mech._, 544:143-171, 2005.
