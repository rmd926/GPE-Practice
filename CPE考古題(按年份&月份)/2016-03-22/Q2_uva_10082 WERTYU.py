keyboard = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"

while True:
	target = input()
	output = ""
	for char in target:
		if char == " ":
			output += " "
		
		else:
			output += keyboard[keyboard.index(char)-1]

	print("".join(output))	
