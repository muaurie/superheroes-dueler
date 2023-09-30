from hero import Hero
#team class will manage all of our superheros
class Team:
    def __init__(self, name):
        '''init team with team name and empty list of heroes'''
        self.name = name
        self.heroes = list()
    def remove_hero(self, name):
        '''if hero isn't found return zero'''
        #if hero in list, remove hero from list by name
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        #if looping through list and didn't find hero, indicator would not change so return 0
        if not foundHero:
            #if not = if not True
            return 0
    def view_all_heroes(self):
        '''print heroes to console'''
        print(self.heroes)
    def add_hero(self,hero):
        '''Add hero object to self.heroes'''
        #add hero object that is passed into list of heroes in self.heroes
        self.heroes.append(hero)