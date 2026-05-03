import math

tc = int(input())
for _ in range(tc):
    try:
        D, L = map(int, input().split())
    except:
        break

    c = D / 2
    a = L / 2
    b = abs(a**2 - c**2) ** 0.5

    ans = math.pi * a * b # pi * ab
    print(f"{ans:.3f}")
