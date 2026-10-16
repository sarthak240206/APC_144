class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price: ₹", self.price)

    def price_after_discount(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


phone = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)
phone.display_specs()
print("Price after 10% discount: ₹", phone.price_after_discount(10))
