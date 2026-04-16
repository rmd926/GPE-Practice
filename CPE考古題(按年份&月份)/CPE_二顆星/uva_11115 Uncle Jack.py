while True:
    try:
        a, b = map(int, input().split())
    except:
        break

    if a == b == 0:
        break

    print(a**b)
