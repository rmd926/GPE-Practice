tc = 1
while True:
	length = int(input())
	print(f"Case #{tc}: ",end = "")
	status = True
	sequence = []
	target = list(map(int, input().split()))
	for i in range(length-1):
		for j in range(i+1, length):
			if target != sorted(target) or 0 in target:
				status = False
				break
			
			else:
				if target[i] + target[j] in sequence:
					status = False
					break
				else:
					sequence.append(target[i] + target[j])
	if status:
		print("It is a B2-Sequence.")
	else:
		print("It is not a B2-Sequence.")
		
	print()
	tc += 1
	space = input()
