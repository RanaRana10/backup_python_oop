class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width = {self.width}, height = {self.height})\nThis is came as a result of using __str__ in the class"

    def __eq__(self, other):
        return self.width == other.width and self.height  == other.height

    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __len__(self):
        return 2 * (self.width + self.height)

    
    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rectangle_1 = Rectangle(5,10)
rectangle_2 = Rectangle(3,88)

print(rectangle_1)
print(rectangle_1 == rectangle_2)
print(rectangle_1 < rectangle_2)

print(rectangle_1 + rectangle_2)

print(len(rectangle_1))
print(len(rectangle_2))







