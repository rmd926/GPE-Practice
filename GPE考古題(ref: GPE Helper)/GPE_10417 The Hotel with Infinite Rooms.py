import math
while True:
    try:
        S, D = map(int, input().split())
    except:
        break

    discriminant = 1 - 4 * S + 4 * (S ** 2) + 8 * D
    n = (-1 + discriminant ** 0.5) / 2
    ans = math.ceil(n)

    print(ans)
