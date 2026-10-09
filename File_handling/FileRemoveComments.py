source_file = input("Enter Python source file name: ")
output_file = input("Enter output file name: ")

try:
    with open(source_file, "r") as src, open(output_file, "w") as out:
        for line in src:
            stripped = line.lstrip()
            if not stripped.startswith("#"):
                out.write(line)
    print("Comments removed successfully.")
except FileNotFoundError:
    print("File not found.")
