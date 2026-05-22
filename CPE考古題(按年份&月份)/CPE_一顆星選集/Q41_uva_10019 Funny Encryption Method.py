tc = int(input())
for _ in range(tc):
	target = int(input())
	hex_target = int(str(target), 16)
	
	X1 = bin(target)[2:]
	X2 = bin(hex_target)[2:]
	
	ans1, ans2 = 0, 0
	for ch in X1:
		if ch == "1":
			ans1 += 1
	
	for ch in X2:
		if ch == "1":
			ans2 += 1

	print(ans1, ans2)

# 2026.05.23 二刷 要看清楚題意，int(x, base=10) x需要是字串或者是數字
