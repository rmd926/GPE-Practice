tc = int(input())
lookup = {}
for _ in range(tc):
	line = input().upper()
	for char in line:
		if "A" <= char <= "Z":
			if char not in lookup:
				lookup[char] = 1
			else:
				lookup[char] += 1

for key, value in sorted(lookup.items(), key = lambda x: (-x[1], x[0])):
	print(key, value)
