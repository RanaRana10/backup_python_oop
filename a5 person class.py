class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self):
        return f"Hi, I'm {self.name}, and I'm {self.age} years old."

    def make_friend(self, other_person):
        self.friends.append(other_person)
        other_person.friends.append(self)

    def list_friends(self):
        friend_names = [friend.name for friend in self.friends]
        return f"{self.name}'s friends: {', '.join(friend_names)}."

# Creating two Person objects
alice = Person("Alice", 30)
bob = Person("Bob", 25)

# Introducing themselves
print(alice.introduce())
print(bob.introduce())

# Making them friends
alice.make_friend(bob)

# Listing friends
print(alice.list_friends())
print(bob.list_friends())
