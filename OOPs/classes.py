from car import Car

car1 = Car("Tata Punch", 2026, 180, "red")
car2 = Car("Bugati", 2026, 300, "White")

print(Car.origin_of_car) # prefering the Class Car directly for batter readablity.

car1.details()
# car2.details()