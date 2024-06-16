class Person:
      def __init__(self, fname, lname = "Not Present"):
        self.firstname = fname
        self.lastname = lname

      def printname(self):
        print(self.firstname, self.lastname,"My name is wwe")


class Student(Person):
    def study(self):
        print("I am studying")


s1 = Student("Alice")
s1.printname()
s1.study()

# Creating another Student instance with both first and last name
s2 = Student("Bob", "Johnson")
s2.printname()
s2.study()


