# Logon Procedure
# Work of Lachlan T 2024
# 12/09/2024

import time  # Imports community time.py to use the time.sleep function
import functionlib  # Written by myself to store functions frequently used through the program
import launch_logan  # Call launch.launch function when logon procedure is successful

accountsFile = "accounts.txt"


def logon():  # Define the launch function to act as a start menu interface
    logon_username = input("Logon \n Enter Username: ")
    if logon_username == "!exit":
        functionlib.exit_command()
        return

    functionlib.clear()
    logon_password = input("Logon \n Enter Password: ")
    if logon_password == "!exit":
        functionlib.exit_command()
        return
    functionlib.clear()

    logon_username_password = f"{logon_username},{logon_password}"
    # Combine username and password into an f-string, seperated by ','

    try:
        with open("accounts.txt", "r") as file: # Opens the accounts file in read mode
            accounts = file.readlines() # Reads all lines from the file into a list
            if any(logon_username_password == account.strip() for account in accounts):
                # Checks if the combined username and password exist in the accounts list
                print("Logon Successful")
                time.sleep(2)
                functionlib.clear()
                launch_logan.launch_logon()
            else:
                print("Logon Unsuccessful")
                time.sleep(1)
                functionlib.clear()
    except FileNotFoundError:
        print("No registered users found")
        time.sleep(2)
        functionlib.clear()
        pass
