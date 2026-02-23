MAX = 10 **6
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
	
	for i in range(2, target//2 + 1):
		low, high = i, target-i
		if is_prime[low] and is_prime[high]:
			break
			
	print(f"{target} = {low} + {high}")
