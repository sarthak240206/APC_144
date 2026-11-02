from abc import ABC, abstractmethod


class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked.")

    def calculate_fee(self):
        return 300


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked.")

    def calculate_fee(self):
        return 800


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment arranged.")

    def calculate_fee(self):
        return 1500


for appointment in [GeneralAppointment(), SpecialistAppointment(), EmergencyAppointment()]:
    appointment.book_appointment()
    print("Fee: Rs.", appointment.calculate_fee())
