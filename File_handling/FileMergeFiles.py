file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
output_file = input("Enter destination file name: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as out:
        out.write(f1.read())
        out.write("\n")
        out.write(f2.read())
    print("Files merged successfully into", output_file)
except FileNotFoundError:
    print("One or both input files not found.")
