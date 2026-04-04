while True:
	try:
		seq = list(map(int, input().split()))
	except:
		break
	
	for num in seq:
		if num == 0:
			break
	
		step = 1
		
		while True:
			target = [int(x) for x in range(1, num+1)]
			target.pop(0)
			idx = 0
			
			while len(target) > 1:
				idx = (idx + step - 1) % len(target)
				target.pop(idx)
			
			if target[0] == 13:
				print(step)
				break
			
			step += 1

while True:
	try:
		n = int(input())
	except:
		break

	if n == 0:
		break
	
	step = 1

	while True:
		target = [int(x) for x in range(1, n+1)]
		target.pop(0)
		idx = 0

		while len(target) > 1:
			idx = (idx + step - 1) % len(target)
			target.pop(idx)

		if target[0] == 13:
			print(step)
			break

		step += 1
