while True:
	target = list(map(float, input().split()))
	point = []
	for i in range(0, 8, 2):
		point.append([target[i], target[i+1]])
	
	dup = [0, 0]
	for i in range(4):
		if point.count(point[i]) == 2:
			dup = point[i]
			point.remove(dup)
			point.remove(dup)
			break
	
	print(f"{(point[0][0] + point[1][0] - dup[0]):.3f} {(point[0][1] + point[1][1] - dup[1]):.3f}")
