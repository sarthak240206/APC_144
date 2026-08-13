temps=[]
for i in range(30):
    temps.append(float(input(f"Temperature of day {i+1}: ")))
avg=sum(temps)/30
print("Hottest temperature:",max(temps))
print("Coldest temperature:",min(temps))
print("Average temperature:",avg)
print("Days above average:",sum(x>avg for x in temps))
print("Days below average:",sum(x<avg for x in temps))
