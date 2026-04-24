#!$MACFP/macfp-db/.github/macfp_python_env/bin/python

import subprocess
import fdsplotlib
import matplotlib.pyplot as plt
import importlib
import runpy
importlib.reload(fdsplotlib) # use for development (while making changes to fdsplotlib.py)
print("Using:", fdsplotlib.__file__)

# If there is an error in one of the sub-scripts, print the message but do not stop the main script.

def safe_run(script_path):
    try:
        runpy.run_path(script_path, run_name="__main__")
        plt.clf()         # Clear the current figure (if any)
        plt.close('all')  # Close all open figure windows
    except Exception as exc:
        print(f"Error in {script_path}: {exc}")



print("SBI..."); safe_run("./SBI.py")
print("FSRI_NIST_SBI_contours..."); safe_run("./FSRI_NIST_SBI_contours.py")

Dataplot_Inputs_File = 'FSRI_NIST_SBI_config.csv'
EXP_Dir = '../../../Experimental_Data/'
OUT_Dir = './Outputs/'
Plots_Dir = './Plots/'

# Run dataplot and scatplot scripts

saved_data, drange = fdsplotlib.dataplot(config_filename=Dataplot_Inputs_File,
                                         expdir=EXP_Dir,
                                         cmpdir=OUT_Dir,
                                         pltdir=Plots_Dir,
                                         close_figs=True,
                                         verbose=True,
                                         plot_range=["SBI"],
                                         ) # see notes below on plot_range

print("Python validation scripts completed successfully!")

# ------------------------------
# plot_range usage examples
#
# plot_range lets you select which rows of the config file to process.
# You can mix row numbers, ranges, and Dataname strings:
#
#  1. Single row by number (Spreadsheet-style, including header rows):
#       plot_range = [1995]
#
#  2. Inclusive ranges by "start:stop":
#       plot_range = ["5:9"]        # rows 5 through 9
#
#  3. Open-ended ranges:
#       plot_range = ["1995:"]      # from row 1995 to the end
#
#  4. Named selection by Dataname (case-insensitive):
#       plot_range = ["CSTB Tunnel", "Steckler Compartment"]
#
#  5. Mixed selection:
#       plot_range = [1, 2, "5:9", "CSTB Tunnel", "7000:"]
#
#  6. All rows:
#       plot_range = ["all"]
#
# Notes:
# - Row numbers are 1-based (like Spreadsheet).
# - Ranges are inclusive, e.g. "5:9" means 5,6,7,8,9.
# - "start:" runs to the last row.
# - Strings that are not ranges or "all" are matched to the Dataname column.
# ------------------------------

