MAX = 100

dp = [0] * (MAX + 1)
dp[1] = 1
dp[2] = 2

for num in range(3, MAX + 1):
    dp[num] = dp[num - 1] + dp[num - 2]


while True:
    try:
        n = int(input())
    except:
        break

    print(dp[n])
  
# 參考leetcode 70. Climbing Stairs
