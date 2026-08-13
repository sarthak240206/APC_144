marks=[]
for i in range(20):
    marks.append(float(input(f"Marks of student {i+1}: ")))
avg=sum(marks)/20
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))
print("Average marks:",avg)
print("Students above average:",sum(x>avg for x in marks))
print("Students below average:",sum(x<avg for x in marks))
