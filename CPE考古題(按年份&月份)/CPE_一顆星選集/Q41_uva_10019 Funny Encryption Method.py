tc = int(input())
for _ in range(tc):
	target = int(input())
	hex_target = int(str(target), 16)
	
	X1 = bin(target)[2:]
	X2 = bin(hex_target)[2:]
	ans1, ans2 = 0, 0
	
	for char in X1:
		if char == "1":
			ans1 += 1
	
	for char in X2:
		if char == "1":
			ans2 += 1
	
	print(ans1, ans2)
