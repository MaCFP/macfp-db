"""
FM_Burner.py
Python translation of FM_Burner.m (McGrattan, 7-30-2018)

Reads and processes FDS output files for FM_Burner cases.
"""

import os
import numpy as np
import pandas as pd

EXP_Dir = '../../../Experimental_Data/'


hrr_file = os.path.join(EXP_Dir, f"HRR_1Hz_7TestAverage.csv")
hrr_data = pd.read_csv(hrr_file, skiprows=[1])

hrrplus = hrr_data['HRR']+hrr_data['HRR_Error']
hrrminus = hrr_data['HRR']-hrr_data['HRR_Error']
hrrminus = np.maximum(hrrminus,0)

new_hrr_file = os.path.join(EXP_Dir, f"HRR_processed.csv")

selected_columns=hrr_data[['Time','HRR']]
np1 = pd.Series(hrrplus,name='HRRplus')
np2 = pd.Series(hrrminus,name='HRRminus')
hrr_processed = pd.concat([selected_columns,np1,np2],axis=1)
hrr_processed.to_csv(new_hrr_file,index=False)

rad_file = os.path.join(EXP_Dir, f"Rad_flux_away_from_the_flame_binned.csv")
rad_data = pd.read_csv(rad_file, skiprows=[1])

hfz = np.array([0.10,0.35,0.60,0.85,1.10,1.35])
hf35 = rad_data.loc[rad_data['Time']==35,['HFG_y10','HFG_y35','HFG_y60','HFG_y85','HFG_y110','HFG_y135']].values
hferr = rad_data.loc[rad_data['Time']==35,['Error_y10','Error_y35','Error_y60','Error_y85','Error_y110','Error_y135']].values
hf35p = hf35 + hferr
hf35m = hf35 - hferr

hf105 = rad_data.loc[rad_data['Time']==105,['HFG_y10','HFG_y35','HFG_y60','HFG_y85','HFG_y110','HFG_y135']].values
hferr = rad_data.loc[rad_data['Time']==105,['Error_y10','Error_y35','Error_y60','Error_y85','Error_y110','Error_y135']].values
hf105p = hf105 + hferr
hf105m = hf105 - hferr

hf145 = rad_data.loc[rad_data['Time']==145,['HFG_y10','HFG_y35','HFG_y60','HFG_y85','HFG_y110','HFG_y135']].values
hferr = rad_data.loc[rad_data['Time']==145,['Error_y10','Error_y35','Error_y60','Error_y85','Error_y110','Error_y135']].values
hf145p = hf145 + hferr
hf145m = hf145 - hferr

hf185 = rad_data.loc[rad_data['Time']==185,['HFG_y10','HFG_y35','HFG_y60','HFG_y85','HFG_y110','HFG_y135']].values
hferr = rad_data.loc[rad_data['Time']==185,['Error_y10','Error_y35','Error_y60','Error_y85','Error_y110','Error_y135']].values
hf185p = hf185 + hferr
hf185m = hf185 - hferr

rad_processed = pd.concat([pd.Series(hfz,name='z'),
                           pd.Series(hf35[0],name='HF35'),pd.Series(hf35p[0],name='HF35p'),pd.Series(hf35m[0],name='HF35m'),
                           pd.Series(hf105[0],name='HF105'),pd.Series(hf105p[0],name='HF105p'),pd.Series(hf105m[0],name='HF105m'),
                           pd.Series(hf145[0],name='HF145'),pd.Series(hf145p[0],name='HF145p'),pd.Series(hf145m[0],name='HF145m'),
                           pd.Series(hf185[0],name='HF185'),pd.Series(hf185p[0],name='HF185p'),pd.Series(hf185m[0],name='HF185m')],axis=1)

new_rad_file = os.path.join(EXP_Dir, f"Rad_processed.csv")
rad_processed.to_csv(new_rad_file,index=False)

y_10_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_10cm.csv"),skiprows=[1])
y_30_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_30cm.csv"),skiprows=[1])
y_50_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_50cm.csv"),skiprows=[1])
y_70_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_70cm.csv"),skiprows=[1])
y_90_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_90cm.csv"),skiprows=[1])
y_110_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_110cm.csv"),skiprows=[1])
y_130_data = pd.read_csv(os.path.join(EXP_Dir, f"Total_HF_binned_y_130cm.csv"),skiprows=[1])

