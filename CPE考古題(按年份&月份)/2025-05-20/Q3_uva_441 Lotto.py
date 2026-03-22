from itertools import combinations

tc = 0
while True:
	seq = list(map(int, input().split()))
	if sum(seq) == 0:
		break
		
	n = int(seq[0])
	target = seq[1:]
	
	if tc > 0:
		print()
		
	for p in combinations(target, 6):
		print(*list(p))
	
	tc += 1
