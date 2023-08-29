import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path1 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting\Experimental_Data\HRR_1Hz_7TestAverage.csv'
path2 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_UMD_hrr_1cm.csv'
path3 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_UMD_hrr_2_5cm.csv'
path4 = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\DBI_DBI_hrr_2_5cm.csv'

exp_data1 = pd.read_csv(path1, encoding='latin-1')
exp_data2 = pd.read_csv(path2, encoding='latin-1')
exp_data3 = pd.read_csv(path3, encoding='latin-1')
exp_data4 = pd.read_csv(path4, encoding='latin-1')

# Experimental data    
x_string_exp1 = exp_data1.iloc[2:, 0]  #
x_exp1 = [float(x) for x in x_string_exp1]  # Convert a list of strings to a list of floating-point numbers

y_string_exp1 = exp_data1.iloc[2:, 1]  # HRRin test 5
y_exp1 = [float(x) for x in y_string_exp1]  # Convert a list of strings to a list of floating-point numbers

y_string_exp1_error = exp_data1.iloc[2:, 2]  # HRR error
y_exp1_error_value = [float(x) for x in y_string_exp1_error]  # Convert a list of strings to a list of floating-point numbers

x_exp1_error = x_exp1[::10]
y_exp1_error = y_exp1[::10]
y_exp1_corrected = y_exp1_error_value[::10]


# Simulation  UMD Props 1 cm
x_string_exp2 = exp_data2.iloc[2:, 0]  # time in test 28
x_exp2 = [float(x) for x in x_string_exp2]  # Convert a list of strings to a list of floating-point numbers
   
y_string_exp2 = exp_data2.iloc[2:, 1]  # HRR in v2_20030820
y_exp2 = [float(x) for x in y_string_exp2]  # Convert a list of strings to a list of floating-point numbers

# Simulation  UMD Props 2.5 cm  
x_string_exp3 = exp_data3.iloc[2:, 0]  # time in test 28
x_exp3 = [float(x) for x in x_string_exp3]  # Convert a list of strings to a list of floating-point numbers
   
y_string_exp3 = exp_data3.iloc[2:, 1]  # HRR in v2_20030820
y_exp3 = [float(x) for x in y_string_exp3]  # Convert a list of strings to a list of floating-point numbers

# Simulation  DBI Props 2.5 cm 
x_string_exp4 = exp_data4.iloc[2:, 0]  # time in test 28
x_exp4 = [float(x) for x in x_string_exp4]  # Convert a list of strings to a list of floating-point numbers
   
y_string_exp4 = exp_data4.iloc[2:, 1]  # HRR in v2_20030820
y_exp4 = [float(x) for x in y_string_exp4]  # Convert a list of strings to a list of floating-point numbers


# Calculate the moving average of y_exp2 (HRR_Simulation_UMD_Props_1_cm)
window_size = 2  # Adjust the window size as needed
y_exp2_moving_avg = np.convolve(y_exp2, np.ones(window_size)/window_size, mode='same')
y_exp3_moving_avg = np.convolve(y_exp3, np.ones(window_size)/window_size, mode='same')
y_exp4_moving_avg = np.convolve(y_exp4, np.ones(window_size)/window_size, mode='same')


# Plot area
fig = plt.figure(dpi=1600, figsize=(10, 6))

plt.plot(x_exp1, y_exp1, c='black', alpha=0.9, label='HRR_Experiment')
plt.errorbar(x_exp1_error, y_exp1_error, yerr=y_exp1_corrected, fmt='o', color='black', capsize=5, label='HRR_Error')
#plt.plot(x_exp2, y_exp2, c='blue', alpha=0.1, label='Simulation_UMD_Props_1_cm')
plt.plot(x_exp2, y_exp2_moving_avg, c='blue', alpha=1, linewidth=1, label='Simulation_UMD_Props_1_cm_Moving_Average')  # Adding moving average line



# Plot area
#fig=plt.figure(dpi=1000,figsize=(10,6))  

#plt.plot(x_exp1,y_exp1,c='black',alpha=0.9,label='HRR_Experiment') #实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明  

#plt.errorbar(x_exp1_error,y_exp1_error, yerr=y_exp1_corrected, fmt='o', color='blue', capsize=5, label='HRR_Error')

#plt.plot(x_exp2,y_exp2,c='blue',alpha=0.4,label='HRR_Simulation_UMD_Props_1_cm') #实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明  

#plt.plot(x_exp3,y_exp3,c='red',alpha=0.1,label='Simulation_UMD_Props_2_5_cm') #实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明  
plt.plot(x_exp3, y_exp3_moving_avg, c='red', alpha=1, linewidth=1, label='Simulation_UMD_Props_2_5_cm_Moving_Average')  # Adding moving average line





#plt.plot(x_exp4,y_exp4,c='purple',alpha=0.1,label='HRR_Simulation_DBI_Props_2_5_cm') #实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明  
plt.plot(x_exp4, y_exp4_moving_avg, c='purple', alpha=1, linewidth=1, label='Simulation_DBI_Props_2_5_cm_Moving_Average')  # Adding moving average line



plt.title('HRR camparison between experiment and simulations',fontsize=14)  
plt.xlabel('Time [s]',fontsize=16)
plt.ylabel('HRR [$kW$]',fontsize=16)  
plt.axis([0, 200, 0, 400])

plt.grid(True)

#plt.legend(ncol=2, loc='best', labels=['Experiment', 'Simulation_UMD_Props_1_cm', 'Simulation_UMD_Props_1_cm_Moving_Average', 'Simulation_UMD_Props_2.5_cm', 'Simulation_UMD_Props_2.5_cm_Moving_Average','Simulation_DBI_Props_2.5_cm','Simulation_DBI_Props_2.5_cm_Moving_Average'])
plt.legend(ncol=2, loc='best', labels=['Experiment', 'Sim_UMD_Props_1_cm_Moving_Average', 'Sim_UMD_Props_2.5_cm_Moving_Average','Sim_DBI_Props_2.5_cm_Moving_Average'])


# Specify the complete file path including the desired folder
save_folder = r'E:\macfp-db-master\macfp-db-master\Fire_Growth\UMD_SBI\Computational_Results\2023\DBI\plotting'
save_filename = 'HRR_comparison_experiment_simulations.pdf'
save_path = os.path.join(save_folder, save_filename)

plt.savefig(save_path, dpi=1200)

plt.show()