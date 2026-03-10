while True:
	target = input()
	sum = 0
	max_num = 1
	
	for char in target:
		if char.isdigit():
			temp = int(char)
			
		elif "A" <= char <= "Z":
			temp = ord(char) - ord("A") + 10
			
		elif "a" <= char <= "z":
			temp = ord(char) - ord("a") + 36
		
		else:
			continue
		
		if max_num < temp:
			max_num = temp
		
		sum += temp
	for i in range(max_num, 62):
		if sum % i == 0:
			print(i+1)
			break
	else:
		print("such number is impossible!")
