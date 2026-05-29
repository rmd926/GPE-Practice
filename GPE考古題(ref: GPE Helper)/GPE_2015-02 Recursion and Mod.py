MOD = 10 ** 9 + 9

while True:
    try:
        n = int(input())
    except:
        break

    ans = (pow(3, n, MOD) - 2) % MOD

    print(ans)
# 直接用快速冪
