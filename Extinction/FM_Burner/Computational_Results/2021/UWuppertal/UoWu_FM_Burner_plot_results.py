#!/usr/bin/env python3
# McDermott
# Feb 2021

# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository

#================================================================================
import glob
import sys
#--------------------------------------------------------------------------------
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
# sys.path.append('../../../../../../macfp-db/Utilities/')
macfp_db_root="/Users/fbraenns/09_TOOLs_Application/MaCFP/macfp-db/"
sys.path.append(macfp_db_root+'Utilities/')

#--------------------------------------------------------------------------------
import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

#================================================================================
expdirA="/Users/fbraenns/09_TOOLs_Application/MaCFP/macfp-db/Extinction/FM_Burner/Experimental_Data/"
expdirA= macfp_db_root + "Extinction/FM_Burner/Experimental_Data/"

#================================================================================
# Plot standard averaging
plotFile = glob.glob("*UoWu_FM_Burner_dataplot*")[0]
#................................................................................
# Plot weighted averaging
# plotFile = glob.glob("*UoWu_FM_Burner_Weighted_dataplot*")[0]

#--------------------------------------------------------------------------------
macfp.dataplot(config_filename = plotFile,
               institute='UoWu',
               expdir=expdirA,
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
#================================================================================
# plt.show()

