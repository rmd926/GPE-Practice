while True:
	step = int(input())
	if step == 0:
		break
	dice = [1,6,2,5,3,4] # top bottom north south west east
    
	for _ in range(step):
		command = input()
		if command == "north":
			dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
		
		elif command == "south":
			dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

		elif command == "east":
			dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
		
		elif command == "west":
			dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

	print(dice[0])
