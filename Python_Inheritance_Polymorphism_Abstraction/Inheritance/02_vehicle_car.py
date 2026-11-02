class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount_percent):
        return self.price - self.price * discount_percent / 100

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price: Rs.", self.price)


car = Car("Maruti", "Swift", "Petrol", 800000)
car.display()
discount = float(input("Enter discount percentage: "))
if 0 <= discount <= 100:
    print("Discounted Price: Rs.", car.discounted_price(discount))
else:
    print("Invalid discount.")
