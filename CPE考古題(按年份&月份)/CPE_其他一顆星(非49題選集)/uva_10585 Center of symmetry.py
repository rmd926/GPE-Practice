tc = int(input())
for _ in range(tc):
    n = int(input())
    point = []
    x_sum, y_sum = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        x_sum += x
        y_sum += y
        point.append([x, y])

    target_x, target_y = x_sum // n, y_sum // n
    point.sort()

    left, right = 0, n-1
    status = True
    while left < right:
        if point[left][0] + point[right][0] != target_x * 2 or point[left][1] + point[right][1] != target_y * 2:
            status = False
            break

        left += 1
        right -= 1

    if status:
        print("yes")
    else:
        print("no")
