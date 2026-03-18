while True:
	target = int(input())
	if target == 0:
		break
	
	if target == 9:
		print("9 is a multiple of 9 and has 9-degree 1.")
	
	elif target % 9 != 0:
		print(f"{target} is not a multiple of 9.")

	
	else:
		new_num = target
		count = 0
		
		while new_num != 9:
			count += 1
			temp = 0
			for char in str(new_num):
				temp += int(char)
			new_num = temp
		
		print(f"{target} is a multiple of 9 and has 9-degree {count}.")
