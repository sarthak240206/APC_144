# Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
# Program: Gross Salary

def gross_salary(basic):
    hra = basic * 0.10
    da = basic * 0.15
    return basic + hra + da

print(gross_salary(50000))
