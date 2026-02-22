while True:
	tc = int(input())
	stack = []
	for _ in range(tc):
		command = input()
		if command == "Kick":
			if not stack:
				continue
			else:
				stack.pop()
		
		elif command == "Test":
			if not stack:
				print("Not in a dream")
			else:
				print(stack[-1])
		
		else:
			name = command.split()[-1]
			stack.append(name)