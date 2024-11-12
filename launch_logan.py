# Logged in menu
# Work of Lachlan T 2024
# 12/09/2024

import launch  # Written by myself as a starting off point menu
import functionlib  # Written by myself to store functions frequently used through the program
import lookup  # Written by myself to show just the usernames in accounts.txt
import shared_variables # Written by myself for commonly used variables


def launch_logon():
    while True:
        logon_system = input("\n Logon Options \n 1 - Return: \n 2 - Logoff: \n 3 - User-list: \n \n > ")

        if logon_system == "1":
            functionlib.clear()
            shared_variables.logon_status = 1
            launch.launch()
        elif logon_system == "2":
            functionlib.clear()
            shared_variables.logon_status = 0
            launch.launch()
        elif logon_system == "3":
            functionlib.clear()
            lookup.lookup()
        elif logon_system == "!exit":
            functionlib.exit_command()
            shared_variables.logon_status = 1
            launch.launch()
        elif logon_system == "!clear":
            functionlib.clear()
        else:
            functionlib.clear()
            print("Input not recognised. \n")
