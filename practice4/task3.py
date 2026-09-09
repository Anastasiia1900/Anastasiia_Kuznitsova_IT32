print("Anastasiia Kuznitsova IT-32")

name = "Anastasiia"
surname = "Kuznitsova"
full_name = name + " " + surname
vowels = "aeiou"
vowels_count = 0
consonants_count = 0

for char in full_name:
    char_lower = char.lower()

    if char_lower.isalpha():
        if char_lower in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print(full_name)
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")
print(f"Total letters: {consonants_count}")
