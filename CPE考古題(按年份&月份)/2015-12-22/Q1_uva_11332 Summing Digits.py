while True:
	target = int(input())
	if target == 0:
		break
	
	while target > 9:
		temp = 0
		for digit in str(target):
			temp += int(digit)
		target = temp

	print(target)
