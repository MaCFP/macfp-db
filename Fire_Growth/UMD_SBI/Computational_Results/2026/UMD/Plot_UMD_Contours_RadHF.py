### By: Dushyant chaudhari
### Updated: May 22, 2026
### Plots: 
###		1. UMD contours of flame heat fluxes
###		2. Radiation at a distance as a function of HRR


# Plotting contours
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import re
import scipy.stats as stats
import os

#### Exp data contour
expdir = '../../../Experimental_Data/'
outdir = './Outputs/'
pltdir = './Plots/'

if not os.path.exists(pltdir):
	os.mkdir(pltdir)

xvals = [0.05,0.10,0.15,0.22]
yvals = [10, 30, 50, 70, 90, 110, 130]

expdata = pd.read_csv(expdir + 'GHF_processed.csv')

zvals_e = expdata['z']

e35 = expdata[['x5_35','x10_35','x15_35','x22_35']]
e105 = expdata[['x5_105','x10_105','x15_105','x22_105']]
e145 = expdata[['x5_145','x10_145','x15_145','x22_145']]
e185 = expdata[['x5_105','x10_185','x15_185','x22_185']]

all_es = [e35, e105, e145, e185] # 35, 105, 145, 185

Xe, Ze = np.meshgrid(xvals, zvals_e)

def bin_it(time,data,bin_range):
    bin_means, bin_edges, binnumber = stats.binned_statistic(time,data,
        bins=bin_range,statistic='mean',range=(0,190))
    bin_width = (bin_edges[1] - bin_edges[0])
    bin_centers = bin_edges[1:] - bin_width/2
    
    bin_centers=np.append(0,bin_centers)
    bin_means =np.append(0,bin_means)

    return bin_centers, bin_means

def get_m_idx(file):
	mesh_size = int(re.findall(r'\d+', file)[0])
	if mesh_size == 5:
		mesh_size = 0.5 # cm
	m_ind = m_list.index(mesh_size)

	return mesh_size, m_ind

def format_plot(fig, ax, xlab:str, ylab:str, xlim:list, ylim:list):
	ax.set_xlabel(xlab, fontsize=14)
	ax.set_ylabel(ylab, fontsize=14)
	ax.set_xlim(xlim)
	ax.set_ylim(ylim)
	ax.tick_params('x', labelsize=12)
	ax.tick_params('y', labelsize=12)
	ax.grid()
	ax.legend(fontsize=14)
	fig.tight_layout()


pltdir = 'Plots/'
save_plots = True
brange = np.arange(0, 200, 10)
ts = [35, 105, 145, 185]

for nt , t in enumerate(ts):

	fig, axes = plt.subplots(1, 5, figsize=(5.5, 4.5))
	fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)

	custom_levels = np.linspace(0, 80, 9)
	fig.suptitle(f'{t} s', fontsize=14)
	m_list = [0.5, 1, 2, 4]
	contours = []
	print(f'Plotting HF contours for t = {t}s')
	
	for file in glob.glob('Output/*'):
		if '_devc' not in file or 'full_case' not in file:
			continue
		
		mesh_size, m_ind = get_m_idx(file)
		df = pd.read_csv(file, skiprows=1)

		cols = df.columns.values
		HF_array = []

		for i in yvals:
			subarr = []
			for n in range(4):
				bc, bm = bin_it(df.Time, df[f'HF {i}-{n+1}'],brange)
				t_idx = np.where(np.abs(bc - t)<2)[0][0]
				subarr.append(bm[t_idx])

			HF_array.append(subarr)

		HF_array = np.array(HF_array)

		##################
		### Plot contours
		##################
		evals = all_es[nt]
		cs = axes[0].contourf(Xe, Ze, evals, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
		contours.append(cs)
		axes[0].set_aspect('equal')
		axes[0].set_ylabel('Height (m)')
		axes[0].set_title('Exp', fontsize=10)
		axes[0].set_xlabel('Distance (m)')
		axes[0].set_ylim(0,1.4)

		cs = axes[m_ind+1].contourf(Xe, Ze, HF_array, levels=custom_levels, cmap='rainbow', vmin=0, vmax=80)
		contours.append(cs)
		axes[m_ind+1].set_aspect('equal')
		axes[m_ind+1].set_title(f'{mesh_size} cm', fontsize=10)
		axes[m_ind+1].set_ylim(0,1.4)

	# fig.tight_layout()
	cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical',
	                   fraction=0.05, pad=0.04)
	cbar.set_label('Heat Flux (kW/m²)')

	if save_plots:
		plt.savefig(pltdir + f't{t}_contours.pdf')

