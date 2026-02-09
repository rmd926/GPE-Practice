def find_LCS_length(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

while True:
    try:
        seq1 = input()
        seq2 = input()
        
    except EOFError:
        break
    print(find_LCS_length(seq1, seq2))

# 白癡測資在搞，媽的會TLE