hfz = np.array([0.10,0.30,0.50,0.70,0.90,1.10,1.30])

hf35_10 = y_10_data .loc[y_10_data ['Time']==35,['HFG_x5_y10','HFG_x10_y10','HFG_x15_y10','HFG_x22_y10']].values
hferr = y_10_data .loc[y_10_data['Time']==35,['Error_x5_y10','Error_x10_y10','Error_x15_y10','Error_x22_y10']].values
hf35_10p = hf35_10 + hferr
hf35_10m = hf35_10 - hferr

hf105_10 = y_10_data .loc[y_10_data ['Time']==105,['HFG_x5_y10','HFG_x10_y10','HFG_x15_y10','HFG_x22_y10']].values
hferr = y_10_data .loc[y_10_data['Time']==105,['Error_x5_y10','Error_x10_y10','Error_x15_y10','Error_x22_y10']].values
hf105_10p = hf105_10 + hferr
hf105_10m = hf105_10 - hferr

hf145_10 = y_10_data .loc[y_10_data ['Time']==145,['HFG_x5_y10','HFG_x10_y10','HFG_x15_y10','HFG_x22_y10']].values
hferr = y_10_data .loc[y_10_data['Time']==145,['Error_x5_y10','Error_x10_y10','Error_x15_y10','Error_x22_y10']].values
hf145_10p = hf145_10 + hferr
hf145_10m = hf145_10 - hferr

hf185_10 = y_10_data .loc[y_10_data ['Time']==185,['HFG_x5_y10','HFG_x10_y10','HFG_x15_y10','HFG_x22_y10']].values
hferr = y_10_data .loc[y_10_data['Time']==185,['Error_x5_y10','Error_x10_y10','Error_x15_y10','Error_x22_y10']].values
hf185_10p = hf185_10 + hferr
hf185_10m = hf185_10 - hferr

hf35_30 = y_30_data .loc[y_30_data ['Time']==35,['HFG_x5_y30','HFG_x10_y30','HFG_x15_y30','HFG_x22_y30']].values
hferr = y_30_data .loc[y_30_data['Time']==35,['Error_x5_y30','Error_x10_y30','Error_x15_y30','Error_x22_y30']].values
hf35_30p = hf35_30 + hferr
hf35_30m = hf35_30 - hferr

hf105_30 = y_30_data .loc[y_30_data ['Time']==105,['HFG_x5_y30','HFG_x10_y30','HFG_x15_y30','HFG_x22_y30']].values
hferr = y_30_data .loc[y_30_data['Time']==105,['Error_x5_y30','Error_x10_y30','Error_x15_y30','Error_x22_y30']].values
hf105_30p = hf105_30 + hferr
hf105_30m = hf105_30 - hferr

hf145_30 = y_30_data .loc[y_30_data ['Time']==145,['HFG_x5_y30','HFG_x10_y30','HFG_x15_y30','HFG_x22_y30']].values
hferr = y_30_data .loc[y_30_data['Time']==145,['Error_x5_y30','Error_x10_y30','Error_x15_y30','Error_x22_y30']].values
hf145_30p = hf145_30 + hferr
hf145_30m = hf145_30 - hferr

hf185_30 = y_30_data .loc[y_30_data ['Time']==185,['HFG_x5_y30','HFG_x10_y30','HFG_x15_y30','HFG_x22_y30']].values
hferr = y_30_data .loc[y_30_data['Time']==185,['Error_x5_y30','Error_x10_y30','Error_x15_y30','Error_x22_y30']].values
hf185_30p = hf185_30 + hferr
hf185_30m = hf185_30 - hferr

hf35_50 = y_50_data .loc[y_50_data ['Time']==35,['HFG_x5_y50','HFG_x10_y50','HFG_x15_y50','HFG_x22_y50']].values
hferr = y_50_data .loc[y_50_data['Time']==35,['Error_x5_y50','Error_x10_y50','Error_x15_y50','Error_x22_y50']].values
hf35_50p = hf35_50 + hferr
hf35_50m = hf35_50 - hferr

