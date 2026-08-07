s = input("Enter a string: ")
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

if len(items) >= 2:
    print("Second most frequent character:", repr(items[1][0]))
    print("Frequency:", items[1][1])
else:
    print("Second most frequent character does not exist")
