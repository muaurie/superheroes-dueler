from ability import Ability
import random

class Weapon(Ability):
     def attack(self):
        self.max_damage/2
        random_value = random.randint(0, self.max_damage)
        return random_value