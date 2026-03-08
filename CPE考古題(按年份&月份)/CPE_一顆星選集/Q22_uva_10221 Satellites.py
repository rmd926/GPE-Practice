import math
while True:
	target = list(input().split())
	r = 6440
	s = int(target[0])
	a = int(target[1])
	Type = target[2]
	
	if Type == "min":
		a /= 60
	
	if a > 180:
		a = 360 - a
	
	theta = math.radians(a)
	arc = (r+s) * theta
	chord = 2 * (r+s) * math.sin(theta*0.5)
	
	print(f"{arc:.6f} {chord:.6f}")
