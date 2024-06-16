class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height

    def is_square(self):
        return "This is a Square" if self.width == self.height else "This is not Square"

    def is_square(self):
        if self.width == self.height:
            return "This is a Square"
        else:
            return "This is not a Square"
        
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def calculate_diagonal(self):
        abc =  (self.width ** 2 + self.height ** 2) ** 0.5
        return int(abc)

    def calculate_diagonal_str(self):
        abc =  (self.width ** 2 + self.height ** 2) ** 0.5
        abc = f"The Diagonal of this string is {abc} whose width and length is {self.width} & {self.height}"
        return abc

    def to_dict(self):
        dict_is = {"width": self.width *2, "height": self.height *2}
        return dict_is

    @classmethod
    def from_dict(cls, data):
        return cls(data["width"], data["height"])


    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
    
    def __eq__(self, other):
        return(
            (self.width == other.width and self.height == other.height) or 
            (self.width == other.height and self.height == other.width)
        )
    

    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 7)

# print("Rectangle 1:")
# print("Area:", rectangle1.calculate_area())        
# print("Perimeter:", rectangle1.calculate_perimeter())  

# print("Rectangle 2:")
# print("Area:", rectangle2.calculate_area())        
# print("Perimeter:", rectangle2.calculate_perimeter())  

# if rectangle1 < rectangle2:
#     print("Rectangle 1 has a smaller area than Rectangle 2")
# else:
#     print("Rectangle 2 has a smaller area than Rectangle 1")

# if rectangle1 == rectangle2:
#     print("Rectangle 1 and Rectangle 2 are of equal size")
# else:
#     print("Rectangle 1 and Rectangle 2 are of different sizes")

# combined_rectangle = rectangle1 + rectangle2

# print("Combined Rectangle:")
# print("Area:", combined_rectangle.calculate_area())        
# print("Perimeter:", combined_rectangle.calculate_perimeter())  

# print("Rectangle 1:", rectangle1)  
# print("Rectangle 2:", rectangle2)  
# print("Combined Rectangle:", combined_rectangle)  

# rectangle1 = Rectangle(3, 4)
# rectangle2 = Rectangle(10, 5)

# print(rectangle1 == rectangle2)

# print(rectangle1.to_dict())


# rectangle1 = Rectangle(5, 10)

# rectangle_dict = rectangle1.to_dict()
# print(rectangle_dict)  # Output: {'width': 5, 'height': 10}

# new_rectangle = Rectangle.from_dict(rectangle_dict)
# print(new_rectangle.width)   # Output: 5
# print(new_rectangle.height)  # Output: 10

rectangle_data = {"width": 15, "height": 20}
new_rectangle = Rectangle.from_dict(rectangle_data)
print(new_rectangle.width)   # Output: 15
print(new_rectangle.height)  # Output: 20
print(new_rectangle.calculate_diagonal())

print(new_rectangle.calculate_diagonal_str())

