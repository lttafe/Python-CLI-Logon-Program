# Register Procedure
# Work of Lachlan T 2024
# 12/09/2024

import functionlib  # Written by myself to store functions frequently used through the program
import time  # Imports community time.py to use the time.sleep function


def register():  # defines starting point for user input to register an account
    register_username = input("Register \n Enter Username: ")
    functionlib.clear()
    if register_username == "!exit":
        functionlib.exit_command()
        return

    while True:
        register_password = input("Hint: password needs to be 10 characters minimum.\n \nRegister \n Password: ")
        if register_password == "!exit":
            functionlib.exit_command()
            return
        elif len(register_password) < 10: # Checks if the provided password meets the minimum length
            functionlib.clear()
            print("Registration Unsuccessful")
        else:
            functionlib.clear()
            print("Registration Successful")
            with open('accounts.txt', "a") as file:
                file.write(f"{register_username},{register_password}\n")
                # Writes the username and password to the file seperated by ',' as an f-string
                time.sleep(2)
                functionlib.clear()
            break
