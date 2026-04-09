MAX = 1299709
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, MAX+1, i):
            is_prime[j] = False

while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break
    
    if is_prime[n]:
        print(0)

    else:
        low, high = n, n
        while not is_prime[low]:
            low -= 1
        
        while not is_prime[high]:
            high += 1
        
        print(high - low)
