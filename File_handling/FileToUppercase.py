source_file = input("Enter source file name: ")
output_file = input("Enter destination file name: ")

try:
    with open(source_file, "r") as src, open(output_file, "w") as dest:
        dest.write(src.read().upper())
    print("Content converted to uppercase and saved successfully.")
except FileNotFoundError:
    print("File not found.")
