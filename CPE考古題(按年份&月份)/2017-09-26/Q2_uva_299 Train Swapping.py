def swapping_times(target):
	count = 0
	for i in range(len(target)):
		for j in range(len(target)-i-1):
			if target[j] > target[j+1]:
				count += 1
				target[j], target[j+1] = target[j+1], target[j]
				
	return count

tc = int(input())
for _ in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
	print(f"Optimal train swapping takes {swapping_times(target)} swaps.")
