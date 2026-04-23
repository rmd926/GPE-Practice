while True:
    try:
        n = int(input())
    except:
        break

    if n < 0:
        break

    print(n*(n+1) // 2 + 1)
