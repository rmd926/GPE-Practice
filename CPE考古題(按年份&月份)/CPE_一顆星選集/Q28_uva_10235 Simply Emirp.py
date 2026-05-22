MAX = 10 ** 6
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False

while True:
	target = input()
	if target == target[::-1] and is_prime[int(target)]:
		print(f"{target} is prime.")
	elif is_prime[int(target)] and not is_prime[int(target[::-1])]:
		print(f"{target} is prime.")
		
	elif not is_prime[int(target)]:
		print(f"{target} is not prime.")
	
	elif target != target[::-1] and is_prime[int(target)] and is_prime[int(target[::-1])]:
		print(f"{target} is emirp.")

# 2026.05.23 二刷 要注意條件判斷式，例如11這種case要判斷成prime而不是emirp
