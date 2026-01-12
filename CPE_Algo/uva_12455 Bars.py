
tc = int(input())
for _ in range(tc):
	target = int(input())
	length = int(input())
	bar_list = list(map(int, input().split()))
	
	dp = [0] * (target + 1)
	
	for i in bar_list:
		for j in range(target, 0, -1):
			if j >= i:
				dp[j] = max(dp[j], dp[j - i] + i)
	if dp[target] == target:
		print("YES")
	else:
		print("NO")
		
'''
dp[j] 表示：在總長度不超過 j 的限制下，使用目前已考慮過的鋼條，
所能湊到的最大總長度。

一開始 dp 全為 0，代表尚未選擇任何鋼條。

外層迴圈 for i in bar_list：
逐一考慮每一根鋼條（長度為 i），決定是否要選用。

內層迴圈 for j in range(target, 0, -1)：
容量 j 從大到小更新，確保每一根鋼條在同一輪中只會被使用一次，
避免重複使用同一根鋼條（0/1 背包的關鍵）。

條件 j >= i：
只有當目前容量 j 足以容納長度為 i 的鋼條時，才可能選擇這根鋼條。

狀態轉移：
dp[j] = max(dp[j], dp[j - i] + i)

- dp[j]：不選第 i 根鋼條時的最佳結果
- dp[j - i] + i：選擇第 i 根鋼條後可得到的總長度

取兩者的最大值，代表在容量 j 下的最佳選擇。
'''