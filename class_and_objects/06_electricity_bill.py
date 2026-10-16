class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        # Sample slab rates; replace with your local electricity provider's rates.
        units = self.units
        if units <= 100:
            return units * 3.0
        elif units <= 200:
            return 100 * 3.0 + (units - 100) * 5.0
        else:
            return 100 * 3.0 + 100 * 5.0 + (units - 200) * 7.0

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Bill Amount: ₹", self.calculate_bill())


bill = ElectricityBill(1001, "Priya", 250)
bill.display()
