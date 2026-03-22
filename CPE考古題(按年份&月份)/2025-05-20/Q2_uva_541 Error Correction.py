while True:
	size = int(input())
	if size == 0:
		break
	
	target = [[int(x) for x in input().split()] for _ in range(size)]
	
	x_list = []
	y_list = []
	for r in range(size):
		if sum(target[r]) % 2 != 0:
			y_list.append(r+1)
		else:
			continue
	
	for i in range(size):
		temp = 0
		for j in range(size):
			temp += target[j][i]
		if temp % 2 != 0:
			x_list.append(i+1)
		else:
			continue
	
	if len(x_list) > 1 or len(y_list) > 1:
		print("Corrupt")
	
	elif len(x_list) == 1 and len(y_list) == 1:
		print(f"Change bit ({y_list[0]},{x_list[0]})")
	
	else:
		print("OK")
