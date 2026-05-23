import pandas as pd
import matplotlib.pyplot as plt
import os

exp_data = '../../../Experimental_Data/HRR_processed.csv'

hrr_exp = pd.read_csv(exp_data)

fig, ax = plt.subplots()

def format_plot(ax, xlab, ylab):
	ax.legend(fontsize=14)
	ax.tick_params('x', labelsize=12)
	ax.tick_params('y', labelsize=12)
	ax.set_xlabel(xlab, fontsize=14)
	ax.set_ylabel(ylab, fontsize=14)

# print(hrr_exp)
hrr_err = [hrr_exp.HRR-hrr_exp.HRRminus, hrr_exp.HRRplus-hrr_exp.HRR]
ax.errorbar(hrr_exp.Time, hrr_exp.HRR, yerr=hrr_err, errorevery=10, ls='', marker='*', c='k', capsize=5)

umd_hrr_file = 'Output/UMD_HRR_full_case_p5_1_2_4cm.csv'
umd_hrr = pd.read_csv(umd_hrr_file, skiprows=1, header=0)
print(umd_hrr)

ax.plot(umd_hrr.t, umd_hrr['HRR_4cm'], label='4 cm')
ax.plot(umd_hrr.t, umd_hrr['HRR_2cm'], label='2 cm')
ax.plot(umd_hrr.t, umd_hrr['HRR_1cm'], label='1 cm')
ax.plot(umd_hrr.t, umd_hrr['HRR_0.5cm'], label='0.5 cm')
format_plot(ax, 'Time (s)', 'HRR (kW)')
pltdir = 'Plots/'

if not os.path.exists(pltdir):
	os.mkdir(pltdir)

fig.savefig(pltdir+'HRR.pdf', bbox_inches='tight')

plt.close('all')