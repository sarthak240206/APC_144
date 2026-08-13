students=[]
while True:
    print("\n1.Total 2.Search 3.Add 4.Remove 5.Display 6.Exit")
    c=input("Choice: ")
    if c=="1": print("Total students:",len(students))
    elif c=="2":
        x=input("Student name: ")
        print(x,"is present" if x in students else x+" is absent")
    elif c=="3": students.append(input("Student name: "))
    elif c=="4":
        x=input("Absent student: ")
        if x in students: students.remove(x)
        else: print("Student not found")
    elif c=="5": print(students)
    elif c=="6": break
