tc = 1

while True:
	n = int(input())
	target = list(map(int, input().split()))
	
	print(f"Set #{tc}")
	
	avg = sum(target) // n
	move = 0
	
	for num in target:
		move += int(abs(num-avg))
	
	print(f"The minimum number of moves is {move//2}.")
	print()
	
	tc += 1
