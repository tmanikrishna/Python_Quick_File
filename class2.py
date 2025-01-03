class Car:

    def __init__(self , model, colour):
        self.model = model
        self.colour = colour

    def displayCar(self):
        print(self.model)
        print(self.colour)

car1 = Car('Benz' , 'Black')

car1.displayCar()

car2 = Car('BMW', 'Blue')

print(car2.model)
print(car2.colour)

car2.colour = 'White'

car2.displayCar()