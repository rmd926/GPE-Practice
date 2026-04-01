MAX = 1000
table = [0] * (MAX+1)
fact = 1
table[0] = 1

for num in range(1, MAX+1):
	fact *= num
	total = 0
	for ch in str(fact):
		total += int(ch)
	table[num] = total
	
while True:
	try:
		n = int(input())
	except:
		break
	
	print(table[n])
