case = 1

while True:
	tc = int(input())
	ans = 0
	
	for _ in range(tc):
		target = input()
		lookup = {}
		
		for char in target:
			if char not in lookup:
				lookup[char] = 1
			else:
				lookup[char] += 1
		
		temp = []
	
		for key, value in lookup.items():
			temp.append(value)
			
		if len(temp) >= 2 and len(temp) == len(list(set(temp))):
			ans += 1
		
	print(f"Case {case}: {ans}")
	case += 1
