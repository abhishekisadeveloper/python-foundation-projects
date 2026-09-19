from car import Car

car1 = Car("Tata Punch", 2026, 180, "red")
car2 = Car("Bugati", 2026, 300, "White")

car1.details()
car2.details()

# ===== HERE ARE SOME OF THE MOST UNDERSTANDABLE EXAMPLE:=====

# A class is a blueprint that defines structure and behavior
class Dog:
    # Class attribute -- shared by ALL instances
    species = "Canis familiaris"

    # __init__ is the constructor, called automatically when you create an instance
    def __init__(self, name, age):
        # Instance attributes -- each instance has its OWN copy
        self.name = name
        self.age = age

    # A method (function) that belongs to the class
    def bark(self):
        return f"{self.name} says Woof!"


# --- Creating instances (objects) from the class ---

# Each call to Dog(...) creates a NEW, independent instance
spot = Dog("Spot", 3)   # instance 1
rex  = Dog("Rex", 5)    # instance 2

# Each instance has its own state
print(spot.name)        # "Spot"
print(rex.name)         # "Rex"

# Changing one instance does NOT affect the other
spot.name = "Spot Jr."
print(spot.name)        # "Spot Jr."
print(rex.name)         # "Rex"  (unchanged)

# Methods work per-instance
print(spot.bark())      # "Spot Jr. says Woof!"
print(rex.bark())       # "Rex says Woof!"

# Class attribute is shared
print(spot.species)     # "Canis familiaris"
print(rex.species)      # "Canis familiaris"

# isinstance() checks if an object is an instance of a class
print(isinstance(spot, Dog))   # True
print(isinstance(spot, str))   # False   