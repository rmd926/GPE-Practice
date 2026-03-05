import math

tc = int(input())
for t in range(tc):
	s1 = int(input(), 2)
	s2 = int(input(), 2)
	
	if math.gcd(s1, s2) != 1:
		print(f"Pair #{t+1}: All you need is love!")
	else:
		print(f"Pair #{t+1}: Love is not all you need!")
