MAX = 5000
dp = [0] * (MAX+1)
dp[0], dp[1] = 0, 1

for i in range(2, MAX+1):
	dp[i] = dp[i-1] + dp[i-2]
	
while True:
	target = int(input())
	print(f"The Fibonacci number for {target} is {dp[target]}")
