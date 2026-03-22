tc = int(input())
for t in range(tc):
	x1, y1, x2, y2 = map(int, input().split())
	ans = (x1 + y1 + x2 + y2 + 1) * (x2 + y2 - x1 - y1) // 2 + x2 - x1
	print(f"Case {t+1}: {ans}")
