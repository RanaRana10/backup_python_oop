class Vehicle:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is being driven 🚗")

class Car(Vehicle):
    def __init__(self, color, make, model, year):
        # super().__init__(color, make, model)  # Initialize attributes from Vehicle
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def honk(self):
        print(f"The {self.make} {self.model} goes 'Beep beep!' 📢 in the year of {self.year}")

my_car = Car("Blue", "Toyota", "Corolla", 2022)

my_car.drive()
my_car.honk()
