import random

# Creating the players class which includes name and starting health


class Player:

    def __init__(self, name, current_health=0):
        self.name = name
        self.current_health = int(current_health)
        self.start_game = str(
        input('Welcome to Death Dungeon. Would you like to enter? y or n?'))
        self.loop_game = 'You must be scared.'
        # prints for debugging purposes
        print(f'{self.name},{self.current_health}')
# Starting the game

    def start_adventure(self):
        if (self.start_game == 'y' or self.start_game == 'yes'):
            print(f'Welcome to Death Dungeon {self.name} I will be guiding you to your death. \n {self.loop_game}')
        elif (self.start_game == 'n' or self.start_game =='no'):
            self.loop_game
            return self.start_game
next

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    start_game = str(
        input('Welcome to Death Dungeon. Would you like to enter? y or n?'))
    test_person = Player('Ruot', 100)
    test_person.start_adventure()
