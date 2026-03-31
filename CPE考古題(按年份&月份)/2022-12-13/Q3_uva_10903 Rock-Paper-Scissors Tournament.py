first = False
while True:
	n, k = map(int, input().split())
	if n == 0:
		break
		
	win = [0] * n
	lose = [0] * n
	total = k * n * (n-1)//2
	
	if first:
		print()
		
	for _ in range(total):
		target = list(map(str, input().split()))
		if target[1] == target[3]:
			continue
			
		elif target[1] == "rock" and target[3] == "scissors" or target[1] == "scissors" and target[3] == "paper" or target[1] == "paper" and target[3] == "rock":
			win[int(target[0])-1] += 1
			lose[int(target[2])-1] += 1
			
		else:
			win[int(target[2])-1] += 1
			lose[int(target[0])-1] += 1
			
	for i in range(n):
		if win[i] + lose[i] == 0:
			print("-")
		else:
			print(f"{win[i]/(win[i] + lose[i]):.3f}")
	
	first = True
