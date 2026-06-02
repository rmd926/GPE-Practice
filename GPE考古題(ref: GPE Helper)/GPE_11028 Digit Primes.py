MAX = 1000000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, MAX+1, i):
            is_prime[j] = False

def digit_sum(num: int):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    
    return total

prefix = [0] * (MAX+1)
count = 0

for num in range(1, MAX+1):
    if is_prime[num] and is_prime[digit_sum(num)]:
        count += 1
        
    prefix[num] = count

tc = int(input())
for _ in range(tc):
    try:
        n, m = map(int, input().split())
    except:
        break
    
    print(prefix[m] - prefix[n-1])
