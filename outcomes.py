import random
import Player 

class Outcomes(Player):
    def __init__(self,):
        Player.__init__(self,'Ruot',100)
        
    def choice(self,player):
        odds = [1,2,3,4,5,6]
        choice_good = f'Hmm {self.name} you are very lucky n/ No death!'
        if (random.choice(odds) == 1):
            self.current_health -= 100
            return f'sorry {self.name}, you fell in a well and took some damage n/ hp: {self.current_health}'
        elif (random.choice(odds) == 2):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        elif (random.choice(odds) == 3):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        elif (random.choice(odds) == 4):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        elif (random.choice(odds) == 5):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health}'
        else:
            return choice_good


    


