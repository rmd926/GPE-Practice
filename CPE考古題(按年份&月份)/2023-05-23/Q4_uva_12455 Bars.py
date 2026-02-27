tc = int(input())
for _ in range(tc):
	target = int(input())
	n = int(input())
	bar_list = list(map(int, input().split()))
	
	dp = [0] * (target+1)
	
	for bar in bar_list: # 逐一取出bar_list的bar，然後倒序從 target 值開始往下走到 1
		for i in range(target, 0, -1):
			if i >= bar: # 如果目前容量值i 大於或是剛好等於bar的話，就 dp[i-bar] + bar 並且和原本dp[i]去更新max value
                # 取目前已知的最佳值與新組合的最大值
				dp[i] = max(dp[i], dp[i-bar] + bar)
	
	if dp[target] == target:
		print("YES")
	else:
		print("NO")
