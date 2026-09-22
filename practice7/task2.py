name = "Anastasiia"
surname = "Kuznitsova"
group = "IT-32"
letters = list(surname.lower())

print("Letters:", letters)
print("Length:", len(letters))

print("First letter:", letters[0])
print("Middle letter:", letters[len(letters) // 2])
print("Last letter:", letters[-1])
print("Last letter:", letters[len(letters) - 1])

print("First three letters:", letters[:3])
print("All except first three:", letters[3:])
print("Every second letter:", letters[::2])
print("Reverse:", letters[::-1])
print("Last two letters:", letters[-2:])
print("Part of length 5 starting from position c:", letters[len(letters):len(letters) + 5])

unique = []

for letter in letters:
    if letter not in unique:
        unique.append(letter)

print("Unique letters:", unique)

repeated = False

for letter in unique:
    count = letters.count(letter)
    if count > 1:
        print(f"Letter '{letter}' repeats {count} times")
        repeated = True

if not repeated:
    print("No repeated letters")

print("Alphabetical order:", sorted(letters))