tc = int(input())
for t in range(tc):
    n = int(input())
    record = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        record.append([x1, y1, x2, y2])

    left = record[0][0]
    bottom = record[0][1]
    right = record[0][2]
    top = record[0][3]

    for i in range(1, n):
        left = max(left, record[i][0])
        bottom = max(bottom, record[i][1])
        right = min(right, record[i][2])
        top = min(top, record[i][3])

    if (top-bottom) <= 0 or (right-left) <= 0:
        ans = 0
    else:
        ans = (top-bottom) * (right-left)
    print(f"Case {t+1}: {ans}")
