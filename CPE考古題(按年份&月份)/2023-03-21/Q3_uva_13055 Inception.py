tc = int(input())
stack = []
for _ in range(tc):
	command = input()
	
	if command == "Test":
		if not stack:
			print("Not in a dream")
		else:
			print(stack[-1])
	
	elif command == "Kick":
		if not stack:
			continue
		else:
			stack.pop()
			
	else:
		name = command.split()[-1]
		stack.append(name)
