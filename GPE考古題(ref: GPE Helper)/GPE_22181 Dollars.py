MAX = 30000

dp = [0] * (MAX+1)
dp[0] = 1
coins = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for c in coins:
    for i in range(c, MAX+1):
        dp[i] += dp[i-c]

while True:
    try:
        n = input()
    except:
        break

    if n == "0.00":
        break
    
    n = float(n)
    target = int(round(n*100))
    
    print(f"{n:6.2f}{dp[target]:17d}")
