#!/usr/bin/env python3
# McDermott
# 25 Sep 2023
#
# Integrate vertical radiant power distribution to confirm radiant fraction

import pandas as pd

outdir = './Output4/'


XO2 = ["20p9", "19p0", "16p8", "15p2"]
Q_TOTAL = 15. # kW
for o2 in XO2:
    R = pd.read_csv(outdir+'FM_15cm_Burner_C2H4_'+o2+'_5mm_line.csv', sep=',', header=1);
    R = R.fillna(0.)
    QR = 0.
    z_last = 0.
    for i in range(1,len(R)):
        if i>1:
            z_last = float(R["z"].values[i-1])

        dz = (float(R["z"].values[i]) - z_last)*0.01
        QR += float(R["RHRRPUL"].values[i])*dz

    print("Radiant fraction "+o2+" = "+str(QR/Q_TOTAL))

# these values are used in the file Radiant_fraction3.csv
# In [1]: run Integrate_radiant_power.py
# Radiant fraction Air-mean = 0.32916522093333334
# Radiant fraction 19per-mean = 0.31399408879999996
# Radiant fraction 17per-mean = 0.2822435130666666
# Radiant fraction 15per-mean = 0.21575806480000004