while True:
	target = int(input())
	if target == 0:
		break
	
	count = 0
	output = bin(target)[2:]
	
	for digit in output:
		if digit == "1":
			count += 1
			
	print(f"The parity of {output} is {count} (mod 2).")
