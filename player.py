

# Creating the players class which includes name and starting health
class Player:
    def __init__(self, name, current_health=0):
        self.name = name
        self.current_health = int(current_health)
        # prints for debugging purposes
        print(f'{self.name},{self.current_health}')
# Starting the game

    def player_name(self):
        # self.name = str(input('I haven\'t seen you around here /n are you a what is your name?')
        pass

    def start_adventure(self):
        start_game = str(
            input('Welcome to Death Dungeon. Would you like to enter? y or n?'))
        if (start_game == 'y' or start_game == 'yes'):
            return f'Welcome to Death Dungeon {self.name} n/ I will be guiding you to your death.'
        else:
            print('What are you scared!?')
            return quit

    def player_class(self):
        pass




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    test_person = Player('Ruot', 100)
