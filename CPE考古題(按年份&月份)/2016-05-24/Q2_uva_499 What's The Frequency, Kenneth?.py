while True:
	lookup = {}
	target = list(input())
	for char in target:
		if char == " ":
			continue
		elif char.isalpha():
			if char not in lookup:
				lookup[char] = 1
			else:
				lookup[char] += 1
	
	ans = []
	for key, value in lookup.items():
		if value == max(lookup.values()):
			ans.append(key)
	
	for ch in sorted(ans):
		print(ch, end = "")
	
	print(f" {max(lookup.values())}")
