# Prerequisite start
# Work of Lachlan T 2024
# 12/09/2024

import launch  # Written by myself as a starting off point menu
import os  # Imported 'os' to be able to see if os.environ is equal to PYCHARM_HOSTED or not


warning_color = "\033[91m"  # string color red (to prompt a warning)
warning_color_reset = "\033[0m"  # string color default (to reset color to default)


if "PYCHARM_HOSTED" in os.environ:
    # PYCHARM Detection - prompt user, that user should run from CMD because clear...
    # isn't well represented when run from pycharm, print error not allowing...
    # pycharm application:
    print(warning_color + "Please run this program from a CLI command line interface environment")
    print("This allows the intended interface with the program" + warning_color_reset)
else:  # Not running on PYCHARM then proceed
    launch.launch()  # Starts the function launch in launch.py that is a starting menu for the user
