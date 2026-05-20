while True:
	seq = list(map(int, input().split()))
	n = seq[0]
	target = seq[1:]
	temp = []
	
	gt = [int(x) for x in range(1, n)]
	for i in range(1, n):
		temp.append(abs(target[i] - target[i-1]))
	
	if sorted(temp) == gt:
		print("Jolly")
		
	else:
		print("Not jolly")

# 2026.05.20 二刷
