tc = int(input())
for _ in range(tc):
	target = input()
	score = 0
	combo = 0
	
	for i in range(len(target)):
		if target[i] == "O":
			combo += 1
			score += combo
		elif target[i] == "X":
			combo = 0
			score += combo
		
	print(score)