hf105_50 = y_50_data .loc[y_50_data ['Time']==105,['HFG_x5_y50','HFG_x10_y50','HFG_x15_y50','HFG_x22_y50']].values
hferr = y_50_data .loc[y_50_data['Time']==105,['Error_x5_y50','Error_x10_y50','Error_x15_y50','Error_x22_y50']].values
hf105_50p = hf105_50 + hferr
hf105_50m = hf105_50 - hferr

hf145_50 = y_50_data .loc[y_50_data ['Time']==145,['HFG_x5_y50','HFG_x10_y50','HFG_x15_y50','HFG_x22_y50']].values
hferr = y_50_data .loc[y_50_data['Time']==145,['Error_x5_y50','Error_x10_y50','Error_x15_y50','Error_x22_y50']].values
hf145_50p = hf145_50 + hferr
hf145_50m = hf145_50 - hferr

hf185_50 = y_50_data .loc[y_50_data ['Time']==185,['HFG_x5_y50','HFG_x10_y50','HFG_x15_y50','HFG_x22_y50']].values
hferr = y_50_data .loc[y_50_data['Time']==185,['Error_x5_y50','Error_x10_y50','Error_x15_y50','Error_x22_y50']].values
hf185_50p = hf185_50 + hferr
hf185_50m = hf185_50 - hferr

hf35_70 = y_70_data .loc[y_70_data ['Time']==35,['HFG_x5_y70','HFG_x10_y70','HFG_x15_y70','HFG_x22_y70']].values
hferr = y_70_data .loc[y_70_data['Time']==35,['Error_x5_y70','Error_x10_y70','Error_x15_y70','Error_x22_y70']].values
hf35_70p = hf35_70 + hferr
hf35_70m = hf35_70 - hferr

hf105_70 = y_70_data .loc[y_70_data ['Time']==105,['HFG_x5_y70','HFG_x10_y70','HFG_x15_y70','HFG_x22_y70']].values
hferr = y_70_data .loc[y_70_data['Time']==105,['Error_x5_y70','Error_x10_y70','Error_x15_y70','Error_x22_y70']].values
hf105_70p = hf105_70 + hferr
hf105_70m = hf105_70 - hferr

hf145_70 = y_70_data .loc[y_70_data ['Time']==145,['HFG_x5_y70','HFG_x10_y70','HFG_x15_y70','HFG_x22_y70']].values
hferr = y_70_data .loc[y_70_data['Time']==145,['Error_x5_y70','Error_x10_y70','Error_x15_y70','Error_x22_y70']].values
hf145_70p = hf145_70 + hferr
hf145_70m = hf145_70 - hferr

hf185_70 = y_70_data .loc[y_70_data ['Time']==185,['HFG_x5_y70','HFG_x10_y70','HFG_x15_y70','HFG_x22_y70']].values
hferr = y_70_data .loc[y_70_data['Time']==185,['Error_x5_y70','Error_x10_y70','Error_x15_y70','Error_x22_y70']].values
hf185_70p = hf185_70 + hferr
hf185_70m = hf185_70 - hferr

hf35_90 = y_90_data .loc[y_90_data ['Time']==35,['HFG_x5_y90','HFG_x10_y90','HFG_x15_y90','HFG_x22_y90']].values
hferr = y_90_data .loc[y_90_data['Time']==35,['Error_x5_y90','Error_x10_y90','Error_x15_y90','Error_x22_y90']].values
hf35_90p = hf35_90 + hferr
hf35_90m = hf35_90 - hferr

hf105_90 = y_90_data .loc[y_90_data ['Time']==105,['HFG_x5_y90','HFG_x10_y90','HFG_x15_y90','HFG_x22_y90']].values
hferr = y_90_data .loc[y_90_data['Time']==105,['Error_x5_y90','Error_x10_y90','Error_x15_y90','Error_x22_y90']].values
hf105_90p = hf105_90 + hferr
hf105_90m = hf105_90 - hferr

hf145_90 = y_90_data .loc[y_90_data ['Time']==145,['HFG_x5_y90','HFG_x10_y90','HFG_x15_y90','HFG_x22_y90']].values
hferr = y_90_data .loc[y_90_data['Time']==145,['Error_x5_y90','Error_x10_y90','Error_x15_y90','Error_x22_y90']].values
hf145_90p = hf145_90 + hferr
hf145_90m = hf145_90 - hferr

