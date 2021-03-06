# Name: Andrew

# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # try to open the file and display error messages if there is no such file or
        # its data not JSON formatted
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
        self.btnFrame = None

        # create labels for constraints
        # and place them using grid
        tkinter.Label(self.main, text='Constraints:').grid(columnspan=3)

        tkinter.Label(self.main, text='Number of players: ').grid(row=1, column=0)
        tkinter.Label(self.main, text='Time available (mins): ').grid(row=2, column=0)
        tkinter.Label(self.main, text='Age of youngest player: ').grid(row=3, column=0)
        tkinter.Label(self.main, text='Matching Games: ').grid(row=6, columnspan=3)

        self.matchingLabel = tkinter.Label(self.main, text='No criteria submitted.', justify='center')
        self.matchingLabel.grid(row=7, columnspan=3)

        # stores the data from Entry widgets
        self.youngestAge = tkinter.StringVar()
        self.playersNum = tkinter.StringVar()
        self.timeAvail = tkinter.StringVar()

        # create Entry widgets for players number, available time and the youngest age for the game
        tkinter.Entry(self.main, textvariable=self.playersNum, width=5).grid(row=1, column=1)
        tkinter.Entry(self.main, textvariable=self.timeAvail, width=5).grid(row=2, column=1)
        tkinter.Entry(self.main, textvariable=self.youngestAge, width=5).grid(row=3, column=1)

        # widged for Submit button, that triggers the function to find games with sepcified criteria
        self.submitButton = tkinter.Button(self.main, text='Submit', command=self.findGames)
        self.submitButton.grid(row=4, columnspan=3)

        tkinter.mainloop()

# Method to display game information if game button clicked
# show the message box with the information about the game
    def gameInfo(self, btnIndex):
        message = '{}\n Players: {} - {}\n Duration: {}\n Minimum Age: {}'.format(self.data[btnIndex]['name'], self.data[btnIndex]
                                                                                  ['min_players'], self.data[btnIndex]['max_players'],
                                                                                  self.data[btnIndex]['duration'],
                                                                                  self.data[btnIndex]['min_age'])
        tkinter.messagebox.showinfo(self.data[btnIndex]['name'], message)

# This method finds and displays games matching the criteria entered by the user.
    def findGames(self):
        try:
            youngestAge = int(self.youngestAge.get())
            timeAvail = int(self.timeAvail.get())
            playersNum = int(self.playersNum.get())
            noMatches = True
            self.buttons = {}
            if self.btnFrame:  # if button frame Exists remove it (to clear the space)
                self.btnFrame.grid_remove()

            buttonFrame = self.btnFrame = tkinter.Frame(self.main)
            buttonFrame.grid(columnspan=3)

            # Check if there are games in data.txt that match the specified criteria enteterd by the user
            # if there are no games, displays the "not found" message
            # if there are games, displays how many of them are there out of total number of games
            # displays the name of the games as buttons that can be clicked for more information about particular game
            for game in self.data:
                if (game['min_players'] <= playersNum <= game['max_players']) and (timeAvail >= game['duration']) and (youngestAge >= game['min_age']):
                    btnIndex = self.data.index(game)
                    self.buttons[game['name']] = tkinter.Button(buttonFrame, text=game['name'],
                                                                command=lambda x=btnIndex: self.gameInfo(x), width=25)
                    self.buttons[game['name']].grid(row=8 + btnIndex, columnspan=3)
                    noMatches = False

            text = '{} out of {} games matched the search:'.format(len(self.buttons), len(self.data))
            self.matchingLabel.config(text=text)
            if noMatches:
                self.matchingLabel.config(text='No matching games found.')

        except ValueError:
            tkinter.messagebox.showerror('Error!', 'Invalid criteria specified.')
            if self.btnFrame:
                self.btnFrame.grid_remove()
                self.matchingLabel.config(text='Wrong criteria specified.')


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
