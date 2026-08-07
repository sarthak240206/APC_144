s = input("Enter a string: ")
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

if frequency:
    most = max(frequency, key=frequency.get)
    print("Most frequent character:", repr(most))
    print("Frequency:", frequency[most])
else:
    print("String is empty")
