while True:
	J, R = map(int, input().split())
	if J == R == 0:
		break
	
	target = list(map(int, input().split()))
	player_score = [0] * J
	winner = 0
	
	for index, score in enumerate(target):
		player_score[index % J] += score
	
	for i in range(J):
		if player_score[i] == max(player_score):
			winner = i + 1
	
	print(winner)
