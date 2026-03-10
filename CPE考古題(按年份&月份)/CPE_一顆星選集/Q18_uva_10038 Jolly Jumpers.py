while True:
	target = list(map(int, input().split()))
	n = target[0]
	nums = target[1:]
	check = []
	gt = [int(x) for x in range(1, n)]
	
	for i in range(1, n):
		check.append(abs(nums[i-1]-nums[i]))
	
	if sorted(check) == gt:
		print("Jolly")
	
	else:
		print("Not jolly")
