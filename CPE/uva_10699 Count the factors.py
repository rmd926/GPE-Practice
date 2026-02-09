import sys

def count_unique_prime_factors(n: int):
    record = set()
    p = 2 # the first prime
    while p ** 2 < n:
        while n % p == 0:
            record.add(p)
            n //= p
        p += 1
    if n > 1: # the prime that is bigger than sqrt(n)
        record.add(n)
    return len(record)

data = sys.stdin.read().split() # cuz fxcking terrible testing case so we can not use while True: and n = int(input())
for target in data:
    n = int(target)
    if n == 0:
        break

    print(f"{n} : {count_unique_prime_factors(n)}")
