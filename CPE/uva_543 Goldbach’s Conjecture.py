# 建表，然後使用sieve method處理primes
MAX = 10 ** 6
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5+1)):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False

while True:
    target = int(input())
    if target == 0:
        break

    for i in range(2, target+1):
        low = i
        high = (target-i)

        # 因為是要求high-low是maximum，所以從low去往上加只抓第一個符合的就是答案
        if is_prime[low] and is_prime[high]:
            break 
    
    print(f"{target} = {low} + {high}")