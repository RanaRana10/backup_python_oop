
'''
This is from 
https://realpython.com/python-super/
'''

import inspect


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(2*length, 2*length)

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


s1 = Square(4)
c1 = Cube(4)
print(s1.perimeter())
print(c1.perimeter())
c1 = Cube(sid)

