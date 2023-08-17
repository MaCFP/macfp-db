#!/usr/bin/env python3
# McDermott
# 16 Aug 2023
#
# Read and process FDS output files for FM_Burner cases to compute
# Eta (combustion efficiency) and Chi_r (radiative fraction)

import numpy as np
import pandas as pd

outdir = './Preliminary_Results/'

# create files with XO2 as independent column

fuel_name = ['C2H4','C3H6','C3H8','CH4']
res_name  = ['2cm','1cm'] #,'5mm']

for fuel in fuel_name:
   for res in res_name:

      DEV = pd.read_csv(outdir+'FM_15cm_Burner_'+fuel+'_'+res+'_devc.csv', sep=',', header=1)
      HRR = pd.read_csv(outdir+'FM_15cm_Burner_'+fuel+'_'+res+'_hrr.csv', sep=',', header=1)

      XO2_FDS  = DEV["XO2"].values[:].astype(float)
      Qdot_FDS = HRR["HRR"].values[:].astype(float)
      Qrad_FDS = HRR["Q_RADI"].values[:].astype(float)

      ETA = Qdot_FDS/np.max(Qdot_FDS)
      CHI_R = np.minimum(1.,np.maximum(0.,-Qrad_FDS)/np.maximum(0.001,Qdot_FDS))

      df = pd.DataFrame({'XO2': XO2_FDS[1:],
                         'eta': ETA[1:],
                         'Chi_R': CHI_R[1:]})

      df.to_csv(outdir+'FM_15cm_Burner_'+fuel+'_'+res+'.csv',index=False,float_format='%5.3f')

# create files with Time as independent column for C2H4 fuel

O2_name  = ['20p9','19p0','16p8','15p2']
res_name = ['2cm','1cm'] #,'5mm']

for O2 in O2_name:
   for res in res_name:

      HRR = pd.read_csv(outdir+'FM_15cm_Burner_C2H4_'+O2+'_'+res+'_hrr.csv', sep=',', header=1);

      Time_FDS = HRR["Time"].values[:].astype(float)
      Qdot_FDS = HRR["HRR"].values[:].astype(float)
      Qrad_FDS = HRR["Q_RADI"].values[:].astype(float)

      CHI_R = np.minimum(1.,np.maximum(0.,-Qrad_FDS)/np.maximum(0.001,Qdot_FDS))

      df = pd.DataFrame({'Time': Time_FDS[1:],
                         'Chi_r': CHI_R[1:]})

      df.to_csv(outdir+'FM_15cm_Burner_C2H4_'+O2+'_'+res+'_chir.csv',index=False,float_format='%5.3f')


