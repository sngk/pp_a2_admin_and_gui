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
        self.btnFrame = None
        # self.constraints = tkinter.Frame(self.main)
        # self.matchingGames = tkinter.Frame(self.main)

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
        self.matchingLabel = tkinter.Label(self.main, text='No criteria submitted.', justify='center')
        self.matchingLabel.grid(row=7, columnspan=3)

        tkinter.mainloop()

    def gameInfo(self, btnIndex):
        message = '{}\n Players: {} - {}\n Duration: {}\n Minimum Age: {}'.format(self.data[btnIndex]['name'], self.data[btnIndex]
                                                                                  ['min_players'], self.data[btnIndex]['max_players'], self.data[btnIndex]['duration'], self.data[btnIndex]['min_age'])
        tkinter.messagebox.showerror(self.data[btnIndex]['name'], message)
        # for counter, game in enumerate(self.data):
        #     if btn in game['name']:

    def findGames(self):
        # This method finds and displays games matching the criteria entered by the user.
        try:
            youngestAge = int(self.youngestAge.get())
            timeAvail = int(self.timeAvail.get())
            playersNum = int(self.playersNum.get())
            gameList = []
            noMatches = True
            for counter, game in enumerate(self.data):
                if (game['min_players'] <= playersNum <= game['max_players']) and (timeAvail >= game['duration']) and (youngestAge >= game['min_age']):
                    gameName = game['name']
                    gameList.append(gameName)
                    noMatches = False
            text = '{} out of {} games matched the search:'.format(len(gameList), len(self.data))
            self.matchingLabel.config(text=text)

            if noMatches:
                self.criteriaLabel.config(text='No matching games found.')

        except ValueError:
            tkinter.messagebox.showerror('Error!', 'Invalid criteria specified.')
        except IndexError:
            tkinter.messagebox.showerror('Error!', 'Invalid criteria specified.')

        else:
            self.criteriaLabel.grid_remove()
            # self.criteriaLabel.config(text='\n'.join(gameList))  # version of program without buttons for game info
            self.buttons = {}
            if self.btnFrame:  # Exists?
                self.btnFrame.grid_forget()
            buttonFrame = self.btnFrame = tkinter.Frame(self.main)
            buttonFrame.grid(columnspan=3)
            nameList = []
            for btnIndex, btn in enumerate(gameList):
                for counter, game in enumerate(self.data):
                    nameList.append(game['name'])
                    if btn in nameList:
                        btnIndex = nameList.index(btn)
                self.buttons[btn] = tkinter.Button(buttonFrame, text=btn, command=lambda x=btnIndex: self.gameInfo(x))
                self.buttons[btn].grid(row=8 + btnIndex, columnspan=3)
            self.btnFrame.grid()


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
