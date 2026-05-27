while True:
    try:
        seq = list(map(int, input().split()))
    except:
        break

    n = seq[0]
    m = seq[1]
    moves = seq[2:]

    moves.sort()

    dp = [False] * (n + 1)

    for i in range(1, n + 1):
        for move in moves:
            if move > i:
                break

            if dp[i - move] == False:
                dp[i] = True
                break

    if dp[n]:
        print("Stan wins")
    else:
        print("Ollie wins")
