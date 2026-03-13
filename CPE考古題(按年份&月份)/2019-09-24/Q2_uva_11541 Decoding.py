tc = int(input())

for t in range(tc):
	target = input()
	output = ""
	i = 0
	
	while i < len(target):
		char = target[i]
		i += 1
		num = ""
		
		while i < len(target) and target[i].isdigit():
			num += target[i]
			i += 1
		
		output += char * int(num)
	
	print(f"Case {t+1}: {output}")
