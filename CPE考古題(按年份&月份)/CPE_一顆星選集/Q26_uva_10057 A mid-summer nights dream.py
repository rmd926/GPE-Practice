while True:
	n = int(input())
	nums = []
	for _ in range(n):
		target = int(input())
		nums.append(target)
	
	nums.sort()
	mid_left = nums[(n-1) // 2]
	mid_right = nums[n // 2]
	
	count = 0
	for num in nums:
		if num == mid_left or num == mid_right:
			count += 1
	
	case = mid_right - mid_left + 1
	print(f"{mid_left} {count} {case}")

# 2026.05.23 二刷 要小心mid_left、mid_right，不要算錯。
# hints: 當n是奇數的時候，mid_left = mid_right
