MAX = 10000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i**2, MAX+1, i):
            is_prime[j] = False

prime_list = []
for num in range(2, MAX+1):
    if is_prime[num]:
        prime_list.append(num)

while True:
    try:
        target = int(input())
    except:
        break

    if target == 0:
        break
    
    left, right = 0, 0
    total = 0
    count = 0

    while True:
        if total == target:
            count += 1

        if total >= target:
            total -= prime_list[left]
            left += 1
        
        else:
            if right == len(prime_list):
                break
            total += prime_list[right]
            right += 1
    
    print(count)
