full_name = "  aNASTASIIA   kUZnitsova   oLEKSANDRIVNA  "

words = full_name.split()
full_name = " ".join(words).title()
print("Full name:", full_name)
print("Length:", len(full_name))

name, surname, patronymic = full_name.split()

print("First character of surname:", surname[0])
print("Last character of surname:", surname[-1])
print("Surname backwards:", surname[::-1])
print("Formatted name:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Initials:", f"{name[0]}{surname[0]}{patronymic[0]}")

vowels = "aeiou"
vowels_count = sum(1 for char in full_name.lower() if char in vowels)
print("Number of vowels:", vowels_count)

group = "IT-32"
dash = group.find("-")
print("Part before dash:", group[:dash])
print("Part after dash:", group[dash + 1:])
print("Part after dash is a number:", group[dash + 1:].isdigit())

login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"
print("Login:", login)
print("Email:", email)