MAX = 13
dp = [0] * (MAX+1)
dp[0] = 1
dp[1] = 1

for i in range(2, MAX+1):
    dp[i] = dp[i-2] * (i-1) * i

while True:
    try:
        n = int(input())
    except:
        break
    
    if n < 0: # 白癡規則== 負的奇數是Overflow，正偶數是Underflow
        if n % 2 == 0:
            print("Underflow!")
        else:
            print("Overflow!")

    else:
        if n > MAX:
            print("Overflow!")
        else:
            if dp[n] > 10000 and dp[n] <= 6227020800:
                print(dp[n])
            else:
                print("Underflow!")
