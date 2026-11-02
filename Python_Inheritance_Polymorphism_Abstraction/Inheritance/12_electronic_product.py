class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount_percent):
        return self.price - self.price * discount_percent / 100

    def display(self, discount_percent):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Original Price: Rs.", self.price)
        print("Final Price: Rs.", round(self.final_price(discount_percent), 2))


product = ElectronicProduct(101, "Laptop", 60000, "Dell", "2 years")
product.display(10)
