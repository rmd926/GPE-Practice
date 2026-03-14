while True:
	seq = list(map(int, input().split()))
	n = seq[0]
	target = seq[1:]
	
	check = []
	gt = [int(x) for x in range(1, n)]
	
	for i in range(1, n):
		check.append(abs(target[i-1] - target[i]))
	
	if sorted(check) == gt:
		print("Jolly")
	else:
		print("Not jolly")
