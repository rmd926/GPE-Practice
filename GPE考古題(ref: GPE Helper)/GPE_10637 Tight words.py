while True:
    try:
        k, n = map(int, input().split())
    except:
        break

    dp = [1] * (k + 1)

    for i in range(1, n):
        temp = [0] * (k + 1)

        for num in range(k + 1):
            temp[num] += dp[num]

            if num - 1 >= 0:
                temp[num] += dp[num - 1]

            if num + 1 <= k:
                temp[num] += dp[num + 1]
        
        dp = temp

    tight = sum(dp)
    total = (k+1) ** n

    ans = 100 * tight / total
    print(f"{ans:.5f}")
