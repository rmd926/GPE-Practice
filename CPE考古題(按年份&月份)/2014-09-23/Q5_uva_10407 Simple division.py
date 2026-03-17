import math
while True:
	seq = list(map(int, input().split()))
	if len(seq) == 1 and sum(seq) == 0:
		break
		
	target = seq[:-1]
	ans = []
	for i in range(1, len(target)):
		ans.append(abs(target[i]-target[i-1]))
	
	print(math.gcd(*ans))
