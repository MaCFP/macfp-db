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
sys.path.append('../../../../../../macfp-db/Utilities/')
sys.path.append('../../../../../../../macfp-db/Utilities/')
sys.path.append('../../../../../../../../macfp-db/Utilities/')

#--------------------------------------------------------------------------------
import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------
plotFile = "01_very_coarse_v0a_v0b_v0f_UoWu_FM_Burner_dataplot_config.csv"
plotFile = "02_coarse_RadImpact_UoWu_FM_Burner_dataplot_config.csv"

macfp.dataplot(config_filename = plotFile,
               institute='UWuppertal',
               expdir='../../../../../Experimental_Data/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
