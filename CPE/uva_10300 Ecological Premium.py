tc = int(input())
for _ in range(tc):
	farmer = int(input())
	ans = 0
	for _ in range(farmer):
		a, b, c = list(map(int, input().split()))
		ans += a*c
		
	print(ans)