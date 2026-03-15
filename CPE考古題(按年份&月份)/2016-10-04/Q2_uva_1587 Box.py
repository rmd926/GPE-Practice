while True:
	temp = []
	status = True
	for _ in range(6):
		h, w = map(int, input().split())
		temp.append(h)
		temp.append(w)
	
	for i in range(len(temp)):
		if temp.count(temp[i]) % 4 != 0:
			status = False
			break
		else:
			continue
				
	print("POSSIBLE") if status else print("IMPOSSIBLE")
