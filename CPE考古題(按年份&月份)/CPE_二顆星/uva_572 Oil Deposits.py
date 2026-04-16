while True:
    try:
        m, n = map(int, input().split())
    except:
        break
    
    if m == 0 and n == 0:
        break

    target = []
    for _ in range(m):
        target.append(list(input()))
    
    def dfs(x, y):
        target[x][y] = "*" # 跑dfs之前，先把原座標改成*
        for step_x, step_y in [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]: # 把八個方向寫出來
            neighbor_x = x + step_x # 鄰居座標
            neighbor_y = y + step_y

            if 0 <= neighbor_x < m and 0 <= neighbor_y < n and target[neighbor_x][neighbor_y] == "@": # 檢查是否過界以及檢查鄰居座標是否是油田
                dfs(neighbor_x, neighbor_y)
    
    ans = 0

    for i in range(m):
        for j in range(n):
            # 發現一個還沒處理過的油田
            if target[i][j] == "@":
                ans += 1 # # 找到一塊新的油田接著去跑dfs
                dfs(i, j)
    
    print(ans)
