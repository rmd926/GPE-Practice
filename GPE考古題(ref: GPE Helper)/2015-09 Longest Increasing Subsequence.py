def cal_LIS(seq):
    n = len(seq)
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


while True:
    try:
        n = int(input())
    except:
        break

    seq = []

    while len(seq) < n:
        seq += list(map(int, input().split()))

    print(cal_LIS(seq))
