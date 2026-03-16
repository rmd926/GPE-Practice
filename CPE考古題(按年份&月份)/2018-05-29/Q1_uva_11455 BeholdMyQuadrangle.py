tc = int(input())
for _ in range(tc):
	target = list(map(int, input().split()))
	target = sorted(target)
	
	if target[0] == target[1] == target[2] == target[3]:
		print("square")
		
	elif target[0] == target[1] and target[2] == target[3]:
		print("rectangle")
	
	elif target[0] + target[1] + target[2] > target[3]:
		print("quadrangle")
	
	else:
		print("banana")
