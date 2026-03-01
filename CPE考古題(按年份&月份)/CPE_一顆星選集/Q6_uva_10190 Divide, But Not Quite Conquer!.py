while True:
	n, m = map(int, input().split())
	if n == 0 or m == 0 or n == 1 or m == 1:
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
		
		if status:
			print(*ans)
		
		else:
			print("Boring!")	
