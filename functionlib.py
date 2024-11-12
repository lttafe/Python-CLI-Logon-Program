# Common functions
# Work of Lachlan T 2024
# 12/09/2024


import os  # Import 'os' to check use cls function on windows or clear on other devices to clear the screen
import time  # Import 'time' to provide an increment waiting period to display a message


def clear():  # Creates a clear function to be used throughout the program
    os.system("cls" if os.name == "nt" else "clear")
    # Assigns string cls for windows or clear for other 'OS' for os.system function


def exit_command():
    clear()
    print("Exiting Application")
    time.sleep(0.5)
    clear()
    print("Exiting Application.")
    time.sleep(0.5)
    clear()
    print("Exiting Application..")
    time.sleep(0.5)
    clear()
    print("Exiting Application...")
    time.sleep(1)
    clear()

