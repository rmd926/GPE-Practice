MAX = 2 ** 15
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, MAX+1, i):
            is_prime[j] = False

primes_list = []
for i in range(2, MAX+1):
    if is_prime[i]:
        primes_list.append(i)

while True:
    try:
        target = int(input())
    except:
        break
    
    if target == 0:
        break

    count = 0

    for p in primes_list:
        if p > target // 2:
            break
        else:
            if is_prime[target-p]:
                count += 1

    print(count)
