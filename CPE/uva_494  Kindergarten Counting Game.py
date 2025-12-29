while True:
	target = input()
	count = 0
	flag = False
	
	for char in target:
		if char.isalpha():
			if flag == False:
				count += 1
				flag = True
			else:
				continue
		else:
			flag = False
			
	print(count)