hf185_90 = y_90_data .loc[y_90_data ['Time']==185,['HFG_x5_y90','HFG_x10_y90','HFG_x15_y90','HFG_x22_y90']].values
hferr = y_90_data .loc[y_90_data['Time']==185,['Error_x5_y90','Error_x10_y90','Error_x15_y90','Error_x22_y90']].values
hf185_90p = hf185_90 + hferr
hf185_90m = hf185_90 - hferr

hf35_110 = y_110_data .loc[y_110_data ['Time']==35,['HFG_x5_y110','HFG_x10_y110','HFG_x15_y110','HFG_x22_y110']].values
hferr = y_110_data .loc[y_110_data['Time']==35,['Error_x5_y110','Error_x10_y110','Error_x15_y110','Error_x22_y110']].values
hf35_110p = hf35_110 + hferr
hf35_110m = hf35_110 - hferr

hf105_110 = y_110_data .loc[y_110_data ['Time']==105,['HFG_x5_y110','HFG_x10_y110','HFG_x15_y110','HFG_x22_y110']].values
hferr = y_110_data .loc[y_110_data['Time']==105,['Error_x5_y110','Error_x10_y110','Error_x15_y110','Error_x22_y110']].values
hf105_110p = hf105_110 + hferr
hf105_110m = hf105_110 - hferr

hf145_110 = y_110_data .loc[y_110_data ['Time']==145,['HFG_x5_y110','HFG_x10_y110','HFG_x15_y110','HFG_x22_y110']].values
hferr = y_110_data .loc[y_110_data['Time']==145,['Error_x5_y110','Error_x10_y110','Error_x15_y110','Error_x22_y110']].values
hf145_110p = hf145_110 + hferr
hf145_110m = hf145_110 - hferr

hf185_110 = y_110_data .loc[y_110_data ['Time']==185,['HFG_x5_y110','HFG_x10_y110','HFG_x15_y110','HFG_x22_y110']].values
hferr = y_110_data .loc[y_110_data['Time']==185,['Error_x5_y110','Error_x10_y110','Error_x15_y110','Error_x22_y110']].values
hf185_110p = hf185_110 + hferr
hf185_110m = hf185_110 - hferr

hf35_130 = y_130_data .loc[y_130_data ['Time']==35,['HFG_x5_y130','HFG_x10_y130','HFG_x15_y130','HFG_x22_y130']].values
hferr = y_130_data .loc[y_130_data['Time']==35,['Error_x5_y130','Error_x10_y130','Error_x15_y130','Error_x22_y130']].values
hf35_130p = hf35_130 + hferr
hf35_130m = hf35_130 - hferr

hf105_130 = y_130_data .loc[y_130_data ['Time']==105,['HFG_x5_y130','HFG_x10_y130','HFG_x15_y130','HFG_x22_y130']].values
hferr = y_130_data .loc[y_130_data['Time']==105,['Error_x5_y130','Error_x10_y130','Error_x15_y130','Error_x22_y130']].values
hf105_130p = hf105_130 + hferr
hf105_130m = hf105_130 - hferr

hf145_130 = y_130_data .loc[y_130_data ['Time']==145,['HFG_x5_y130','HFG_x10_y130','HFG_x15_y130','HFG_x22_y130']].values
hferr = y_130_data .loc[y_130_data['Time']==145,['Error_x5_y130','Error_x10_y130','Error_x15_y130','Error_x22_y130']].values
hf145_130p = hf145_130 + hferr
hf145_130m = hf145_130 - hferr

hf185_130 = y_130_data .loc[y_130_data ['Time']==185,['HFG_x5_y130','HFG_x10_y130','HFG_x15_y130','HFG_x22_y130']].values
hferr = y_130_data .loc[y_130_data['Time']==185,['Error_x5_y130','Error_x10_y130','Error_x15_y130','Error_x22_y130']].values
hf185_130p = hf185_130 + hferr
hf185_130m = hf185_130 - hferr

x5_35 = np.array([hf35_10[0][0],hf35_30[0][0],hf35_50[0][0],hf35_70[0][0],hf35_90[0][0],hf35_110[0][0],hf35_130[0][0]])
x5_35p = np.array([hf35_10p[0][0],hf35_30p[0][0],hf35_50p[0][0],hf35_70p[0][0],hf35_90p[0][0],hf35_110p[0][0],hf35_130p[0][0]])
x5_35m = np.array([hf35_10m[0][0],hf35_30m[0][0],hf35_50m[0][0],hf35_70m[0][0],hf35_90m[0][0],hf35_110m[0][0],hf35_130m[0][0]])

