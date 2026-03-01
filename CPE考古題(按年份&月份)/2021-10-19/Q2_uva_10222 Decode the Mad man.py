keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
tc = int(input())

for _ in range(tc):
	target = input()
	output = ""
	
	for char in target.lower():
		if char == " ":
			output += " "
		else:
			output += keyboard[keyboard.index(char)-2]
			
	print(output)
