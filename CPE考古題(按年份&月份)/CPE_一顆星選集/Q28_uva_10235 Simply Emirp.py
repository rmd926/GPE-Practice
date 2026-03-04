MAX = 10 ** 6
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False

while True:
	target = input()
	if int(target) == int(target[::-1]) and is_prime[int(target)] and is_prime[int(target[::-1])]:
		print(f"{target} is prime.")
		
	elif is_prime[int(target)] and is_prime[int(target[::-1])]:
		print(f"{target} is emirp.")
		
	elif is_prime[int(target)] and not is_prime[int(target[::-1])]:
		print(f"{target} is prime.")
		
	elif not is_prime[int(target)]:
		print(f"{target} is not prime.")
