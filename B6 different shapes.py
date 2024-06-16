import math

class Shape:
    @classmethod
    def create_circle(cls, radius):
        return cls(radius)

    @classmethod
    def create_square(cls, side):
        return cls(side, side)

    @classmethod
    def create_rectangle(cls, length, width):
        return cls(length, width)

    def __init__(self, *args):
        self.args = args

    def calculate_area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def calculate_area(self):
        radius = self.args[0]
        return math.pi * (radius ** 2)

class Square(Shape):
    def calculate_area(self):
        side = self.args[0]
        return side ** 2

class Rectangle(Shape):
    def calculate_area(self):
        length, width = self.args
        return length * width



circle = Circle.create_circle(5)
print("Area of Circle:", circle.calculate_area())  # Output: Area of Circle: 78.53981633974483

square = Square.create_square(4)
print("Area of Square:", square.calculate_area())  # Output: Area of Square: 16

rectangle = Rectangle.create_rectangle(6, 8)
print("Area of Rectangle:", rectangle.calculate_area())  # Output: Area of Rectangle: 48








