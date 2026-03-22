t = int(input())

for _ in range(t):
    m, y, c, s = input().split()
    m = int(m)
    y = int(y)
    c = int(c)

    status = True

    for ch in s:
        if ch == 'M':
            m -= 1
        elif ch == 'Y':
            y -= 1
        elif ch == 'C':
            c -= 1
        elif ch == 'R':
            m -= 1
            y -= 1
        elif ch == 'G':
            y -= 1
            c -= 1
        elif ch == 'V':
            m -= 1
            c -= 1
        elif ch == 'B':
            m -= 1
            y -= 1
            c -= 1
        elif ch == 'W':
            pass

        if m < 0 or y < 0 or c < 0:
            status = False
            break

    if status:
        print("YES", m, y, c)
    else:
        print("NO")
