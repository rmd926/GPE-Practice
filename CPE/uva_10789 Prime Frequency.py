MAX = 2001
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, MAX+1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False


tc = int(input())
for t in range(tc):
	target = input()
	lookup = {}
	for char in target:
		if char not in lookup:
			lookup[char] = 1
		else:
			lookup[char] += 1
	ans = ""
	for key, value in sorted(lookup.items()):
		if is_prime[value]:
			ans += key
	
	if len(ans) > 0:
		print(f"Case {t+1}: {ans}")
	else:
		print(f"Case {t+1}: empty")
