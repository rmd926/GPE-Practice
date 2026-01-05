while True:
	n, m = map(int,input().split())
	if  n == 0 or m == 0 or m == 1 or n == 1:
		print("Boring!")
	else:
		ans = [n]
		status = True
		while n > 1:
			if n % m == 0:
				n //= m
				ans.append(n)
			else:
				status = False
				break
				
		if status == False:
			print("Boring!")
		else:
			print(*ans)
		