# Starting Menu
# Work of Lachlan T 2024
# 12/09/2024

import logon  # Written by myself to be called based on user input, if the user wants to logon
import register  # Written by myself to be called based on user input, if the user wants to register
import functionlib  # Written by myself to store functions frequently used through the program
import lookup # Imported User-List into main menu
import shared_variables # Written by myself for commonly used variables

def launch():
    while True:
        if shared_variables.logon_status == 1:
            logon_register_lookup = input(
                "\n Gelos Enterprises Logon program by Lachlan Tanfield: \n"
                " 1 - Logoff: \n"
                " 2 - Register: \n"
                " 3 - Commands: \n"
                " 4 - User-list: \n"
                " 5 - Exit: \n"
                " \n > "
            )
        else:
            logon_register_lookup = input(
                "\n Gelos Enterprises Logon program by Lachlan Tanfield: \n"
                " 1 - Logon: \n"
                " 2 - Register: \n"
                " 3 - Commands: \n"
                " 4 - User-list: \n"
                " 5 - Exit: \n"
                " \n > "
            )
        if logon_register_lookup == "1" and shared_variables.logon_status == 1:
            functionlib.clear()
            shared_variables.logon_status = 0
        elif logon_register_lookup == "1":
            functionlib.clear()
            logon.logon()
        elif logon_register_lookup == "2":
            functionlib.clear()
            register.register()
        elif logon_register_lookup == "3":
            functionlib.clear()
            print("Commands: \n !exit \n !clear")
        elif logon_register_lookup == "4" and shared_variables.logon_status == 1:
            functionlib.clear()
            lookup.lookup()
        elif logon_register_lookup == "4":
            functionlib.clear()
            print("Logon to gain access.")
        elif logon_register_lookup == "!clear":
            functionlib.clear()
        elif logon_register_lookup == "!exit":
            functionlib.exit_command()
            quit()
        elif logon_register_lookup == "5":
            functionlib.exit_command()
            quit()
        else:
            functionlib.clear()
            print("Input not recognised.")
