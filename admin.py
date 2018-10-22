# Name:
# Student Number:

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 2, 2018.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to "do nothing".  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSP5110 Requirement: Also enforce a minimum value of 1.  See assignment brief.
def inputInt(prompt):
    pass


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    pass


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveData(dataList):
    pass


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.



# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Details of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Game Finder Admin Program.')

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()

    if choice == 'a':
        # Add a new game.
        # See Point 3 of the "Details of admin.py" section of the assignment brief.
        pass

    elif choice == 'l':
        # List the current games.
        # See Point 4 of the "Details of admin.py" section of the assignment brief.
        pass

    elif choice == 's':
        # Search the current games.
        # See Point 5 of the "Details of admin.py" section of the assignment brief.
        pass

    elif choice == 'v':
        # View a game.
        # See Point 6 of the "Details of admin.py" section of the assignment brief.
        pass

    elif choice == 'd':
        # Delete a game.
        # See Point 7 of the "Details of admin.py" section of the assignment brief.
        pass

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Details of admin.py" section of the assignment brief.
        pass

    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Details of admin.py" section of the assignment brief.
        pass
