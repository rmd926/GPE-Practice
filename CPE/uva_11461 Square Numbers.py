while True:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		break
	lower = int(a ** 0.5)
	upper = int(b ** 0.5)
	
	if lower ** 2 != a:
		lower += 1
	print(upper - lower + 1)
