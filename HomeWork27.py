class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname} {self.numberphone}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = sum(item.price * cnt for item, cnt in self.products.items())
        return total

    def __str__(self):
        order_info = f"User: {self.user}\nItems:\n"
        for item, cnt in self.products.items():
            order_info += f"{item.name}: {cnt} pcs.\n"
        order_info += f"Total: {self.get_total()}"
        return order_info

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
Total: 60
"""

assert isinstance(cart.user, User) is True, 'Instance of the User class'
assert cart.calculate_total() == 60, "Total should be 60"
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
Total: 40
"""

assert cart.calculate_total() == 40, "Total should be 40"
