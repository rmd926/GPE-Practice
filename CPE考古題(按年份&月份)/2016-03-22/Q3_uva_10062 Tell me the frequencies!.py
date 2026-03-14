tc = 0
while True:
	lookup = {}
	target = input()
	
	tc += 1
	if tc > 1:
		print()
		
	for char in target:
		if char not in lookup:
			lookup[char] = 1
		else:
			lookup[char] += 1
	
	for key, value in sorted(lookup.items(), key = lambda x: (x[1], -ord(x[0]))):
		print(ord(key), value)
