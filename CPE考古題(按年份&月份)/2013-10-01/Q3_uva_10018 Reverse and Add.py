tc = int(input())
for _ in range(tc):
	target = int(input())
	count = 0

	while True:
		target += int(str(target)[::-1])
		count += 1

		if str(target) == str(target)[::-1]:
			break
	
	print(f"{count} {target}")
