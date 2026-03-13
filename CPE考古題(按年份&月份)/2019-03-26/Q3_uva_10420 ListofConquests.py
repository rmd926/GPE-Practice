tc = int(input())
lookup = {}

for _ in range(tc):
	target = list(input().split())
	country = target[0]
	
	if country not in lookup:
		lookup[country] = 1
		
	else:
		lookup[country] += 1
	
for key, value in sorted(lookup.items()):
	print(key, value)
