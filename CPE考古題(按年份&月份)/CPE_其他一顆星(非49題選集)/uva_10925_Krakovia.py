tc = 1
while True:
	N, P = map(int, input().split())
	if N == P == 0:
		break
	
	total = 0
	for _ in range(N):
		cost = int(input())
		total += cost
	
	print(f"Bill #{tc} costs {total}: each friend should pay {total // P}")
	print()
	tc += 1
