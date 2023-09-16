class Dog:
    def __init__(self, name, breed):
        self.name = name #Str will be name
        self.breed = breed
        print("dog initialized!")
    #Methods are their own named funcs within a class
    #use "self" parameter everytime when making a class method
    def bark(self):
        print("Woof!")
