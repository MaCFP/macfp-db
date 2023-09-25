#!/usr/bin/env python3
# McDermott
# 25 Sep 2023
#
# Integrate vertical radiant power distribution to confirm radiant fraction

import pandas as pd

R = pd.read_csv('./Radiant_power_distribution.csv', sep=',', header=0);
R = R.fillna(0.)

XO2 = ["Air-mean","19per-mean","17per-mean","15per-mean"]
Q_TOTAL = 15. # kW
for o2 in XO2:
    QR = 0.
    z_last = 0.
    for i in range(1,21):
        if i>1:
            z_last = float(R["height"].values[i-1])

        dz = (float(R["height"].values[i]) - z_last)*0.01
        QR += float(R[o2].values[i])*dz

    print("Radiant fraction "+o2+" = "+str(QR/Q_TOTAL))

# these values are used in the file Radiant_fraction3.csv
# In [1]: run Integrate_radiant_power.py
# Radiant fraction Air-mean = 0.32916522093333334
# Radiant fraction 19per-mean = 0.31399408879999996
# Radiant fraction 17per-mean = 0.2822435130666666
# Radiant fraction 15per-mean = 0.21575806480000004