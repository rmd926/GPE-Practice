tc = int(input())
for _ in range(tc):
	n = int(input())
	target = list(map(int, input().split()))
	print((max(target) - min(target)) * 2)
