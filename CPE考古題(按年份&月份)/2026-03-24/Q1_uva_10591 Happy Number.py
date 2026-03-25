tc = int(input())
for t in range(tc):
	target = int(input())
	temp = []
	new_num = target
	while new_num != 1 and new_num not in temp:
		digit_sum = 0
		temp.append(new_num)
		for char in str(new_num):
			digit_sum += int(char) ** 2
		
		new_num = digit_sum
	if new_num == 1:
		print(f"Case #{t+1}: {target} is a Happy number.")
	else:
		print(f"Case #{t+1}: {target} is an Unhappy number.")
