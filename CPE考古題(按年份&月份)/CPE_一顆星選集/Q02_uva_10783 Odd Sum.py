tc = int(input())
for t in range(tc):
	a = int(input())
	b = int(input())
	ans = 0
	
	if a % 2 == 0:
		a += 1
	
	for odd in range(a, b+1, 2):
		ans += odd
	
	print(f"Case {t+1}: {ans}")
