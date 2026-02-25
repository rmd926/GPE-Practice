while True:
	target = int(input())
	if target == 0:
		break
		
	if int(target ** 0.5) ** 2 == target:
		print("yes")
	
	else:
		print("no")
