'''
UVA 10050 - Hartals（罷工天數統計）

輸入 tc 組測資。每組測資：
- N：總天數（從第 1 天算到第 N 天）
- P：政黨數量
- 接下來 P 行：每個政黨的罷工週期 gap（表示每隔 gap 天就會罷工一次）

作法：
1) 用 record 陣列標記每一天是否為「罷工日」（1 代表罷工，0 代表不罷工）。
2) 對每個政黨，依照 gap 的倍數天逐一標記為罷工日。
3) 週末（第 6、7 天）不計入罷工日：
   - 若天數從 1 開始，則 i % 7 == 6 表示星期五、i % 7 == 0 表示星期六（題目定義的週末）。
4) 最後把 record 加總（得到罷工天數）並輸出。
'''

tc = int(input())
for _ in range(tc):
	N = int(input()) # day
	P = int(input()) # party
	record = [0] * (N+1) # create table
	
	for _ in range(P):
		gap = int(input())
		for i in range(0, N+1, gap):
			if i % 7 != 6 and i % 7 != 0:
				record[i] = 1
	ans = sum(record)
	print(ans)