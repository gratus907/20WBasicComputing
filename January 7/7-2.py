def is_prime(n):
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

primes = []
max_number = int(input())
for i in range(3, max_number, 2):
    if is_prime(i):
        primes.append(i)

print(primes)