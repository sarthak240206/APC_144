class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


class SportsCar(Car):
    def __init__(self, brand, model, doors, top_speed):
        super().__init__(brand, model, doors)
        self.top_speed = top_speed

    def display(self):
        super().display()
        print("Doors:", self.doors)
        print("Top Speed:", self.top_speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, engine_cc, battery_range):
        super().__init__(brand, model, engine_cc)
        self.battery_range = battery_range

    def display(self):
        super().display()
        print("Engine/Equivalent CC:", self.engine_cc)
        print("Battery Range:", self.battery_range, "km")


SportsCar("Porsche", "911", 2, 310).display()
print()
ElectricBike("Ather", "450X", 0, 120).display()
