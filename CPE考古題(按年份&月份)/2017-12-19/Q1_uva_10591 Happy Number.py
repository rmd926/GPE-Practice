tc = int(input())
for t in range(tc):
	target = int(input())
	seq = [target]
	new_num = target
	
	while new_num != 1 and new_num not in seq[:-1]:
		temp = 0
		for char in str(new_num):
			temp += int(char) ** 2
		
		seq.append(temp)
		new_num = temp
		
	if new_num == 1:
		print(f"Case #{t+1}: {target} is a Happy number.")
		
	else:
		print(f"Case #{t+1}: {target} is an Unhappy number.")
