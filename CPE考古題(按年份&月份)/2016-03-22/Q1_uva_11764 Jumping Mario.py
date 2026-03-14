tc = int(input())
for t in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
	low, high = 0, 0
	
	for i in range(0, n-1):
		if target[i+1] > target[i]:
			high += 1
			
		elif target[i+1] < target[i]:
			low += 1
			
		else:
			continue
	
	print(f"Case {t+1}: {high} {low}")
