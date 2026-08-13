n=int(input("Number of employees: "))
salaries=[]
for i in range(n):
    salaries.append(float(input(f"Salary {i+1}: ")))
avg=sum(salaries)/len(salaries)
print("Highest salary:",max(salaries))
print("Lowest salary:",min(salaries))
print("Average salary:",avg)
print("Above 50000:",sum(x>50000 for x in salaries))
print("Below 30000:",sum(x<30000 for x in salaries))
