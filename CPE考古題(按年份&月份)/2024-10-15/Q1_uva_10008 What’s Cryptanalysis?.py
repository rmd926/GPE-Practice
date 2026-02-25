lookup = {}
tc = int(input())
for _ in range(tc):
	target = input()
	for char in target:
		if "A" <= char <= "Z" or "a" <= char <= "z":
			char = char.upper()
			
			if char not in lookup:
				lookup[char] = 1
			else:
				lookup[char] += 1

for key, value in sorted(lookup.items(), key = lambda x: (-x[1], x[0])):
	print(key, value)
