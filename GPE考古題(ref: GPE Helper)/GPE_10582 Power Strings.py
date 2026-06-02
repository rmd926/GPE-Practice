def sol(target: str):
	n = len(target)
	res = [0] * n
	j = 0
	
	for i in range(1, n):
		while j > 0 and target[i] != target[j]:
			j = res[j-1]
		
		if target[i] == target[j]:
			j += 1
		
		res[i] = j
	
	return res

while True:
	try:
		target = input()
	except:
		break
	
	if target == ".":
		break
	
	n = len(target)
	res = sol(target)
	period = n - res[-1]
	
	if n % period == 0:
		print(n // period)
	else:
		print(1)
