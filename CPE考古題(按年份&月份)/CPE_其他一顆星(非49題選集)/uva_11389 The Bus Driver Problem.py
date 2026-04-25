while True:
	n, d, r = list(map(int, input().split()))
	morn_distance = sorted(list(map(int, input().split())))
	night_distance = sorted(list(map(int, input().split())))[::-1]
	
	cost = 0
	
	for i in range(n):
		cost += max((morn_distance[i] + night_distance[i] - d) * r, 0)
		
	print(cost)
