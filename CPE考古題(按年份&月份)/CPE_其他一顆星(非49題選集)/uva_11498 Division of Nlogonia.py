while True:
	tc = int(input())
	if tc == 0:
		break
	div_point = list(map(int, input().split()))
	
	for _ in range(tc):
		x, y = map(int, input().split())
		if x > div_point[0] and y > div_point[1]:
			print("NE")
		
		elif x > div_point[0] and y < div_point[1]:
			print("SE")
		
		elif x < div_point[0] and y < div_point[1]:
			print("SO")
		
		elif x < div_point[0] and y > div_point[1]:
			print("NO")
		
		elif x == div_point[0] or y == div_point[1]:
			print("divisa")
