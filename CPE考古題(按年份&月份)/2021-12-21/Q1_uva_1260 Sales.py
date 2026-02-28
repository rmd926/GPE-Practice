tc = int(input())
for _ in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
	ans = 0
	
	for i in range(1, n):
		for j in range(0, i):
			if target[i] >= target[j]:
				ans += 1
	
	print(ans)
