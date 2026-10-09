file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    identical = True
    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        l1 = lines1[i] if i < len(lines1) else None
        l2 = lines2[i] if i < len(lines2) else None
        if l1 != l2:
            print(f"Files differ at line {i + 1}.")
            print("File 1:", repr(l1))
            print("File 2:", repr(l2))
            identical = False
            break

    if identical:
        print("Files are identical.")
except FileNotFoundError:
    print("One or both files not found.")
