while True:
    line = input()
    if line == "":
        continue

    W, H, N = map(int, line.split())
    if W == H == N == 0:
        break

    grid = []

    for _ in range(H):
        grid.append([0] * W)
    
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())

        left = min(x1, x2)
        right = max(x1, x2)
        bottom = min(y1, y2)
        top = max(y1, y2)

        for i in range(bottom-1, top):
            for j in range(left-1, right):
                grid[i][j] = 1
    
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0:
                count += 1
    
    if count == 0:
        print("There is no empty spots.")
    
    elif count == 1:
        print("There is one empty spot.")
    
    else:
        print(f"There are {count} empty spots.")
