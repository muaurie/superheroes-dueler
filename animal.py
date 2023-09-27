class Animal:
    def __init__(self, name, sleep_time, eat, drink):
        self.name = name
        self.sleep_time = sleep_time
        self.eat = eat
        self.drink = drink

    def sleep(self):
        print(f"{self.name} sleeps for hours {self.sleep_time}")
    def eat(self):
        print(f"{self.name} is eating")
class Frod(Animal):
    def hop(self):
        print(f"{self.name} leaps!")

class Dog(Animal):
    #create a class in the Animal category
    def bark(self):
        print("Woof! Woof! WOOOOOOOOF!")

#instantiate like so
my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()
#should print:
print("Sophie sleeps for 12 hours", "Woof! Woof! WOOOOOOOF!")

