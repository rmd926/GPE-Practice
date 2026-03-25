tc = int(input())
for _ in range(tc):
	target = int(input())
	factor_list = []
	
	for i in range(1, target+1):
		if target % i == 0:
			factor_list.append(i)
	
	ans = float("inf")
	
	for i in range(len(factor_list)):
		a = factor_list[i]
		for j in range(i, len(factor_list)):
			b = factor_list[j]
			if target % (a*b) != 0:
				continue
			c = target // (a*b)
			
			if c < b:
				continue
			area = 2 * (a*b+b*c+a*c)
			ans = min(area, ans)
	print(ans)
