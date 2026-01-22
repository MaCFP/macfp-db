## Plotting scripts for NIST simulations of the JIS A 1310 experiments

The Python script in this directory creates plots that compare FDS and experimental results for the JIS Facade experiments. The plots are based on those found in Sun et al., Fire and Materials, 48:411–425, 2024. To create the plots, you should only need to run a single Python script:
```
python NIST_JIS_Facade_plots.py
```
The script creates a sub-directory called `Plots` containing:
   1. Experimental and simulated temperature contours in three vertical planes normal to the wall (Fig. 8 from Sun et al.)
   2. Experimental and simulated surface temperature profiles across and above the window (Fig. 9 from Sun et al.)
   3. Experimental and simulated heat flux profiles above the window (Fig. 10, Row C from Sun et al.)
