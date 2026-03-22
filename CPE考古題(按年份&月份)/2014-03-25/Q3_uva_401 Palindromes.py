mirror = {
    "A": "A", "E": "3", "3": "E", "H": "H", "I": "I",
    "J": "L", "L": "J", "M": "M", "O": "O", "S": "2",
    "2": "S", "T": "T", "U": "U", "V": "V", "W": "W",
    "X": "X", "Y": "Y", "Z": "5", "5": "Z", "1": "1",
    "8": "8"
}

while True:
	target = input()
	
	is_palindrome = True
	if target == target[::-1]:
		is_palindrome = True
        
	elif target != target[::-1]:
		is_palindrome = False
	
	is_mirrored = True
	for i in range(len(target)):
		if target[i] not in mirror or mirror[target[i]] != target[len(target)-i-1]:
			is_mirrored = False
			break
	
	if is_palindrome and is_mirrored:
		print(f"{target} -- is a mirrored palindrome.")
	
	elif is_palindrome:
		print(f"{target} -- is a regular palindrome.")
	
	elif is_mirrored:
		print(f"{target} -- is a mirrored string.")
	
	else:
		print(f"{target} -- is not a palindrome.")
	
	print()
