import math

while True:
	try:
		seq = list(map(int, input().split()))
	except:
		break
	
	if len(seq) == 1 and seq[0] == 0:
		break
		
	target = seq[:-1]
	temp = []
	
	for i in range(1, len(target)):
		temp.append(abs(target[i-1] - target[i]))
	
	ans = math.gcd(*temp)
	print(ans)
