class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi

    def calculate_area(self):
        area = Circle.pi * (self.radius **2)
        print("This area is", area)
        return area
        # return Circle.pi * (self.radius **2)
        

circle_1 = Circle(5)

print(f"Area with the default pi is: {circle_1.calculate_area()}")

Circle.set_pi(30.14159)

print("Area with updated pi:", circle_1.calculate_area())


