#!/usr/bin/env python3
# McDermott
# Feb 2021

# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository

#================================================================================
# import glob
import sys
#--------------------------------------------------------------------------------
sys.path.append('../../../../../../macfp-db/Utilities/')

#--------------------------------------------------------------------------------
import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------
plotFile_01 = "01_very_coarse_v0a_v0b_v0f_UoWu_FM_Burner_dataplot_config.csv"
plotFile_02 = "02_coarse_RadImpact_UoWu_FM_Burner_dataplot_config.csv"
plotFile_03 = "03_allMesh_v0f_v2f_v3f_UoWu_FM_Burner_dataplot_config.csv"
plotFile_04 = "04_averaging_15s_vs_40s_v2e_v3i_UoWu_FM_Burner_dataplot_config.csv"
plotFile_all = "UoW_FM_Burner_dataplot_config.csv"

macfp.dataplot(config_filename = plotFile_01,
               institute='UWuppertal',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots_01/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
macfp.dataplot(config_filename = plotFile_02,
               institute='UWuppertal',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots_02/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
macfp.dataplot(config_filename = plotFile_03,
               institute='UWuppertal',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots_03/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

macfp.dataplot(config_filename = plotFile_04,
               institute='UWuppertal',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots_04/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
macfp.dataplot(config_filename = plotFile_all,
               institute='UWuppertal',
               expdir='../../../Experimental_Data/',
               pltdir='./Plots_all/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
