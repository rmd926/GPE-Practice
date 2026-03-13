tc = 1
while True:
	target = int(input())
	if target == -1:
		break
	
	temp = 1
	count = 0
	
	while temp < target:
		temp *= 2
		count += 1
	
	print(f"Case {tc}: {count}")
	tc += 1
