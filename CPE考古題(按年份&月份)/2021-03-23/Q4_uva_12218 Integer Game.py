players = ["S", "T"]
tc = int(input())
for t in range(tc):
	N = input()
	target = []
	total_rounds = -1
	for char in N:
		target.append(int(char))
	
	while True:
		for num in target:
			temp_sum = sum(target)
			if (temp_sum - num) % 3 == 0:
				total_rounds += 1
				target.remove(num)
				break
		else:
			break
			
	ans = players[total_rounds % 2]
	print(f"Case {t+1}: {ans}")
