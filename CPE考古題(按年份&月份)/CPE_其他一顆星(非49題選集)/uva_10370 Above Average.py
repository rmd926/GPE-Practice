tc = int(input())
for _ in range(tc):
	seq = list(map(int, input().split()))
	n = seq[0]
	target = seq[1:]
	target.sort()
	avg = sum(target) / n
	
	count = 0
	for num in target:
		if num > avg:
			count += 1
		else:
			continue
	
	ans = 100 * count / n
	print(f"{ans:.3f}%")
# 2026.05.25 二刷
