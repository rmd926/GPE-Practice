tc = int(input())
for i in range(tc):
	x1, y1, x2, y2 = map(int, input().split())
	x3, y3, x4, y4 = map(int, input().split())
	strong = [max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4)]
	
	if strong[2]>strong[0] and strong[3]>strong[1]:
		strong_safe = (strong[2] - strong[0]) * (strong[3] - strong[1])
	else:
		strong_safe = 0
		
	weak_safe = (x2-x1)*(y2-y1) + (x4-x3)*(y4-y3) - strong_safe * 2
	unsafe = 10000 - weak_safe - strong_safe
	
	print(f"Night {i+1}: {strong_safe} {weak_safe} {unsafe}")