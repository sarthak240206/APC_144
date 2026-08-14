
numbers = (10, 20, 10, 30, 20, 10, 40, 30, 20)

frequency = {}

for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Tuple:", numbers)
print("Frequency of each element:")

for item, count in frequency.items():
    print(item, ":", count)