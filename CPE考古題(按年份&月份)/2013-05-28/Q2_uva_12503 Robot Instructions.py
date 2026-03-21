tc = int(input())
for _ in range(tc):
	step = int(input())
	history = []
	pos = 0
	
	for _ in range(step):
		command = input()
		if command == "LEFT":
			pos -= 1
			history.append(command)
		
		elif command == "RIGHT":
			pos += 1
			history.append(command)
		
		else:
			index = int(command.split()[-1])
			lookup = history[index-1]
			
			if lookup == "RIGHT":
				pos += 1
				history.append("RIGHT")
			
			elif lookup == "LEFT":
				pos -= 1
				history.append("LEFT")
	print(pos)
