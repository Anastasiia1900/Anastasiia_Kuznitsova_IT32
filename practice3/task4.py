score = int(input("Enter your score: "))
missed = int(input("Enter your missed: "))

if score < 0 or score > 100:
    print("Your score must be between 0 and 100")

else:
    if score <= 59:
        grade = "F"
    elif score <= 63:
        grade = "E"
    elif score <= 73:
        grade = "D"
    elif score <= 81:
        grade = "C"
    elif score <= 89:
        grade = "B"
    else:
        grade = "A"

    if missed > 16 * 0.3:
        print("Warning: you are not allowed to take the test")
        result = "failed"
    elif score >= 60:
        result = "passed"
    else:
        result = "failed"

    print (f"Your score is {score}, grade is {grade}, and result is {result}")
