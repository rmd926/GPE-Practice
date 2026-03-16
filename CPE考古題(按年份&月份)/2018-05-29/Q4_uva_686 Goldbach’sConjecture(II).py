MAX = 2 ** 15
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False

while True:
	target = int(input())
	if target == 0:
		break
	count = 0
	
	for i in range(2, target//2+1):
		if i % 2 == 1 and is_prime[i] and is_prime[target-i]:
			count += 1
			
	print(count)
