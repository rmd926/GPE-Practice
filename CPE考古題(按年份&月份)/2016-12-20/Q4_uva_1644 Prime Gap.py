MAX = 1299709
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
	
	if is_prime[target]:
		print(0)
		
	else:
		upper, lower = target, target
		while not is_prime[upper]:
			upper += 1
			
		while not is_prime[lower]:
			lower -= 1
		
		print(upper - lower)
