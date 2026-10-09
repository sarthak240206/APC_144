filename = input("Enter file name: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

try:
    with open(filename, "r") as file:
        text = file.read()
        for ch in text:
            if ch.isalpha():
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        print("Vowels:", vowel_count)
        print("Consonants:", consonant_count)
except FileNotFoundError:
    print("File not found.")
