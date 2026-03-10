def cal_prob(n, p, target):
	if p == 0:
		return f"{0:.4f}"
	q = 1 - p
	prob = p * (q ** (target - 1) / (1 - q ** n))

	return f"{prob:.4f}"
	
tc = int(input())
for _ in range(tc):
	n, p, target = input().split()
	print(cal_prob(int(n), float(p), int(target)))
