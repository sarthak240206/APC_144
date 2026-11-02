class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key or push button.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start or kick.")


class Bus(Vehicle):
    def start(self):
        print("Bus engine starts.")


for vehicle in [Car(), Bike(), Bus()]:
    vehicle.start()
