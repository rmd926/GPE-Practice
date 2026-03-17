while True:
	N, R = map(int, input().split())
	rest = list(map(int, input().split()))
	gt = [int(x) for x in range(1, N+1)]
	
	for num in rest:
		if num in gt:
			gt.remove(num)
	
	print("*") if not gt else print(*gt, "")
