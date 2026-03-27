soundex_dict = {
    "B": 1, "F": 1, "P": 1, "V": 1,
    "C": 2, "G": 2, "J": 2, "K": 2, "Q": 2, "S": 2, "X": 2, "Z": 2,
    "D": 3, "T": 3,
    "L": 4,
    "M": 5, "N": 5,
    "R": 6
}

while True:
	try:
		target = input()
	except:
		break
	output = ""
	prev_code = 0

	for i in range(len(target)):
		if target[i] not in soundex_dict:
			prev_code = 0
			continue
			
		elif soundex_dict[target[i]] == prev_code:
			continue
		
		else:
			output += str(soundex_dict[target[i]])

		prev_code = soundex_dict[target[i]]
	
	print(output)