x10_35 = np.array([hf35_10[0][1],hf35_30[0][1],hf35_50[0][1],hf35_70[0][1],hf35_90[0][1],hf35_110[0][1],hf35_130[0][1]])
x10_35p = np.array([hf35_10p[0][1],hf35_30p[0][1],hf35_50p[0][1],hf35_70p[0][1],hf35_90p[0][1],hf35_110p[0][1],hf35_130p[0][1]])
x10_35m = np.array([hf35_10m[0][1],hf35_30m[0][1],hf35_50m[0][1],hf35_70m[0][1],hf35_90m[0][1],hf35_110m[0][1],hf35_130m[0][1]])

x15_35 = np.array([hf35_10[0][2],hf35_30[0][2],hf35_50[0][2],hf35_70[0][2],hf35_90[0][2],hf35_110[0][2],hf35_130[0][2]])
x15_35p = np.array([hf35_10p[0][2],hf35_30p[0][2],hf35_50p[0][2],hf35_70p[0][2],hf35_90p[0][2],hf35_110p[0][2],hf35_130p[0][2]])
x15_35m = np.array([hf35_10m[0][2],hf35_30m[0][2],hf35_50m[0][2],hf35_70m[0][2],hf35_90m[0][2],hf35_110m[0][2],hf35_130m[0][2]])

x22_35 = np.array([hf35_10[0][3],hf35_30[0][3],hf35_50[0][3],hf35_70[0][3],hf35_90[0][3],hf35_110[0][3],hf35_130[0][3]])
x22_35p = np.array([hf35_10p[0][3],hf35_30p[0][3],hf35_50p[0][3],hf35_70p[0][3],hf35_90p[0][3],hf35_110p[0][3],hf35_130p[0][3]])
x22_35m = np.array([hf35_10m[0][3],hf35_30m[0][3],hf35_50m[0][3],hf35_70m[0][3],hf35_90m[0][3],hf35_110m[0][3],hf35_130m[0][3]])

x5_105 = np.array([hf105_10[0][0],hf105_30[0][0],hf105_50[0][0],hf105_70[0][0],hf105_90[0][0],hf105_110[0][0],hf105_130[0][0]])
x5_105p = np.array([hf105_10p[0][0],hf105_30p[0][0],hf105_50p[0][0],hf105_70p[0][0],hf105_90p[0][0],hf105_110p[0][0],hf105_130p[0][0]])
x5_105m = np.array([hf105_10m[0][0],hf105_30m[0][0],hf105_50m[0][0],hf105_70m[0][0],hf105_90m[0][0],hf105_110m[0][0],hf105_130m[0][0]])

x10_105 = np.array([hf105_10[0][1],hf105_30[0][1],hf105_50[0][1],hf105_70[0][1],hf105_90[0][1],hf105_110[0][1],hf105_130[0][1]])
x10_105p = np.array([hf105_10p[0][1],hf105_30p[0][1],hf105_50p[0][1],hf105_70p[0][1],hf105_90p[0][1],hf105_110p[0][1],hf105_130p[0][1]])
x10_105m = np.array([hf105_10m[0][1],hf105_30m[0][1],hf105_50m[0][1],hf105_70m[0][1],hf105_90m[0][1],hf105_110m[0][1],hf105_130m[0][1]])

x15_105 = np.array([hf105_10[0][2],hf105_30[0][2],hf105_50[0][2],hf105_70[0][2],hf105_90[0][2],hf105_110[0][2],hf105_130[0][2]])
x15_105p = np.array([hf105_10p[0][2],hf105_30p[0][2],hf105_50p[0][2],hf105_70p[0][2],hf105_90p[0][2],hf105_110p[0][2],hf105_130p[0][2]])
x15_105m = np.array([hf105_10m[0][2],hf105_30m[0][2],hf105_50m[0][2],hf105_70m[0][2],hf105_90m[0][2],hf105_110m[0][2],hf105_130m[0][2]])

