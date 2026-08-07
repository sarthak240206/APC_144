s = input("Enter a string: ")

if not s:
    print("Compressed string:", s)
else:
    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    compressed += s[-1] + str(count)

    if len(compressed) < len(s):
        print("Compressed string:", compressed)
    else:
        print("Original string:", s)
