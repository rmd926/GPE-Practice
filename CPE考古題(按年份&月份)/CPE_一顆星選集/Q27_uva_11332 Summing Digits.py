while True:
	target = input()
	if target == "0":
		break
		
	while int(target) > 9:
		temp = 0
		for char in target:
			temp += int(char)
		target = str(temp)
	
	print(target)
