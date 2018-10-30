# Name: Andrew Udodov
# Student Number: 10472552


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
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
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    while True:
        value = input(prompt).strip()
        if value == '':
            print('Can not be empty - Please enter something.')
            continue
        else:
            return value

# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.


def saveData(dataList):
    with open('data.txt', 'w') as file:
        json.dump(dataList, file, indent=4, ensure_ascii=False)

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Details of admin.py" section of the assignment brief.
# The rest is up to you.
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
        nameList = []
        for counter, game in enumerate(data):
            name = game['name'].lower()
            nameList.append(name)
        if gameName.lower() in nameList:
            index = nameList.index(gameName.lower())
            print('The game already exists.')
            print('Index: {}; Game name: {}'.format(index, data[index]['name']))
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
        if not data:
            print('No Games Saved!')
        else:
            print('List of Saved Games: ')
            for counter, game in enumerate(data):
                print ('Index: {}; Game name: {}'.format(counter, game['name']))

    elif choice[0] == 's':
        # Search the current games.
        if not data:
            print('No Games Saved!')
        else:
            if len(choice) == 1:
                gameName = inputSomething('Enter the name of the game you would like to look for > ').lower()
            else:
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
        if not data:
            print('No Games Saved!')
        else:
            try:
                if len(choice) == 1:
                    value = inputInt('Game number (index) to view > ', minValue=0)
                else:
                    value = int(choice[1])
                print(data[value]['name'])
                print('\tPlayers: {} - {}'.format(data[value]['min_players'], data[value]['max_players']))
                print('\tDuration: {} minutes'.format(data[value]['duration']))
                print('\tMinumum Age: {}'.format(data[value]['min_age']))
            except ValueError:
                print('Invalid input - Try again. Index should be integer number.')
            except IndexError:
                print('Invalid index number - Out of range.')

    elif choice[0] == 'd':
        # Delete a game.
        if not data:
            print('No Games Saved!')
        else:
            try:
                if len(choice) == 1:
                    value = inputInt('Game number (index) to delete > ', minValue=0)
                else:
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
