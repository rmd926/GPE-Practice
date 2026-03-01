while True:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		break
		
	ans = 0
	low = int(a ** 0.5)
	high = int(b ** 0.5)
	
	if low ** 2 != a:
		low += 1
	
	print(high - low + 1)
