from itertools import permutations

MAX = 10 ** 7
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False

tc = int(input())
for _ in range(tc):
	target = input()
	temp = set()
	count = 0
	
	for i in range(1, len(target)+1):
		for p in permutations(target, i):
			temp.add(int("".join(p)))
	
	for num in temp:
		if is_prime[num]:
			count += 1

	print(count)
