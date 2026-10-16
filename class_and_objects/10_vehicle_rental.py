class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, available=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = available

    def rent(self):
        if self.available:
            self.available = False
            print(self.model, "has been rented.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.available = True
        print(self.model, "has been returned.")

    def rental_charges(self, days):
        if days <= 0:
            return 0
        return self.rental_rate * days


vehicle = Vehicle("MH12AB1234", "Hatchback", 1500)
vehicle.rent()
print("Charges for 3 days: ₹", vehicle.rental_charges(3))
vehicle.return_vehicle()
