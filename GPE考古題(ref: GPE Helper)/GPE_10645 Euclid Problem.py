def sol(a, b):
    if b == 0:
        return 1, 0, a
    
    x1, y1, d = sol(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return x, y, d

while True:
    try:
        a, b = map(int, input().split())
    except:
        break

    x, y, d = sol(a, b)
    print(x, y, d)
