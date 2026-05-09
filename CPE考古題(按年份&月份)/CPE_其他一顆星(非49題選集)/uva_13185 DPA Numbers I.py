def factor_sum(target):
	ans = 0
	for num in range(1, target//2 + 1):
		if target % num == 0:
			ans += num
	return ans

tc = int(input())
for _ in range(tc):
	target = int(input())
	if factor_sum(target) > target:
		print("abundant")
		
	elif factor_sum(target) < target:
		print("deficient")
	
	else:
		print("perfect")
