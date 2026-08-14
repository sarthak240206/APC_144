emp_id = (1,78,56,3,98,100,101,32,2,19,48)
print("The employee IDs are:", emp_id)
target = int(input("Enter an employee ID to check index of it: "))
for i in range(len(emp_id)):
    if emp_id[i] == target:
        print("The index of the employee ID is:", i)