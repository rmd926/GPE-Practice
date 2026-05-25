tc = int(input())
for t in range(tc):
	lookup = {}
	for _ in range(10):
		link, score = map(str, input().split())
		lookup[link] = int(score)
	
	print(f"Case #{t+1}:")
	max_score = max(lookup.values())
	
	for key, value in lookup.items():
		if value == max_score:
			print(key)

# 2026.05.26 二刷
