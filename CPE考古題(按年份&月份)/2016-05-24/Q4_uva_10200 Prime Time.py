def is_prime(n):
	if n <= 1:
		return False
	
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False

	return True
		

while True:
	low, high = map(int, input().split())
	count = 0
	for num in range(low, high+1):
		if is_prime(num**2+num+41):
			count += 1
	
	ans = 100 * count / (high-low+1)		
	print(f"{ans:.2f}")
