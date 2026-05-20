def cal_length(n, target):
	ans = 0
	mid = n // 2
	target.sort()
	for num in target:
		ans += abs(target[mid] - num)
		
	return ans

tc = int(input())
for _ in range(tc):
	seq = list(map(int, input().split()))
	n = seq[0]
	target = seq[1:]
	
	print(cal_length(n, target))

# 2026.05.20 二刷
