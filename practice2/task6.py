#task6, Kuznitsova, IT-32
name = input("Enter your name: ")
age = int(input("Enter your age: "))

age_range = 18 <= age <= 60
even = age % 2 == 0
both = age_range and even
one = age_range or even

print("Name:", name)
print("Age from 18 to 60:", age_range)
print("Age is even:", even)
print("Both conditions are true:", both)
print("At least one condition is true:", one)

years_left = 60 - age
print("Years left until 60:", years_left)