##############################
####### Radiation at a distance 
# as a function of HRR
Rad_HF_locs = [10,35,60,85,110, 135]
figs_hrr, axes_hrr =[],[]
for n in Rad_HF_locs:
	fig_hrr, axis_hrr = plt.subplots()
	figs_hrr.append(fig_hrr)
	axes_hrr.append(axis_hrr)

# Get exp rad HRR data
Rad_Exp_file = 'Rad_flux_away_from_the_flame_binned.csv'
exp_rad = pd.read_csv(expdir+Rad_Exp_file)
exp_rad_cols = exp_rad.columns
exp_rad = pd.read_csv(expdir+Rad_Exp_file, skiprows=1)
exp_rad.columns = exp_rad_cols

Exp_hrr_file = 'HRR_processed.csv'
exp_df = pd.read_csv(expdir+Exp_hrr_file)
bt_e, bhrr_e = bin_it(exp_df.Time, exp_df.HRR, brange)

for rl, rad_l in enumerate(Rad_HF_locs):
	bc_rad_e, bm_rad_e = bin_it(exp_rad.Time, exp_rad[f'HFG_y{rad_l}'], brange)
	_, bm_rad_e_e = bin_it(exp_rad.Time, exp_rad[f'Error_y{rad_l}'], brange)
	axes_hrr[rl].plot(bhrr_e, bm_rad_e, c='k',ls='-', label='Exp')
	axes_hrr[rl].plot(bhrr_e, bm_rad_e_e + bm_rad_e, c='k',ls='--')
	axes_hrr[rl].plot(bhrr_e, bm_rad_e - bm_rad_e_e, c='k',ls='--')

All_HRRs = []
hrr_files = {}
for file in glob.glob('Output/*'):
	if '_hrr' not in file:
		continue
	mesh_size, m_ind = get_m_idx(file)
	hrr_files[file]=mesh_size

hrr_files = dict(sorted(hrr_files.items(), key=lambda item: item[1]))

for file in hrr_files:
	mesh_size, m_ind = get_m_idx(file)
	hrr_df = pd.read_csv(file, skiprows=1)
	bc_hrr_s, bm_hrr_s = bin_it(hrr_df.Time, hrr_df.HRR, brange)


	##################
	### Plot Rad HRR
	##################
	for rl, rad_l in enumerate(Rad_HF_locs):
		print(f'Plotting HRR vs Rad at a distance for y = {rad_l} cm')
		devc_file = '_'.join(file.split('_hrr.csv'))+'devc.csv'
		df = pd.read_csv(devc_file, skiprows=1)
		
		bc_hf_s, bm_hf_s = bin_it(df.Time, df[f'HFG {rad_l}'],brange)
		axes_hrr[rl].plot(bm_hrr_s, bm_hf_s, label=f'{mesh_size} cm')

		axes_hrr[rl].legend()

		format_plot(figs_hrr[rl], axes_hrr[rl], 
					'HRR (kW)', r'Radiation Heat Flux (kW/m$^\mathrm{2}$)',
					[0,300],[0,10])

for rl, rad_l in enumerate(Rad_HF_locs):
	if save_plots:
		figs_hrr[rl].savefig(pltdir + f'Rad_HRR_v_HF_y{rad_l}.pdf', bbox_inches='tight')

plt.close('all')
