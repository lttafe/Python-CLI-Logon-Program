# User Lookup
# Work of Lachlan T 2024
# 12/09/2024

import os  # Imports the 'os' module to use function to check if directories exist
accounts = "accounts.txt"


def lookup():  # Defines a function named 'lookup' to find and display registered user accounts in accounts.txt
    if not os.path.exists(accounts):  # Checks if the file 'accounts.txt' does not exist
        print("No users registered")
    else:  # If accounts.txt exists, open in read mode and process the file
        print("Users List:\n")
        user_count = 0  # Initialize a counter for the number of users
        with open(accounts, "r") as file:
            for line in file:
                username = line.split(',')[0]  # Get the username from each line
                print(username)  # Print the username
                user_count += 1  # Increment the user counter

        print(f"\nTotal users: {user_count}")  # Print the total number of users
