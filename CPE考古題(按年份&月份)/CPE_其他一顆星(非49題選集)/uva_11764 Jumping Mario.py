tc = int(input())
for t in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
	
	high, low = 0, 0
	for i in range(0, n-1):
		if target[i] < target[i+1]:
			high += 1
		elif target[i] > target[i+1]:
			low += 1
		else:
			continue
            
	print(f"Case {t+1}: {high} {low}")
