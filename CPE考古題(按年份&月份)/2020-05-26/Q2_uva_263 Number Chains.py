while True:
	target = input()
	if target == "0":
		break
	temp = []
	count = 0
	new_num = int(target)
	print(f"Original number was {target}")
	
	while True:
		high = "".join(sorted(str(new_num))[::-1])
		low = "".join(sorted(str(new_num)))
		
		new_num = int(high) - int(low)
		print(f"{int(high)} - {int(low)} = {new_num}")
		if new_num not in temp:
			temp.append(new_num)
			count += 1
		else:
			count += 1
			break
	
	print(f"Chain length {count}")
	print()	
