import os
import sys

sys.path.insert(0, os.path.abspath("hospital_management"))

from patients.manage import register_patient
from doctors.manage import assign_doctor
from medical_records.records import add_medical_record
from billing.invoice import calculate_bill

patient = register_patient("P001", "Kavita Reddy", 32)
doctor = assign_doctor("D101", "Dr. Mehta", "Cardiology")
record = add_medical_record("P001", "D101", "Regular checkup - normal vitals")
bill = calculate_bill("P001", 1500, 500)

print("Patient:", patient)
print("Doctor:", doctor)
print("Medical Record:", record)
print("Total Bill:", bill)
