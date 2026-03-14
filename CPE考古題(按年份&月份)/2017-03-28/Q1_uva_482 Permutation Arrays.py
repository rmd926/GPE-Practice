tc = int(input())

for _ in range(tc):
	space = input()
	perm = list(map(int, input().split()))
	target = list(map(eval, input().split()))
	lookup = {}
	
	for i in range(len(perm)):
		lookup[target[i]] = perm[i]
	
	for key, value in sorted(lookup.items(), key = lambda x: (x[1], x[0])):
		print(key)
		
	tc -= 1
	if tc > 0:
		print()
