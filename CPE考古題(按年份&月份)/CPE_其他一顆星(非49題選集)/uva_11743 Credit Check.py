tc = int(input())
for _ in range(tc):
	c1, c2, c3, c4 = map(str, input().split())
	card = c1 + c2 + c3 + c4
	odd = ""
	even = ""
	
	for i in range(len(card)):
		if i % 2 == 0:
			double = int(card[i]) * 2
			odd += str(double)
		else:
			even += str(card[i])
	
	odd_sum = 0
	even_sum = 0
	
	for ch in odd:
		odd_sum += int(ch)	
	
	for ch in even:
		even_sum += int(ch)
		
	if (odd_sum + even_sum) % 10 == 0:
		print("Valid")
	else:
		print("Invalid")
