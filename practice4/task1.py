print("Anastasiia Kuznitsova IT-32")

d = 19
c = 10
count = 0
sum_num = 0
product = 1
even = 0
odd = 0

print(f"Numbers from {d} to 31:", end=" ")

for i in range(d, 32):
    print(i, end=" ")
    count += 1
    sum_num += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print()
print(f"Count: {count}")
print(f"Sum: {sum_num}")
print(f"Product: {product}")
print(f"Average: {sum_num / count}")
print(f"Even: {even}, odd: {odd}")

print("Countdown: ", end=" ")
for i in range(c, 0, -1):
    print(i, end=" ")
print()

#while version
count = 0
sum_num = 0
product = 1
even = 0
odd = 0

print()
print(f"Numbers from {d} to 31:", end=" ")
i = d
while i <= 31:
    print(i, end=" ")
    count += 1
    sum_num += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

print()
print(f"Countdown: {count}")
print(f"Sum: {sum_num}")
print(f"Product: {product}")
print(f"Average: {sum_num / count}")
print(f"Even: {even}, odd: {odd}")

print("Countdown: ", end=" ")
i = c
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
