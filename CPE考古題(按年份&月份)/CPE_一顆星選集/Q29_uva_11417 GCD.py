import math

while True:
	target = int(input())
	if target == 0:
		break
	ans = 0
	for i in range(1, target):
		for j in range(i+1, target+1):
			ans += math.gcd(i, j)
	
	print(ans)
