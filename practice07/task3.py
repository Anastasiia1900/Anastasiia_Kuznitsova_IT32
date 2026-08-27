num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
operation_symbol = input("Enter a operation symbol (+, -, *, /, //, %, **): ")

if operation_symbol == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.4f}")
elif operation_symbol == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.4f}")
elif operation_symbol == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.4f}")
elif operation_symbol == "/":
    if num2 == 0:
        print("cannot be divided by 0")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.4f}")
elif operation_symbol == "//":
    if num2 == 0:
        print("cannot be divided by 0")
    else:
        result = num1 // num2
        print(f"{num1} // {num2} = {result:.4f}")
elif operation_symbol == "%":
    if num2 == 0:
        print("cannot be divided by 0")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result:.4f}")
elif operation_symbol == "**":
    if num2 == 0:
        print("cannot be divided by 0")
    else:
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result:.4f}")
else:
    print("Invalid operation")
