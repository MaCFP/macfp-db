import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path1 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting\Experimental_Data\Total_HF_binned_y_50cm.csv'
path2 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_UMD_devc_1cm.csv'

# Experimental data  

data_start_row = 1  # Data start row index (0-based)
exp_data1_full = pd.read_csv(path1, header=0)
exp_data1 = exp_data1_full.iloc[data_start_row:, :]

x_string_exp1 = exp_data1['Time']  # Replace 'X_Column' with the appropriate column name
y_string_exp1 = exp_data1['HFG_x10_y50']

# Read the simulation data

data_start_row = 1  # Data start row index (0-based)
exp_data2_full = pd.read_csv(path2, header=1)
exp_data2 = exp_data2_full.iloc[data_start_row:, :]

x_string_exp2 = exp_data2['Time']  # Replace 'X_Column' with the appropriate column name
y_string_exp2 = exp_data2['HFG_x10_y50']

# Convert string data to float
x_exp1 = [float(x) for x in x_string_exp1]
y_exp1 = [float(x) for x in y_string_exp1]
x_exp2 = [float(x) for x in x_string_exp2]
y_exp2 = [float(x) for x in y_string_exp2]


# Plot area
fig = plt.figure(dpi=1600, figsize=(10, 6))

plt.plot(x_exp1, y_exp1, c='black', alpha=0.9, label='Experiment', marker='o')
# plt.errorbar(x_exp1_error, y_exp1_error, yerr=y_exp1_corrected, fmt='o', color='black', capsize=5, label='HRR_Error')

plt.plot(x_exp2, y_exp2, c='blue', alpha=0.9, label='Simulation_UMD_Props_1_cm')


plt.title('Gaugage Heat Flux at x10 y50',fontsize=14)  
plt.xlabel('Time [s]',fontsize=16)
plt.ylabel('Gaugage Heat Flux [kW]',fontsize=16)  
plt.axis([0, 200, 0, 80])


plt.grid(True)

plt.legend(ncol=2, loc='best', labels=['Experiment', 'Sim_UMD_Props_1_cm'])


# Specify the complete file path including the desired folder
save_folder = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting'
save_filename = 'Gaugage_Heat_Flux_x10_y50.pdf'
save_path = os.path.join(save_folder, save_filename)

plt.savefig(save_path, dpi=1600)

plt.show()