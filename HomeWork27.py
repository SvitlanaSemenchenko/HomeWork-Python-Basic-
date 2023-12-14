class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Purchase:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items.items())
        return total

    def __str__(self):
        order_info = f"User: {self.customer}\nItems:\n"
        for item, quantity in self.items.items():
            order_info += f"{item.name}: {quantity} pcs.\n"
        order_info += f"Total: {self.calculate_total()}"
        return order_info
