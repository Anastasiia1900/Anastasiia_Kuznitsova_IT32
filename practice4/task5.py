d = 19
c = 10
n = d * c

print(f"n = {d} * {c} = {n}")

divisors = []
divisors_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisors_sum += i

divisors_count = len(divisors)
divisors_str = " ".join(map(str, divisors))
print(f"Divisors: {divisors_str}")
print(f"Divisors count: {divisors_count}, sum: {divisors_sum}")


if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

prime_numbers = []

for num in range(2, n + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)

primes_str = " ".join(map(str, prime_numbers))
print(f"Primes up to {n}: {primes_str}")
print(f"Primes count: {len(prime_numbers)}")
