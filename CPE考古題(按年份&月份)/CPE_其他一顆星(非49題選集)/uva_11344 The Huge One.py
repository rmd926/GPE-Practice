tc = int(input())
for _ in range(tc):
	target = int(input())
	seq = list(map(int, input().split()))
	n = seq[0]
	nums = seq[1:]
	status = True
	
	for num in nums:
		if target % num != 0:
			status = False
			break
		else:
			continue
	
	if status:
		print(f"{target} - Wonderful.")
	else:
		print(f"{target} - Simple.")
