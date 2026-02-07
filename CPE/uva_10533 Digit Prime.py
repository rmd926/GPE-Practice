MAXN = 10**6

is_prime = [True] * (MAXN+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, MAXN+1, i):
            is_prime[j] = False

def digit_sum(n):
	result = 0
	while n > 0:
		result += n % 10
		n //= 10
		
	return result

tc = int(input())
for _ in range(tc):
	low, high = map(int, input().split())
	count = 0
	for num in range(low, high+1):
		if is_prime[num] and is_prime[digit_sum(num)]:
			count += 1
	print(count)
