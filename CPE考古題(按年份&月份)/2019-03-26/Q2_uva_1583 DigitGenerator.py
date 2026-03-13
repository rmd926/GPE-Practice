tc = int(input())
for _ in range(tc):
	target = int(input())
	ans = []
	for num in range(max(0, target-len(str(target)*9)), target):
		digit_sum = 0
		for digit in str(num):
			digit_sum += int(digit)
		
		if num + digit_sum == target:
			ans.append(num)
	
	print(min(ans)) if ans else print(0)		
