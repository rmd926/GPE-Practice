tc = 1
while True:
	n = int(input())
	target = list(map(int, input().split()))
	status = True
	seq = []
	
	for i in range(n-1):
		for j in range(i+1, n):
			if target != sorted(target) or 0 in target:
				status = False
				break
			else:
				if target[i] + target[j] in seq:
					status = False
					break
				else:
					seq.append(target[i] + target[j])
					
	if status:
		print(f"Case #{tc}: It is a B2-Sequence.")
	
	else:
		print(f"Case #{tc}: It is not a B2-Sequence.")
		
	print()
	tc += 1
	space = input()
