while True:
	n, m = map(int, input().split())
	if n == 0 or m == 0:
		print(0)
	
	else:
		p = 2 ** m
		size = 3 * (2 ** (m-1))
		dp = [0] * (size+1)
		dp[0], dp[1] = 0, 1
		
		for i in range(2, size+1):
			dp[i] = (dp[i-1] + dp[i-2]) % p
			
		print(dp[n % size])
