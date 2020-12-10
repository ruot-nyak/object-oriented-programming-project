import random
from player import Player  

class Outcomes(Player):
    #defined these variables outside of a function so they can be called to any function
    #with in the class
    odds = [1,2,3,4,5,6]
    option = random.choice(odds)

    def __init__(self, name, current_health,damage):
        super().__init__(name, current_health)
        self.damage = damage


    
    def choice(self):
        choice_good = f'Hmm {self.name} you are very lucky n/ No death!'
        self.damage = '.Your Damage : -100'

#IF statement to grab on of the options defined above the class, to then return an outcome
        if (self.option == 1):
            #Taking -100 to current health integer 100
            self.current_health -= 100
            #return a message that returns the users name, as well as their current health after the damgage taken
            #then returning damage.
            return f'Haha {self.name}, clumsy, you fell in a well. n/ hp: {self.current_health} {self.damage}'
        elif (self.option == 2):
            self.current_health -= 100
            return f'Sorry {self.name}, you hurt your foot n/ hp: {self.current_health} {self.damage}'
        elif (self.option == 3):
            self.current_health -= 100
            return f'Sorry {self.name}, you had a leg cramp n/ hp: {self.current_health} {self.damage}'
        elif (self.option == 4):
            self.current_health -= 100
            return f'Sorry {self.name}, you had a bear in a headlock, tripped and hit your head n/ hp: {self.current_health} {self.damage}'
        elif (self.option == 5):
            self.current_health -= 100
            return f'Sorry {self.name}, you forgot to wear a bandaid, and got a cut n/ hp: {self.current_health} {self.damage}'
        else:
            return choice_good


class Movement(Outcomes):
 
    death = print(f'invalid response, now you have to die....')
    # weather or not the user chooses right or left
    def __init__(self, name, current_health,damage,msg):
        super().__init__(name, current_health,damage)
        self.msg = msg
        self.right_left = input('You see two tunnels left or right?')
    def move(self):
        self.msg = 'You take a step down the tunnel and ...'
        if (self.right_left == 'right' or self.right_left == 'left'):
            return print(f'{self.msg} {self.choice()}')
        else:
            self.current_health -= 1000
            return print(f'{self.death()} {self.damage()}')


class End(Player):
    message_list = [
    'HAHAHA YOU ARE DEAD GOODBYE!',
    'Unlucky, or staged. You\'ll never know. ',
    'We\'re not built the same I guess.',
    'LMAO that\'s how you died?',]
    message = print(random.choice(message_list))
    def __init__(self, name, current_health):
        super().__init__(name, current_health,)
        
    

    def game_over(self):
        player_death = self.current_health <= 0
        if (player_death == True):
            return self.message
        else:
            pass

if __name__ == "__main__":
    # start_game =    
    # start_game = str(
    #     input('Welcome to Death Dungeon. Would you like to enter? y or n?')) 
    test_person = Player('Ruot', 100)
    test_person.start_adventure()

    # outcomes = Outcomes('Ruot',100,0)
    # outcomes.choice()
    test_move = Movement('Ruot',100,0,0)
    test_move.move()
    