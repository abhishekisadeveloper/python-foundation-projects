class Car:

    origin_of_car = 'india' # class variable.
    
    def __init__(self, modal, year, top_speed, color):
        self.modal = modal
        self.year = year
        self.top_speed = top_speed
        self.color = color

    # This is called Methode.
    def details(self):
        print(
            f"This {self.modal} is aussambled in {self.year} and his top speed is {self.top_speed} and the color is {self.color}"
        )
