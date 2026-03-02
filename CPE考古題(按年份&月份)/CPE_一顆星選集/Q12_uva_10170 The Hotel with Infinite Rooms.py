import math

while True:
    S, D = map(int, input().split())

    discriminant = 1 - 4 * S + 4 * (S ** 2) + 8 * D
    n = (-1 + math.sqrt(discriminant)) / 2
    ans = math.ceil(n)

    print(ans)
