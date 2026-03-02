while True:
	target = input()
	if target == "0":
		break
		
	odd_sum = 0
	even_sum = 0
		
	for odd in range(0, len(target), 2):
		odd_sum += int(target[odd])
	
	for even in range(1, len(target), 2):
		even_sum += int(target[even])
	
	if abs(odd_sum - even_sum) % 11 == 0:
		print(f"{target} is a multiple of 11.")
	else:
		print(f"{target} is not a multiple of 11.")
