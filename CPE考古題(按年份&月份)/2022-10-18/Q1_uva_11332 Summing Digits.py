while True:
	target = int(input())
	if target == 0:
		break
	
	while target > 9:
		temp = 0
		for i in str(target):
			temp += int(i)
		target = temp
	
	print(target)
