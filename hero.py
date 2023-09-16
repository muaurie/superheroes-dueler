import random
from Opponent import Opponent

class Hero:
    def __init__(self, name, starting_health=100):
       ''' Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
       #assign name of hero, known required value
       self.name = name
       #pass in starting health
       self.starting_health = starting_health
       #upon creation, starting health = current health
       self.current_health = starting_health

    def fight(self, opponent): #no init bc not an object  
        outcome = ['wins','loses','draw']
        result = random.choice(outcome)
        print(f"{self.name} {result} against {opponent.name}")
    #call constructor
if __name__ == "__main__": #this code only runs if directly called
    #here the if[] prevents this from being run when imported by another script
    #later when import the hero class, don't test with this!!
    hero = Hero("Grace Hopper", 200)
    opponent = Opponent("Monkey Man", 150)
    hero.fight(opponent)
    
    