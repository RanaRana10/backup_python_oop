import inspect



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
    
rec = Rectangle(3,3)
sq = Square(5)
print(inspect.getmembers(rec, predicate=inspect.ismethod))  
print(inspect.getmembers(sq, predicate=inspect.ismethod))  




