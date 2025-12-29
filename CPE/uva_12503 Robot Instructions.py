tc = int(input())

for _ in range(tc):
	num = int(input())
	move_history = []
	pos = 0
	
	for _ in range(num):
		move = input()
		if move == 'LEFT':
			pos -= 1
			move_history.append(move)
			
		elif move == 'RIGHT':
			pos += 1
			move_history.append(move)
		
		else: # SAME AS ???
			step_num = int(move.split()[-1])
			lookup = move_history[step_num - 1]
			if lookup == 'LEFT':
				pos -= 1
			else:
				pos += 1
			
			move_history.append(lookup)
	
	print(pos)	