print("Anastasiia Kuznitsova IT-32")

attempts = 0

while True:
    score = int(input("Enter your score(0-100): "))
    attempts += 1

    if score > 100:
        print('Score is too big, max is 100')
    elif score < 0:
        print('Score cannot be negative')
    else:
        break

if score >= 90:
    grade = "A"
elif score >= 82:
    grade = "B"
elif score >= 74:
    grade = "C"
elif score >= 64:
    grade = "D"
elif score >= 60:
    grade = "E"
else:
    grade = "F"

print(f'Accepted after {attempts} attempts')
print(f'Grade: {grade}')