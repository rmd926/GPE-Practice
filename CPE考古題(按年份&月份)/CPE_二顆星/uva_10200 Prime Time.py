MAX = 10000
prime_list = [0] * (MAX+1)

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

for i in range(MAX + 1): # create tables
	if is_prime(i**2 + i + 41):
		prime_list[i] = 1
	else:
		prime_list[i] = 0
	
while True:
	try:
		a, b = map(int, input().split())
	except:
		break
	
	prime_times = sum(prime_list[a:b+1])
	
	ans = 100 * prime_times / (b-a+1)
	print(f"{ans:.2f}")
