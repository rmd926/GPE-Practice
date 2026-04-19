while True:
    try:
        low, high = map(int, input().split())
    except:
        break

    if low == high == 0:
        break

    print(high // 5 - low // 5 + 1)
