lookup = {}
tc = int(input())
for _ in range(tc):
	target = input().upper()
	
	for ch in target:
		if ch.isalpha():
			if ch not in lookup:
				lookup[ch] = 1
			else:
				lookup[ch] += 1
	
for key, value in sorted(lookup.items(), key = lambda x: (-x[1], x[0])):
	print(key, value)

# 2026.05.21 二刷
