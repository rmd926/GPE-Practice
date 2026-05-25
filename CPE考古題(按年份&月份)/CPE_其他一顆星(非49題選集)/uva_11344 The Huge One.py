tc = int(input())
for _ in range(tc):
	target = input()
	seq = list(map(int, input().split()))
	n = seq[0]
	nums = seq[1:]
	status = True
	
	for num in nums:
		if int(target) % num != 0:
			status = False
			break
		else:
			continue
	
	if status:
		print(f"{target} - Wonderful.")
	else:
		print(f"{target} - Simple.")

# 2026.05.25 二刷，要注意line 3輸入的時候要用str，運算時再改用int去包
