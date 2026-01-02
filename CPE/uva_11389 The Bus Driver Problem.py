while True:
	n, d, r = list(map(int, input().split()))
	if n == 0 and d == 0 and r == 0:
		break
	
	morn_length = sorted(list(map(int, input().split())))
	night_length = list(map(int, input().split()))
	
	night_length = sorted(night_length)[::-1]
	
	cost = 0
	for i in range(n):
		cost += max((morn_length[i] + night_length[i] - d) * r, 0)
	print(cost)