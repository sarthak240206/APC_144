filename = input("Enter source file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
output_filename = input("Enter output file name (press enter for same file): ")

if not output_filename:
    output_filename = filename

try:
    with open(filename, "r") as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(output_filename, "w") as file:
        file.write(content)
    print("Replacement complete. Saved to", output_filename)
except FileNotFoundError:
    print("File not found.")
