from math import factorial

tc = int(input())
for _ in range(tc):
	target = sorted(input())
	n = int(input())
	ans = ""
	
	while len(target) > 0:
		x = factorial(len(target)-1)
		i = n // x
		ans += target[i]
		target = target[:i] + target[i+1:]
		n %= x
	print(ans)