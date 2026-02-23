while True:
	low, high = map(int, input().split())
	if low == 0 and high == 0:
		break
	
	root_l = int(low **0.5)
	root_h = int(high ** 0.5)
	
	if root_l ** 2 != low:
		root_l += 1
		
	print(root_h - root_l + 1)
