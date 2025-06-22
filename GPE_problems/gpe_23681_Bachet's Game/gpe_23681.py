import sys

for line in sys.stdin:
    if not line.strip():
        continue

    token = list(map(int,line.strip().split()))
    n, m = token[0], token[1]
    valid_move = token[2:]

    dp = [False] * (n+1)

    
    for i in range(1, n+1):
        for move in valid_move:
            if i - move and dp[i-move] == False:
                dp[i] = True
                break

    if dp[n] == True:
        print("Stan wins")
    else:
        print("Ollie wins")