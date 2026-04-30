target = []
while True:
    try:
        n = int(input())
        target.append(n)
    except:
        break

MAX = max(target)
dp = [0] * (MAX+1)
dp[0], dp[1] = 0, 1

for i in range(2, MAX+1):
    dp[i] = dp[i-1] + dp[i-2]
    
for num in target:
    print(dp[num])
