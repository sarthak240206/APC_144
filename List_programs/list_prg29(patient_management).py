names=[]
ages=[]
while True:
    print("\n1.Add 2.Delete 3.Search 4.Display 5.Count 6.Exit")
    c=input("Choice: ")
    if c=="1":
        names.append(input("Name: "))
        ages.append(int(input("Age: ")))
    elif c=="2":
        x=input("Patient name: ")
        if x in names:
            i=names.index(x); names.pop(i); ages.pop(i)
        else: print("Patient not found")
    elif c=="3":
        x=input("Patient name: ")
        if x in names:
            i=names.index(x); print("Name:",names[i],"Age:",ages[i])
        else: print("Patient not found")
    elif c=="4":
        for i in range(len(names)): print("Name:",names[i],"Age:",ages[i])
    elif c=="5": print("Total patients:",len(names))
    elif c=="6": break
