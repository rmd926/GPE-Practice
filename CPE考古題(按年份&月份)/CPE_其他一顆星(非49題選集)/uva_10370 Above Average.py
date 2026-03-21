tc = int(input())
for _ in range(tc):
	seq = list(map(int, input().split()))
	n = int(seq[0])
	target = seq[1:]
	
	avg = sum(target) // n
	target = sorted(target)[::-1]
	
	count = 0
	for num in target:
		if num > avg:
			count += 1
		else:
			break
	
	ans = 100 * count / n
	print(f"{ans:.3f}%")
