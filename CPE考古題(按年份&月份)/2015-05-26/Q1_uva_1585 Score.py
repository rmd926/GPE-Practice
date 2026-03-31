tc = int(input())
for _ in range(tc):
	combo = 0
	score = 0
	target = input()
	for ch in target:
		if ch == "X":
			combo = 0
		else:
			combo += 1
			score += combo
	print(score)
