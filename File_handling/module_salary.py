import salary_utils

basic = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
pf = float(input("Enter PF deduction: "))
tax = float(input("Enter Tax deduction: "))

gross = salary_utils.calculate_gross(basic, hra, da)
deductions = salary_utils.calculate_deductions(pf, tax)
net = salary_utils.calculate_net(gross, deductions)

print("Gross Salary:", gross)
print("Total Deductions:", deductions)
print("Net Salary:", net)
