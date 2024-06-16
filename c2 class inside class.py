class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, My Attributes, Age: {self.age}")

    class Address:
        def __init__(self, street, city):
            self.street = street
            self.city = city

        def display_address(self):
            print(f"Address: {self.street}, {self.city}")




person1 = Person("Alice", 30)
person1.display_info()

address1 = Person.Address("123 Main St", "Cityville")
address1.display_address()
