
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from fdsplotlib import configure_fds_fonts

configure_fds_fonts(usetex=True)

expdir = '../../../Experimental_Data/'
outdir = './'
pltdir = './Plots/'

# Read the CSV file, skipping the first two header rows
df = pd.read_csv(outdir + 'JIS_facade_2cm_line.csv', skiprows=2, header=None)

# Remove rows with all NaN values and handle NaN values
df = df.dropna(how='all')

# Set vector z to column 5 (assuming 1-indexed, so column index 4)
z = df.iloc[:,10].dropna().values

# Create vector x to be the distances from the wall
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

X, Z = np.meshgrid(x, z)

custom_levels = np.linspace(48.0, 1175.0, 9)

# Make 3 sets of plots for 600, 750, 900 kW
for j in range(3):

    # Temperatures at the center, center-right and right
    T1 = df.iloc[:,11+27*j:20+27*j].dropna().values
    T2 = df.iloc[:,20+27*j:29+27*j].dropna().values
    T3 = df.iloc[:,29+27*j:38+27*j].dropna().values
    
    # Create figure with three subplots
    fig, axes = plt.subplots(1, 3, figsize=(4.5, 4.5))
    fig.suptitle(f'{600+j*150} kW', fontsize=14)
    fig.subplots_adjust(left=0.02, right=0.85, wspace=-0.30)
    
    # Plot contour maps
    contours = []
    for i, (ax, T) in enumerate(zip(axes, [T1, T2, T3])):
        cs = ax.contourf(X, Z, T, levels=custom_levels, cmap='rainbow', vmin=50, vmax=1100)
        contours.append(cs)
        
        # Set equal aspect ratio for same scaling
        ax.set_aspect('equal')
        
        # Only add labels to left and bottom
        if i == 0:  # leftmost plot gets y-axis labels
            ax.set_ylabel('Height (m)')
            ax.set_title('Middle', fontsize=10)
            ax.set_xlabel('Distance (m)')
            ax.xaxis.set_major_locator(MultipleLocator(0.4))
        elif i == 1:
            ax.set_title('Middle-Right', fontsize=10)
            ax.set_xticks([])
            ax.set_yticks([])
        else:
            ax.set_title('Right', fontsize=10)
            ax.set_xticks([])
            ax.set_yticks([])
        
    # Adjust layout and add colorbar to the right
    #plt.tight_layout(pad=0.0, w_pad=0.0, h_pad=0.0)
    cbar = plt.colorbar(contours[0], ax=axes, orientation='vertical', 
                       fraction=0.05, pad=0.04)
    cbar.set_label('Temperature (°C)')
    
    plt.savefig(pltdir + 'JIS_facade_contours_' + str(600+j*150) + '.pdf')