x22_105 = np.array([hf105_10[0][3],hf105_30[0][3],hf105_50[0][3],hf105_70[0][3],hf105_90[0][3],hf105_110[0][3],hf105_130[0][3]])
x22_105p = np.array([hf105_10p[0][3],hf105_30p[0][3],hf105_50p[0][3],hf105_70p[0][3],hf105_90p[0][3],hf105_110p[0][3],hf105_130p[0][3]])
x22_105m = np.array([hf105_10m[0][3],hf105_30m[0][3],hf105_50m[0][3],hf105_70m[0][3],hf105_90m[0][3],hf105_110m[0][3],hf105_130m[0][3]])

x5_145 = np.array([hf145_10[0][0],hf145_30[0][0],hf145_50[0][0],hf145_70[0][0],hf145_90[0][0],hf145_110[0][0],hf145_130[0][0]])
x5_145p = np.array([hf145_10p[0][0],hf145_30p[0][0],hf145_50p[0][0],hf145_70p[0][0],hf145_90p[0][0],hf145_110p[0][0],hf145_130p[0][0]])
x5_145m = np.array([hf145_10m[0][0],hf145_30m[0][0],hf145_50m[0][0],hf145_70m[0][0],hf145_90m[0][0],hf145_110m[0][0],hf145_130m[0][0]])

x10_145 = np.array([hf145_10[0][1],hf145_30[0][1],hf145_50[0][1],hf145_70[0][1],hf145_90[0][1],hf145_110[0][1],hf145_130[0][1]])
x10_145p = np.array([hf145_10p[0][1],hf145_30p[0][1],hf145_50p[0][1],hf145_70p[0][1],hf145_90p[0][1],hf145_110p[0][1],hf145_130p[0][1]])
x10_145m = np.array([hf145_10m[0][1],hf145_30m[0][1],hf145_50m[0][1],hf145_70m[0][1],hf145_90m[0][1],hf145_110m[0][1],hf145_130m[0][1]])

x15_145 = np.array([hf145_10[0][2],hf145_30[0][2],hf145_50[0][2],hf145_70[0][2],hf145_90[0][2],hf145_110[0][2],hf145_130[0][2]])
x15_145p = np.array([hf145_10p[0][2],hf145_30p[0][2],hf145_50p[0][2],hf145_70p[0][2],hf145_90p[0][2],hf145_110p[0][2],hf145_130p[0][2]])
x15_145m = np.array([hf145_10m[0][2],hf145_30m[0][2],hf145_50m[0][2],hf145_70m[0][2],hf145_90m[0][2],hf145_110m[0][2],hf145_130m[0][2]])

x22_145 = np.array([hf145_10[0][3],hf145_30[0][3],hf145_50[0][3],hf145_70[0][3],hf145_90[0][3],hf145_110[0][3],hf145_130[0][3]])
x22_145p = np.array([hf145_10p[0][3],hf145_30p[0][3],hf145_50p[0][3],hf145_70p[0][3],hf145_90p[0][3],hf145_110p[0][3],hf145_130p[0][3]])
x22_145m = np.array([hf145_10m[0][3],hf145_30m[0][3],hf145_50m[0][3],hf145_70m[0][3],hf145_90m[0][3],hf145_110m[0][3],hf145_130m[0][3]])

x5_185 = np.array([hf185_10[0][0],hf185_30[0][0],hf185_50[0][0],hf185_70[0][0],hf185_90[0][0],hf185_110[0][0],hf185_130[0][0]])
x5_185p = np.array([hf185_10p[0][0],hf185_30p[0][0],hf185_50p[0][0],hf185_70p[0][0],hf185_90p[0][0],hf185_110p[0][0],hf185_130p[0][0]])
x5_185m = np.array([hf185_10m[0][0],hf185_30m[0][0],hf185_50m[0][0],hf185_70m[0][0],hf185_90m[0][0],hf185_110m[0][0],hf185_130m[0][0]])

x10_185 = np.array([hf185_10[0][1],hf185_30[0][1],hf185_50[0][1],hf185_70[0][1],hf185_90[0][1],hf185_110[0][1],hf185_130[0][1]])
x10_185p = np.array([hf185_10p[0][1],hf185_30p[0][1],hf185_50p[0][1],hf185_70p[0][1],hf185_90p[0][1],hf185_110p[0][1],hf185_130p[0][1]])
x10_185m = np.array([hf185_10m[0][1],hf185_30m[0][1],hf185_50m[0][1],hf185_70m[0][1],hf185_90m[0][1],hf185_110m[0][1],hf185_130m[0][1]])

