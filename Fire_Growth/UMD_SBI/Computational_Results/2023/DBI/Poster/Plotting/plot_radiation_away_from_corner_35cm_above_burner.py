import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path1 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting\Experimental_Data\Rad_flux_away_from_the_flame_binned.csv'
path2 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_UMD_devc_1cm.csv'


exp_data1 = pd.read_csv(path1, encoding='latin-1')



# Read the CSV file into a pandas DataFrame

header_row = 1  # Header row index (0-based)
data_start_row = 3  # Data start row index (0-based)
exp_data2 = pd.read_csv(path2, header=header_row, skiprows=range(2, data_start_row))

# Choose the column to plot
column_to_plot = 'RHF_z30'  # Replace with the actual column name

# Access the data in the chosen column
x_string_exp2 = exp_data2['Time']  # Replace 'X_Column' with the appropriate column name
y_string_exp2 = exp_data2[column_to_plot]


# Experimental data    
x_string_exp1 = exp_data1.iloc[2:, 0]  #
x_exp1 = [float(x) for x in x_string_exp1]  # Convert a list of strings to a list of floating-point numbers

y_string_exp1 = exp_data1.iloc[2:, 2]  # HRRin test 5
y_exp1 = [float(x) for x in y_string_exp1]  # Convert a list of strings to a list of floating-point numbers

y_string_exp1_error = exp_data1.iloc[2:, 8]  # HRR error
y_exp1_error_value = [float(x) for x in y_string_exp1_error]  # Convert a list of strings to a list of floating-point numbers

x_exp1_error = x_exp1[::1]
y_exp1_error = y_exp1[::1]
y_exp1_corrected = y_exp1_error_value[::1]


# Simulation  UMD Props 1 cm

x_exp2 = [float(x) for x in x_string_exp2]  # Convert a list of strings to a list of floating-point numbers


y_exp2 = [float(x) for x in y_string_exp2]  # Convert a list of strings to a list of floating-point numbers


# Plot area
fig = plt.figure(dpi=1600, figsize=(10, 6))

plt.plot(x_exp1, y_exp1, c='black', alpha=0.9, label='Experiment')
plt.errorbar(x_exp1_error, y_exp1_error, yerr=y_exp1_corrected, fmt='o', color='black', capsize=5, label='HRR_Error')
plt.plot(x_exp2, y_exp2, c='blue', alpha=0.9, label='Simulation_UMD_Props_1_cm')


plt.title('Radiative Heat Flux at 35 cm above burner',fontsize=14)  
plt.xlabel('Time [s]',fontsize=16)
plt.ylabel('Radiative Heat Flux [kW]',fontsize=16)  
plt.axis([0, 200, 0, 10])


plt.grid(True)

plt.legend(ncol=2, loc='best', labels=['Experiment', 'Sim_UMD_Props_1_cm'])


# Specify the complete file path including the desired folder
save_folder = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting'
save_filename = 'Radiative Heat Flux away from corner 35 cm above burner.pdf'
save_path = os.path.join(save_folder, save_filename)

plt.savefig(save_path, dpi=1200)

plt.show()