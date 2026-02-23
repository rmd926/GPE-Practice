MAX = 30000
dp = [0] * (MAX+1)
dp[0] = 1
coins = [1, 5, 10, 25, 50] # 先把所有面額的存起來

for c in coins:
	for i in range(c, MAX+1):
		dp[i] += dp[i-c] # 如果要湊出金額 i，只要在「湊出金額 i-c 的方法」後面再加上一枚面額 c 的硬幣，就能形成新的方法。
		
while True:
	target = int(input())
	if dp[target] == 1:
		print(f"There is only 1 way to produce {target} cents change.")
	
	else:
		print(f"There are {dp[target]} ways to produce {target} cents change.")
