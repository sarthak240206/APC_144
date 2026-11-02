from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return 50 + distance * 12


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 8


distance = float(input("Enter distance in km: "))
for transport in [Bus(), Train(), Taxi(), Flight()]:
    print(transport.__class__.__name__, "Fare: Rs.", round(transport.calculate_fare(distance), 2))
