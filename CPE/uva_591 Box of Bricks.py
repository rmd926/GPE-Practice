import numpy as np
tc = 0

while True:
	n = int(input())
	if n == 0:
		break

	tc += 1
	print(f"Set #{tc}")
	
	target = list(map(int, input().split()))
	avg = int(np.mean(target))
	ans = 0
	
	for i in target:
		if int(i) <= avg:
			ans += abs(i-avg)
	print(f"The minimum number of moves is {ans}.")
	print()