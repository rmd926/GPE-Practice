n = 30000
dp = [0] * (n+1)
dp[0] = 1
coins = [1, 5, 10, 25, 50]

for i in coins:
    for j in range(i, n+1):  
        dp[j] += dp[j-i] 

while True:
    target = int(input())

    if dp[target] == 1:
        print(f"There is only 1 way to produce {target} cents change.")
		
    else:
        print(f"There are {dp[target]} ways to produce {target} cents change.")


'''
解題想法:
一開始先建立一個極大的一維陣列，並且把dp[0]設為1
接著先枚舉硬幣，再枚舉金額 => 這樣每個金額的累加只會把「使用到目前為止硬幣種類」的組合算一次，不會重複計順序。
檢查coin[ i ]時，可湊成 j 元的最新組合數 = 未使用 coin[ i ] 的組合數 dp[ j ] + 採用 coin[ i ] 的組合數 dp[ j – coin[ i ] ]。

以dp[0]~dp[2]為例:
原本只有dp[0]是1，其他都是0；當i = 1，j從1-30000會變成是dp[1] = dp[1] + dp[0]，並且把dp[1]更新為1
接著在dp[2] += dp[1]的時候=>dp[2] = dp[2] + dp[1] => 0 += 1 => 1接著以此類推 
'''
