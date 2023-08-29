import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path1 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_UMD_line_1cm.csv'


data_start_row = 0  # Data start row index (0-based)
exp_data1_full = pd.read_csv(path1, header=1)
exp_data1 = exp_data1_full.iloc[data_start_row:, :]

# Read the simulation data 105 s

x_string_exp1 = exp_data1['NormalDistance']  # Replace 'X_Column' with the appropriate column name
y_string_exp1 = exp_data1['TEMPERATURE_RMS_x5_30']

# Read the simulation data 145 s

y_string_exp2 = exp_data1['TEMPERATURE_RMS_x5_90']


# Convert string data to float
x_exp1 = [float(x) for x in x_string_exp1]
y_exp1 = [float(x) for x in y_string_exp1]
y_exp2 = [float(x) for x in y_string_exp2]



# Plot area
fig = plt.figure(dpi=1600, figsize=(10, 6))

plt.plot(x_exp1, y_exp1, c='black', alpha=0.9, label='x5y30')
plt.plot(x_exp1, y_exp2, c='blue', alpha=0.9, label='x5y90')


plt.title('RMS Temperature x=5 t=105s',fontsize=14)  
plt.xlabel('Distance from the Panel (m)',fontsize=16)
plt.ylabel('RMS Temperature ($^\circ$C)',fontsize=16)  
plt.axis([0, 0.7, 0, 600])


plt.grid(True)

plt.legend(ncol=1, loc='best', labels=['y=30cm', 'y=90cm'])


# Specify the complete file path including the desired folder
save_folder = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting'
save_filename = 'RMS_Temprerature_x5_t105s.pdf'
save_path = os.path.join(save_folder, save_filename)

plt.savefig(save_path, dpi=1600)

plt.show()