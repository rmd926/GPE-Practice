tc = int(input())
for _ in range(tc):
	target = int(input())
	count = 0
	
    # while target != int(str(target)[::-1]):
	while True: 
		target += int(str(target)[::-1])
		count += 1
		if target == int(str(target)[::-1]):
			break

	print(f"{count} {target}")