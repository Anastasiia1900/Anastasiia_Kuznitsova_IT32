name = input("What is your full name?")

if name:
    name = name
else:
    print("Name not entered; you are now Anonymous.")
    name = "Anonymous"

age = int(input("How old are you?"))

if age <0:
    category = "invalid value"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"
print(f"Hello {name}, your category is {category}")