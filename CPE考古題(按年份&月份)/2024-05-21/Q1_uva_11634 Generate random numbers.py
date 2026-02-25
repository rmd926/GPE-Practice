while True:
	target = int(input())
	if target == 0:
		break
	seen = set()
	while target not in seen:
		seen.add(target)
		target = ((target ** 2) // 100) % 10000
	
	print(len(seen))
