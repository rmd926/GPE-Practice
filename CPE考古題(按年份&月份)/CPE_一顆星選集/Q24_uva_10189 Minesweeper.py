tc = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break
    grid = []
    ans = []

    for _ in range(n):
        grid.append(list(input()))
        ans.append([0] * m)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "*":
                ans[i][j] = "*"

                for step_x, step_y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    ni = i + step_x
                    nj = j + step_y

                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] != "*":
                            ans[ni][nj] += 1
    
    if tc > 1:
        print()
    
    print(f"Field #{tc}:")

    for row in ans:
        for item in row:
            print(item, end="")
        print()
    
    tc += 1
