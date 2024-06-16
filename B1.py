class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)


print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

 


