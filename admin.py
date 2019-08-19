# Name: Andrew


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
# If the invalid input  -- displays an error and asks for another try
def inputInt(prompt, errorMessage='Invalid input - Try again.', minValue=None, maxValue=None):
    while True:
        value = input(prompt)
        try:
            numResponse = int(value)
        except ValueError:
            print(errorMessage)
            continue
        if minValue is not None and numResponse < minValue:
            print('Minimum of', minValue, 'permitted.')
            continue
        if maxValue is not None and numResponse > maxValue:
            print('Maximum of', maxValue, 'permitted.')
            continue
        return numResponse


# This function repeatedly prompts for input until something other than whitespace is entered.
# If nothing entered displays an error
def inputSomething(prompt):
    while True:
        value = input(prompt).strip()
        if value == '':
            print('Can not be empty - Please enter something.')
            continue
        else:
            return value

# This function opens "data.txt" in write mode and writes the data to it in JSON format.


def saveData(dataList):
    with open('data.txt', 'w') as file:
        json.dump(dataList, file, indent=4, ensure_ascii=False)


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the Game Finder Admin Program.')
try:
    with open('data.txt') as file:
        data = json.load(file)

except IOError:
    data = []
except ValueError:
    data = []

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [b]reakdown or [q]uit.')
    choice = input('> ').lower().split()

    if choice[0] == 'a':
        # Add a new game.
        gameName = inputSomething('Enter the game name > ')
        nameList = []  # create an empty list to use it later for checking if game already exists
        for counter, game in enumerate(data):
            name = game['name'].lower()
            nameList.append(name)
            # check if game exists, and displays a proper message
            # the message contains the name of the existing game and its index
        if gameName.lower() in nameList:
            index = nameList.index(gameName.lower())
            print('The game already exists.')
            print('Index: {}; Game name: {}'.format(index, data[index]['name']))
            # if no such game exists, asks user to provide more information about the game
            # and saves it
        else:
            minPlayers = inputInt('Enter the minimum players for the game > ', minValue=1)
            maxPlayers = inputInt('Enter the maximum players for the game > ', minValue=minPlayers)
            duration = inputInt('Enter the duration of the game > ', minValue=1)
            minAge = inputInt('Enter the minimum age > ', minValue=1, maxValue=120)
            dictionary = {'name': gameName, 'min_players': minPlayers, 'max_players': maxPlayers, 'duration': duration, 'min_age': minAge}
            data.append(dictionary)
            saveData(data)
            print('Game added.')

    elif choice[0] == 'l':
        # List the current games.
        # if the data.txt file is empty displays the message that there are no games saved
        # Otherwise, displays the game's index and name
        if not data:
            print('No Games Saved!')
        else:
            print('List of Saved Games: ')
            for counter, game in enumerate(data):
                print ('Index: {}; Game name: {}'.format(counter, game['name']))

    elif choice[0] == 's':
        # Search the current games.
        # reads user input and based on it desides what to display
        if not data:
            print('No Games Saved!')
        else:
            # if user input is just one character -- asks for more details like the game name to look for
            if len(choice) == 1:
                gameName = inputSomething('Enter the name of the game you would like to look for > ').lower()
            else:
                # if user input is more than 1 character, strips the input and search the game based on what user's entered
                # if user's input matches the game name in data.txt displays the message that contains game name and its index
                # if nothing found, displays the message
                gameName = ' '.join(choice[1:]).strip().lower()
            print('Searching results: ')
            noMatches = True
            for counter, game in enumerate(data):
                name = game['name'].lower()
                if gameName in name:
                    noMatches = False
                    print ('Index: {}; Game name: {}'.format(counter, game['name']))
            if noMatches:
                print ('No games found.')

    elif choice[0] == 'v':
        # View a game.
        # reads user input and based on it desides what to display
        if not data:
            print('No Games Saved!')
        else:
            try:
                # if user input is just one character -- asks for game's index to display information about the game
                if len(choice) == 1:
                    value = inputInt('Game number (index) to view > ', minValue=0)
                else:
                    # if user input is more than 1 character, gets the second character (should be a number) and do the following
                    # if index that user entered exists in data.txt, displays game information
                    # if index is out of range or not a number, displays the error messages
                    value = int(choice[1])
                print(data[value]['name'])
                print('\tPlayers: {} - {}'.format(data[value]['min_players'], data[value]['max_players']))
                print('\tDuration: {} minutes'.format(data[value]['duration']))
                print('\tMinumum Age: {}'.format(data[value]['min_age']))
            except ValueError:
                print('Invalid input - Try again. Index should be integer number.')
            except IndexError:
                print('Invalid index number - Out of range. There is total of {} games saved.'.format(len(data)))

    elif choice[0] == 'd':
        # Delete a game.
        if not data:
            print('No Games Saved!')
        else:
            try:
                # if user input is just one character -- asks for game's index to delete
                if len(choice) == 1:
                    value = inputInt('Game number (index) to delete > ', minValue=0)
                else:
                    # if user input is more than 1 character, gets the second character (should be a number) and do the following
                    # if index that user entered exists in data.txt, deletes the recording
                    # if index is out of range or not a number, displays the error messages
                    value = int(choice[1])
                del data[value]
                saveData(data)
                print('Game Deleted!')
            except ValueError:
                print('Invalid input - Try again. Index should be integer number.')
            except IndexError:
                print('Invalid index number - Out of range.')

    elif choice[0] == 'b':
        # Display breakdown
        # the breakdown consists of:
        # Total number of games, maximum and minimum players across all games, average duration of game, average minimum age
        if not data:
            print('No Games Saved!')
        else:
            totalDuration = 0
            totalAge = 0
            maxNumOfPlayers = 0
            minNumOfPlayers = data[0]['min_players']
            for counter in range(len(data)):
                maximum = data[counter]['max_players']
                minimum = data[counter]['min_players']
                totalDuration += data[counter]['duration']
                totalAge += data[counter]['min_age']
                if minimum < minNumOfPlayers:
                    minNumOfPlayers = minimum
                if maximum > maxNumOfPlayers:
                    maxNumOfPlayers = maximum
            print('Total number of games: ', len(data))
            print('Maximum players across all games: {} '.format(maxNumOfPlayers))
            print('Minimum players across all games: {} '.format(minNumOfPlayers))
            print('Average duration across all gmaes: {0:.2f}'.format(float(totalDuration / len(data))))
            print('Average min Age across all games: {0:.2f}'.format(float(totalAge / len(data))))

    elif choice[0] == 'q':
        # Quit the program.
        print('Goodbye!')
        break

    else:
        # Print "invalid choice" message.
        print('Invalid choice!')
