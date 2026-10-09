filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

try:
    with open(filename, "r") as file:
        occurrences = 0
        found_lines = []
        for line_num, line in enumerate(file, start=1):
            count = line.split().count(search_word)
            if count > 0:
                occurrences += count
                found_lines.append(line_num)
        print("Number of occurrences:", occurrences)
        print("Found in line numbers:", found_lines)
except FileNotFoundError:
    print("File not found.")
