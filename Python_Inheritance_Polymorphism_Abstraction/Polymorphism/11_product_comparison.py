class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Phone", 25000)
p2 = Product("Laptop", 60000)
print("Prices equal:", p1 == p2)
print(p1.name, "costs more than", p2.name, ":", p1 > p2)
