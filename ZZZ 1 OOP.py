item1 = 'Phone'
item1_price = 100
item1_quantity = 5.0
item_price_total = item1_price*item1_quantity


print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item_price_total))

class Item:
    pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5




print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

