tc = int(input())
space = input()
for _ in range(tc):
	
	plain = input()
	sub = input()
	lookup = {}
	
	print(sub)
	print(plain)
	
	for i in range(len(plain)):
		lookup[plain[i]] = sub[i]
	
	while True:
		target = input()
		if target == "":
			print("")
			break
			
		output = ""
		for char in target:
			if char in lookup:
				output += lookup[char]
			else:
				output += char

		print(output)
