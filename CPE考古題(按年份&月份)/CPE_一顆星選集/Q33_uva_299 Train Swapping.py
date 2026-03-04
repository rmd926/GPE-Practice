def swapping_times(target):
	count = 0
	n = len(target)
	for i in range(n):
		for j in range(n-i-1):
			if target[j] > target[j+1]:
				target[j], target[j+1] = target[j+1], target[j]
				count += 1
	return count

tc = int(input())
for _ in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
	print(f"Optimal train swapping takes {swapping_times(target)} swaps.")
