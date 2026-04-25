while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break

    ans = 0
    for i in range(1, n+1):
        ans += (i**2)
    print(ans)
