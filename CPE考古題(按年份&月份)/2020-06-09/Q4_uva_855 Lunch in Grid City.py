tc = int(input())
for _ in range(tc):
	s, a, f = map(int, input().split())
	x_list, y_list = [], []
	for _ in range(f):
		x, y = map(int, input().split())
		x_list.append(x)
		y_list.append(y)
	
	x_list.sort()
	y_list.sort()	
	print(f"(Street: {x_list[(f+1)//2-1]}, Avenue: {y_list[(f+1)//2-1]})")
