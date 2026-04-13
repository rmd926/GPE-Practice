tc = int(input())
stack = []

for _ in range(tc):
	command = input()
	
	if command == "Test":
		if stack:
			print(stack[-1])
		else:
			print("Not in a dream")
	
	elif command == "Kick":
		if stack:
			stack.pop()
		else:
			continue
	
	else:
		name = command.split()[-1]
		stack.append(name)
