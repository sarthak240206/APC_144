import re

text = input("Enter invoice text: ")

invoice_numbers = re.findall(r"INV-\\d+", text)
dates = re.findall(r"\\b\\d{2}-\\d{2}-\\d{4}\\b", text)
amounts = re.findall(r"₹\\s?[\\d,]+(?:\\.\\d{2})?", text)

print("Invoice numbers:", invoice_numbers)
print("Dates:", dates)
print("Monetary amounts:", amounts)
