# Name: Andrew Udodov
# Student Number: 10472552

# This file is provided to you as a starting point for the "game_finder.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 2, 2018.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to "do nothing".  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        try:
            with open('data.txt') as file:
                self.data = json.load(file)

        except IOError:
            tkinter.messagebox.showerror('Error!', 'Missing File.')
            self.data = []
            self.main.destroy()
            return
        except ValueError:
            self.data = []
            tkinter.messagebox.showerror('Error!', 'Invalid File.')
            self.main.destroy()
            return
        self.main = tkinter.Tk()

        self.main.title("Game Finder")

        self.constraints = tkinter.Frame(self.main)
        self.matchingGames = tkinter.Frame(self.main)

        tkinter.Label(self.main, text='Constraints:').grid(columnspan=3)

        tkinter.Label(self.main, text='Number of players: ').grid(row=1, column=0)
        tkinter.Label(self.main, text='Time available (mins): ').grid(row=2, column=0)
        tkinter.Label(self.main, text='Age of youngest player: ').grid(row=3, column=0)

        self.youngestAge = tkinter.StringVar()
        self.playersNum = tkinter.StringVar()
        self.timeAvail = tkinter.StringVar()

        tkinter.Entry(self.main, textvariable=self.playersNum, width=10).grid(row=1, column=1)
        tkinter.Entry(self.main, textvariable=self.timeAvail, width=10).grid(row=2, column=1)
        tkinter.Entry(self.main, textvariable=self.youngestAge, width=10).grid(row=3, column=1)

        self.submitButton = tkinter.Button(self.main, text='Submit', command=self.greet)
        self.submitButton.grid(row=4, columnspan=3)

        # self.criteriaLabel = tkinter.StringVar()

        tkinter.Label(self.main, text='Matching Games: ').grid(row=6, columnspan=3)
        self.criteriaLabel = tkinter.Label(self.main, text='No criteria submitted.', justify='center')
        self.criteriaLabel.grid(row=7, columnspan=3)
        tkinter.Button(self.main, text='Quit', command=self.greet).grid(row=10, columnspan=3)

        tkinter.mainloop()

    def greet(self):
        print("Greetings!")
        self.criteriaLabel.config(text='Hello :D')
        if len(self.youngestAge.get() + self.playersNum.get() + self.timeAvail.get()) == 0:
            tkinter.messagebox.showerror('Error!', 'enter data')
        else:
            # text = self.data[0]
            # self.criteriaLabel.config(text)
        pass

    def findGames(self):
        # This method finds and displays games matching the criteria entered by the user.
        # See the "The findGames() Method of the GUI Class of game_finder.py" section of the assignment brief.
        pass


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
