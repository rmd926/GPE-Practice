MAX = 800
dp = [0] * (MAX+1)
dp[0] = dp[1] = 0
dp[2], dp[3] = 1, 2

for i in range(3, MAX+1):
    dp[i] = (i-1) * (dp[i-1] + dp[i-2])

while True:
    try:
        n = int(input())
    except:
        break

    if n == -1 :
        break
    
    print(dp[n])
