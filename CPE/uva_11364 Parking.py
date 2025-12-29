tc = int(input())
for _ in range(tc):
	num = int(input())
	pos = list(map(int, input().split()))
	pos = sorted(pos)
	
	print(abs(pos[-1]-pos[0]) * 2)