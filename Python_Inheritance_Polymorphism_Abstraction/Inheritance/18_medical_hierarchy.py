class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id


class Surgeon(Doctor):
    def perform_surgery(self):
        print(self.name, "is performing surgery.")


class MedicalResearcher(Doctor):
    def __init__(self, name, age, specialization, research_area):
        super().__init__(name, age, specialization)
        self.research_area = research_area


class SurgeonResearcher(Surgeon, MedicalResearcher):
    def __init__(self, name, age, specialization, research_area):
        Doctor.__init__(self, name, age, specialization)
        self.research_area = research_area

    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Research Area:", self.research_area)


doctor = SurgeonResearcher("Dr. Patil", 40, "Cardiology", "Heart Disease")
doctor.display()
doctor.perform_surgery()
patient = Patient("Amit", 30, "P101")
patient.display()
print("Patient ID:", patient.patient_id)
