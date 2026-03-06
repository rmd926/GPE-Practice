count = 0
while True:
	target = input()
	for char in target:
		if char == '"':
			count += 1
			if count % 2 == 1:
				print("``", end = "")
			else:
				print("''", end = "")
		
		else:
			print(char, end = "")
	
	print()
