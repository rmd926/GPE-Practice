while True:
	target = int(input())

	if target == 0:
		break
	
	count = 0
	for i in str(bin(target)[2:]):
		if i == "1":
			count += 1
	print(f"The parity of {bin(target)[2:]} is {count} (mod 2).")
