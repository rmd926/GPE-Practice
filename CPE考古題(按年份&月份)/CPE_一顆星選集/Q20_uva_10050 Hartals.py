tc = int(input())
for _ in range(tc):
	day = int(input())
	party = int(input())
	hartal_table = [False] * (day+1)
	
	for _ in range(party):
		gap = int(input())
		for i in range(0, day+1, gap):
			if i % 7 != 0 and i % 7 != 6:
				hartal_table[i] = True
	
	print(sum(hartal_table))
