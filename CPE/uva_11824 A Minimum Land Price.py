tc = int(input())
for _ in range(tc):
	ans = 0
	temp = []
	while True:
		target = int(input())
		if target == 0:
			break
		temp.append(target)
		temp = sorted(temp)[::-1]
	
	for i in range(len(temp)):
		ans += 2 * (temp[i]) ** (i+1)
		
	if ans > 5_000_000:
		print("Too expensive")
	else:
		print(ans)