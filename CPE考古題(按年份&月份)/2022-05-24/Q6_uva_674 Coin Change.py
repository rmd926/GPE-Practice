MAX = 7489
dp = [0] * (MAX+1)
dp[0] = 1

coins = [1, 5, 10, 25, 50]
for c in coins:
	for i in range(c, MAX+1):
		dp[i] += dp[i-c]

while True:
	target = int(input())
	print(dp[target])
