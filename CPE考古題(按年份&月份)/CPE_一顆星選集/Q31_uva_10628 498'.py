while True:
	x = int(input())
	target = list(map(int, input().split()))
	ans = 0
	for i in range(len(target)):
		ans += (len(target)-i-1) * target[i] * x ** max(len(target)-i-2, 0)
		
	print(ans)
