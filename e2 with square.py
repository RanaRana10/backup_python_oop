'''
This i am learnign from 
https://realpython.com/python-super/
'''





class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rec(self):
        return self.length * self.width

    def perimeter_rec(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area_cu(self):
        face_area = super().area()
        return face_area * 6

    def volume_cu(self):
        face_area = super().area()
        return face_area * self.length

import inspect
cu = Cube(6)
print(inspect.getmembers(cu, predicate=inspect.ismethod))  
print(cu.area_rec())
print(cu.perimeter_rec())
cu1 = Rectangle()

# rec = Rectangle(3,3)
# sq = Square(5)
# print(inspect.getmembers(rec, predicate=inspect.ismethod))  
# print(inspect.getmembers(sq, predicate=inspect.ismethod))  