x15_185 = np.array([hf185_10[0][2],hf185_30[0][2],hf185_50[0][2],hf185_70[0][2],hf185_90[0][2],hf185_110[0][2],hf185_130[0][2]])
x15_185p = np.array([hf185_10p[0][2],hf185_30p[0][2],hf185_50p[0][2],hf185_70p[0][2],hf185_90p[0][2],hf185_110p[0][2],hf185_130p[0][2]])
x15_185m = np.array([hf185_10m[0][2],hf185_30m[0][2],hf185_50m[0][2],hf185_70m[0][2],hf185_90m[0][2],hf185_110m[0][2],hf185_130m[0][2]])

x22_185 = np.array([hf185_10[0][3],hf185_30[0][3],hf185_50[0][3],hf185_70[0][3],hf185_90[0][3],hf185_110[0][3],hf185_130[0][3]])
x22_185p = np.array([hf185_10p[0][3],hf185_30p[0][3],hf185_50p[0][3],hf185_70p[0][3],hf185_90p[0][3],hf185_110p[0][3],hf185_130p[0][3]])
x22_185m = np.array([hf185_10m[0][3],hf185_30m[0][3],hf185_50m[0][3],hf185_70m[0][3],hf185_90m[0][3],hf185_110m[0][3],hf185_130m[0][3]])

ghf_wall = pd.concat([pd.Series(hfz,name='z'),
                      pd.Series(x5_35,name='x5_35'),pd.Series(x5_35p,name='x5_35p'),pd.Series(x5_35m,name='x5_35m'),
                      pd.Series(x10_35,name='x10_35'),pd.Series(x10_35p,name='x10_35p'),pd.Series(x10_35m,name='x10_35m'),
                      pd.Series(x15_35,name='x15_35'),pd.Series(x15_35p,name='x15_35p'),pd.Series(x15_35m,name='x15_35m'),
                      pd.Series(x22_35,name='x22_35'),pd.Series(x22_35p,name='x22_35p'),pd.Series(x22_35m,name='x22_35m'),
                      pd.Series(x5_105,name='x5_105'),pd.Series(x5_105p,name='x5_105p'),pd.Series(x5_105m,name='x5_105m'),
                      pd.Series(x10_105,name='x10_105'),pd.Series(x10_105p,name='x10_105p'),pd.Series(x10_105m,name='x10_105m'),
                      pd.Series(x15_105,name='x15_105'),pd.Series(x15_105p,name='x15_105p'),pd.Series(x15_105m,name='x15_105m'),
                      pd.Series(x22_105,name='x22_105'),pd.Series(x22_105p,name='x22_105p'),pd.Series(x22_105m,name='x22_105m'),
                      pd.Series(x5_145,name='x5_145'),pd.Series(x5_145p,name='x5_145p'),pd.Series(x5_145m,name='x5_145m'),
                      pd.Series(x10_145,name='x10_145'),pd.Series(x10_145p,name='x10_145p'),pd.Series(x10_145m,name='x10_145m'),
                      pd.Series(x15_145,name='x15_145'),pd.Series(x15_145p,name='x15_145p'),pd.Series(x15_145m,name='x15_145m'),
                      pd.Series(x22_145,name='x22_145'),pd.Series(x22_145p,name='x22_145p'),pd.Series(x22_145m,name='x22_145m'),
                      pd.Series(x5_185,name='x5_185'),pd.Series(x5_185p,name='x5_185p'),pd.Series(x5_185m,name='x5_185m'),
                      pd.Series(x10_185,name='x10_185'),pd.Series(x10_185p,name='x10_185p'),pd.Series(x10_185m,name='x10_185m'),
                      pd.Series(x15_185,name='x15_185'),pd.Series(x15_185p,name='x15_185p'),pd.Series(x15_185m,name='x15_185m'),
                      pd.Series(x22_185,name='x22_185'),pd.Series(x22_185p,name='x22_185p'),pd.Series(x22_185m,name='x22_185m')],axis=1)

new_ghf_file = os.path.join(EXP_Dir, f"GHF_processed.csv")
ghf_wall.to_csv(new_ghf_file,index=False)