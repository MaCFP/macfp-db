import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path1 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_UMD_line_1cm.csv'


data_start_row = 0  # Data start row index (0-based)
exp_data1_full = pd.read_csv(path1, header=1)
exp_data1 = exp_data1_full.iloc[data_start_row:, :]

# Read the simulation data 105 s

x_string_exp1 = exp_data1['NET_HEAT_FLUX_x22_145-z']  # Replace 'X_Column' with the appropriate column name
y_string_exp1 = exp_data1['NET_HEAT_FLUX_x22_105']

# Read the simulation data 145 s

y_string_exp2 = exp_data1['NET_HEAT_FLUX_x22_145']

# Read the simulation data 185 s

y_string_exp3 = exp_data1['NET_HEAT_FLUX_x22_185']



# Convert string data to float
x_exp1 = [float(x) for x in x_string_exp1]
x_exp1_modified = [x - 0.36 for x in x_exp1]



y_exp1 = [float(x) for x in y_string_exp1]
y_exp2 = [float(x) for x in y_string_exp2]
y_exp3 = [float(x) for x in y_string_exp3]


# Plot area
fig = plt.figure(dpi=1600, figsize=(10, 6))

plt.plot(x_exp1_modified, y_exp1, c='black', alpha=0.9, label='105s')
plt.plot(x_exp1_modified, y_exp2, c='blue', alpha=0.9, label='145s')
plt.plot(x_exp1_modified, y_exp3, c='red', alpha=0.9, label='185s')


plt.title('Net Heat Flux x22',fontsize=14)  
plt.xlabel('Distance above burner(m)',fontsize=16)
plt.ylabel('Net Heat Flux (kW/m$^2$)',fontsize=16)  
plt.axis([0, 1.6, 0, 60])


plt.grid(True)

plt.legend(ncol=1, loc='best', labels=['t=105s', 't=145s','t=185s'])


# Specify the complete file path including the desired folder
save_folder = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting'
save_filename = 'Net_Heat_Flux_x22.pdf'
save_path = os.path.join(save_folder, save_filename)

plt.savefig(save_path, dpi=1600)

plt.show()