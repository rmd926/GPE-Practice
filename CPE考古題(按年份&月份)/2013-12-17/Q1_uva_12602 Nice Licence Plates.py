tc = int(input())
for _ in range(tc):
	alpha, digit = input().split("-")
	value_alpha = 0
	
	for i in range(len(alpha)):
		value_alpha += (ord(alpha[i])-65) * 26 **(3-i-1)
	
	if abs(int(digit) - value_alpha) <= 100:
		print("nice")
		
	else:
		print("not nice")
