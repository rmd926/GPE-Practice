tc = int(input())

for t in range(tc):
	lookup = {}
	print(f"Case #{t+1}:")
	
	for i in range(10):
		target = input().split()
		url = target[0]
		score = int(target[1])
		
		lookup[url] = score
		max_score = max(lookup.values())
	
	for key, value in lookup.items():
		if value == max_score:
			print(key)
