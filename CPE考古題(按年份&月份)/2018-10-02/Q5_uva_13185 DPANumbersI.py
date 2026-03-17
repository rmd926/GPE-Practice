def sol(target):
	temp = 0
	for num in range(1, target//2+1):
		if target % num == 0:
			temp += num
			
	if temp == target:
		return "perfect"
		
	elif temp < target:
		return "deficient"
		
	else:
		return "abundant"
	
tc = int(input())
for _ in range(tc):
	target = int(input())
	print(sol(target))
