tc = int(input())
for _ in range(tc):
	day = int(input())
	party = int(input())
	
	record = [False] * (day+1)
	for _ in range(party):
		gap = int(input())
		for i in range(0, day+1, gap):
			if i % 7 != 0 and i % 7 != 6:
				record[i] = True
	
	print(sum(record))
# 2026.05.22 二刷 需要注意星期5、6 mod 7之後要等於多少 
