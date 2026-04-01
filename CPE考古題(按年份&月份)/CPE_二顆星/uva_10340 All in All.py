while True:
	try:
		s, t = input().split()
	except:
		break
	idx = 0
	
	for char in t:
		if idx < len(s) and char == s[idx]:
			idx += 1
	
	if idx == len(s):
		print("Yes")
	else:
		print("No")
