# https://zerojudge.tw/ShowProblem?problemid=e287
INF = 1_000_001

n, m = map(int, input().split())

# 外圍加牆：大小 (n+2) x (m+2)
A = [[INF] * (m + 2)]
for _ in range(n):
    A.append([INF] + list(map(int, input().split())) + [INF])
A.append([INF] * (m + 2))

# 找起點：掃描 1..n, 1..m
si = sj = 1
mn = INF
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i][j] < mn:
            mn, si, sj = A[i][j], i, j

ans = 0
while True:
    ans += A[si][sj]
    A[si][sj] = INF  # 標記走過

    ni, nj, mn = si, sj, INF
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        v = A[si + di][sj + dj]
        if v < mn:
            mn, ni, nj = v, si + di, sj + dj

    if mn == INF:  # 無可走鄰格
        break
    si, sj = ni, nj

print(ans)
