def dfs(i, j):
    visited[i][j] = True
    for step_x, step_y in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1],  [1, 0],  [1, 1]]:
        ni = i + step_x
        nj = j + step_y

        if ni < 0 or nj < 0 or ni >= m or nj >= n:
            continue

        if grid[ni][nj] == "@" and visited[ni][nj] == False:
            dfs(ni, nj)

while True:
    try:
        m, n = map(int, input().split())
    except:
        break

    if m == n == 0:
        break
    
    grid = []
    for _ in range(m):
        grid.append(list(input()))
    count = 0

    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@" and visited[i][j] == False:
                count += 1
                dfs(i, j)
    
    print(count)
