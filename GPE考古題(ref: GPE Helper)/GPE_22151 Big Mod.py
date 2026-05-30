import sys

seq = list(map(int, sys.stdin.read().split()))

for i in range(0, len(seq), 3):
    B = seq[i]
    P = seq[i + 1]
    M = seq[i + 2]

    print(pow(B, P, M))

# 這題要記輸入怎麼讀
