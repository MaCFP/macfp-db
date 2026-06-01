## Laser Induced Incandescence (LII) Experimental Data Files

Data in this folder has been scaled by 1.823=7.6/4.17 to account for the difference in soot optical properties between what FM used to report the data and what FDS uses in RADCAL.

The emissive power of the flame roughly scales as kappa, the absorption coefficient, which in RADCAL is kappa(lambda) = C0\*fv/lambda.  FM used 7.6 for their C0 and hence report a lower value of fv.  FDS uses 4.17 for C0 and hence needs a higher fv to obtain the same emission.  The key point is that the higher fv and lower C0 are a plausible combination.  This requires more study. [RJM]

#### fvmean.csv
* This file contains the mean soot volume fraction distribution in normal air condition.
* The data were measured at 0.5D, 1.0D, 1.5D, 2.5D, and 3.5D heights, where D is the burner diameter (15.2 cm).
* Each column lists the soot volume fraction (unit: parts-per-million, ppm) at different distance from flame centerline for one height.

#### fvrms.csv
* This file contains the RMS of soot volume fraction fluctuation in normal air condition.
* The data were measured at 0.5D, 1.0D, 1.5D, 2.5D, and 3.5D heights, where D is the burner diameter (15.2 cm).
* Each column lists the RMS of soot volume fraction fluctuation (unit: parts-per-million, ppm) at different distance from flame centerline for one height.

#### Local_fvpdf_0.5D_*.csv
* This file contains the probability density function of soot volume fraction in normal air condition at 0.5D height, where D is the burner diameter (15.2 cm).
* The data were measured at different locations away from the centerline (0 cm, 1 cm, …until 16 cm), with a 1 cm×1 cm area for PDF statistical analysis.
* The first two columns list the edges and center of bins (unit: ppm).
* From the third column, each column lists the PDF for certain soot volume fraction for one location.

#### Local_fvpdf_1.0D_*.csv
* This file contains the probability density function of soot volume fraction in normal air condition at 1.0D height, where D is the burner diameter (15.2 cm).
* The data were measured at different locations away from the centerline (0 cm, 1 cm, …until 16 cm), with a 1 cm×1 cm area for PDF statistical analysis.
* The first two columns list the edges and center of bins (unit: ppm).
* From the third column, each column lists the PDF for certain soot volume fraction for one location.

#### Local_fvpdf_1.5D_*.csv
* This file contains the probability density function of soot volume fraction in normal air condition at 1.5D height, where D is the burner diameter (15.2 cm).
* The data were measured at different locations away from the centerline (0 cm, 1 cm, …until 16 cm), with a 1 cm×1 cm area for PDF statistical analysis.
* The first two columns list the edges and center of bins (unit: ppm).
* From the third column, each column lists the PDF for certain soot volume fraction for one location.

#### Local_fvpdf_2.5D_*.csv
* This file contains the probability density function of soot volume fraction in normal air condition at 2.5D height, where D is the burner diameter (15.2 cm).
* The data were measured at different locations away from the centerline (0 cm, 1 cm, …until 16 cm), with a 1 cm×1 cm area for PDF statistical analysis.
* The first two columns list the edges and center of bins (unit: ppm).
* From the third column, each column lists the PDF for certain soot volume fraction for one location.

#### Local_fvpdf_3.5D_*.csv
* This file contains the probability density function of soot volume fraction in normal air condition at 3.5D height, where D is the burner diameter (15.2 cm).
* The data were measured at different locations away from the centerline (0 cm, 1 cm, …until 16 cm), with a 1 cm×1 cm area for PDF statistical analysis.
* The first two columns list the edges and center of bins (unit: ppm).
* From the third column, each column lists the PDF for certain soot volume fraction for one location.


