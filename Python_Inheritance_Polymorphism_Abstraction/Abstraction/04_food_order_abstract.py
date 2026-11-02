from abc import ABC, abstractmethod


class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def delivery_charge(self):
        return 0

    def calculate_bill(self):
        return self.amount + self.delivery_charge()


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def delivery_charge(self):
        return 50

    def calculate_bill(self):
        return self.amount + self.delivery_charge()


for order in [RestaurantOrder(500), HomeDeliveryOrder(500)]:
    print(order.__class__.__name__, "Bill: Rs.", order.calculate_bill())
