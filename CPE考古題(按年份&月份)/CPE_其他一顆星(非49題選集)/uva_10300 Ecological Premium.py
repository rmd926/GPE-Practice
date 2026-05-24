tc = int(input())
for _ in range(tc):
	n = int(input())
	ans = 0
	for _ in range(n):
		a, b, c = map(int, input().split())
		ans += a * c
	
	print(ans)

# 2026.05.25 二刷
