import sys

def get_prime(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    prime_list = []
    for i in range(2, max_n + 1):
        if is_prime[i] == True:
            prime_list.append(i)
        if i*i <= max_n:
            for j in range(i*i, max_n+1, i):
                is_prime[j] = False
    
    return prime_list

MAX_N = 1_000_000
prime_list = get_prime(MAX_N)

data = sys.stdin.read().split()  # ← 最小改動：用這個取代 while True 的 input()

for s in data:
    target = int(s)
    if target == 0:
        break

    temp = target
    count = 0

    for p in prime_list:
        if p*p > temp:
            break
        if temp % p == 0:
            count += 1
            while temp % p == 0:
                temp //= p
    
    if temp > 1:
        count += 1
    
    print(f"{target} : {count}")
