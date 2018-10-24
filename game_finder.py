# Name: Andrew Udodov
# Student Number: 10472552

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

        self.submitButton = tkinter.Button(self.main, text='Submit', command=self.findGames)
        self.submitButton.grid(row=4, columnspan=3)

        tkinter.Label(self.main, text='Matching Games: ').grid(row=6, columnspan=3)
        self.criteriaLabel = tkinter.Label(self.main, justify='center')
        self.criteriaLabel.grid(row=8, columnspan=3)
        self.matchingLabel = tkinter.Label(self.main, text ='No criteria submitted.', justify='center')
        self.matchingLabel.grid(row=7, columnspan=3)
        tkinter.Button(self.main, text='Quit', command=self.greet).grid(row=10, columnspan=3)

        tkinter.mainloop()

    def greet(self):
        print("Greetings!")
   
    def findGames(self):
        # This method finds and displays games matching the criteria entered by the user.
        try:
        	youngestAge = int(self.youngestAge.get())
        	timeAvail = int(self.timeAvail.get())
        	playersNum = int(self.playersNum.get())
        	gameList = []
        	for counter, game in enumerate(self.data):
        		if self.data[counter]['min_players'] <= playersNum <= self.data[counter]['max_players']:
        			if timeAvail <= self.data[counter]['duration']:
        				if youngestAge >= self.data[counter]['min_age']:
        					game = self.data[counter]['name']
        					gameList.append(game)
        					
        				else:
        					self.criteriaLabel.config(text='No matching games')
        			else:
        				self.criteriaLabel.config(text='No matching games')
        		else:
        			self.criteriaLabel.config(text='No matching games')
        	text = '{} out of {} matched the search:'.format(len(gameList), len(self.data))
        	self.matchingLabel.config(text=text)
        	self.criteriaLabel.config(text='\n'.join(gameList))
        except ValueError:
        	tkinter.messagebox.showerror('Error!', 'Invalid criteria specified.')
        except IndexError:
        	tkinter.messagebox.showerror('Error!', 'Invalid criteria specified.')
        # pass


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
