tc = int(input())
for _ in range(tc):
	target = int(input())
	lookup = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8": 0, "9" : 0}
	s = ""
	for num in range(1, target+1):
		s += str(num)
	
	for char in s:
		lookup[char] += 1
	
	ans = []
	for key, value in sorted(lookup.items()):
		ans.append(value)

	print(*ans)
