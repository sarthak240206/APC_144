class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee: ₹", self.consultation_fee)

    def total_bill(self, medicine_charges=0, test_charges=0):
        return self.consultation_fee + medicine_charges + test_charges


patient = Patient(1, "Ravi", 45, "Fever", 500)
patient.display_info()
print("Total Bill: ₹", patient.total_bill(medicine_charges=300, test_charges=700))
