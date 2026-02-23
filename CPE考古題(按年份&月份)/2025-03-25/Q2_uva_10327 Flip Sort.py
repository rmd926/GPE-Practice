def count_swap_times(target):
	count = 0
	for i in range(len(target)):
		for j in range(len(target)-i-1):
			if target[j] > target[j+1]:
				target[j], target[j+1] = target[j+1], target[j]
				count += 1
	return count
				
while True:
	length = int(input())
	target = list(map(int, input().split()))
	print(f"Minimum exchange operations : {count_swap_times(target)}")
	
