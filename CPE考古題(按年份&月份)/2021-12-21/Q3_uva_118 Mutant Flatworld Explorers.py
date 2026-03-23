a, b = map(int, input().split())
direction_set = ["N", "E", "S", "W"]
scent = set()

while True:
	x, y, direction = map(str, input().split())
	x, y = int(x), int(y)
	command = input()
	
	direction_index = direction_set.index(direction)
	lost = False
    
	for ch in command:
		if ch == "R":
			direction_index = (direction_index + 1) % 4
			direction = direction_set[direction_index]
		
		elif ch == "L":
			direction_index = (direction_index - 1) % 4
			direction = direction_set[direction_index]
		
		elif ch == "F":
			temp_x, temp_y = x, y
			
			if direction == "N":
				temp_y += 1
				
			elif direction == "E":
				temp_x += 1
			
			elif direction == "S":
				temp_y -= 1
			
			elif direction == "W":
				temp_x -= 1
		
			if temp_x < 0 or temp_y < 0 or temp_x > a or temp_y > b:
				if (x, y, direction) in scent:
					continue
					
				else:
					print(f"{x} {y} {direction} LOST")
					scent.add((x, y, direction))
					lost = True
					break
		
			else:
				x, y = temp_x, temp_y
	
	if not lost:
		print(f"{x} {y} {direction}")
