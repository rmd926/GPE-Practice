MAX = 20000000
is_prime = bytearray(b'\x01') * (MAX + 1)
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = 0

check = []
for i in range(2, MAX - 1):
    if is_prime[i] and is_prime[i + 2]:
        check.append((i, i + 2))

while True:
    try:
        n = int(input())
    except:
        break

    print(f"({check[n - 1][0]}, {check[n - 1][1]})")
