import math

tc = int(input())
space = input()

for t in range(tc):
    target = ""
    while target == "":
        try:
            target = input().strip()
        except:
            break

    num = int(target)
    ans = math.isqrt(num)

    print(ans)

    if t != tc - 1:
        print()
