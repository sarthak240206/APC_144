numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print("Two numbers are:", complement, "and", num)
        break

    seen[num] = True
