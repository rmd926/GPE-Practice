tc = int(input())

for _ in range(tc):
    n = int(input())

    n *= 567
    n //= 9
    n += 7492
    n *= 235
    n //= 47
    n -= 498

    ans = abs(n) // 10 % 10
    print(ans)
