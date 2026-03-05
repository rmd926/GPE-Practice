while True:
	n = int(input())
	nums = []
	
	for _ in range(n):
		nums.append(int(input()))
	nums.sort()
	
	mid_left = nums[(n-1)//2]
	mid_right = nums[n//2]
	count = 0
	
	for i in range(len(nums)):
		if nums[i] == mid_left or nums[i] == mid_right:
			count += 1
		case = mid_right - mid_left + 1
	
	print(mid_left, count, case)
