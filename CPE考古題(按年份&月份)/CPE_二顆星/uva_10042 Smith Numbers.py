MAX = 100000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

prime = []
for i in range(2, MAX + 1):
    if is_prime[i]:
        prime.append(i)

tc = int(input())
for _ in range(tc):
	n = int(input())
	target = n + 1
	
	while True:
		temp = target
		sum1 = 0
		for ch in str(target):
			sum1 += int(ch)
		
		factors = []
		
		for p in prime:
			if p * p > temp:
				break
			
			while temp % p == 0:
				factors.append(p)
				temp //= p
		
		if temp > 1:
			factors.append(temp)
		
		if len(factors) == 1 and factors[0] == target:
			target += 1
			continue
		
		sum2 = 0
		for num in factors:
			for ch in str(num):
				sum2 += int(ch)
		
		if sum1 == sum2:
			print(target)
			break
		
		target += 1
