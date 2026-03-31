import math

tc = int(input())
for _ in range(tc):
	target = list(map(int, input().split()))
	if len(target) == 2:
		a = target[0]
		b = target[1]
		ans = ((a+b)**2 - a**2 - b**2) * math.pi
	else:
		a = target[0]
		ans = (a**2 * math.pi / 8)
	print(f"{ans:.4f}")
