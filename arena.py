from ability import Ability
from weapon import Weapon
from armor import Armor
from hero_class import Hero
from team import Team

#Arena does not inherit from Team and Team does not inherit from Arena
class Arena: 
    def __init__(self):
        '''instantiate properties
                team_one": None
                team_two: None'''
        self.team_one = []
        self.team_two = []

    def create_ability(self):
        '''Prompt for ability info.
           Return Ability with values from user Input'''
        
        name = input("What is the ability name?")
        max_damage = input(
            "What is the max damage of the ability?")
        
        return Ability(name, max_damage) #return the input values to Ability
    
    def create_weapon(self):
        '''Prompt user for Weapon info, return values to weapon'''
        name = input("What is the name of the weapon?")
        max_damage = input("What is the max_damage of the weapon?")

        return Weapon(name, max_damage)
    
    def create_armor(self):
        '''Prompt user for armor info, return values'''
        name = input("What is the name of the armor?")
        max_block = input("What is the max block of the armor?")

        return Armor(name, max_block)
    
    def create_hero(self):
        '''Prompt user for Hero info return val'''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4": #While item does not equal 4, 4 = max
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ##create ability and add to hero
                created_ability = self.create_ability() #hold value in var
                hero.add_ability(created_ability) #append to hero add_ability
            elif add_item =="2":
                #create weapon and add to hero
                created_weapon = self.create_weapon
                hero.add_weapon(created_weapon)
            elif add_item == "3":
                #create and add an armor to the hero
                created_armor = self.create_armor
                hero.add_armor(created_armor)
            return hero
        
    def build_team_one(self):
        '''Prompt the user to build team_one'''
        #allow user to create team 
        #prompt user for number of heroes on team 1
        #call self.create_hero() for every hero that user wants in team one
        #add created hero to team one
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        ##convert the input into an integer with int(input"")
        for i in range(numOfTeamMembers):
        #for loop iterate numOfTeamMembers times, which is # of heroes user specified
            hero = self.create_hero()
            #call call and create hero object, hero var holds user input
            self.team_one.add_hero(hero)
            #once created, add hero to team one
        

    def build_team_two(self):
        '''Prompt user to build team two'''
        numOfTeamMembers = int(input("How many members would you like in Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        heroes = self.team_one
        opponents = self.team_two
        battle_result = heroes.fight(opponents)

        for hero in heroes: #loop through ea. hero in team_one and fight oppon.
            battle_result = hero.fight(opponents)
            battle_result.append(battle_result)
        return battle_result
    def show_stats(self):
        '''Print team stats to terminal'''
        print("\n") #used to create a new line
        print(self.team_one.name + " statistics: ")#print message with team 1 name and statistics:... (header label)
        self.team_one.stats() #call stats() on team_one object
        print("\n") #line
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

    # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills #team_kills includes total numb of hero kills
            team_deaths += hero.deaths #team_deaths includes hero.deaths
        if team_deaths == 0: 
            team_deaths = 1 #for the math, so the k/d doesn't calculate 0
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths)) 
        #in python you can concatenate strings with +
    #Now display the average K/D for Team Two
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills 
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + "average K/D was" + str(team_kills/team_deaths))
    # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived  
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()