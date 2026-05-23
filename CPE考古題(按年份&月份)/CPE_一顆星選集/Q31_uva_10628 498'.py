while True:
	x = int(input())
	target = list(map(int, input().split()))
	
	ans = 0
	n = len(target)
	for i in range(n):
		ans += (n-i-1) * target[i] * x ** max((n-i-2), 0)
	print(ans)
# 2026.05.23 二刷
