while True:
	x = int(input())
	p = list(map(int, input().split()))
	ans = 0
	for i in range(len(p)):
		# original = p[i]*x**(len(p)-i-1)
		ans += (len(p)-i-1) * p[i] * x ** (len(p)-i-2)
	print(int(ans))
