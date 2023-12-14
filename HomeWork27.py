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
        return f"{self.first_name} {self.last_name}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.items:
            self.items[item] += cnt
        else:
            self.items[item] = cnt

    def calculate_total(self):
        total = sum(item.price * cnt for item, cnt in self.items.items())
        return total

    def __str__(self):
        order_info = f"User: {self.user}\nItems:\n"
        for item, cnt in self.items.items():
            order_info += f"{item.name}: {cnt} pcs.\n"
        order_info += f"Total: {self.calculate_total()}"
        return order_info
