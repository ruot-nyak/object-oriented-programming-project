import random
from player import Player  

class Outcomes(Player):
    def __init__(self, name, current_health):
        super().__init__(name, current_health)

    
    def choice(self):
        odds = [1,2,3,4,5,6]
        choice_good = f'Hmm {self.name} you are very lucky n/ No death!'
        option = random.choice(odds)

        if (option == 1):
            self.current_health -= 100
            return f'sorry {self.name}, you fell in a well and took some damage n/ hp: {self.current_health}'
        elif (option == 2):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        elif (option == 3):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        elif (option == 4):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        elif (option == 5):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        else:
            return choice_good

class RightLeft(Outcomes):
    # weather or not the user chooses right or left
    def __init__(self, name, current_health):
        super().__init__(name, current_health)

    def move(self):
        movement = input('You see two tunnels left or right?')
        if (movement == 'right' or movement == 'left'):
            return self.choice()

if __name__ == "__main__":
    outcomes = Outcomes('Ruot',100)
    outcomes.choice()
    test_move = RightLeft('Ruot',100)
    test_move.move()