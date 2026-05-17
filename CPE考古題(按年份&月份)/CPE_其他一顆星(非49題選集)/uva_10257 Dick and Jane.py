while True:
    try:
        s, p, y, j = map(int, input().split())
    except:
        break

    Yert = (12 + j - p - y) // 3
    Puff = (12 + j - s - Yert) // 2
    Spot = 12 + j - Puff - Yert

    print(Spot, Puff, Yert)
