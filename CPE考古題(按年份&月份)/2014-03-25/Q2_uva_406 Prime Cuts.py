MAX = 1000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False

while True:
	N, C = map(int, input().split())
	ans = [1]
	
	for num in range(2, N+1):
		if is_prime[num]:
			ans.append(num)
	
	n = len(ans)
	mid = n // 2
	
	if n % 2 == 0:
		if 2 * C >= n:
			output = ans
		else:
			output = ans[mid - C: mid + C]
	
	else:	
		if 2 * C >= n:
			output = ans
		else:
			output = ans[mid - C + 1: mid + C]
	
	print(f"{N} {C}: ",end = "")
	print(*output)
	print()
