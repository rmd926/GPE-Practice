while True:
	n = int(input())
	ans = 1
	temp = 1
	
	while temp % n != 0:
		temp = (temp * 10 + 1) % n
		ans += 1
	
	print(ans)
