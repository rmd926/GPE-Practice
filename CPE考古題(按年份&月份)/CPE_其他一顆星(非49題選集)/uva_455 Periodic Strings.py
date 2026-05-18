tc = int(input())
space = input()

for t in range(tc):
	target = input()
	
	while target == "":
		target = input()
	
	n = len(target)
	for i in range(1, n+1):
		if n % i != 0:
			continue
		
		sub_string = target[:i]
		status = True
		
		for j in range(0, n, i):
			if target[j: j+i] == sub_string:
				continue
			else:
				status = False
				break
		
		if status:
			print(i)
			break
	
	if t != tc - 1:
		print()
