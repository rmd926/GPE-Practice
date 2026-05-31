import math

while True:
    n = int(input())

    if n == 0:
        break

    root = math.isqrt(n)
    print(root * root)
