tc = int(input())
for _ in range(tc):
	c1, c2, c3, c4 = map(str, input().split())
	card = c1+c2+c3+c4
	odd = ""
	even = ""
	ans = 0
	for i in range(len(card)):
		if i % 2 == 0:
			double = int(card[i])*2
			odd += str(double)
		else:
			even += str(card[i])
	
	for char in odd:
		ans += int(char)
		
	for char in even:
		ans += int(char)

	if ans % 10 == 0:
		print("Valid")
		
	else:
		print("Invalid")
