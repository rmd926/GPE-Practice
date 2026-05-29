MAX = 50
dp = [0] * (MAX+1)
dp[0], dp[1], dp[2] = 0, 1, 2
for num in range(3, MAX+1):
    dp[num] = dp[num-1] + dp[num-2]

while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break

    print(dp[n])
