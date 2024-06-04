#You are required to create a simple zoo management system using python inheritance.
#The system should manage different types of animals and their unique behaviors.
#Follow the instructions below to implement the system

class Animal:
    def _init_(self, name , species , sound):
        self.name=name
        self.species= species
        self.sound=sound

    def make_sound(self):
       print(f"the {self.species} named {self.name} goes '{self.sound}")


class Lion(Animal):
    def _init_(self, name):
        super()._init_(name, "Lion","roar")

    def get_info(self):
        print("Lions are the king of the jungle.")


class Elephant(Animal):
    def _init_(self, name):
        super()._init_(name, "Elephant","trumphet")

    def get_info(self):
        print("Elephants are the largest land animals")

class Snake(Animal):
    def _init_(self, name):
        super()._init_(name,  "Snake", "hiss")

    def get_info(self):
        print("Snakes can be found on every continent except antartica")

# Creating instances of each animal
leo = Lion("Leo")
ellie= Elephant("Ellie")
slyther = Snake("Slyther")

# Demonstrating the use of all methods
leo.make_sound()
leo.get_info()
print()

ellie.make_sound()
ellie.get_info()
print()

slyther.make_sound()
slyther.get_info()
print()