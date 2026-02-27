while True:
	
	s1 = input()
	s2 = input()
	
	lookup_s1 = {}
	lookup_s2 = {}
	
	check_s1 = []
	check_s2 = []
	
	for ch in s1:
		if ch not in lookup_s1:
			lookup_s1[ch] = 1
		else:
			lookup_s1[ch] += 1
	
	for ch in s2:
		if ch not in lookup_s2:
			lookup_s2[ch] = 1
		else:
			lookup_s2[ch] += 1
	
	for key, value in lookup_s1.items():
		check_s1.append(value)
	
	for key, value in lookup_s2.items():
		check_s2.append(value)
	
	if sorted(check_s1) == sorted(check_s2):
		print("YES")
	else:
		print("NO")
	
