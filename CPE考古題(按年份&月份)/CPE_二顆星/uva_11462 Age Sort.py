while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break

    target = list(map(int, input().split()))
    target.sort()

    print(*target)
