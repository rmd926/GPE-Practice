tc = int(input())
for _ in range(tc):
	num = int(input())
	pos = 0
	move_history = []
	
	for _ in range(num):
		move = input()
		if move == "RIGHT":
			pos += 1
			move_history.append(move)
		
		elif move == "LEFT":
			pos -= 1
			move_history.append(move)
		
		else:
			index = int(move.split()[-1])
			lookup = move_history[index-1]
			
			if lookup == "RIGHT":
				pos += 1
			else:
				pos -= 1
			
			move_history.append(lookup)
	print(pos)
