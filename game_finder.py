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

        tkinter.Label(self.main, text='Constraints:').grid(columnspan=3)

        tkinter.Label(self.main, text='Number of players: ').grid(row=1, column=0)
        tkinter.Label(self.main, text='Time available (mins): ').grid(row=2, column=0)
        tkinter.Label(self.main, text='Age of youngest player: ').grid(row=3, column=0)
        tkinter.Label(self.main, text='Matching Games: ').grid(row=6, columnspan=3)

        self.matchingLabel = tkinter.Label(self.main, text='No criteria submitted.', justify='center')
        self.matchingLabel.grid(row=7, columnspan=3)

        self.youngestAge = tkinter.StringVar()
        self.playersNum = tkinter.StringVar()
        self.timeAvail = tkinter.StringVar()

        tkinter.Entry(self.main, textvariable=self.playersNum, width=5).grid(row=1, column=1)
        tkinter.Entry(self.main, textvariable=self.timeAvail, width=5).grid(row=2, column=1)
        tkinter.Entry(self.main, textvariable=self.youngestAge, width=5).grid(row=3, column=1)

        self.submitButton = tkinter.Button(self.main, text='Submit', command=self.findGames)
        self.submitButton.grid(row=4, columnspan=3)

        tkinter.mainloop()

    def gameInfo(self, btnIndex):
        message = '{}\n Players: {} - {}\n Duration: {}\n Minimum Age: {}'.format(self.data[btnIndex]['name'], self.data[btnIndex]
                                                                                  ['min_players'], self.data[btnIndex]['max_players'],
                                                                                  self.data[btnIndex]['duration'],
                                                                                  self.data[btnIndex]['min_age'])
        tkinter.messagebox.showinfo(self.data[btnIndex]['name'], message)

    def findGames(self):
        # This method finds and displays games matching the criteria entered by the user.
        try:
            print(self.data[0])
            youngestAge = int(self.youngestAge.get())
            timeAvail = int(self.timeAvail.get())
            playersNum = int(self.playersNum.get())
            noMatches = True
            self.buttons = {}
            if self.btnFrame:  # Exists?
                self.btnFrame.grid_remove()

            buttonFrame = self.btnFrame = tkinter.Frame(self.main)
            buttonFrame.grid(columnspan=3)

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
        except IndexError:
            tkinter.messagebox.showerror('Error!', 'Invalid criteria specified.')
            if self.btnFrame:
                self.btnFrame.grid_remove()
                self.matchingLabel.config(text='Wrong criteria specified.')


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
