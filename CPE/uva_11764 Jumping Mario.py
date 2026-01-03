tc = int(input())
for t in range(tc):
	num_wall = int(input())
	target = list(map(int, input().split()))
	high_count = 0
	low_count = 0
	same = 0
	
	for i in range(1, num_wall):
		if target[i-1] < target[i]:
			high_count += 1
		elif target[i-1] > target[i]:
			low_count += 1
		else:
			same += 1
			
	print(f"Case {t+1}: {high_count} {low_count}")