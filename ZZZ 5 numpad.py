class Item:
    def __init__(self, name: str, price: float, quantity=0):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or not isinstance(quantity, int):
            raise ValueError("Invalid item data. Name should be a string, price should be a number, and quantity should be an integer.")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity should be non-negative values.")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)  # This will work
item2 = Item("Laptop", 1000, 3)  # This will work

# The following line will raise a ValueError and stop the code from executing.
itemq = Item("Invalid Item", "abc", 3)
