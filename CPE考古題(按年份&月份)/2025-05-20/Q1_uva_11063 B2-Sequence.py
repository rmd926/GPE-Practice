tc = 1
while True:
	length = int(input())
	target = list(map(int, input().split()))
	status = True
	temp = []
	
	for i in range(length-1):
		for j in range(i+1, length):
			if target != sorted(target) or 0 in target:
				status = False
				break
			else:
				if target[i] + target[j] in temp:
					status = False
					break
				else:
					temp.append(target[i] + target[j])
	
	if status:
		print(f"Case #{tc}: It is a B2-Sequence.")
		
	else:
		print(f"Case #{tc}: It is not a B2-Sequence.")
	
	print()
	tc += 1
	space = input()
	
