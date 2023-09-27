import random
from Opponent import Opponent
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
       ''' Instance properties:
       abilities: List
       armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
       #abilities and armors are lists, don't have starting values and are set to empty upon initialization
       #assign name of hero, known required value
       self.abilities = list()
       self.armors = list()
       
       self.name = name
       #pass in starting health
       self.starting_health = starting_health
       #upon creation, starting health = current health
       self.current_health = starting_health

    def fight(self, opponent): #no init bc not an object  
        outcome = ['wins','loses','draw']
        result = random.choice(outcome)
        print(f"{self.name} {result} against {opponent.name}")
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        #defin new method to USE hero's ability with attack
        #attack value defined in ability.py
        total_damage = 0
        #loop thru ea. ability
        for ability in self.abilities:
        #add damage of ea. ability to running total
            total_damage += Armor.attack()
        return total_damage
    def add_armor(self, armor):
        #recieve armor object and append to self.armors
        self.armors.append(armor)
    def defend(self, damage):
        self.damage = damage
        #add and init damage
        #state base armor in case none
        total_armor = 0
        #loop through ea. armor
        for armor in self.armors:
            #add block value of each armor to the total
            total_armor += armor.block()
        return total_armor
    def add_weapon(self, weapon):
    # This method will append the weapon object passed in as an
    # argument to self.abilities.
    # This means that self.abilities will be a list of
    # abilities and weapons.
    def take_damage(self, damage):
        #call self.defend to calc damage reduction
        damage_reduction = self.defend(damage)
        #calc actual damage
        if damage < 0:
            #if damage is negative, convert integer
           positive_damage = abs(damage)
           return positive_damage
        else:
            #print ("You didn't do enough damage!")
             actual_damage = damage - damage_reduction
        #subtract total from self.current_health
        self.current_health -= actual_damage
        return actual_damage
    def is_alive(self):
            return self.current_health > 0 




    #call constructor test
if __name__ == "__main__": 
    ability = Ability("Great Debug Bug", 50)
    #ability1 = Ability("Monkey throw", 60)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    #hero.add_ability(ability1)
    shield = Armor("Copper Shield", 75)
    hero.add_armor(shield)
    hero.take_damage(10)
    print(hero.is_alive())
    hero.take_damage(150000)
    print(hero.is_alive())

    opponent = Opponent("Monkey Man", 150)
    hero.fight(opponent)
    ###### simulate attack



    
    