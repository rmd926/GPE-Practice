tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    target = list(map(int, input().split()))
    target.sort()

    print((target[-1] - target[0]) * 2)
