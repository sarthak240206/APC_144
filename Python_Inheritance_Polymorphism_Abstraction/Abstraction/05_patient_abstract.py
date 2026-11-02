from abc import ABC, abstractmethod


class Patient(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        return "Hospital admission and treatment"


class OutPatient(Patient):
    def calculate_bill(self):
        return 800

    def treatment(self):
        return "Consultation and medicine"


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        return "Emergency treatment"


for patient in [InPatient("Amit"), OutPatient("Neha"), EmergencyPatient("Rahul")]:
    print(patient.name, "-", patient.treatment(), "- Bill: Rs.", patient.calculate_bill())
