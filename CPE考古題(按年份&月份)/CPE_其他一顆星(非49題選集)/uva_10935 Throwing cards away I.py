while True:
	try:
		n = int(input())
	except:
		break
		
	if n == 0:
		break
		
	elif n == 1:
		print("Discarded cards: ")
		print(f"Remaining card: 1")
		
	else:
		target = [int(x) for x in range(1, n+1)]
		cur = target
		
		print("Discarded cards: ",end = "")
		
		while len(cur) > 1:
			if len(cur) > 2:
				print(cur[0], end = ", ")
			else:
				print(cur[0])
			cur.pop(0)
			cur.append(cur[0])
			cur.pop(0)
			
		print(f"Remaining card: {cur[0]}")
		
