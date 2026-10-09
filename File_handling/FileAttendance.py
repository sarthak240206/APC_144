records = [
    "Amit,45,50\n",
    "Priya,30,50\n",
    "Rahul,48,50\n",
    "Sneha,32,50\n"
]

with open("attendance.txt", "w") as f:
    f.writelines(records)

print("Attendance Below 75%:")
with open("attendance.txt", "r") as f:
    for line in f:
        name, attended, total = line.strip().split(",")
        percentage = (int(attended) / int(total)) * 100
        print(f"{name}: {percentage:.2f}%")
        if percentage < 75:
            print(f"  -> {name} has attendance below 75% ({percentage:.2f}%)")
