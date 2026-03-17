tc = int(input())

for t in range(tc):
	space = input()
	height = int(input())
	times = int(input())
	
	for i in range(int(times)):
		for num in range(1, height+1):
			print(str(num) * num)
			
		for num in range(height-1, 0, -1):
			print(str(num) * num)
			
		if i+1 < times:
			print()
			
	if t+1 < tc:
		print()
