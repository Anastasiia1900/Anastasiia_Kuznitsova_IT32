print("Anastasiia Kuznitsova IT-32")

date = int(input("Enter an integer: "))
temp = abs(date)
count = 0
digits_sum = 0
min_digit = 9
max_digit = 0
reversed_num = 0

if temp == 0:
    count = 1
    digits_sum = 0
    min_digit = 9
    max_digit = 0
    reversed_num = 0
else:
    while temp > 0:
        last_digit = temp % 10
        digits_sum += last_digit
        count += 1

        if last_digit < min_digit:
            min_digit = last_digit

        if last_digit > max_digit:
            max_digit = last_digit

        reversed_num = (reversed_num * 10) + last_digit

        temp = temp // 10
if date < 0:
    reversed_num = -reversed_num


print(f"Digits: {count}")
print(f"Sum of digits {digits_sum}")
print(f"Max digit: {max_digit}, min digit: {min_digit}")
print(f"Reversed: {reversed_num}")