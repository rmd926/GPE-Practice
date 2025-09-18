TC = int(input())

for i in range(TC):
	target = int(input())
	target += int(str(target)[::-1])
	count = 1
	while True:
		if target == int(str(target)[::-1]):
			break
		target += int(str(target)[::-1])
		count += 1
	print(count, target)
			