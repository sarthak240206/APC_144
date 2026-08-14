student = ((144,"Sarthak",90),(151,"Manjunath",80),(152,"Balaji",70),(145,"Vaishavi",60))
print("The student details are:", student)
for i in range(len(student)):
    for j in range(len(student[i])):
        if j == 0:
            print("Roll no of student is:", student[i][j], end=" ")
        elif j == 1:
            print("Name of student is:", student[i][j], end=" ")
        else:
            print("Marks of student is:", student[i][j], end=" ")