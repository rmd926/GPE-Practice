tc = 1
while True:
	target = int(input())
	if target == 0:
		break
	
	ans_list = []
	for num in range(1, target+1):
		temp = 0
		for i in range(1, num+1):
			if num % i == 0:
				temp += i
		
		if temp == target:
			ans_list.append(num)
	
	if ans_list:
		print(f"Case {tc}: {max(ans_list)}")
	else:
		print(f"Case {tc}: -1")
	
	tc += 1
