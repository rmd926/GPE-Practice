while True:
    try:
        h1, m1, h2, m2 = map(int, input().split())
    except:
        break

    if h1 == h2 == m1 == m2:
        break

    if h1 < h2:
        ans = (h2-h1) * 60 + m2 - m1
    else:
        ans = (h2-h1+24) * 60 + m2 - m1

    print(ans % 1440)
