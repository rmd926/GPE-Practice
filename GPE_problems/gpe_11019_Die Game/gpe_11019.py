while True:
	n = int(input())
	if n == 0:
		break
	dice = [1,6,2,5,3,4] # top, bottom, north, south, west, east
	
	for i in range(n):
		direction = input()
		if direction == 'north':
			dice[2], dice[1], dice[0], dice[3] = dice[0], dice[2], dice[3], dice[1]
			
		elif direction == 'south':
			dice[3], dice[0], dice[1], dice[2] = dice[0], dice[2], dice[3], dice[1]
			
		elif direction == 'west':
			dice[4], dice[5], dice[1], dice[0] = dice[0], dice[1], dice[4], dice[5]
			
		elif direction == 'east':
			dice[5], dice[4], dice[0], dice[1] = dice[0], dice[1], dice[4], dice[5]
			
	print(dice[0])