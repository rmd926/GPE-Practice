lookup = {"W":1, "H": 1/2, "Q": 1/4, "E": 1/8, "S": 1/16, "T": 1/32, "X": 1/64}
while True:
	target = input()
	if target == "*":
		break
	duration = 0
	count = 0
	
	for char in target:
		if char != "/":
			duration += lookup[char]
		else:
			if duration == 1:
				count += 1
			duration = 0
	
	print(count)
